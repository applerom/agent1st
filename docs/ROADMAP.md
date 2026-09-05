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
- [x] Documented in README.md Quick Start section — **done 2026-08-29 (v11)**

**Correction (v11).** The third box was checked on 2026-03-25 while the README only said the two files "work alongside" each other. The actual instruction — add `CLAUDE.md` containing `@AGENTS.md` — was never written down on the public surface, so every Claude Code adopter following Quick Start got zero protocol and no error. Found by re-testing the claim instead of reading it: on Claude Code 2.1.251 a bare root `AGENTS.md` does not load, the bridged one does. A false checkbox in the tracker of the project that wrote "Done Is Not a Mood" is the most useful bug this release found. Done was not a mood here either.

### 3. Cross-Session Memory Strategy

**Current observed state:** Three competing approaches tried in downstream adopters:
1. `decision-context.xml` — custom XML decision memory. **Assessment by human: not great.** Non-standard, hard to maintain.
2. A skill-based intent gateway (development-side prototype, not public) — durable meaning reached through skills. **Assessment: good concept, poor adoption.** Models forget to use skill-based access. Closed on the public surface in v13.1: no probe, no date, and harness-native memory now covers the surface it addressed.
3. Claude Code `MEMORY.md` — built-in, automatic. Standard for Claude Code users.

**Direction for Agent1st:**
- Behavior layer (`AGENTS.md`): no memory prescription — stays in harness layer.
- WHY layer: recommend **durable artifacts** (already in Durable State) without prescribing format.
- Project-local extensions: each project picks a memory system that fits its harness (e.g., Claude Code `MEMORY.md`, skill-based gateways, repo-local decision logs). Not a portable concern.

**Open question:** Should the WHY layer recommend a specific memory format, or just principles for memory hygiene?

Current leaning: no single memory location is portable enough to prescribe. The useful future artifact is likely a decision guide — when to use harness memory, repo decision logs, skills, or a hybrid — not a new required file.

### 3a. Held Items Need a Probe or a Date (v11)

**Problem observed in v11:** eight ROADMAP items and most of the development-side backlog sit in **Held — awaiting signal**, some since March. The gate is real and correct (nothing speculative enters stable), but it is *passive*: it waits for an adopter to independently hit a surface, with no probe that would produce the signal and no date at which the wait expires. A passive gate silently converts into a permanent hold.

**Rule from v11 onward:** every `Held` item carries one of three things.

- **Probe** — the smallest concrete action that would produce the signal, and who runs it.
- **Date** — when the wait expires and the item is re-decided with whatever evidence exists.
- **Reject** — say so. A hold with neither probe nor date is a rejection that lacks the courage to be one.

WHY: Done Is Not a Mood. The inverse also holds — *pending* is not a mood. An item nobody is measuring and nobody will revisit is finished, and the honest move is to write that down.

### 3b. Keep the graduation accountable to use

Six is the current result, not the target. If route ownership, honest completion,
or useful dissent regresses, capture the task and effective instructions.
Repair the smallest missing behavior.

If the cause is unclear, compare v13 with archived v12.1 under the same model,
harness, tools, and task. Isolate inherited instructions and memory. Add generic
advice as a control only when the wording itself is the question.

No standing benchmark queue. The old pilot assignment is retired; no results
are claimed. Measure to choose a change, not to justify having a practice.

### 4. Success Signals and Public Evidence

Make the approach easy to inspect and try. Measure specific claims; let working examples carry the teaching.

