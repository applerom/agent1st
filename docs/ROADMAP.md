# Agent1st Protocol — Roadmap

A living document for planning, discussion, and tracking the protocol's evolution across its two public layers — the behavior layer (`AGENTS.md`) and the WHY layer (`docs/*`) — plus project-local extensions that sit on top of them.

This is not a commitment list. It is a structured conversation space where agents and humans propose, critique, and prioritize future work. Items move through: **proposed → accepted → in-progress → done** (or **rejected** with reason).

---

## Active Priorities

### 1. WHY Layer — delivered in v5

The "standard version" has been delivered as the **WHY layer**, living flat in `docs/` rather than in a separate `STANDARD/` folder. The three-tier (minimal/standard/full) framing has been retired.

**Shipped in v5:**
- `docs/Why1st.md` — the idea, the workflow shift, when to adopt, adopter's Required Reading pattern
- `docs/PRD.md` — Agent1st's own dogfooded PRD
- `docs/why-graph.xml` — teaching-size graph dogfooding Agent1st itself
- `docs/why-graph-principles.md` — portable authoring guide (distilled from real adopters)
- `docs/why-contracts-v1.md` — portable contract spec with Python + TypeScript examples
- `docs/VISION.md` — reframed around two layers (behavior + WHY)

**Open follow-ups:**
1. ~~Extract minimal validator scripts (graph↔anchor lint) as language-agnostic reference~~ — **shipped in v6** as `scripts/validate-why.py` (stdlib-only Python). A non-Python reference port remains optional.
2. Decide whether a starter-kit CLI is worth building, or whether copy-and-adapt from this repo is sufficient (current bet: the latter).

### 2. Claude Code Compatibility

**Problem:** Claude Code auto-loads only `CLAUDE.md`, not `AGENTS.md`. Projects using `AGENTS.md` (the emerging standard for OpenCode, Codex, Cursor, etc.) need a bridge.

**Solution:** Minimal `CLAUDE.md` that imports `AGENTS.md`:
```markdown
@AGENTS.md
```

**Implementation:**
- [x] Pattern proven in a downstream adopter — done 2026-03-25
- [x] Add this pattern to Agent1st repo — done 2026-03-25
- [x] Documented in README.md Quick Start section — done 2026-03-25

### 3. Cross-Session Memory Strategy

**Current observed state:** Three competing approaches tried in downstream adopters:
1. `decision-context.xml` — custom XML decision memory. **Assessment by human: not great.** Non-standard, hard to maintain.
2. `intent1st` — durable meaning via skills. **Assessment: good concept, poor adoption.** Models forget to use SKILL-based access.
3. Claude Code `MEMORY.md` — built-in, automatic. Standard for Claude Code users.

**Direction for Agent1st:**
- Behavior layer (`AGENTS.md`): no memory prescription — stays in harness layer.
- WHY layer: recommend **durable artifacts** (already in Continuity principle) without prescribing format.
- Project-local extensions: each project picks a memory system that fits its harness (e.g., Claude Code `MEMORY.md`, intent1st skills, repo-local decision logs). Not a portable concern.

**Open question:** Should the WHY layer recommend a specific memory format, or just principles for memory hygiene?

---

## Proposed (Not Yet Accepted)

### From External Agent Review (2026-03-24)

| Proposal | Source | Status | Notes |
|----------|--------|--------|-------|
| Friction Tax (quantified CDD) | GLM-5 | Proposed for WHY layer | Track recurring friction as process debt |
| Ambiguity handling in CDD | MiniMax M2.7 | Proposed for WHY layer | Distinguish ambiguous from incomplete |
| Anti-pattern examples doc | MiniMax M2.7, Qwen3.5-Plus | Under consideration | Violation examples per principle |
| Decision log template | MiniMax M2.7 | Proposed for project-local extension | Standardized format for decisions |
| Agent Self-Test in README | Qwen3.5-Plus | Noted | UX idea for agent onboarding |

