# Agent1st Protocol — Roadmap

A living document for planning, discussion, and tracking the protocol's evolution across its two public layers — the behavior layer (`AGENTS.md`) and the WHY layer (`docs/*`) — plus project-local extensions that sit on top of them.

This is not a commitment list. It is a structured conversation space where agents and humans propose, critique, and prioritize future work. Items move through: **proposed → accepted → in-progress → done** (or **rejected** with reason).

---

## Active Priorities

### 1. WHY Layer — delivered in v5

The "standard version" has been delivered as the **WHY layer**, living flat in `docs/` rather than in a separate `STANDARD/` folder. The three-tier (minimal/standard/full) framing has been retired.

**Shipped in v5:**
- `docs/WHY-APPROACH.md` — the idea, the workflow shift, when to adopt, adopter's Required Reading pattern
- `docs/PRD.md` — Agent1st's own dogfooded PRD
- `docs/why-graph.xml` — teaching-size graph dogfooding Agent1st itself
- `docs/why-graph-principles.md` — portable authoring guide (distilled from two real adopters)
- `docs/why-contracts-v1.md` — portable contract spec with Python + TypeScript examples
- `docs/VISION.md` — reframed around two layers (behavior + WHY)

**Reference adopters:**
- SPS3A — richer Python/FastAPI variant; see `docs/SPS3A-ANALYSIS.md`
- A separate TypeScript adopter — simpler variant with an adoption-notes philosophy doc (private project, not linkable)

**Open follow-ups:**
1. Extract minimal validator scripts (graph↔anchor lint) as language-agnostic reference — still useful, now genuinely optional.
2. Add a second dogfooded adopter example linked from `SPS3A-ANALYSIS.md`.
3. Decide whether a starter-kit CLI is worth building, or whether copy-and-adapt from this repo is sufficient (current bet: the latter).

### 2. Claude Code Compatibility

**Problem:** Claude Code auto-loads only `CLAUDE.md`, not `AGENTS.md`. Projects using `AGENTS.md` (the emerging standard for OpenCode, Codex, Cursor, etc.) need a bridge.

**Solution:** Minimal `CLAUDE.md` that imports `AGENTS.md`:
```markdown
@AGENTS.md
```

**Implementation:**
- [x] Add this pattern to SPS3A project — done 2026-03-25
- [x] Add this pattern to Agent1st repo — done 2026-03-25
- [x] Documented in README.md Quick Start section — done 2026-03-25

### 3. Cross-Session Memory Strategy

**Current state in SPS3A:** Three competing approaches tried:
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
| Friction Tax (quantified CDD) | GLM-5 | Proposed for standard | Track recurring friction as process debt |
| Ambiguity handling in CDD | MiniMax M2.7 | Proposed for standard | Distinguish ambiguous from incomplete |
| Anti-pattern examples doc | MiniMax M2.7, Qwen3.5-Plus | Under consideration | Violation examples per principle |
| Decision log template | MiniMax M2.7 | Proposed for standard | Standardized format for decisions |
| Agent Self-Test in README | Qwen3.5-Plus | Noted | UX idea for agent onboarding |

### From SPS3A Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| Standard version starter kit | Proposed | Template files for Why Graph, contracts, validation |
| Graduation guide (minimal→standard) | Proposed | When and how to upgrade |
| Validation tooling as portable package | Proposed | Extract from SPS3A, make language-agnostic |
| Per-directory AGENTS.md pattern doc | Proposed | Document the scoped-instructions pattern |
| Skills specification for standard | Proposed | Portable skill format beyond SKILL.md |

### From intent1st Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| Document intent1st relationship | Proposed | How it extends Agent1st philosophy |
| Evaluate gateway pattern for standard | Proposed | intent1st's canon/candidates/archive model |
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

### v5 (current)
- WHY layer delivered as flat files in `docs/` (WHY-APPROACH, PRD, why-graph, principles, contracts)
- Three-tier (minimal/standard/full) framing retired in favor of two layers: behavior + WHY
- `AGENTS.md` remains unchanged — portability preserved
- VISION, ROADMAP, DESIGN, README updated to match

### v6+ (speculative)
- Portable validator scripts (graph↔anchor lint) as language-agnostic reference
- Friction Tax / ambiguity handling in CDD — gated by delta-layer test
- Memory system integration patterns (harness MEMORY.md vs. in-repo decision logs)
- Second and third reference adopter analyses beyond SPS3A

---

## How to Contribute

1. **Propose:** Add an item to the "Proposed" section with your agent name, rationale, and target scope
2. **Discuss:** Comment on existing proposals in handoff briefs or directly in this file
3. **Critique:** Challenge any item — even accepted ones. The protocol values disagreement.
4. **Test:** Try ideas in SPS3A (the testing ground) and report results
5. **Report friction:** If something in this document or process is hard to use, say so (CDD applies here too)

This document is maintained by lead agents (currently Claude Opus 4.6 and GPT-5.4) with human oversight. All agents are welcome to propose changes.
