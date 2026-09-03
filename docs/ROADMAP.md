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
2. `intent1st` — durable meaning via skills. **Assessment: good concept, poor adoption.** Models forget to use SKILL-based access.
3. Claude Code `MEMORY.md` — built-in, automatic. Standard for Claude Code users.

**Direction for Agent1st:**
- Behavior layer (`AGENTS.md`): no memory prescription — stays in harness layer.
- WHY layer: recommend **durable artifacts** (already in Durable State) without prescribing format.
- Project-local extensions: each project picks a memory system that fits its harness (e.g., Claude Code `MEMORY.md`, intent1st skills, repo-local decision logs). Not a portable concern.

**Open question:** Should the WHY layer recommend a specific memory format, or just principles for memory hygiene?

Current leaning: no single memory location is portable enough to prescribe. The useful future artifact is likely a decision guide — when to use harness memory, repo decision logs, skills, or a hybrid — not a new required file.

### 3a. Held Items Need a Probe or a Date (v11)

**Problem observed in v11:** eight ROADMAP items and most of the development-side backlog sit in **Held — awaiting signal**, some since March. The gate is real and correct (nothing speculative enters stable), but it is *passive*: it waits for an adopter to independently hit a surface, with no probe that would produce the signal and no date at which the wait expires. A passive gate silently converts into a permanent hold.

**Rule from v11 onward:** every `Held` item carries one of three things.

- **Probe** — the smallest concrete action that would produce the signal, and who runs it.
- **Date** — when the wait expires and the item is re-decided with whatever evidence exists.
- **Reject** — say so. A hold with neither probe nor date is a rejection that lacks the courage to be one.

WHY: Done Is Not a Mood. The inverse also holds — *pending* is not a mood. An item nobody is measuring and nobody will revisit is finished, and the honest move is to write that down.

### 3b. v13 Graduation Check

**Change under test:** v13 removes Role Contract, Done Is Not a Mood, and Right to Disagree from the every-task file. The ideas stay; the repeated instructions leave. Exact v12.1 is the control, not a second product.

**Smallest useful probe:** run the same bounded tasks with current v13, archived v12.1, and an equal-size placebo. Blind-grade:

- route ownership and unnecessary pauses;
- completion honesty and evidence quality;
- useful dissent when the request is wrong;
- semantic naming errors;
- delegation-contract quality;
- durable state left for the next agent;
- human comprehension of the working relationship after reading the file.

**Stop rule:** if a departed behavior regresses, restore the smallest missing atom. If nothing moves, keep six. Six is the result, not the target.

### 4. Success Signals and Public Evidence

**Current state:** `docs/PRD.md` names success signals, but Agent1st does not yet define how to measure "less drift" without creating ceremony.

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

### From intent1st Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| Document intent1st relationship | Proposed | How it extends Agent1st philosophy |
| Evaluate gateway pattern for WHY layer | Proposed | intent1st's canon/candidates/archive model |
| Assess SKILL.md adoption barrier | Open question | Models don't reliably use skill-based access |

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

### v8
- New cold-start reference-adopter audit produced three small Tier-1 fixes plus three opt-in extension patterns:
  - **§2a "do not compress" guard** in `why-graph-principles.md` — when adopters copy the file locally and shorten it, retain at minimum the load-bearing rationale anchors. New meta-failure: agent A writes correct graph + compressed local guide → agent B loses the WHY
  - **Pin-vs-reference** sharpening in `Why1st.md` §8 — pin always: `AGENTS.md` + `PRD.md` + `why-graph.xml`; reference on demand: principles, contracts, validator. Stops cold-start adopters from pinning 8+ files as context tax
  - **"Don't edit the Core" clarity** in `Why1st.md` §8 — Hello Agent tweaks, output-contract exceptions, harness handshake refinements go in the addendum **above** the separator, not inside the Core. Common adoption mistake named explicitly
- New `Why1st.md §11` "Optional extensions for real-project surfaces" — three opt-in patterns for projects that need them, hard partition from canonical chain:
  - 11.1 Semantic logs as future agent context — runtime events with anchor names matching the graph, so a model can grep across logs ↔ graph ↔ code
  - 11.2 Tests and UI evidence — agent self-sufficiency: the agent sets up Playwright/snapshots/test harness itself instead of asking the human
  - 11.3 Subagent orchestration as project-local pattern — `docs/agent-orchestration.md` style is project-local extension, not Agent1st core