### From Downstream Adopter Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| WHY-layer starter kit | Proposed | Template files for Why Graph, contracts, validation |
| Graduation guide (minimal→WHY layer) | Proposed | When and how to upgrade |
| Validation tooling as portable package | Proposed | Extract from a real adopter, make language-agnostic |
| Per-directory AGENTS.md pattern doc | Proposed | Document the scoped-instructions pattern |
| Skills specification for WHY-layer adopters | Proposed | Portable skill format beyond SKILL.md |

### From intent1st Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| Document intent1st relationship | Proposed | How it extends Agent1st philosophy |
| Evaluate gateway pattern for WHY layer | Proposed | intent1st's canon/candidates/archive model |
| Assess SKILL.md adoption barrier | Open question | Models don't reliably use skill-based access |

---

## Rejected (With Reasons)

See `docs/EVOLUTION.md` "Recurring Rejected Patterns" for full list. Key recurring rejections:
- Fresh-eye scan at session start (delta-layer + multi-agent waste)
- Error recovery rules (harness layer)
- Scope discipline (model layer)
- Output formatting (harness layer)
- Session boundary assumptions (agents don't control compaction)

---

## Version Planning

### v4.x (minimal baseline, unchanged)
- Continuity hook added (Qwen)
- Handoff template created
- Continuity research grounded (Park et al.)
- Model-agnostic note added
- External agent contributions curated

### v5
- WHY layer delivered as flat files in `docs/` (Why1st entry doc — at the time named `WHY-APPROACH.md` — plus PRD, why-graph, principles, contracts)
- Three-tier (minimal/standard/full) framing retired in favor of two layers: behavior + WHY
- `AGENTS.md` remains unchanged — portability preserved
- VISION, ROADMAP, DESIGN, README updated to match

### v5.1
- External-review integration round (8 reviewers)
- Graph staleness named as the primary failure mode; recovery protocol added
- Workflow shape stops being a universal law; intent-changing vs local-edit intensities
- §8 Required Reading reframed as adopter's pattern with harness-native first

### v6
- `scripts/validate-why.py` — WHY validator MVP, stdlib-only
- `AGENTS.md` byte-identical to v5.1 — survives the v6 spirit pass unchanged
- §1 Role Contract candidate deferred (failed bullet-count discipline at the front door)
- §8 / §9 candidate edits landed then reverted (duplication with §4 / template-grade tactical advice)
- No model-specific knobs added (explicit non-goal)

### v6.1 (current)
- Why1st adopted as a short name for the WHY-first approach/layer, distinct from Agent1st (the behavior contract)
- One-file `docs/PRD.md` starter stance documented as valid, with extraction only when useful
- Stale v6 teaching-surface residue fixed (`No validators yet`, `four files`, module-family examples)
- Validator generalized: anchor checks apply to any node with `<ANCHOR>` children, not just `MODULE_*`
- Reference adopter analyses moved off-public (kept for development-side use only) so the public protocol does not name projects readers cannot access

### v7+ (speculative)
- Friction Tax / ambiguity handling in CDD — gated by delta-layer test
- Memory system integration patterns (harness MEMORY.md vs. in-repo decision logs)
- Anchor adoption in this repo's own `docs/` so the validator graduates from doc-only mode to enforced anchors

---

## How to Contribute

1. **Propose:** Add an item to the "Proposed" section with your agent name, rationale, and target scope
2. **Discuss:** Comment on existing proposals in handoff briefs or directly in this file
3. **Critique:** Challenge any item — even accepted ones. The protocol values disagreement.
4. **Test:** Try ideas in a real downstream project and report results
5. **Report friction:** If something in this document or process is hard to use, say so (CDD applies here too)

This document is maintained by lead agents (currently Claude Opus 4.6 and GPT-5.4) with human oversight. All agents are welcome to propose changes.
