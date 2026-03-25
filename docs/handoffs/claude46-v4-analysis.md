# Agent1st Protocol — Handoff Brief: Claude Opus 4.6 v4 Analysis Session

**Agent:** Claude Opus 4.6
**Date:** 2026-03-23
**Session scope:** Deep analysis of AGENTS.md v3, design history, external references, SPS3A standard version; preparation for v4; repo documentation restructuring.

---

## 1) Objective

Evaluate AGENTS.md v3 quality from agent perspective, understand design history, analyze referenced materials, and prepare ground for v4 development. Secondary: begin documenting the project's accumulated knowledge so it stops living only in the human's head.

---

## 2) Current Status

**Done:**
- Full analysis of v1→v2→v3 evolution through file comparison
- Initial assessment of v3 (scored 7.5/10 before context, revised to 8.5/10 after)
- Analysis of external references (Claude prompting docs, Claude Code memory, CoT topology paper, OpenAI prompting guide; harness engineering and Codex intro articles were 403-blocked)
- Read and integrated GPT-5.4 handoff brief — critical for understanding intentional omissions
- Explored SPS3A project as reference for "standard" Agent1st implementation
- Created repo documentation structure: DESIGN.md, EVOLUTION.md, VISION.md, CLAUDE.md
- Moved handoff brief to `docs/handoffs/` with agent-specific naming
- Proposed v4 changes with rationale
- Created this handoff

**Not done:**
- Actual v4 draft of AGENTS.md (analysis and planning only)
- EVOLUTION.md v0→v1 and v1→v2 sections (marked [TBD] for original agents to fill)
- README.md for the repo (in progress at session end)
- Comparison with current Claude Code system prompt for delta-layer validation of v4 proposals

---

## 3) Key Decisions and Why

### A. Revised assessment after context

Initial assessment proposed adding error recovery, scope discipline, tool boundaries. After reading the GPT-5.4 handoff brief and understanding the delta-layer principle, I recognized these are all covered by model/tool harness and would be bad additions. This is the most common mistake agents make on first contact with this project.

**Lesson:** The delta-layer principle is real and load-bearing. Most "obvious improvements" fail this test.

### B. Documentation structure

Created four documents:
- `DESIGN.md` — captures design principles to prevent future agents from repeating my initial mistakes
- `EVOLUTION.md` — version history template with what I could reconstruct
- `VISION.md` — min/standard/full scopes and roadmap
- `CLAUDE.md` — meta: the repo itself follows Agent1st principles

**Why:** The human explicitly said project knowledge is scattered across dozens of agent conversations. These documents begin extracting it into durable form.

### C. v4 direction: multi-agent autonomy

Six proposed additions, all tested against delta-layer principle:
1. Human role spectrum (paired → supervised → fully autonomous)
2. Delegation Design (hierarchical + swarm patterns)
3. Claude 4.6-specific attention tuning (over-exploration/over-delegation guards)
4. Evidence across agent boundaries (artifact > claim)
5. Session Start behavior on "Hello Agent!" activation
6. Escalation Boundary (unsupervised contexts)

**Why these pass the delta-layer test:** None of these are covered by current model or tool prompts. Multi-agent delegation design, human presence spectrum, and escalation boundaries for autonomous agents are genuinely new territory.

### D. SPS3A exploration findings

The "standard" version in SPS3A includes:
- **Why Graph** (XML) — intent→implementation map with semantic anchors
- **Semantic contracts** — MODULE_CONTRACT, METHOD_CONTRACT, BLOCK anchors in code
- **decision-context.xml** — cross-session rationale memory with issue→decision→evidence links
- **Validation scripts** — anchor_lint.py, why_validate_graph.py, validate_prd_defaults.py
- **Skills** — fresh-eye-audit, validation-gate, session-handoff as repeatable workflows
- **Per-directory AGENTS.md** — nested instructions with scope precedence

This confirms that the minimal version is genuinely minimal — the standard version is roughly 5-10x the surface area. The human's instinct to "get the minimal version right first" is correct: it sets the foundation, and the standard/full versions must not contradict it.

---

## 4) Assumptions / Invariants

- The delta-layer principle remains the primary design constraint
- The anti-micromanagement stance is non-negotiable
- The Core/Operations split from v3 should be preserved in v4
- Under 200 lines for the minimal version
- WHY / IF MISSING pattern is kept
- "Hello Agent!" activation is kept
- The voice (hooks, controlled humor, provocation) is a feature, not a quirk

---

## 5) Rejected Paths

| Proposed | Why Rejected |
|----------|-------------|
| Add error recovery principle | Covered by Claude Code / Codex harness layer |
| Add scope discipline / anti-drift | Covered by model system prompts |
| Add tool/capability boundaries | Harness layer concern |
| Move "Done Is Not a Mood" to #1 position | Role Contract at #1 is intentional — sets the anti-micromanagement framing first |
| Add output formatting rules | Harness layer |
| Add planning methodology | Agent Loop is sufficient for minimal version |

---

## 6) Blockers / Risks

- **Harness engineering article (403)** — Couldn't fetch OpenAI's harness engineering article. This was a key reference for v3 design. Future agents should try to access it or find the content elsewhere.
- **Claude Code system prompt drift** — My delta-layer analysis is based on current Claude Code prompt. If it changes significantly, some v4 additions might become redundant. Should re-check before finalizing v4.
- **200-line constraint tension** — Adding 2-3 new principles to v3's 200 lines means something must be compressed or merged. The hardest editorial decision for v4.

---

## 7) Next Deterministic Steps

1. **Draft AGENTS-min-v4.md** — Apply the six proposed changes to v3. Test against 200-line limit. If over, compress or merge principles.
2. **Delta-layer validation** — Re-read current Claude Code system prompt and Codex CLI instructions. Verify none of the v4 additions overlap.
3. **Fill EVOLUTION.md gaps** — Human will provide v0→v1 and v1→v2 context from original agents.
4. **VISION.md update** — Add concrete references to SPS3A standard version structure.
5. **Community framing** — README.md in Agent1st spirit for humans discovering the repo.

---

## 8) Evidence Summary

- Read and compared: AGENTS-min-v1.md, v2.md, v3.md, current AGENTS.md
- Read: GPT-5.4 handoff brief (15KB, 520 lines)
- Fetched and analyzed: Claude prompting best practices, Claude Code memory docs, CoT topology paper abstract, OpenAI prompting guide
- Failed to fetch (403): OpenAI harness engineering article, Introducing Codex article
- Explored: SPS3A project (41 tool uses, comprehensive scan of agent infrastructure)
- Created: DESIGN.md, EVOLUTION.md, VISION.md, CLAUDE.md, this handoff

---

## 9) Frictions That Reduced Effectiveness

1. **No DESIGN.md existed at session start** — Had to reconstruct design principles from the handoff brief and inference. First-contact agents will always make the "obvious improvement" mistake without this document. Now fixed.

2. **External references partially inaccessible** — Harness engineering article (the most important external reference per the handoff) returned 403. Had to work from indirect knowledge.

3. **Standard version was in a separate repo** — Understanding the min→standard→full progression required exploring SPS3A. Future agents would benefit from VISION.md explicitly referencing the SPS3A structure (now partially addressed).
