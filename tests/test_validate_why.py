"""Regression checks for the validator's advertised mechanical guarantees."""

import io
from pathlib import Path
import runpy
import shutil
import unittest
from unittest.mock import patch
from uuid import uuid4
import xml.etree.ElementTree as ET


REPO = Path(__file__).resolve().parents[1]
VALIDATOR = runpy.run_path(str(REPO / "scripts" / "validate-why.py"))


def graph(*markers, state="IMPLEMENTED"):
    root = ET.Element("Why_Graph")
    node = ET.SubElement(root, "MODULE", ID="MOD-X", STATE=state)
    for marker in markers:
        ET.SubElement(node, "ANCHOR", NAME=marker, COORD=f"code.py#{marker}")
    return root


class AnchorTests(unittest.TestCase):
    def check(self, content, *markers, state="IMPLEMENTED"):
        with patch.object(Path, "exists", return_value=True), \
             patch.object(Path, "is_file", return_value=True), \
             patch.object(Path, "read_text", return_value=content):
            return VALIDATOR["check_anchors"](graph(*markers, state=state), REPO)

    def test_exact_marker_in_supported_comment_shapes(self):
        for start, end in [
            ("# START_BLOCK_X:", "# :END_BLOCK_X"),
            ("// START_BLOCK_X:", "// :END_BLOCK_X"),
            ("{/* START_BLOCK_X */}", "{/* :END_BLOCK_X */}"),
        ]:
            with self.subTest(start=start):
                issues, valid, _, _ = self.check(f"{start}\nbody\n{end}", "START_BLOCK_X")
                self.assertEqual([], issues)
                self.assertEqual(1, valid)

    def test_broken_envelopes_are_rejected(self):
        cases = {
            "missing start": "# :END_BLOCK_X",
            "missing end": "# START_BLOCK_X:",
            "duplicate start": "# START_BLOCK_X:\n# START_BLOCK_X:\n# :END_BLOCK_X",
            "duplicate end": "# START_BLOCK_X:\n# :END_BLOCK_X\n# :END_BLOCK_X",
            "reversed": "# :END_BLOCK_X\n# START_BLOCK_X:",
            "prefix collision": "# START_BLOCK_X_EXTRA:\n# :END_BLOCK_X_EXTRA",
            "hyphen suffix collision": "# START_BLOCK_X-EXTRA:\n# :END_BLOCK_X-EXTRA",
            "end prefix collision": "# START_BLOCK_X:\n# :END_BLOCK_X_EXTRA",
        }
        for name, content in cases.items():
            with self.subTest(name=name):
                issues, valid, _, _ = self.check(content, "START_BLOCK_X")
                self.assertTrue(any(i.severity == "error" for i in issues))
                self.assertEqual(0, valid)

    def test_nested_and_disjoint_envelopes_pass(self):
        for content in [
            "START_A:\nSTART_B:\n:END_B\n:END_A",
            "START_A:\n:END_A\nSTART_B:\n:END_B",
        ]:
            with self.subTest(content=content):
                issues, valid, _, _ = self.check(content, "START_A", "START_B")
                self.assertEqual([], issues)
                self.assertEqual(2, valid)

    def test_crossed_envelopes_fail(self):
        issues, _, _, _ = self.check("START_A:\nSTART_B:\n:END_A\n:END_B", "START_A", "START_B")
        self.assertTrue(any("crosses" in i.problem for i in issues))

    def test_planned_and_deprecated_anchors_need_no_source(self):
        for state in ["PLANNED", "DEPRECATED"]:
            with self.subTest(state=state):
                issues, valid, skipped, _ = self.check("", "START_A", state=state)
                self.assertEqual([], issues)
                self.assertEqual((0, 1), (valid, skipped))

    def test_unknown_state_fails(self):
        issues, _, _, _ = self.check("", "START_A", state="UNKNOWN")
        self.assertTrue(any(i.severity == "error" for i in issues))

    def test_shared_graph_reference_is_not_a_duplicate_source_marker(self):
        issues, valid, _, _ = self.check("START_A:\n:END_A", "START_A", "START_A")
        self.assertEqual([], issues)
        self.assertEqual(2, valid)


class PrdMarkerTests(unittest.TestCase):
    def test_only_one_exact_comment_resolves(self):
        root = ET.fromstring('<Why_Graph><FEATURE ID="FEAT-X"><PRD_REF>PRD.md#KEY</PRD_REF></FEATURE></Why_Graph>')
        for text, expected in [
            ("<!-- PRD_ANCHOR: KEY -->", 1),
            ("<!-- PRD_ANCHOR: KEY_EXTRA -->", 0),
            ("PRD_ANCHOR: KEY", 0),
            ("<!-- PRD_ANCHOR: KEY --><!-- PRD_ANCHOR: KEY -->", 0),
        ]:
            with self.subTest(text=text), \
                 patch.object(Path, "is_file", return_value=True), \
                 patch.object(Path, "read_text", return_value=text):
                issues, valid = VALIDATOR["check_prd_refs"](root, REPO)
                self.assertEqual(expected, valid)
                self.assertEqual(expected == 0, bool(issues))


class ExampleIntegrationTests(unittest.TestCase):
    def test_complete_example_and_broken_coordinate(self):
        source = REPO / "docs" / "examples" / "reading-list"
        # Windows Python's mode-700 temp dirs can exclude a sandbox's secondary
        # token. A normal directory inherits the checkout's usable permissions.
        tmp = (REPO / "tests" / f"why-test-{uuid4().hex}").resolve()
        self.assertEqual((REPO / "tests").resolve(), tmp.parent)
        tmp.mkdir(mode=0o777)
        try:
            target = tmp / "example"
            shutil.copytree(source, target)
            out, err = io.StringIO(), io.StringIO()
            self.assertEqual(0, VALIDATOR["run"](target / "why-graph.xml", target, out, err))
            self.assertIn("anchors_validated=2", out.getvalue())
            self.assertIn("warnings=0", out.getvalue())
            code = target / "reading_list.py"
            code.write_text(code.read_text(encoding="utf-8").replace(
                "START_METHOD_can_add_book", "START_METHOD_renamed"
            ), encoding="utf-8")
            out, err = io.StringIO(), io.StringIO()
            self.assertEqual(1, VALIDATOR["run"](target / "why-graph.xml", target, out, err))
            self.assertIn("START_METHOD_can_add_book occurs 0 times", err.getvalue())
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