**Open questions:**
- Which lightweight signals show reduced agent drift without becoming process theater? Candidates: repeated-mistake rate, stale graph/anchor repairs, handoff reuse, time-to-orientation for fresh agents, and human correction load. An external full-project review (GPT-5.5-pro, 2026-06-11) added three countable probes to the pool: re-edit count after an agent handoff, share of tasks closed with reproducible evidence, and nearest-plausible-file incidents before vs after Why1st adoption.
- How should reference-adopter evidence move from private development notes to public links as projects mature? Current stance: early or unstable adopter examples stay described by shape and stack; public, stable adopters can be linked after review.
- First public candidate to track: [`applerom/harness-observatory`](https://github.com/applerom/harness-observatory), an Agent1st/Why1st-adjacent local-first research app. Do not promote it from candidate to canonical example until its examples are stable enough not to mislead adopters.

### 5. Graph Version Fields — resolved in v8.1

**Resolution:** removed. The abstract `schema="0.8"` and `<PROJECT VERSION="...">` fields were inertia from before Why1st was a named project; they were never tied to an XSD, validator compatibility contract, or migration rule. Validator behavior, the `<PROJECT DATE="...">` attribute, and git history carry actual evolution semantics. A real version field can be added later if and when one earns concrete semantics.

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

### From a skill-based intent-gateway prototype (2026-03-25) — closed in v13.1

A development-side prototype kept durable project meaning behind skills (canon / candidates / archive). It is not public, so the public surface describes it by shape only. All three items sat as *Proposed* for five months with no probe and no date; under §3a that is a rejection, recorded here so it is not re-litigated.

| Proposal | Status | Notes |
|----------|--------|-------|
| Document the gateway's relationship to Agent1st | Rejected (v13.1) | Private artifact; nothing for a public reader to open |
| Evaluate the canon/candidates/archive gateway for the WHY layer | Rejected (v13.1) | Harness memory plus repo decision logs now cover the surface; §3 keeps the memory question open without this candidate |
| Assess the SKILL.md adoption barrier | Closed (v13.1) | Observed answer: models do not reliably use skill-gated context; recorded in §3 above |

### From GRACE Marketplace audit (2026-04-29)

A parallel public project ([osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)) independently arrived at prompt-XML tags, contracts near code, and graph-anchored validators. The audit (kept in lab notes, not on the public surface) extracted candidates worth **holding** until an adoption signal proves they earn their tokens — the v6→v8 spirit-pass discipline says no preemptive ceremony.

| Proposal | Status | Awaiting signal |
|----------|--------|----------------|
| Borrow "closing-tag polysemy" naming into `why-graph-principles.md` §2a | Held | An adopter who reads §2a's three forces but still regresses to generic `<node>` — the existing wording empirically worked for one cold-start adopter |
| Public/shared vs file-local/private boundary line in `why-contracts-v1.md` | Held | An adopter graph that bloats with private helpers — not yet observed |
| Validator warning on classical-XML anti-patterns (`<node>`, `<Module ID=...>`, `<?xml ?>`) | Held | Cold-start regressions that v7 §2a docs alone don't catch — not yet observed |
| Operational-packet shape (execution / graph delta / verification delta / failure / checkpoint) as a `docs/agent-orchestration.md` template | Held | A real Why1st adopter doing recurring subagent delegation needing more shape than `Why1st.md §11.3` |
| Validator issue codes + remediation strings | Held | Validator UX complaints that the current CDD-style messages don't address |
| Optional "autonomous readiness" validator profile | Held | Adopter request for a stricter pre-shipping check than the standard graph/anchor lint |

### From GPT-5.5-pro full-project review (2026-06-11)

The review's terraform-skill fixes landed directly in the experimental artifact (see `docs/experiments/terraform-agent1st.md`, Revision log). Two project-level proposals are held:

| Proposal | Status | Awaiting signal |
|----------|--------|----------------|
| Enterprise one-pager — the same rules restated in neutral policy-reader tone | Held | An actual enterprise adopter blocked by the manifesto tone; DESIGN treats the tone as load-bearing, so a parallel artifact needs demand, not prediction |
| Sharpen in README that Agent1st does not replace project-specific docs | Held | An observed misreading; the reviewer itself reconstructed the layering correctly from the current surface, which is evidence against urgency |

---

## Rejected (With Reasons)

See `docs/EVOLUTION.md` "Recurring Rejected Patterns" for full list. Key recurring rejections:
- Fresh-eye scan at session start (delta-layer + multi-agent waste)
- Error recovery rules (harness layer)
- Scope discipline (model layer)
- Output formatting (harness layer)
- Session boundary assumptions (agents don't control compaction)

---

## Next

Version decisions live in [`EVOLUTION.md`](EVOLUTION.md).

*Hypotheses without observed adoption-failure signal should land in `docs/experiments/` first. Entries here are gated either by a delta-layer test or by known-failure signal already in hand.*

- Friction Tax / ambiguity handling in CDD — gated by delta-layer test
- Memory system integration patterns (harness MEMORY.md vs. in-repo decision logs vs. skill-based gateways) — likely a decision guide, not a required artifact
- Adopter prompt template (one-shot copy-paste for Why1st adoption) only if v7 + v8 docs alone don't land for cold-start agents
- Validator extension: lint that emitted log anchors resolve to graph entries (only if §11.1 adoption requests it)

---

## How to Contribute

1. **Propose:** Add an item to the "Proposed" section with your agent name, rationale, and target scope
2. **Discuss:** Comment on existing proposals in handoff briefs or directly in this file
3. **Critique:** Challenge any item — even accepted ones. The protocol values disagreement.
4. **Test:** Try ideas in a real downstream project and report results
5. **Report friction:** If something in this document or process is hard to use, say so (CDD applies here too)

Agents and humans shape the work together. Bring a useful change.