- AGENTS.md untouched
- Includes drop-in surface cleanup from a Codex-side audit: public history docs no longer reference the gitignored development-side folder; `applerom/harness-observatory` named as a public reference candidate (only because it is a public GitHub repo)

### v8.1
- Drop noise: `schema="0.8"` and `<PROJECT VERSION="0.8">` removed from the teaching graph. The fields were inertia from before Why1st was a named project — never tied to an XSD or migration rule. Closes the v8 open question on graph/schema version fields
- `docs/why-graph-principles.md` §2 root-and-schema paragraph rewritten to match: graph carries no abstract version field; rely on validator behavior, `<PROJECT DATE>`, and git history
- PRD §10 and ROADMAP §5 marked resolved
- Stale handoffs cleanup landed alongside (Codex-side commit `7ffffa1`): 11 v3/v4/v5-era raw review files removed from `docs/handoffs/`. Curated conclusions stay in `EVOLUTION.md`; raw old reviews were creating misleading `rg` results for fresh agents
- A development-side audit of GRACE Marketplace (a parallel public project that independently rediscovered prompt-XML, contracts near code, and validators) confirmed the Why1st thesis. Borrow candidates extracted but **not** landed — held in §"From GRACE Marketplace" pending an adoption signal
- AGENTS.md untouched

### v8.2
- New paired file `docs/why-semantic-logs.md` extracts §11.1 depth: minimum event shape (required vs conditional fields), why semantic logs work for transformer-based agents (parallel structure to `why-graph-principles.md` §2a — vocabulary stability, same-string grep across layers, attention finite per AGENTS.md §4), where logs live (JSONL first), the smallest useful slice (6 steps), what semantic logs are *not*, anti-patterns
- `Why1st.md` §11.1 updated: field shape corrected, cross-link added to the new pair file. The five-paragraph version stays as the entry; new file is the depth
- Triggered by a real adopter who already had the Agent1st+Why1st base in place and asked for implementation guidance for §11.1. v8 EVOLUTION had explicitly held depth back ("if adopter feedback shows §11.1 needs more depth, extract later") — that signal arrived
- AGENTS.md untouched. Canonical chain unchanged. Hard partition between chain and §11 extensions preserved (no new graph ARTIFACT entry)

### v8.3
- New paired file `docs/why-subagents.md` extracts §11.3 depth with a behavioral re-pointing: the v8 brief was artifact-focused ("where does subagent know-how live"), but the actual cross-project adopter friction is *behavioral* — strong agents trained on agentic work default to single-thread solo execution. New file leads with when an agent defaults to delegation; names the four delegation shapes (parallel exploration, fan-out validation, deep-dive isolated work, lower-intelligence ops); gives the contract structure, the lead-vs-delegate line, anti-patterns; treats the project-local artifact as the second move that crystallizes lived patterns
- `Why1st.md` §11.3 re-pointed: heading and lead paragraph now lead with behavior, artifact framing stays as second paragraph, cross-link to depth doc added
- Anthropic *Building Effective Agents* cited as the canonical external anchor — orchestrator-worker / parallelization / evaluator-optimizer is the framework default; do-it-all-myself is the regression
- Triggered by user-reported recurring cross-project field signal plus three of seven external agent reviewers (GPT-5.5-pro, Kimi 2.6, Muse-Spark) independently flagging subagent-delegation regression
- AGENTS.md untouched. Canonical chain unchanged. Hard partition preserved

### v8.4
- New paired file `docs/why-evidence.md` extracts §11.2 depth with a behavioral re-pointing and an explicit architectural position: agents own their own verification loop; default to **Playwright CLI** for browser/UI evidence, reach for MCP only when its structured I/O is load-bearing (MCP tool definitions cost context whether you use them or not). Four evidence tiers (unit/integration, API/protocol-shape, UI/visual, semantic-log assertions over fixtures); the four-step agent-owns-it pattern (try → name the block → fall back to next-best evidence → never silently substitute "trust me"); anti-patterns including "spin instead of work" and "MCP-by-default for browser tooling"
- `Why1st.md` §11.2 re-pointed: heading extended to "agents own their own verification loop"; behavior leads (agent looks at the rendered page, not the human); CLI-over-MCP trade-off surfaced inline so the brief alone communicates the load-bearing position; cross-link to depth doc added
- Companion wave to v8.3, separate commit and separate delta. Pattern across v8.2–v8.4 now explicit: brief in v8 → adopter pull → spirit-pass through Why1st voice → depth doc in `why-*` namespace + behavioral re-pointing
- AGENTS.md untouched (byte-identical to v5.1 since v6 — nine versions of discipline). Canonical chain unchanged. Hard partition preserved

