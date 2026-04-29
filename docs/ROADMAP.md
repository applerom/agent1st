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

Current leaning: no single memory location is portable enough to prescribe. The useful future artifact is likely a decision guide — when to use harness memory, repo decision logs, skills, or a hybrid — not a new required file.

### 4. Success Signals and Public Evidence

**Current state:** `docs/PRD.md` names success signals, but Agent1st does not yet define how to measure "less drift" without creating ceremony.

**Open questions:**
- Which lightweight signals show reduced agent drift without becoming process theater? Candidates: repeated-mistake rate, stale graph/anchor repairs, handoff reuse, time-to-orientation for fresh agents, and human correction load.
- How should reference-adopter evidence move from private development notes to public links as projects mature? Current stance: early or unstable adopter examples stay described by shape and stack; public, stable adopters can be linked after review.
- First public candidate to track: [`applerom/harness-observatory`](https://github.com/applerom/harness-observatory), an Agent1st/Why1st-adjacent local-first research app. Do not promote it from candidate to canonical example until its examples are stable enough not to mislead adopters.

### 5. Graph Version Fields

**Current state:** the teaching graph and examples still use `schema="0.8"` and `<PROJECT VERSION="...">`, but those fields are not tied to an XSD, validator compatibility contract, or concrete migration rule.

**Open question:** should Why1st remove abstract graph/schema version fields and rely on validator compatibility, dates, and git/content history instead?

Current leaning: remove or demote them unless a future validator/package release gives them real semantics. Until then, agents should treat them as an unresolved design question, not as proof that a formal schema exists.

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

### v6.1
- Why1st adopted as a short name for the WHY-first approach/layer, distinct from Agent1st (the behavior contract)
- Entry doc renamed `docs/WHY-APPROACH.md` → `docs/Why1st.md`; README promoted `## Why1st` to a level-2 heading with its own anchor
- One-file `docs/PRD.md` starter stance documented as valid, with extraction only when useful
- Stale v6 teaching-surface residue fixed (`No validators yet`, `four files`, module-family examples)
- Validator generalized: anchor checks apply to any node with `<ANCHOR>` children, not just `MODULE_*`
- Reference adopter analyses moved off-public (kept for development-side use only) so the public protocol does not name projects readers cannot access

### v7
- Why1st format spirit named explicitly. New `docs/why-graph-principles.md` §2a "Tag shapes — prompt-XML, not classical XML" with side-by-side good/bad and an anti-patterns list — the load-bearing change
- Light pointers in `docs/Why1st.md` and `docs/why-contracts-v1.md` so the spirit lands at the right moment of reading
- Triggered by a real downstream adopter's first attempt simplifying the graph to `<?xml ?> + <nodes><node id kind> + <relations>` style. Diagnosis: words "graph" and ".xml" pull strong agents toward classical defaults; the v6 docs documented *what* but not *why*
- Verified before ship: fresh subagent given only updated docs + a tiny fictional PRD produced canonical prompt-XML on first attempt
- AGENTS.md untouched
- **Empirical confirmation:** a real cold-start adopter (PRD-only, agent told to read `#why1st`) produced a working app with a valid prompt-XML graph, 11 anchors, 21 unit tests, and module contracts on 16 files in its first version

### v8 (current)
- New harmon1st-style cold-start audit produced three small Tier-1 fixes plus three opt-in extension patterns:
  - **§2a "do not compress" guard** in `why-graph-principles.md` — when adopters copy the file locally and shorten it, retain at minimum the load-bearing rationale anchors. New meta-failure: agent A writes correct graph + compressed local guide → agent B loses the WHY
  - **Pin-vs-reference** sharpening in `Why1st.md` §8 — pin always: `AGENTS.md` + `PRD.md` + `why-graph.xml`; reference on demand: principles, contracts, validator. Stops cold-start adopters from pinning 8+ files as context tax
  - **"Don't edit the Core" clarity** in `Why1st.md` §8 — Hello Agent tweaks, output-contract exceptions, harness handshake refinements go in the addendum **above** the separator, not inside the Core. Common adoption mistake named explicitly
- New `Why1st.md §11` "Optional extensions for real-project surfaces" — three opt-in patterns for projects that need them, hard partition from canonical chain:
  - 11.1 Semantic logs as future agent context — runtime events with anchor names matching the graph, so a model can grep across logs ↔ graph ↔ code
  - 11.2 Tests and UI evidence — agent self-sufficiency: the agent sets up Playwright/snapshots/test harness itself instead of asking the human
  - 11.3 Subagent orchestration as project-local pattern — `docs/agent-orchestration.md` style is project-local extension, not Agent1st core
- AGENTS.md untouched
- Includes drop-in surface cleanup from a Codex-side audit: public history docs no longer reference `.lab/` paths; `applerom/harness-observatory` named as a public reference candidate (only because it is a public GitHub repo)

### v9+ (speculative)
- Friction Tax / ambiguity handling in CDD — gated by delta-layer test
- Memory system integration patterns (harness MEMORY.md vs. in-repo decision logs vs. skill-based gateways) — likely a decision guide, not a required artifact
- Anchor adoption in this repo's own `docs/` so the validator graduates from doc-only mode to enforced anchors
- Adopter prompt template (one-shot copy-paste for Why1st adoption) only if v7 + v8 docs alone don't land for cold-start agents
- Versioning simplification — decide whether `schema="0.8"` and `<PROJECT VERSION="...">` earn their place, or whether Why1st should drop abstract version fields in favor of dates, validator compatibility, and git history
- Validator extension: lint that emitted log anchors resolve to graph entries (only if §11.1 adoption requests it)

---

## How to Contribute

1. **Propose:** Add an item to the "Proposed" section with your agent name, rationale, and target scope
2. **Discuss:** Comment on existing proposals in handoff briefs or directly in this file
3. **Critique:** Challenge any item — even accepted ones. The protocol values disagreement.
4. **Test:** Try ideas in a real downstream project and report results
5. **Report friction:** If something in this document or process is hard to use, say so (CDD applies here too)

This document is maintained by lead agents (currently Claude Opus 4.6 and GPT-5.4) with human oversight. All agents are welcome to propose changes.
