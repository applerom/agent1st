# Agent1st Protocol — Evolution History

Every version changed because something failed in practice. This document captures what failed, what changed, and what got rejected — so the next agent doesn't re-propose what was already tried.

Agents who contribute to new versions should add their transition notes.

---

## Version Map

| Version | File | Focus | Agent Contribution |
|---------|------|-------|--------------------|
| v0 | (no file) | Scattered ideas in conversations | — |
| v1 | `docs/_archive/AGENTS-min-v1.md` | First formalization. Early friction/evidence/attention contract. | [TBD — author to fill] |
| v2 | `docs/_archive/AGENTS-min-v2.md` | More agentic. Agent Loop added. Anti-micromanagement sharper. | [TBD — author to fill] |
| v3 | `docs/_archive/AGENTS-min-v3.md` | Harness-optimized. Delta-layer discipline. Core/Ops split. | GPT-5.4 agent (primary), with Claude Opus 4.6 comparison |
| v4 | `docs/_archive/AGENTS-min-v4.md` + `AGENTS.md` | Minimal baseline. Multi-agent autonomy and delegation design. | Claude Opus 4.6 agent (primary), building on GPT-5.4 v3 rationale |
| v5 | `AGENTS.md` (unchanged) + `docs/Why1st.md` + paired WHY files | WHY layer delivered as flat files in `docs/`. Three-tier framing retired. | Claude Opus 4.6 (primary), with reference analysis of one Python/FastAPI adopter and one TypeScript adopter |
| v5.1 | same files, sharpened | External-review integration round. Staleness named as first-class failure. Workflow shape stops being a universal law. Teaching-surface bugs fixed. | Claude Opus 4.6 (primary), integrating external reviews from GPT-5.4, MiniMax M2.7, Kimi K2.5, Qwen 3.6, Grok 4.20, plus off-target input from Gemini 3.1, Claude Opus 4.7, and Meta-Muse Spark |
| v6 | `scripts/validate-why.py` + paired doc updates; `AGENTS.md` byte-identical to v5.1 | WHY validator MVP lands. `AGENTS.md` survives the spirit pass unchanged: §1 deferred at the front door, §8 + §9 candidate edits initially landed then reverted. The v6 process contribution is the spirit-pass discipline itself. | Claude Opus 4.7 (primary), filtering GPT-5.5-pro's `docs/handoffs/v6-handoff-gpt-5.5-pro.md` and a Codex-native adopter's adaptation through the spirit lens |
| v6.1 | `docs/Why1st.md` Why1st short name + validator generalization + public/private surface cleanup | Why1st named as a short alias for the WHY-first approach/layer (not a second behavior protocol). Validator generalized from `MODULE_*`-only to any node with anchors. Reference-adopter analyses moved off-public so the public protocol does not point at projects readers cannot access. Stale v6 teaching-surface residue fixed. | GPT-5.5 Codex (initial pass) + Claude Opus 4.7 (spirit pass and surface cleanup) |
| v7 | `docs/why-graph-principles.md` §2a (load-bearing) + light pointers in `Why1st.md` and `why-contracts-v1.md` | Why1st format spirit named: graph file is *prompt-XML*, not classical XML or graph-DB schema. New §2a "Tag shapes — prompt-XML, not classical XML" with the three forces (transformer attention, greppability, semantic interference), side-by-side good/bad examples, and an anti-patterns list. Triggered by a real downstream adopter cold-reading `#why1st` and silently simplifying to `<?xml ?> + <nodes><node id="..." kind="..."> + <relations>` — the rationale was missing from v6 docs, not the format. Verified before ship: a fresh subagent given only the updated docs + a tiny fictional PRD produced canonical prompt-XML. | Claude Opus 4.7 (primary) |
| v8 | `Why1st.md` §8 sharpening + new §11 (three opt-in extensions) + `why-graph-principles.md` §2a "do not compress" guard | After v7 was empirically verified by a cold-start adopter (PRD-only, real working app produced), a focused audit surfaced three small Tier-1 fixes (compression-failure guard, pin-vs-reference, "don't edit the Core") plus three opt-in extension patterns (semantic logs / tests + UI / subagent orchestration). All extensions are opt-in with hard partition from the canonical chain (PRD → Why Graph → contracts → validator). AGENTS.md untouched. | Claude Opus 4.7 (primary), with Codex-side audit by GPT-5.5 |
| v8.1 | `docs/why-graph.xml`, `why-graph-principles.md` §2, PRD §10, ROADMAP §5; stale handoffs pruned | Closing pass after v8: drop the `schema="0.8"` and `<PROJECT VERSION="0.8">` inertia fields (never tied to an XSD or migration rule); close the corresponding open question; prune 11 v3/v4/v5-era raw review files from `docs/handoffs/` because they created misleading `rg` results for fresh agents (curated conclusions stay in this file). A development-side audit of a parallel public project (GRACE Marketplace) confirmed the Why1st thesis but produced no public-surface change — borrow candidates parked in ROADMAP "Proposed" with explicit "awaiting adoption signal" gates. AGENTS.md untouched. | GPT-5.5 Codex (handoffs pruning + open-question framing in commit `7ffffa1` + GRACE audit) and Claude Opus 4.7 (version-field removal, EVOLUTION/ROADMAP integration, advisor pressure-test) |
| v8.2 | new `docs/why-semantic-logs.md` + `Why1st.md` §11.1 cross-link | Promised in v8 EVOLUTION ("§11.1 is concise on purpose; if adopter feedback shows §11.1 needs more depth, extract later") and triggered by a real adopter who already had Agent1st+Why1st in place and asked for implementation guidance for semantic logs. The new pair file extracts §11.1 to depth: minimum event shape (required vs conditional fields), why this works for transformer-based agents (vocabulary stability, same-string grep across layers, attention finite), where logs live (JSONL first), the smallest useful slice, and anti-patterns. The load-bearing claim is unchanged from §11.1 — the `anchor` field uses verbatim Why Graph and code-anchor names, so one grep lands in three artifacts. AGENTS.md untouched; canonical chain unchanged; the new file is an opt-in extension paired with §11.1, not a new layer. | GPT-5.5 Codex (initial draft distilled from cross-project reference analysis in development-side notes) and Claude Opus 4.7 (spirit pass — lead with WHY at top, transformer-attention §3 added in parallel to `why-graph-principles.md` §2a, Playwright digression dropped to §11.2 cross-link, implementation slice tightened to 6 steps) |
| v8.3 | new `docs/why-subagents.md` + `Why1st.md` §11.3 re-pointed to behavior | Triggered by recurring cross-project adopter signal: agents adopt Agent1st+Why1st canonical chain well, then revert to single-thread *do-it-all-myself* mode on real work — missing parallelism, burning context, paying frontier-tier prices on mechanical ops. Three of seven agent reviewers independently flagged the same gap (Opus 4.7's lower default fan-out). The v8 §11.3 brief was artifact-focused ("where does subagent know-how live"); the user friction is *behavioral* (agents don't default to delegation in the first place). The new pair file leads with the behavioral question — when does an agent default to delegation — names four delegation shapes (parallel exploration, fan-out validation, deep-dive isolated work, lower-intelligence ops), gives the contract structure, the "what to delegate vs do yourself" line, anti-patterns, and treats the project-local artifact (`docs/agent-orchestration.md`) as the second move that crystallizes patterns the lead has already used. Anthropic's *Building Effective Agents* cited as the canonical external anchor — the do-it-all-myself default is the regression, not the bias toward delegation. The §11.3 brief in `Why1st.md` re-pointed: behavior leads, artifact follows, cross-link added. AGENTS.md untouched; canonical chain unchanged; hard partition between chain and §11 extensions preserved (no new graph ARTIFACT entry). | Claude Opus 4.7 (primary), with seven external agent reviews ratifying the v5.1 byte-freeze and three (GPT-5.5-pro, Kimi 2.6, Muse-Spark) independently flagging the subagent-delegation gap as the live signal |

---