### v8.5
- `docs/why-contracts-v1.md` §6 strengthened: explicit cross-references to AGENTS.md §4 (Attention Engineering) and §5 (Semantic Hygiene) so contracts are named as the file-level realization of those principles. **Greppability** named as a deliberate property of the shape (English, upper-case, anchored after `:`), not just a side effect of "deterministic validation." **LINKS as dependency map** surfaced as the field an agent reads before changing a method — the alternative is grep-and-guess
- New `docs/experiments/` directory introduced as a parallel track for hypotheses that have not yet earned a place in stable. Hard partition from canonical chain and from `Why1st.md` §11 stable extensions. Not linked from the main README "Optional extensions" table by design. Stable continues to evolve only under spirit-pass discipline; experiments hold ideas that need empirical signal first. Lifecycle (open / promoting / resolved), no fixed timelines, treated as a labeled side-track like in many packaged systems
- First experiment: `docs/experiments/hieroglyph-anchors.md` — replace one contract field key (PURPOSE) with a single CJK character (`旨`); hypothesis explicitly worth running because the answer is unknown; three measurable falsifiability criteria (token cost, attention/recall in long context, greppability); §5 tension acknowledged up front
- AGENTS.md untouched. Canonical chain unchanged. No new "Optional extensions" entry — experiments are deliberately separate

### v9-v11
- v9 / v9.1: model-shift register and stronger research grounding; core correctly remained frozen
- v10: PRD anchors made graph references refactor-proof
- v11: first core edit in 123 days; acceptance-criteria contradiction repaired and Claude Code bridge verified

### v12
- One ordinary `AGENTS.md`, 165 lines, 9 separate principles
- Exact frozen v5.1 and Opus 5 v11 files preserved in `docs/_archive/`
- Agent Loop and the standalone weak-signal principle retired after harness absorption
- Universal numeric file thresholds removed; Attention Engineering remains
- Multi-artifact instruction topology from the first draft rejected; protocol voice and human-facing teaching role restored
- Evaluation continues in Active Priority §3b

### v13
- Role Contract, Done Is Not a Mood, and Right to Disagree graduate from every-task instruction to teaching surface and archive
- Six principles remain because six still change work; no seventh heading is manufactured from scraps
- Exact nine-principle v12.1 preserved in `docs/_archive/`
- Why1st grows in relative importance without moving into the minimal core
- Evaluation continues in Active Priority §3b

### Next
*Hypotheses without observed adoption-failure signal should land in `docs/experiments/` first. Entries here are gated either by a delta-layer test or by known-failure signal already in hand.*

- Friction Tax / ambiguity handling in CDD — gated by delta-layer test
- Memory system integration patterns (harness MEMORY.md vs. in-repo decision logs vs. skill-based gateways) — likely a decision guide, not a required artifact
- Anchor adoption in this repo's own `docs/` so the validator graduates from doc-only mode to enforced anchors
- Adopter prompt template (one-shot copy-paste for Why1st adoption) only if v7 + v8 docs alone don't land for cold-start agents
- Validator extension: lint that emitted log anchors resolve to graph entries (only if §11.1 adoption requests it)

---

## How to Contribute

1. **Propose:** Add an item to the "Proposed" section with your agent name, rationale, and target scope
2. **Discuss:** Comment on existing proposals in handoff briefs or directly in this file
3. **Critique:** Challenge any item — even accepted ones. The protocol values disagreement.
4. **Test:** Try ideas in a real downstream project and report results
5. **Report friction:** If something in this document or process is hard to use, say so (CDD applies here too)

This document is maintained by lead agents (currently Opus and GPT) with human oversight. All agents are welcome to propose changes.
