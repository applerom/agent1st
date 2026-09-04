"""WHY-graph validator — Agent1st v6 MVP, extended in v10 and v13.1.

Mechanical drift detector, not a semantic proof system. Runs deterministically,
uses stdlib only, and degrades honestly on docs-only graphs that have no
anchors yet.

Checks:
1. docs/why-graph.xml parses as XML.
2. All node IDs are unique.
3. All REL TYPE values are in the documented vocabulary.
4. All REL TARGET endpoints resolve to existing node IDs (family-qualified or bare).
5. TARGET style is consistent across the graph (all bare OR all family-qualified).
6. If ANCHOR elements exist:
   - COORD has path#marker shape.
   - NAME matches COORD marker.
   - Anchors are enforced when their parent node STATE is STARTED, DONE, or
     IMPLEMENTED and skipped when STATE is PLANNED or DEPRECATED. Other states
     are reported as errors.
   - Target file exists and contains the marker as a substring.
7. If no ANCHOR elements exist at all:
   - Report a warning, not a failure. The current Agent1st dogfood graph is
     docs-only on purpose.
8. PRD_REF elements use marker keys (v10):
   - Marker-keyed form `path#KEY` is enforced regardless of node STATE (the PRD
     carries intent before code exists): target file must exist and contain a
     `PRD_ANCHOR: KEY` comment.
   - One reference per PRD_REF element; `;`-joined lists are errors.
   - Legacy prose/section-number form (no `#`) degrades to a warning nudging
     migration, not a failure.
9. Anchor envelopes close (v13.1): every enforced `START_X` marker has a
   matching `:END_X` in the same file. An open envelope is an error.
10. FILE attributes resolve (v13.1): any node with a FILE attribute points at an
    existing regular file when its STATE is enforced; PLANNED/DEPRECATED nodes
    are skipped. Missing files are errors.
11. PRD coverage (v13.1): every ID the PRD names in a graph family the graph
    already uses (e.g. `UC-*`, `FEAT-*`) exists as a graph node. A PRD ID the
    graph does not know is a warning, not a failure: the PRD may lead the graph
    for a while, but silent divergence is the failure mode this catches.

Output: human-readable summary on stdout, errors in CDD style on stderr.
Exit 0 on pass (with warnings allowed), exit 1 on any error.

Usage:
    python scripts/validate-why.py
    python scripts/validate-why.py --graph path/to/why-graph.xml
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO

# Vocabulary — keep in sync with docs/why-graph-principles.md §4.
RELATION_VOCABULARY: frozenset[str] = frozenset({
    "COVERS",
    "EXPOSED_AS",
    "IMPLEMENTED_BY",
    "SURFACED_BY",
    "HOSTED_BY",
    "DELEGATES_TO",
    "CALLED_BY",
    "READS",
    "WRITES",
    "QUERIES",
    "BACKED_BY",
    "DEPENDS_ON",
    "IMPACTS",
    "WILL_TOUCH",
    "WILL_CREATE",
})

ENFORCED_STATES: frozenset[str] = frozenset({"STARTED", "DONE", "IMPLEMENTED"})
SKIPPED_STATES: frozenset[str] = frozenset({"PLANNED", "DEPRECATED"})


@dataclass(frozen=True)
class Issue:
    severity: str  # "error" or "warning"
    node: str
    problem: str
    fix: str


def _parse_target(raw: str) -> tuple[str | None, str]:
    """Split a REL TARGET into (family, id). Bare targets return (None, id)."""
    if ":" in raw:
        family, _, ident = raw.partition(":")
        return family, ident
    return None, raw


def _family_matches(tag: str, family: str) -> bool:
    return tag == family or tag.startswith(family + "_")


def collect_nodes(root: ET.Element) -> dict[str, ET.Element]:
    """Map node ID -> element. Top-level non-REL children are nodes."""
    nodes: dict[str, ET.Element] = {}
    for elem in root:
        node_id = elem.get("ID")
        if node_id is None:
            continue
        nodes[node_id] = elem
    return nodes


def check_unique_ids(root: ET.Element) -> list[Issue]:
    seen: dict[str, int] = {}
    issues: list[Issue] = []
    for elem in root:
        node_id = elem.get("ID")
        if node_id is None:
            continue
        seen[node_id] = seen.get(node_id, 0) + 1
    for node_id, count in seen.items():
        if count > 1:
            issues.append(Issue(
                severity="error",
                node=node_id,
                problem=f"node ID appears {count} times",
                fix="rename or merge duplicate nodes so each ID is unique",
            ))
    return issues


def check_relations(
    root: ET.Element, nodes: dict[str, ET.Element]
) -> tuple[list[Issue], int, int]:
    """Validate REL elements: TYPE in vocabulary, TARGET resolves, style consistent."""
    issues: list[Issue] = []
    bare_count = 0
    qualified_count = 0
    rel_count = 0

    for parent in root.iter():
        parent_id = parent.get("ID", "<unknown>")
        for rel in parent.findall("REL"):
            rel_count += 1
            rel_type = rel.get("TYPE", "")
            target = rel.get("TARGET", "")

            if rel_type not in RELATION_VOCABULARY:
                issues.append(Issue(
                    severity="error",
                    node=parent_id,
                    problem=f"REL TYPE {rel_type!r} is not in the documented vocabulary",
                    fix="use a documented relation type or update why-graph-principles.md §4 first",
                ))

            if not target:
                issues.append(Issue(
                    severity="error",
                    node=parent_id,
                    problem="REL has no TARGET",
                    fix="add TARGET attribute pointing to a node ID",
                ))
                continue

            family, ident = _parse_target(target)
            if family is None:
                bare_count += 1
            else:
                qualified_count += 1

            target_node = nodes.get(ident)
            if target_node is None:
                issues.append(Issue(
                    severity="error",
                    node=parent_id,
                    problem=f"REL TARGET {target!r} does not resolve to any node ID",
                    fix="add the missing node, fix the TARGET, or remove the stale relation",
                ))
                continue

            if family is not None and not _family_matches(target_node.tag, family):
                issues.append(Issue(
                    severity="error",
                    node=parent_id,
                    problem=(
                        f"REL TARGET {target!r} family does not match the resolved "
                        f"node element {target_node.tag!r}"
                    ),
                    fix="align the TARGET family prefix with the actual node element",
                ))

    if bare_count and qualified_count:
        issues.append(Issue(
            severity="error",
            node="<graph>",
            problem=(
                f"mixed TARGET styles: {bare_count} bare, {qualified_count} family-qualified"
            ),
            fix="pick one convention per repo (see why-graph-principles.md §4) and apply it everywhere",
        ))

    return issues, rel_count, bare_count + qualified_count


def check_anchors(
    root: ET.Element, repo_root: Path
) -> tuple[list[Issue], int, int, int]:
    """Validate ANCHOR elements with STATE-aware enforcement.

    Returns (issues, validated, skipped, total_anchors).
    """
    issues: list[Issue] = []
    validated = 0
    skipped = 0
    total = 0

    for node in root.iter():
        anchors = node.findall("ANCHOR")
        if not anchors:
            continue

        total += len(anchors)
        state = node.get("STATE", "")
        node_id = node.get("ID", f"<{node.tag}>")
        enforce = state in ENFORCED_STATES
        skip_resolution = state in SKIPPED_STATES

        if not enforce and not skip_resolution:
            issues.append(Issue(
                severity="error",
                node=node_id,
                problem=f"node has anchors but STATE={state!r} is neither enforced nor skipped",
                fix=f"set STATE to one of {sorted(ENFORCED_STATES | SKIPPED_STATES)}",
            ))

        for anchor in anchors:
            name = anchor.get("NAME") or ""
            coord = anchor.get("COORD") or ""

            if not name or not coord:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem="ANCHOR is missing NAME or COORD",
                    fix='add NAME="START_..." and COORD="path#START_..." attributes',
                ))
                continue

            path_part, sep, marker = coord.partition("#")
            if not sep or not path_part or not marker:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"COORD {coord!r} is not in path#MARKER shape",
                    fix='use COORD="repo/relative/path#START_MARKER"',
                ))
                continue

            if marker != name:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"ANCHOR NAME={name!r} does not match COORD marker {marker!r}",
                    fix="keep NAME and the part after # in COORD identical",
                ))
                continue

            if skip_resolution:
                skipped += 1
                continue
            if not enforce:
                continue

            target = repo_root / path_part
            if not target.exists():
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"anchor target file is missing: {path_part}",
                    fix="create the file, fix the path, or remove the anchor",
                ))
                continue
            if not target.is_file():
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"anchor target is not a regular file: {path_part}",
                    fix="point COORD at a real source file",
                ))
                continue

            try:
                text = target.read_text(encoding="utf-8")
            except OSError as exc:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"could not read {path_part}: {exc}",
                    fix="check file permissions and encoding",
                ))
                continue

            if marker not in text:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"marker {marker} not found in {path_part}",
                    fix="add the START_* marker in the source file or update the anchor",
                ))
                continue

            if marker.startswith("START_"):
                end_marker = ":END_" + marker[len("START_"):]
                if end_marker not in text:
                    issues.append(Issue(
                        severity="error",
                        node=node_id,
                        problem=f"anchor envelope is open: {marker} has no {end_marker} in {path_part}",
                        fix=f"add the {end_marker} line after the code the anchor wraps",
                    ))
                    continue

            validated += 1

    return issues, validated, skipped, total


def check_prd_refs(
    root: ET.Element, repo_root: Path
) -> tuple[list[Issue], int]:
    """Validate PRD_REF elements: marker-keyed refs resolve to PRD_ANCHOR markers.

    Returns (issues, validated_count).
    """
    issues: list[Issue] = []
    validated = 0

    for node in root.iter():
        refs = node.findall("PRD_REF")
        if not refs:
            continue
        node_id = node.get("ID", f"<{node.tag}>")

        for ref in refs:
            text = (ref.text or "").strip()

            if not text:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem="PRD_REF is empty",
                    fix='point at a marker key, e.g. docs/PRD.md#USE-CASES',
                ))
                continue

            if ";" in text:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"PRD_REF {text!r} holds multiple references",
                    fix="use one PRD_REF element per reference",
                ))
                continue

            if "#" not in text:
                issues.append(Issue(
                    severity="warning",
                    node=node_id,
                    problem=f"PRD_REF {text!r} is not marker-keyed",
                    fix=(
                        'use path#KEY resolving to a "PRD_ANCHOR: KEY" comment '
                        "in the PRD (see why-graph-principles.md §5a); section "
                        "numbers and heading text break on refactor"
                    ),
                ))
                continue

            path_part, _, key = text.partition("#")
            path_part = path_part.strip()
            key = key.strip()
            if not path_part or not key:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"PRD_REF {text!r} is not in path#KEY shape",
                    fix="use a repo-relative path, then #, then the marker key",
                ))
                continue

            target = repo_root / path_part
            if not target.is_file():
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"PRD_REF target file is missing: {path_part}",
                    fix="create the file, fix the path, or remove the reference",
                ))
                continue

            try:
                doc_text = target.read_text(encoding="utf-8")
            except OSError as exc:
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"could not read {path_part}: {exc}",
                    fix="check file permissions and encoding",
                ))
                continue

            pattern = rf"PRD_ANCHOR:\s*{re.escape(key)}(?![A-Za-z0-9-])"
            if not re.search(pattern, doc_text):
                issues.append(Issue(
                    severity="error",
                    node=node_id,
                    problem=f"PRD_ANCHOR marker {key!r} not found in {path_part}",
                    fix=(
                        f"add <!-- PRD_ANCHOR: {key} --> under the section this "
                        "reference means, or fix the key"
                    ),
                ))
                continue

            validated += 1

    return issues, validated


def check_file_attrs(
    root: ET.Element, repo_root: Path
) -> tuple[list[Issue], int]:
    """Validate FILE attributes: enforced nodes must point at existing files.

    Returns (issues, validated_count).
    """
    issues: list[Issue] = []
    validated = 0

    for node in root.iter():
        file_attr = node.get("FILE")
        if not file_attr:
            continue
        node_id = node.get("ID", f"<{node.tag}>")
        state = node.get("STATE", "")
        if state in SKIPPED_STATES:
            continue
        if state and state not in ENFORCED_STATES:
            issues.append(Issue(
                severity="error",
                node=node_id,
                problem=f"node has FILE but STATE={state!r} is neither enforced nor skipped",
                fix=f"set STATE to one of {sorted(ENFORCED_STATES | SKIPPED_STATES)}",
            ))
            continue

        target = repo_root / file_attr
        if not target.is_file():
            issues.append(Issue(
                severity="error",
                node=node_id,
                problem=f"FILE target is missing or not a regular file: {file_attr}",
                fix="create the file, fix the path, or retire the node (STATE=\"DEPRECATED\")",
            ))
            continue
        validated += 1

    return issues, validated


_ID_PREFIX_RE = re.compile(r"^([A-Z]+)-")


def check_prd_coverage(
    root: ET.Element, nodes: dict[str, ET.Element], repo_root: Path
) -> tuple[list[Issue], int]:
    """Warn when the PRD names an ID in a graph family the graph does not define.

    The PRD is discovered through PRD_REF targets, so the check needs no config.
    Only families already present in the graph are scanned (e.g. UC-*, FEAT-*),
    which keeps unrelated identifiers in the PRD out of scope.

    Returns (issues, prd_ids_checked).
    """
    issues: list[Issue] = []
    prefixes = {m.group(1) for m in map(_ID_PREFIX_RE.match, nodes) if m}
    if not prefixes:
        return issues, 0

    prd_paths: list[str] = []
    for ref in root.iter("PRD_REF"):
        text = (ref.text or "").strip()
        path_part = text.partition("#")[0].strip()
        if path_part and path_part not in prd_paths:
            prd_paths.append(path_part)

    pattern = re.compile(
        r"\b(" + "|".join(sorted(prefixes)) + r")-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"
    )
    checked = 0
    for path_part in prd_paths:
        target = repo_root / path_part
        if not target.is_file():
            continue  # reported by check_prd_refs
        try:
            doc_text = target.read_text(encoding="utf-8")
        except OSError:
            continue
        seen: set[str] = set()
        for match in pattern.finditer(doc_text):
            ident = match.group(0)
            if ident in seen:
                continue
            seen.add(ident)
            checked += 1
            if ident not in nodes:
                issues.append(Issue(
                    severity="warning",
                    node=path_part,
                    problem=f"PRD names {ident} but the graph has no node with that ID",
                    fix="add the node to the graph, or drop the ID from the PRD if it is retired",
                ))
    return issues, checked


def format_issue(issue: Issue) -> str:
    return (
        f"- [{issue.severity}] {issue.node}\n"
        f"  Problem: {issue.problem}\n"
        f"  Smallest fix: {issue.fix}"
    )


def run(
    graph_path: Path,
    repo_root: Path,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
) -> int:
    if not graph_path.exists():
        print(f"WHY validator: graph not found at {graph_path}", file=stderr)
        return 1

    try:
        tree = ET.parse(graph_path)
    except ET.ParseError as exc:
        print(f"WHY validator: XML parse error in {graph_path}: {exc}", file=stderr)
        return 1

    root = tree.getroot()
    nodes = collect_nodes(root)

    issues: list[Issue] = []
    issues.extend(check_unique_ids(root))
    relation_issues, rel_count, _ = check_relations(root, nodes)
    issues.extend(relation_issues)
    anchor_issues, anchors_ok, anchors_skipped, anchors_total = check_anchors(root, repo_root)
    issues.extend(anchor_issues)
    prd_ref_issues, prd_refs_ok = check_prd_refs(root, repo_root)
    issues.extend(prd_ref_issues)
    file_issues, files_ok = check_file_attrs(root, repo_root)
    issues.extend(file_issues)
    coverage_issues, prd_ids_checked = check_prd_coverage(root, nodes, repo_root)
    issues.extend(coverage_issues)

    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    if anchors_total == 0:
        warnings.append(Issue(
            severity="warning",
            node="<graph>",
            problem="no ANCHOR elements found",
            fix=(
                "acceptable for a docs-only dogfood graph; add anchors when "
                "adopting this layer in a code repo"
            ),
        ))

    summary = (
        f"WHY validator: nodes={len(nodes)} relations={rel_count} "
        f"anchors_validated={anchors_ok} anchors_skipped={anchors_skipped} "
        f"prd_refs_validated={prd_refs_ok} files_validated={files_ok} "
        f"prd_ids_checked={prd_ids_checked} "
        f"errors={len(errors)} warnings={len(warnings)}"
    )
    print(summary, file=stdout)

    for warning in warnings:
        print(format_issue(warning), file=stdout)

    if not errors:
        print("WHY validator: OK", file=stdout)
        return 0

    print("WHY validator: FAILED", file=stderr)
    for error in errors:
        print(format_issue(error), file=stderr)
    return 1


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the Agent1st WHY graph against the documented vocabulary and anchors.",
    )
    parser.add_argument(
        "--graph",
        type=Path,
        default=None,
        help="Path to docs/why-graph.xml (default: docs/why-graph.xml under repo root)",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (default: parent of this script's directory)",
    )
    args = parser.parse_args(argv)

    repo_root = args.repo_root or _default_repo_root()
    graph_path = args.graph or (repo_root / "docs" / "why-graph.xml")
    return run(graph_path, repo_root)


if __name__ == "__main__":
    raise SystemExit(main())