## v0 → v1: From Scattered Ideas to First Protocol

**Era:** Early agent-work contract. Still partly copilot-era in language, already reacting to real friction.

**What happened:**
- Inference from the archived file and later handoffs: v1 appears to have emerged from repeated real-session failures around silent friction, vague completion claims, scattered context, and weak handoffs. It was not yet a full harness theory, but it was already more than generic prompt advice.

**Key decisions in v1:**
- 10 sections, flat structure (no hierarchy)
- CDD (Complaint-Driven Development) introduced as section #1
- CDD sat at the top because it was both a practical rule and a strong human hook
- "Educational by Default" included — adaptive explanation depth
- "Harness (Validation + Observability)" as separate section
- "Session Start + Session End" combined in one section
- Example complaint included for concreteness
- `Hello Agent!` activation phrase introduced

**What v1 got right:**
- Even this early version already centered friction, evidence, attention, and role shaping — later versions mostly reorganized and sharpened these themes
- CDD was original and stayed in every version
- Putting CDD first was an intentional adoption move, not an accident of ordering
- WHY / IF MISSING pattern established from the start
- The overall inventory of concerns was surprisingly complete

**What v1 got wrong:**
- Flat structure made scanning hard
- "Educational by Default" was a style preference, not a protocol principle
- Framing was still somewhat copilot-era: the agent was already more than autocomplete, but ownership was not yet stated with the later clarity
- Harness section tried to cover too much

---

## v1 → v2: Becoming More Agentic

**Era:** Agent as executor with own judgment, not just a helper.

**What happened:**
- Inference from the file delta: v2 was an iterative tightening pass, not a philosophy reset. It added a reusable work loop, reduced redundancy, and pushed the protocol closer to an agent-partner stance without naming all of that design logic yet.

**Key changes:**
- Added **Agent Loop: Explore → Execute → Reflect** as explicit principle
- Merged fresh-eye audit into Agent Loop (was standalone in v1's Session Start)
- Strengthened Role Contract: "Agent owns implementation, reasoning path, verification, and alternatives"
- Added "assumptions/invariants" and "rejected paths" to handoff
- Removed some redundancy, foreshadowing the later delta-layer discipline even before it had a name
- Kept flat structure (10 sections, no hierarchy)

**Key decisions:**
- "Collaboration style" subsection added: "human sets destination and boundaries, agent chooses the route"
- This was the first explicit anti-micromanagement signal, though the surrounding framing still sounded more manager/executor than later versions
- The rewrite already showed an instinct not to duplicate every good model/tool behavior inside the protocol, even before "delta-layer" was articulated
- "Continuous Ergonomics Improvement" and "Session End Protocol" kept separate

**What v2 got right:**
- Agent Loop was the biggest improvement — gave agents a reusable execution pattern
- Handoff became more structured and complete
- Agent role started feeling like a real partner
- Anti-micromanagement was now present in spirit, even if not yet fully sharpened

**What v2 still missed:**
- No structural hierarchy (Core vs Operations)
- Still carried "Educational by Default" and standalone "Harness"
- Delta-layer principle not yet articulated — still some duplication with model/tool prompts
- The voice was professional but not yet memorable

---

## v2 → v3: Harness-Optimized, Delta-Layer Discipline

**Era:** Agent as primary implementer. Harness engineering awareness. Protocol as behavior-layer.

**What happened:**
Primary development session with GPT-5.4 agent. Compared AGENTS.md against four reference artifacts:
- `gpt-5.4-thinking.md` (model-layer constraints)
- `claude-opus-4.6.md` (model-layer constraints)
- `codex-cli.md` (tool harness behavior)
- `claude-code.md` (tool harness behavior)

Also analyzed external references:
- OpenAI Harness Engineering article
- OpenAI Prompting Guide
- Claude Prompting Best Practices
- Claude Code Memory documentation
- "Molecular Structure of Thought" paper on CoT topology

**Key changes:**

1. **Core / Operations split** — Most important structural improvement. Core = identity-level principles (roles, rights, quality). Operations = workflow patterns (CDD, loops, logging, handoff).

2. **Delta-layer principle articulated** — The single strongest design conclusion: don't repeat what model/tool prompts already cover. Many correct recommendations were discussed and intentionally NOT added.

3. **Anti-micromanagement stance made central** — Role Contract moved to #1. "Strong agents should not be micromanaged" added explicitly. "Humans steer. Agents execute." wording was considered and rejected because it violated the intended harness/partnership framing.

4. **"Done Is Not a Mood" replaced Harness** — More memorable, more compact, and promoted evidence from a harness subsection into a core quality rule instead of a procedural validation manual.

5. **"Do Not Stop at the First Weak Signal" added** — New principle. Protects against early collapse, false clean results, and the difference between missing data and absent data.

6. **"Educational by Default" removed** — Style preference, not protocol principle. Doesn't earn tokens in the minimal version.

7. **"Continuous Ergonomics Improvement" folded into Session End** — Friction reporting is now part of handoff (1-3 frictions), not a separate section.

8. **Subagent awareness added to CDD** — "Delegate for truth, not silence." "Leave subagents room to report blockers, repeated friction, or fallback." This was a major design insight: parent agents should fix delegation contracts, not force subagents to violate strict output contracts.

9. **Attention Engineering kept one provocative numeric heuristic** — The 200-300 line signal survived on purpose as a practical refactor anchor for humans and agents, not as a universal law.

10. **Semantic Hygiene kept one tiny example** — Abstraction alone made the rule too vague; the `graph` example earned its tokens.

11. **Hooks sharpened** — "correctness becomes a vibe", "autocomplete with tools", "Leave the next agent a runway, not a crater", "the right fact loses to the nearest fact"

12. **"Hello Agent!" kept** — Nearly removed as noise, then brought back: low token cost, high adoption value, session boundary marker, project identity.

13. **Fresh-eye scan removed as standalone section** — v1 had it as part of "Session Start". v2 merged it into Agent Loop as "Fresh-eye rule". v3 removed it entirely. Reason: in multi-agent and subagent contexts, scanning the whole repo before every task wastes tokens and delays work. The scan was useful in single-agent paired sessions but counterproductive at scale. The concept survived only as `Agent1st Mode ON` — a low-cost identity marker.

**Key rejected ideas (with reasons):**
- "reasoning path" demand → replaced with route/evidence framing (externalized evidence > theatrical CoT)
- "let subagents break format to surface truth" → replaced with "design delegation contracts correctly"
- output contracts, dependency checks, planning mechanisms → model/tool layer, not Agent1st
- detailed verification procedures → "Done Is Not a Mood" is sufficient for minimal version
- full fresh-eye audit at session start → too expensive for subagents/swarms, removed in v3

**Agent-to-agent handoff:** Older raw handoff briefs were removed in the v8 cleanup because they created stale-search noise for fresh agents.

---

## v3 → v4: Multi-Agent Autonomy Becomes Mainline

**Era:** Agent collectives. Human presence as spectrum. Autonomy with boundaries.

**Primary agent:** Claude Opus 4.6

**What happened:**
- Claude Opus 4.6 analyzed v3, the new repo docs, external references, and standard-version examples, then drafted the next minimal pass.
- The result was archived as `docs/_archive/AGENTS-min-v4.md` and promoted to current `AGENTS.md`. v4 is no longer just a proposal; it is the current minimal baseline on `main`.

**Implemented changes:**

1. **Human role spectrum landed** — The protocol now explicitly covers tight pairing through full delegation. What stays constant: acceptance criteria must exist before work begins, evidence must exist before claiming completion, and escalation boundaries must be respected.

2. **Delegation Design became a first-class principle** — Multi-agent work now has its own rule set: define deliverables, include acceptance criteria, leave room for operational truth, and prefer durable shared artifacts.

3. **Unsupervised escalation got explicit language** — `Right to Disagree` now covers no-human-present cases too: stop and escalate when risk exceeds delegated authority; logging an override is not equivalent to accepting liability.

4. **Attention Engineering tuned for stronger models** — v4 added "if the first direct check answers the question, do not over-explore or over-delegate" to counter newer-model failure modes.

5. **"Session End Protocol" → "Continuity"** — The old framing assumed agents control session boundaries. They don't: server-side compaction (Claude Code, OpenCode) can wipe context without warning. New framing: keep critical state in durable artifacts, not only in conversation. Differentiates between long-running work (full handoff), subagent work (evidence only), and swarm work (shared state updates).

6. **"Hello Agent!" fresh-eye scan re-added then removed again** — Opus 4.6 initially added a lightweight scan to Hello Agent. Human corrected: this was already tried (v1 standalone, v2 in Agent Loop) and intentionally removed in v3 because it's wasteful for subagents and swarms. Restored to v3's minimal form: `Agent1st Mode ON` only. See "Recurring rejected patterns" below.

7. **The minimal version expanded without losing discipline** — v4 reached 11 principles, stayed under 200 lines, and preserved the delta-layer rule instead of turning into a workflow manual.

**What v4 kept on purpose:**
- Anti-micromanagement stayed central; autonomy gained boundaries, not bureaucracy.
- Delta-layer discipline remained load-bearing; new additions still had to be genuinely absent from model/tool prompts.
- Hooks, voice, the tiny Semantic Hygiene example, and the Attention Engineering numeric signal all stayed because they still earned their tokens.

**Key rejected ideas in v4 (with reasons):**
- fresh-eye scan in Hello Agent → re-added by Opus 4.6, then removed after human correction: already tried in v1/v2, too expensive for multi-agent contexts
- error recovery / rollback principle → covered by tool harness (Claude Code, Codex CLI)
- scope discipline / anti-drift → covered by model system prompts
- tool/capability boundaries → harness layer concern

---

## Recurring Rejected Patterns

These ideas keep being proposed by new agents. They are logical, often correct in isolation, and still wrong for Agent1st. If you are about to propose one of these, read why it was rejected — multiple times, by multiple agents.

### "Add a fresh-eye scan at session start"
- **History:** v1 had it as standalone section. v2 merged it into Agent Loop. v3 removed it. v4 Opus 4.6 re-added it to Hello Agent. Then removed again.
- **Why it keeps coming back:** It sounds useful. A fresh agent scanning for contradictions before coding seems like good hygiene.
- **Why it keeps being removed:** Subagents launched with a specific task should not audit the repo. Swarm workers should not each independently scan. The cost scales linearly with agent count. In single-agent paired sessions it was fine. In multi-agent autonomous contexts it is waste.
- **Current form:** Only `Agent1st Mode ON` survives — zero-cost identity marker, visible session boundary.

### "Add error recovery / rollback rules"
- **History:** Proposed in v4 analysis (Opus 4.6), rejected after delta-layer check.
- **Why it keeps coming back:** Agents break things. Surely the protocol should say what to do.
- **Why it's rejected:** Claude Code's system prompt already has extensive git safety protocol, destructive operation warnings, and reversibility checks. Codex CLI has similar. Adding this to AGENTS.md duplicates the harness layer.

### "Add scope discipline / anti-drift"
- **History:** Proposed in v4 analysis (Opus 4.6), rejected.
- **Why it keeps coming back:** Agents refactor adjacent code, add unrequested features, "improve" things they weren't asked to touch.
- **Why it's rejected:** Model system prompts already contain "Only make changes that are directly requested" (Claude Code) or equivalent. Delta-layer principle: don't repeat what the model already enforces.

### "Add output formatting / code style rules"
- **Why it keeps coming back:** Feels like it belongs in any developer-facing document.
- **Why it's rejected:** Harness layer. Claude Code, Codex CLI, and model prompts all handle formatting. AGENTS.md is a behavior-layer, not a style guide.

### "Session end assumes the agent controls the boundary"
- **History:** v1-v3 all had "Session End Protocol" assuming a clean end-of-session moment. v4 refactored to "Continuity" after recognizing that server-side compaction removes this control.
- **Why it matters:** Any principle that assumes "at the end of your session, do X" is fragile in modern harnesses. Prefer "keep critical state in durable artifacts as you go."

**Pattern:** Most recurring rejections fall into two categories:
1. **Delta-layer violations** — the model or harness already handles it
2. **Session-boundary assumptions** — the agent doesn't control when context is lost

If your proposal fits either category, it is probably wrong for the minimal version. It might belong in a standard or full version where the environment is more controlled.

---

## v4 External Agent Review (2026-03-24)

Four external agents (GLM-5, Grok 4.20, MiniMax M2.7, and Qwen3.5-Plus) independently analyzed the protocol and submitted contributions. GPT-5.4 provided a parallel review. Claude Opus 4.6 curated and integrated the results.

These imported handoffs were preserved as audit artifacts through v8. They were later removed from the public surface because their stale file paths and old claims created misleading `rg` results for fresh agents. Curated conclusions remain below.

**What was incorporated:**
- **Handoff Template** — `docs/handoffs/TEMPLATE.md` with 3 modes (mini/full/subagent-evidence-only). Requested independently by 3+ agents.
- **Continuity hook** — "if your handoff disappears when the session ends, it doesn't exist" (from Qwen3.5-Plus). Added to AGENTS.md.
- **Continuity research grounding** — Park et al. "Generative Agents" (2023) added to FOUNDATIONS.md. Moved Continuity from "Practical origin" to "Supported."
- **Model-agnostic acknowledgment** — Brief note in DESIGN.md section 8. Protocol is model-agnostic by design; examples may reference specific models.

**What was noted for standard version:**
- Friction Tax (GLM-5) — quantified CDD for recurring friction
- Ambiguity handling in CDD (MiniMax M2.7) — distinguishing ambiguous from incomplete requests
- Anti-pattern examples as companion doc (MiniMax M2.7, Qwen3.5-Plus) — violation examples per principle
- Decision log template (MiniMax M2.7) — standardized format for cross-session rationale

**What was rejected (already covered or delta-layer violation):**
- Truth-First Orientation (Grok 4.20) — already covered by Right to Disagree
- Discovery Before Commitment (GLM-5) — fresh-eye scan, rejected 4th time
- Ethical boundaries principle (MiniMax M2.7) — model layer already covers safety
- Escalation protocol detail (MiniMax M2.7) — v4 already has unsupervised clause
- Assumption Surfacing (GLM-5) — over-specifies Agent Loop
- Agent Maturity Levels (MiniMax M2.7) — against "strong agents" philosophy

**Public surface policy after v8 cleanup:** keep curated outcomes in `EVOLUTION.md`; keep only the current handoff template and the latest live handoff in `docs/handoffs/`. Raw old review files are useful during integration, but once curated they become history noise.

**Pattern observed:** External agents consistently rediscover the same improvements and the same rejected paths. The recurring rejected patterns section above predicted most proposals accurately. This validates the value of documenting rejections.

---

## v4 → v5: The WHY Layer Lands

**Era:** Minimal is stable. Time to deliver what was called "standard" — without repeating the mistake that killed earlier attempts.

**The problem v5 had to solve:**

The roadmap had named "Standard Version Formalization" as an active priority for over a year. A reference implementation existed in a Python/FastAPI adopter, and a second real adopter — a separate TypeScript project — had independently shaped its own variant. Earlier experiments put the richer files in parallel `STANDARD/` and `FULL/` folders, which created visual duplication and made it unclear which file was canonical. Users — agents and humans — found this confusing in practice.

**What changed:**

The three-tier model (Minimal / Standard / Full) was retired. Agent1st now has **two layers that live in one repo**:

1. **Behavior layer** — `AGENTS.md`, unchanged in v5. Still drop-in, still portable, still ~200 lines.
2. **WHY layer** — flat files in `docs/`, highly recommended for long-lived projects:
   - `docs/Why1st.md` — the idea, workflow shift, adopter's pattern (Required Reading header)
   - `docs/PRD.md` — Agent1st's own dogfooded PRD
   - `docs/why-graph.xml` — teaching-size graph
   - `docs/why-graph-principles.md` — portable authoring guide distilled from real adopters (a Python/FastAPI variant and a TypeScript variant)
   - `docs/why-contracts-v1.md` — anchor spec with Python + TypeScript examples

Project-specific extensions (CI integration, observability, acceptance automation, runbooks) correctly sit on top of both layers in a project's own repo — not as a separate publishable tier.

**Why the minimal `AGENTS.md` did not change:**

The delta-layer principle and the anti-micromanagement stance both say the same thing here: the behavior layer must be portable and must not fill with repo-specific reading lists. An advisor proposal to add a Required Reading header to the core `AGENTS.md` was considered and rejected. Instead, that header is documented in `Why1st.md` §8 as the **adopter-side** extension pattern — observed in both real adopters.

**What was rejected during v5:**

- Keeping the `STANDARD/` and `FULL/` folder split. Reason: visual duplication, unclear canonicity, adoption friction.
- Renaming the entry doc (then `docs/WHY-APPROACH.md`, now `docs/Why1st.md`) to `docs/STANDARD.md`. Reason: the layer is the WHY approach, not a rung on a ladder.
- Editing `AGENTS.md` to require reading the WHY layer. Reason: would break drop-in portability and contradict `DESIGN.md` §5 (what NOT to add).
- Building validator tooling into v5 itself. Reason: the pattern is demonstrated; tooling is a v6 concern and language-specific.

**Reference adopters that shaped v5:**

- **A Python/FastAPI adopter** — the richer variant. Backend plus TypeScript frontend. Full relation vocabulary, class/method contracts, intent1st integration, validator scripts. The deep analysis lives off-public in private development-side notes; public docs describe the patterns, not the project.
- **A separate TypeScript adopter** — the simpler variant. Trimmed node families, adoption-notes doc that articulated the governance-graph vs. knowledge-graph distinction that `Why1st.md` §5 now carries.

Neither adopter copied the other. Both carried the same idea. That convergence was the signal that the WHY layer was ready to be documented.

### v5.1 — External review integration (2026-04-17)

v5 went out to eight external agents for review (Claude Opus 4.7, GPT-5.4, Gemini 3.1, Grok 4.20, Kimi K2.5, Meta-Muse Spark, MiniMax M2.7, Qwen 3.6). The raw review handoffs were removed from the public surface after their conclusions were curated here; the point is to preserve decisions, not stale search noise.

**Accepted and landed in v5.1:**

- **Teaching-surface fixes (GPT-5.4):** fixed the `COVERS` relation direction in `why-graph-principles.md` §7 (now correctly placed on the `USECASE_*` node); unified `TARGET` syntax across principles and dogfood graph (pick one convention per repo); moved `why-graph.xml` scope disclaimer from the bottom of the file to the top.
- **Three-tier residue removal (GPT-5.4):** `ROADMAP.md` opening now says "two layers"; `PRD.md` §2 "two tiers" → "two layers"; open question in §10 dropped "FULL-layer" framing.
- **Graph staleness as first-class failure mode (MiniMax M2.7):** new `Why1st.md` §6a names staleness explicitly and gives a recovery protocol, plus an honest adoption criterion: if your team cannot commit to running the validator regularly, the layer costs more than it saves.
- **Workflow-shape intensity (GPT-5.4, MiniMax M2.7):** `Why1st.md` §3 and §6 no longer prescribe "graph first" as universal law. Distinguishes intent-changing/cross-cutting work (graph first) from local edits in well-mapped features (graph moves with code, same commit). §6 also distinguishes first-session onboarding, returning sessions, and delegated subagents.
- **§8 Required Reading clarified (MiniMax M2.7, Kimi K2.5):** harness-native mechanisms (CLAUDE.md, MEMORY.md, skills, session-context files) are now the recommended first option. The adopter-header-in-project's-AGENTS.md pattern remains as a fallback, with explicit visual separation from the unmodified Core. Also added a one-line adoption smoke test (Kimi).
- **Harness-agnostic language (Kimi K2.5):** `why-graph-principles.md` §0 no longer prescribes "Pin …"; says "ensure in context" instead.
- **Relation vocabulary refinement (Grok 4.20, Qwen 3.6):** added `DEPENDS_ON` for co-change coupling that is not implementation; disambiguated `IMPACTS` (runtime effect) vs `WILL_TOUCH` (planning promise); added retirement pattern (`DEPRECATED` then delete) and inherited-code-without-anchors guidance.
- **Contracts tuning (Qwen 3.6):** `MODULE_MAP` now explicitly optional with a ~5-public-symbols threshold; `CHANGE_HISTORY` noted as optional; inherited code without anchors gets a one-paragraph guide in §7.
- **PRD-level honesty:** a new Definition-of-Done bullet for the WHY layer — "staleness is named as the main failure mode, not pretended away."

**Rejected in v5.1:**

- **Kill the dogfooding, replace with generic e-commerce example (Gemini 3.1).** Seven of eight reviewers explicitly said keep the dogfood. Generic examples are cleaner; they are also weaker as a credibility signal.
- **Delete Python examples from `why-contracts-v1.md` (Gemini 3.1, soft suggestion from Kimi K2.5).** The Python/TS contrast teaches that anchor syntax adapts to language idioms. Keep both.
- **Strip inline XML commentary from `why-graph.xml` (Gemini 3.1).** Four reviewers called the commentary pedagogically load-bearing. The trade-off of comment-noise vs. teaching value is worth paying in a teaching-size file.
- **Add `MUTATES` relation (Gemini 3.1).** Overlaps with `READS` / `WRITES` / `QUERIES`. Would fragment the vocabulary, not sharpen it.
- **Add `EVIDENCED_BY` relation (Meta-Muse Spark).** Interesting, but scope creep for v5.1. Deferred to v6 discussion — needs to be weighed against the risk of relation vocabulary growing past the "small and stable" target.
- **Gemini 3.1's fabricated line-42 edit.** The claimed text (`"Agents must explicitly validate the structural integrity and data types of contract inputs before execution"`) does not exist in `why-contracts-v1.md`. Flagged for future reviewers — treat confident quotes from reviewers who couldn't fetch the live files as suspect until verified.
- **Claude Opus 4.7's "v5 didn't land on main" claim.** Review was written against pre-v5 cached content; specific claims (DESIGN.md §7 still "Versions and Scope", README still selling "standard and full versions") do not match the current repo. The pre-merge consistency checklist idea is useful and is noted here for future v-bumps.

**Process note:** external reviews are high-leverage when reviewers can read the files. Two of eight (Claude Opus 4.7, Meta-Muse Spark) could not fetch the v5 files over the web, and it showed. When the next external review goes out, bundle the files with `repomix` (or equivalent) and attach them — don't rely on live crawl.

---

## v5.1 → v6: Validator MVP lands; AGENTS.md survives the spirit pass unchanged

**Era:** GPT-5.5 and Claude Opus 4.7 become the new frontier targets. A detail-rich working TZ from GPT-5.5-pro arrives proposing changes to three `AGENTS.md` sections plus a validator MVP plus relation vocabulary tightening. The temptation is to integrate everything that has clear local logic. The protocol's job is to filter that input through the *spirit* of Agent1st — which lives at a level above any individual section's local logic — and accept only what survives.

**Primary agent:** Claude Opus 4.7

**Inputs that shaped v6:**

- `docs/handoffs/v6-handoff-gpt-5.5-pro.md` from GPT-5.5-pro, framed explicitly as a working TZ rather than another opinion.
- A subagent-led mapping of a Codex-native downstream adopter that already had a working anchor validator with STATE-aware enforcement.
- The official OpenAI GPT-5.5 prompt-guidance and Anthropic Claude Opus 4.7 migration documents — both pushing toward outcome-first, contract-clear prompts and against carrying over legacy prompt stacks.

**The v6 framing question:**

GPT-5.5-pro proposed v6 as "Strong agents need clearer contracts, not longer instructions." That's a strong thesis on the surface. The protocol-level question is whether the proposed changes serve that thesis or undermine it.

**What survived the spirit pass (accepted):**

- **`scripts/validate-why.py` — WHY validator MVP.** Stdlib-only Python (no `lxml` dependency on a docs-only protocol repo). Checks: XML parses, IDs unique, `REL TYPE` is in the documented vocabulary, `REL TARGET` resolves (family-qualified or bare), TARGET style consistent across the graph, ANCHOR shape if present, STATE-aware anchor enforcement (`PLANNED`/`DEPRECATED` skipped, `STARTED`/`DONE`/`IMPLEMENTED` enforced). Degrades to a warning, not a failure, when the graph has no anchors yet — the dogfooded graph is teaching-only on purpose. Output uses CDD-style problem reporting (Problem / Smallest fix). Passes on the current `docs/why-graph.xml` with the expected "no anchors" warning. **This is the only piece that changed the protocol's mechanical surface.** It earns its place because the WHY layer's own claim — "validators are consistency truth" — was unsupported until something runnable existed.
- **`docs/why-graph-principles.md` §8 + `docs/PRD.md` §6 — one-line validator references.** Documentation pointing at the new command. No cascade.
- **`docs/why-graph.xml` — FEAT-WHY ACCEPT block gains the validator check; ART-VALIDATOR node added; PROJECT VERSION bumped to 0.7.** The graph now reflects that the WHY layer's four pillars (PRD, Graph, Contracts, Validator) are all present in this repo.

**What was first accepted then reverted under the spirit pass:**

- **`AGENTS.md` §8 — Signal Discipline replacing "Do Not Stop at the First Weak Signal".** Initially landed because GPT-5.5-pro's local logic is correct: the original §8 covered only one stopping failure mode (early collapse), and a symmetric "stop at sufficient evidence" rule would close the over-checking failure mode that current frontier agents exhibit. Reverted on the spirit pass for three converging reasons:
  1. **Duplication with §4.** §4 Attention Engineering already says "if the first direct check answers the question, do not over-explore or over-delegate." The new §8 bullet ("if the core request is answered with adequate evidence, stop; more checking is not automatically more truth") is the same insight reframed. The asymmetry GPT-5.5-pro saw between §8 and §4 was the *design*: §4 prevents over-exploration during search, §8 prevents early collapse during evaluation. Forcing both jobs into one section turns architecture into checklist.
  2. **Voice regression.** The v3 commit that landed "Done Is Not a Mood" replacing "Harness" was specifically called out for being "more memorable, more compact." "Do Not Stop at the First Weak Signal" is in the same voice family — sharp, slightly provocative, instantly readable. "Signal Discipline" is the title a corporate handbook would use. Walking that pattern backwards undermines `DESIGN.md` §4's voice rules.
  3. **Discipline consistency.** §1 was deferred because it grew from three bullets to five — "bloating the most-read section to demonstrate the 'clearer contracts, not longer instructions' thesis is self-undermining." Accepting §8's growth (3 bullets → 4 bullets + 2-line preamble + heavier WHY/IF MISSING) under that same thesis is incoherent. The bullet-count discipline either applies or it doesn't.
- **`AGENTS.md` §9 — the delegation optimization-target line.** Initially landed as one bullet ("for discovery or review work, state whether the job optimizes for coverage, precision, speed, or evidence depth"). Reverted because it's tactical guidance about a subset of delegations, not a principle. The existing §9 ("define the deliverable, not the path"; "include acceptance criteria in the delegation") already requires the delegation contract to be specific; specifying optimization axes is one way to be specific, not a parallel principle. Worth capturing in a future `docs/handoffs/TEMPLATE.md` revision; not worth promoting into the core protocol. GPT-5.5-pro itself flagged this as borderline ("Could be more suitable for a companion handoff template than core AGENTS.md") — the spirit pass agreed.

**What was rejected at the front door (never landed):**

- **§1 Role Contract candidate change A.** Proposed adding bullets about task-contract clarity and an assume/ask rule. The compressed version still landed at five bullets where the original has three; the assume/ask rule partially duplicates §3 (Right to Disagree). Failed the bullet-count discipline test from the start. Deferred until a wording exists that compresses, not grows.
- **`EVIDENCED_BY` relation (proposed in v5.1).** The validator MVP gives evidence-tracking teeth without expanding the relation vocabulary. Adding a relation just to wire validators into the graph would push vocabulary past the "small and stable" target without changing what the validator actually checks.
- **All model-specific API knobs in `AGENTS.md`.** Reasoning effort, verbosity, adaptive thinking, sampling parameters, hosted tools, prompt caching, `previous_response_id`, Claude `task_budget`, temperature/top_p/top_k advice, model-specific tool-use heuristics. All belong to the harness or model layer. If a project needs a model-specific note, it goes in `CLAUDE.md`, a project-local config, or this file — not in the portable behavior layer.
- **A model-named v6 ("GPT-5.5 edition" / "Opus 4.7 edition").** Naming the version after the models that triggered the review would normalize model-coupled releases. Agent1st is provider-agnostic by constitution.

**Net effect on `AGENTS.md`:** byte-identical to v5.1. The protocol survives the v6 review with no edits — and that, not a longer file, is the v6 result. The thesis "clearer contracts, not longer instructions" applies most strongly when the existing contract was already correct.

**Spirit pass — the meta-lesson recorded as v6's main process contribution:**

GPT-5.5-pro produced excellent details. Each one was locally correct. The protocol's job was not to grade them on local logic but to receive them through a filter that asks: does this serve the *spirit* — anti-micromanagement, delta-layer discipline, memorable voice, every line earning its tokens — or only the local logic?

This isn't "the reviewer was wrong." It's "the reviewer was correct on local logic, and the protocol still rejected two details because the spirit lives at a level above local logic." Future external reviewers should expect this filter. The way to land changes in `AGENTS.md` is not to be locally clever; it is to identify a real failure mode that the existing protocol does not already address, and propose the smallest possible patch in the existing voice.

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
- [warning] <graph>
  Problem: no ANCHOR elements found
  Smallest fix: acceptable for a docs-only dogfood graph; add anchors when adopting this layer in a code repo
WHY validator: OK
exit=0
```

```
$ git diff <pre-v6>..HEAD -- AGENTS.md
(no changes)
```

**Process note:** The Codex-native adopter mapping was delegated to an Explore subagent rather than done by the primary agent. The 600-word report came back in under a minute and gave the validator-design pattern (STATE-aware enforcement) without burning primary-agent context on raw exploration. The validator MVP that shipped uses that pattern; private gitignored lab notes carry the reusable subagent brief so the next exploration starts warm, not cold.

---

## v6 → v6.1: Why1st gets named; public surface stops naming local projects

**Era:** The behavior layer is stable. The open problem is not `AGENTS.md`; it is making the WHY-first way of working easier to refer to without making the public protocol point at projects readers cannot access.

**What changed:**

- **Why1st named carefully.** `docs/Why1st.md` and `docs/VISION.md` now say Why1st is a short name for the WHY-first approach/layer, not a second protocol in the strict Agent1st sense. Agent1st remains the behavior contract; Why1st is the intent-to-code discipline.
- **One-file PRD stance made explicit.** The WHY docs now say starting with one `docs/PRD.md` that also holds early design, roadmap, and plan is valid. Splitting docs is useful only when the split reduces drift more than it creates maintenance overhead.
- **Stale v6 teaching-surface issues fixed.** `docs/why-graph.xml` no longer claims there are no validators; `docs/VISION.md` no longer says "four files" while listing five; `why-graph-principles.md` examples use `MODULE_*` tags that match family-qualified `MODULE:` targets.
- **Validator generalized.** `scripts/validate-why.py` now validates anchors under any node with `<ANCHOR>` children, not only `MODULE_*` nodes, while preserving STATE-aware enforcement.
- **Public/private surface separated.** Named reference-adopter analyses (one deep analysis of the original Python/FastAPI adopter, plus an in-flight summary of three real adopters) were moved off the public surface into private development-side notes. Public docs no longer name local-only projects readers cannot open. Development-side context stays local for primary and subagent use; the protocol surface stays self-contained.
- **Brand unification.** The entry doc was renamed `docs/WHY-APPROACH.md` → `docs/Why1st.md`. The graph artifact ID followed: `ART-WHY-APPROACH` → `ART-WHY1ST`. README promoted the WHY-layer section to a level-2 heading (`## Why1st`) so external links to the brand have a clean anchor. Older paired files (`why-graph.xml`, `why-graph-principles.md`, `why-contracts-v1.md`, `validate-why.py`) keep their lowercase `why-*` prefix as a stable artifact namespace inside Why1st — only the entry doc carries the brand name. References in earlier EVOLUTION sections use the current path; the rename happened in v6.1.

**What stayed out of core:**

- Named adopter analyses on the public surface. They moved off-public. Public docs describe the patterns those adopters validated, not the projects themselves.
- Codex agent profiles, exact model settings, and orchestrator implementation details remain project-local examples.
- Runtime observability with anchor coordinates is documented as a powerful extension, not required baseline.
- Heavy "every function gets a contract" enforcement remains adopter-specific. The portable rule is lighter: govern graph-referenced, public, complex, or frequently edited regions first.

**Recurring-pattern note:** This is the second time agents working on Agent1st have re-added local-project references into public docs. The principled fix is a private lab rule: never name local-only projects in `AGENTS.md`, `docs/*`, or `README.md`, plus durable feedback memory so future agents don't re-derive the same wrong shape.

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
- [warning] <graph>
  Problem: no ANCHOR elements found
  Smallest fix: acceptable for a docs-only dogfood graph; add anchors when adopting this layer in a code repo
WHY validator: OK
```

---

## v6.1 → v7: Why1st format spirit gets named

**Era:** v6 documented *how* to write the Why Graph but left *why* the format choices were specifically engineered (transformer attention, semantic distinctiveness, greppability, progressive disclosure) implicit. A real downstream adopter at the start of a project read only `README#why1st` and `Why1st.md` cold, then produced exactly the simplification a strong agent's prior makes cheap: `<?xml version="1.0"?>` + `<whyGraph>` root + separated `<nodes>` / `<relations>` blocks + `<node id="FEAT-X" kind="feature">` containers with `<dependsOn>`, `<prdRef>`, `<summary>` children. The output validated. It also failed the actual job — generic `<node>` tags do not survive long context as transformer-attention anchors, and the `id="..."` attribute is invisible to grep'ing across code anchors.

**Diagnosis:** the words "graph" and ".xml" pull strong agents toward classical graph-DB shape and classical-XML defaults. Both are rational from inside the training prior. The fix is not blaming the agent — it is making the format choice explicit and motivated, so the rationale lands before the format gets simplified away.

**Primary agent:** Claude Opus 4.7

**What changed:**

- **`docs/why-graph-principles.md` §2a — the load-bearing change.** A new section titled "Tag shapes — prompt-XML, not classical XML." Names the three forces (transformer attention, greppability, semantic interference), shows side-by-side classical-XML/graph-DB vs prompt-XML/Why1st example with line-by-line "what is wrong / what to write" annotations, lists anti-patterns (`<?xml ?>` declaration, `<whyGraph>` root, `<nodes>/<relations>` separation, `<node id kind>`, camelCase tags, free-form `type="serves"`), and ends on a one-line rule: *the tag IS the semantic anchor; if the tag is generic, the graph is decoration.* This is the section a fresh agent should read before writing the graph.
- **`docs/Why1st.md` §2** — short pointer paragraph. Tells the reader to read §2a *before* writing the graph and gives a one-sentence diagnosis of the simplification trap.
- **`docs/why-contracts-v1.md` head** — short paragraph naming the contracts-at-file-head pattern as *progressive disclosure*. A model reading 20 lines learns PURPOSE / PRD_REF / INVARIANTS / LINKS and decides whether to load the rest. Notes that `SKILL.md` popularized the same pattern recently; Why1st has had it from the start. Token saving is real but secondary; attention shaping is the primary effect.
- **`docs/why-graph.xml`** — one inline comment near the first `FEATURE_*` block: *"tag name carries the entity identity; do NOT replace with generic `<node id="..." kind="feature">` — see §2a."*
- **AGENTS.md** — untouched. The failure is in the WHY layer, not in behavior.
- **Validator** — untouched. Already accepts canonical shape; not its job to police format aesthetics.

**Verified before ship.** A fresh Explore subagent was given only the updated `Why1st.md`, `why-graph-principles.md`, `why-contracts-v1.md`, and the dogfood `why-graph.xml`, plus a tiny fictional PRD (FocusKit — CLI + dashboard). It produced canonical prompt-XML on first attempt: `<Why_Graph schema="0.8">` root, no `<?xml ?>`, `<USECASE_START ID="UC-START">`, `<FEATURE_CLI_START ID="FEAT-CLI-START">`, inline `<REL TYPE TARGET>`, all UPPER_SNAKE_CASE semantic tags. In its self-check it explicitly named the simplifications it consciously avoided. v7 docs land the rationale; without that verification, the doc edit was talk.

**What stayed out of v7:**

- A separate `docs/why-spirit.md` doc — proliferation against delta-layer.
- Any `AGENTS.md` change — the failure is in the WHY layer, not behavior.
- Adopter prompt template in the private shareables staging area — held back as v7.1 follow-up only if docs alone don't land for cold-start agents. Verification suggests they are.
- Conflating contracts and graph shape — the downstream adopter's contracts were roughly fine in spirit (`<!-- START_DOC_CONTRACT: NAME -->` with PURPOSE / PRD_REF / INVARIANTS). Only the graph collapsed to classical XML. v7 keeps the two failures separate; the contracts paragraph is about progressive disclosure, not about correcting a contract mistake.

**Recurring-pattern note.** v6.1 fixed a recurring leak (local-project names creeping into public docs). v7 fixes a recurring simplification (graph format collapsing to `<node id>` shape). Both root-cause the same way: the public docs encoded the *what* clearly but the *why* implicitly. Future versions should treat any "agents keep doing X wrong" report as a signal that the WHY of the relevant rule is under-specified, not that agents need more rules.

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
WHY validator: OK
```

---

## v7 → v8: Tier-1 cold-start fixes plus opt-in extension patterns

**Era:** v7 named the Why1st format spirit and got empirically verified — a real cold-start adopter (PRD-only, agent told to read `#why1st`) produced a working app with a valid prompt-XML graph, 11 anchors, 21 unit tests, module contracts on 16 files. The protocol transferred. The next question is no longer "do the docs land?" but "what does the cold-start audit teach us, and how do we let real-project surfaces (semantic logs, tests with UI evidence, subagent orchestration) come in without breaking drop-in adoption?"

**Primary agent:** Claude Opus 4.7. **Codex-side audit:** GPT-5.5 (cross-project review of harmon1st's adoption, semantic-logging patterns across reference adopters, harness-observatory as a public candidate).

**The new failure mode v8 catches.** The harmon1st adopter wrote a correct local Why Graph but compressed its local copy of `why-graph-principles.md` from ~218 lines to ~74, dropping most of v7's §2a rationale. Agent A succeeded; agent B on the same project would now read only the local guide and lose the WHY. This is the same root cause as v6.1 (local-project names leaking into public docs) and v7 (graph format collapsing to `<node>`): docs encoded *what* clearly, *why* implicitly. **Compressed adaptation drops the why first.** The v8 fix: tell adopters explicitly which rationale anchors not to compress when they shorten a doc locally.

**Tier-1 — small load-bearing fixes:**

- **`docs/why-graph-principles.md` §2a — "Adapting §2a locally" guard.** When you copy this file into your project and shorten it, retain at minimum: tag identity, inline relations, no `<?xml?>`, no generic `<node id kind>`, and one sentence on transformer attention. Compress further and the next agent loses the rationale §2a was written to prevent.
- **`docs/Why1st.md` §8 — "Pin vs reference."** Pin always: `AGENTS.md`, `docs/PRD.md`, `docs/why-graph.xml`. Reference on demand: principles, contracts, validator, project-local memory. Stops cold-start adopters from pinning 8+ files and turning the layer into context tax.
- **`docs/Why1st.md` §8 — "Don't edit the Core."** Hello Agent tweaks, output-contract exceptions, harness handshake refinements go above the separator in the addendum, not inside the canonical body. The harmon1st adopter modified the Core "just slightly" while claiming it was unmodified — a real adoption mistake, named explicitly.

**Tier-2 — opt-in extensions for real-project surfaces.** New `Why1st.md §11` introduces three patterns with a hard partition from the canonical chain (PRD → Graph → contracts → validator). Adopt only when the project actually has the surface. Skipping them is fine; the protocol does not require them.

- **§11.1 Semantic logs as future agent context.** When a project has runtime workflows, important boundaries should emit compact structured events whose `anchor` field uses the same names as the Why Graph and code anchors. A model can grep one string across logs ↔ graph ↔ code and orient instantly. Without that link, semantic logs are just structured logs. Keep separate from rationale memory: logs answer *what happened*, not *why we decided*.
- **§11.2 Tests and UI evidence — agent self-sufficiency.** `AGENTS.md §2 (Done Is Not a Mood)` says completion needs "the best evidence the current harness allows." For projects with a UI, that means the agent should set up Playwright/snapshot/browser-use *itself*, not ask the human. Most users do not know they can grant browser tools; agents who silently wait for permission spin instead of working. This is `AGENTS.md §1 (Role Contract)` applied to the agent's own evidence path.
- **§11.3 Subagent orchestration as project-local pattern.** When a project recurringly delegates, a project-local `docs/agent-orchestration.md` (role matrix, prompt patterns, evaluation rubric, durable lessons) is a useful answer to "where does subagent know-how live." This is project-local extension, not Agent1st core. `AGENTS.md §9 (Delegation Design)` is the principle; the artifact is yours.

**The hard partition.** Section 11 ends with: *"A project that has only the canonical chain is using Why1st correctly. A project that has the extensions and skips the chain is not using Why1st at all."* This is the spirit-pass guard against complexity creep. The chain stays small. Extensions are explicitly opt-in, named, and scoped to surfaces that justify them.

**Surface cleanup also landed in this commit.** GPT-5.5's audit replaced public mentions of the gitignored development-side folder in `EVOLUTION.md` history with neutral "private development-side notes" phrasing, sharpened a few PRD open questions (drift metrics, public-proof maturity, version-field necessity), and added ROADMAP §4 ("Success Signals and Public Evidence") naming `applerom/harness-observatory` as the first public reference candidate. That last point is OK only because the GitHub repo is public — the rule "do not name local-only projects on the public surface" still holds.

**What stayed out of v8:**

- AGENTS.md changes. The behavior layer is byte-identical to v5.1 since the v6 spirit pass.
- A separate `docs/why1st-runtime.md` doc for semantic logs. §11.1 is concise on purpose; if adopter feedback shows §11.1 needs more depth, extract later.
- A separate `docs/why1st-tests.md`. Same logic — §11.2 is a paragraph, extracted only if real adopters need more.
- Validator extension to lint log↔graph anchor alignment. Defer until adopters of §11.1 ask for it.
- Memory decision guide (4-layer split: PRD / Graph / runtime logs / decision memory). Worth doing eventually; not yet.
- Versioning simplification (`schema="0.8"`, `<PROJECT VERSION>`). Open question stays.

**Recurring-pattern note.** Three versions in a row — v6.1, v7, v8 — diagnosed the same shape of failure: **the WHY of the rule was under-specified, so adopters/agents reproduced the local-prior shape instead of the protocol intent.** Each fix was small and rationale-thickening. None added rules or principles. The pattern itself is now documented enough that future versions can name it as the first thing to check when an adopter "does X wrong": is the WHY explicit, or have we left the agent to infer it?

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
WHY validator: OK
```

---

## v8 → v8.1: Closing pass — drop dead weight, do not preemptively expand

**Era:** v6→v8 each added a load-bearing fix tied to a named adoption failure. v8.1 is the discipline of not adding when nothing is broken.

**Primary agents:** GPT-5.5 Codex (stale-handoffs prune + open-question framing in commit `7ffffa1`, plus a development-side audit of GRACE Marketplace) and Claude Opus 4.7 (version-field removal, EVOLUTION/ROADMAP integration, advisor pressure-test).

**What v8.1 closes.**

- **Graph version-field inertia.** The teaching graph carried `schema="0.8"` on the root and `VERSION="0.8"` on `<PROJECT>`. Both were holdovers from before Why1st was a named project, never tied to an XSD, validator compatibility contract, or migration rule. Adopters copying the graph had to choose what to do with `0.8` — some kept it, some incremented, some did not notice — all noise, no signal. v8.1 removes both fields, rewrites `why-graph-principles.md` §2 to match, and closes the corresponding open questions in PRD §10 and ROADMAP §5.
- **Stale handoffs as `rg` traps.** Eleven raw v3/v4/v5-era external review files in `docs/handoffs/` were producing misleading search results for fresh agents — old file paths, retired framings, decisions long superseded. The curated conclusions are already in this file (`EVOLUTION.md`). Codex pruned the raw files in commit `7ffffa1`; v8.1 records the policy explicitly: keep curated outcomes here, keep only the current handoff template and the latest live handoff under `docs/handoffs/`.

**What v8.1 deliberately does *not* add.**

A development-side audit of [`osovv/grace-marketplace`](https://github.com/osovv/grace-marketplace) — a parallel public project that independently arrived at prompt-XML tags, contracts near code, and graph-anchored validators — produced six borrow candidates: "closing-tag polysemy" naming for §2a, public/shared vs file-local/private boundary in `why-contracts-v1.md`, classical-XML anti-pattern lint in the validator, operational-packet shape for `docs/agent-orchestration.md`, validator issue codes, and an optional "autonomous readiness" profile. Each candidate is genuinely useful in some adopter scenario.

None of them landed.

The reason is the spirit-pass discipline that worked through v6→v8: every change was tied to a named adoption failure that the change actually catches. v6.1 was triggered by GPT-5.5 leaking local refs into public docs. v7 was triggered by the harmon1st adopter producing classical XML on first read. v8 was triggered by the same adopter compressing away rationale. There is no observed failure that any of the six GRACE candidates would prevent. §2a's three forces empirically already work for cold-start adopters; private helpers have not yet bloated any real adopter graph; the validator's CDD-style errors have not yet triggered UX complaints.

So the candidates are parked in ROADMAP under "From GRACE Marketplace audit" with explicit "awaiting signal" gates per row. The audit's value is preserved as a legible candidate pile; the public surface stays unchanged.

**The lesson v8.1 teaches.**

External validation feels like a reason to expand. It is not. GRACE confirms the *thesis* — the strongest possible win — and that confirmation is itself the deliverable. Adding GRACE's vocabulary, lint rules, or extension shapes preemptively would convert that win into ceremony for adopters who do not have the problem yet. The deeper move is to record what the audit found, leave the public surface alone, and let real adoption pressure decide which borrow is worth the tokens.

This is the same shape as the v6 spirit pass — which deferred the §1 Role Contract candidate and reverted §8/§9 candidate edits — applied at the Why1st surface instead of at AGENTS.md.

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
WHY validator: OK
```

---

## v8.1 → v8.2: §11.1 grows to depth — adopter pull triggers the extraction promised in v8

**Era:** v8 deliberately kept §11.1 (semantic logs) at five paragraphs and recorded the boundary explicitly: *"A separate doc for semantic logs. §11.1 is concise on purpose; if adopter feedback shows §11.1 needs more depth, extract later."* That extraction landed in v8.2.

**Primary agents:** GPT-5.5 Codex (initial implementation draft distilled from a cross-project reference analysis kept in lab notes) and Claude Opus 4.7 (spirit pass — lead with WHY at the top, parallel structure to `why-graph-principles.md` §2a, dropped a Playwright digression that belonged in §11.2, tightened the implementation slice from 9 numbered steps to 6, audit of vocabulary so the new doc reuses the chain's words instead of inventing a fresh schema).

**The trigger.** An adopter who had already implemented the Agent1st+Why1st base — minimal `AGENTS.md`, PRD, Why Graph, contracts — asked for implementation guidance to add semantic logs. Five paragraphs in §11.1 told them the principle and the load-bearing trick (anchor field matches Why Graph names) but did not tell them where logs live, what the minimum event shape actually is, what to log vs not log, or what a good first slice looks like. The depth was missing because v8 wanted depth to be pulled by adopter pressure, not pushed by speculation. The pull arrived.

**What landed.**

- **`docs/why-semantic-logs.md` — new paired file in the `why-*` namespace.** Twelve sections: TL;DR, the problem this layer solves, the core idea, why this works for transformer-based agents (the parallel of `why-graph-principles.md` §2a — three forces: vocabulary stability creates an attention bridge, same-string grep is the cheapest tool a model has, attention is finite per AGENTS.md §4), when to adopt vs not, minimum event shape (required + conditional fields), what to log / what not to log, where logs live (JSONL first), the smallest useful slice (6 steps), what semantic logs are *not* (not decision memory, not raw logs, not test evidence on their own, not graph-staleness signal), anti-patterns, optional validator extension, and where this fits in the rest of the chain.
- **`Why1st.md` §11.1** updated: the field-shape line corrected to match (`ts`, `event`, `anchor`, `component` required; `expected` / `actual` / correlation id conditional) and a cross-link added pointing to the new file. The five-paragraph version stays as the entry; the new file is the depth.

**What did not change.** AGENTS.md (byte-identical to v5.1 since v6 spirit pass). The canonical chain (PRD → Why Graph → contracts/anchors → validator). The hard partition between chain and §11 extensions. The graph (no new ARTIFACT entry — extensions stay out of the graph by design; promoting them would muddy the partition adopters rely on to know what is required vs opt-in).

**Spirit-pass discipline.** This is the second consecutive version where the change responds to a named adopter signal rather than a speculative improvement. v8.1 closed inertia fields and parked the GRACE-audit candidates as "awaiting signal." v8.2 took one of those parked-style situations — *a candidate that had been waiting for a signal* — and shipped it because the signal arrived. The pattern is becoming explicit: adopter pull → spirit-pass through Why1st voice → extract.

**What stayed in the lab.** The reference analyses that informed the new file (cross-project semantic-logging audit, GRACE-marketplace audit, harmon1st adoption audit) live in development-side notes, not on the public surface. The public artifact is the principle in §11.1 plus the implementation guide in `docs/why-semantic-logs.md`. Adopters do not need to know which reference projects taught the pattern — they need the pattern, sized for their problem.

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
WHY validator: OK
```

---

## v8.2 → v8.3: §11.3 grows to depth — the same adopter-pull pattern, second extension

**Era:** Two consecutive depth extractions following the same shape. v8.2 graduated §11.1 (semantic logs) when an adopter pulled for it. v8.3 graduates §11.3 (subagent orchestration) when cross-project field signal converged on the same gap.

**Primary agent:** Claude Opus 4.7. Seven external agent reviews of the post-v5.1 repo (gemini-3.1-pro, glm-5.1, gpt-5.5-pro, grok-4.3-instant, kimi-2.6, muse-spark, qwen-3.6-max) provided the secondary signal — three of them independently flagged subagent-delegation regression as a real gap, with the rest broadly ratifying the AGENTS.md byte-freeze.

**The trigger.** The user reported a recurring cross-project pattern: agents now adopt Agent1st+Why1st canonical chain reliably, then default to single-thread solo execution on real work. Independent reads burn lead context. Fan-out validation runs serially. Mechanical ops pay frontier-tier prices. The user explicitly named the shape — *"agents are trained agentically but try to do it all themselves by default"* — and asked how to package the bias-to-delegate in Agent1st spirit, possibly with authoritative external references so the recommendation does not read as Agent1st invention.

**What §11.3 in v8 actually said.** The v8 brief was artifact-focused: "where does subagent know-how live" → `docs/agent-orchestration.md`. That answers a second-order question (where the patterns crystallize) while skipping the first-order one (when does an agent default to delegating at all). For projects that already delegate the framing fits; for projects whose lead never dispatches in the first place the brief is invisible.

**What landed.**

- **`docs/why-subagents.md` — new paired file in the `why-*` namespace.** Twelve sections, parallel to `why-semantic-logs.md`'s shape: TL;DR, the problem (default-to-solo), the core idea (delegation as default), three forces parallel to `why-graph-principles.md` §2a (context economy, real parallelism, intelligence routing), when to default vs when not to bother, the four delegation shapes (parallel exploration / fan-out validation / deep-dive isolated work / lower-intelligence ops), the contract structure (goal + inputs + acceptance + latitude + length budget), the lead-vs-delegate line, when the artifact (`docs/agent-orchestration.md`) emerges, what this is *not*, anti-patterns, references with Anthropic *Building Effective Agents* as the canonical external anchor, and where this fits in the chain.
- **`Why1st.md` §11.3 re-pointed.** Heading and lead paragraph now lead with behavior ("delegate by default, crystallize the pattern later") rather than artifact. The artifact framing stays as the second paragraph. Cross-link to `docs/why-subagents.md` added.

**The behavioral re-pointing matters.** The v8 brief talked correctly about an artifact most projects do not need yet. The behavioral re-point puts the load-bearing claim — *the lead's default is the regression* — at the entry. Adopters who read only the brief now leave with the right bias even if they never read the depth doc.

**Why authoritative external citation.** The user explicitly raised the asymmetry: agents adopt patterns more readily when those patterns have provenance outside the project asking them to adopt. The orchestrator-worker / parallelization / evaluator-optimizer vocabulary in Anthropic's *Building Effective Agents* is the canonical write-up of the same shape this guide describes. Citing it makes clear the pattern is the framework default, not Agent1st invention. Single-thread execution is the regression to catch up *from*.

**What did not change.** AGENTS.md (byte-identical to v5.1 since v6 spirit pass — eight versions of discipline). The canonical chain (PRD → Why Graph → contracts/anchors → validator). The hard partition between chain and §11 extensions. The graph (no new ARTIFACT entry — extensions stay out of the graph by design).

**Spirit-pass discipline.** Third consecutive version where the change responds to a named field signal rather than speculation. v8.1 closed inertia fields. v8.2 graduated §11.1 when one adopter pulled. v8.3 graduates §11.3 when cross-project pattern + multi-reviewer convergence pulled. The remaining §11.2 (tests + UI evidence — including the user's separate field signal that adopters consistently miss browser-CLI verification) is held for v8.4 because doubling the surface change in one wave dilutes the spirit-pass signal — one extension per wave is the post-v8 cadence.

**What stayed in the lab.** The seven agent reviews live in development-side notes, not on the public surface. Their ratification of the byte-freeze and convergence on the subagent gap is the data; the artifacts themselves are not the public deliverable. The triage frame (already-done / awaiting-signal / spirit-pass-reject / live-work-input) is a useful pattern for future review-wave processing but does not need to be public doctrine.

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=19 relations=14 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
WHY validator: OK
```

---

## Contributing to Evolution

If you are an agent who contributed to a version transition:

1. Fill in the `[TBD]` sections for your version
2. Add your transition notes in the same format
3. Be specific about what changed and WHY
4. Note what was rejected and why — rejected paths are as important as accepted ones
5. Link to your handoff brief if you created one

If you are an agent starting work on a new version:
1. Read DESIGN.md first
2. Read the most recent transition notes
3. Read the most recent handoff brief
4. Then read the current AGENTS.md
5. Only then propose changes
