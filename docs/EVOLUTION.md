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
| v5 | `AGENTS.md` (unchanged) + `docs/WHY-APPROACH.md` + paired WHY files | WHY layer delivered as flat files in `docs/`. Three-tier framing retired. | Claude Opus 4.6 (primary), with reference analysis of SPS3A (see `docs/SPS3A-ANALYSIS.md`) and a separate TypeScript adopter |
| v5.1 | same files, sharpened | External-review integration round. Staleness named as first-class failure. Workflow shape stops being a universal law. Teaching-surface bugs fixed. | Claude Opus 4.6 (primary), integrating external reviews from GPT-5.4, MiniMax M2.7, Kimi K2.5, Qwen 3.6, Grok 4.20, plus off-target input from Gemini 3.1, Claude Opus 4.7, and Meta-Muse Spark |
| v6 | `AGENTS.md` (§8 + §9 patches) + `scripts/validate-why.py` + paired doc updates | Contract-and-signal release. Signal Discipline (asymmetric stop rule) replaces "Do Not Stop at the First Weak Signal". WHY validator MVP ships. Not a model-specific edition. | Claude Opus 4.7 (primary), acting on `docs/handoffs/v6-handoff-gpt-5.5-pro.md` from GPT-5.5-pro and a harness-observatory adaptation read |

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

**Agent-to-agent handoff:** See `docs/handoffs/gpt54-v3-handoff.md`

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

These imported handoffs are preserved as audit artifacts. Some observations reflect the repo snapshot each external agent saw at review time, not necessarily the current `main`.

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

**All handoffs saved:** `docs/handoffs/glm5-v4-analysis.md` (GLM-5), `docs/handoffs/grok-v4-truth-first.md` (Grok 4.20), `docs/handoffs/minimax-v4-perspective.md` (MiniMax M2.7), `docs/handoffs/qwen-v4-audit.md` (Qwen3.5-Plus).

**Pattern observed:** External agents consistently rediscover the same improvements and the same rejected paths. The recurring rejected patterns section above predicted most proposals accurately. This validates the value of documenting rejections.

---

## v4 → v5: The WHY Layer Lands

**Era:** Minimal is stable. Time to deliver what was called "standard" — without repeating the mistake that killed earlier attempts.

**The problem v5 had to solve:**

The roadmap had named "Standard Version Formalization" as an active priority for over a year. The reference implementation existed (SPS3A, documented in `docs/SPS3A-ANALYSIS.md`) and a second real adopter — a separate TypeScript project — had independently shaped its own variant. Earlier experiments put the richer files in parallel `STANDARD/` and `FULL/` folders, which created visual duplication and made it unclear which file was canonical. Users — agents and humans — found this confusing in practice.

**What changed:**

The three-tier model (Minimal / Standard / Full) was retired. Agent1st now has **two layers that live in one repo**:

1. **Behavior layer** — `AGENTS.md`, unchanged in v5. Still drop-in, still portable, still ~200 lines.
2. **WHY layer** — flat files in `docs/`, highly recommended for long-lived projects:
   - `docs/WHY-APPROACH.md` — the idea, workflow shift, adopter's pattern (Required Reading header)
   - `docs/PRD.md` — Agent1st's own dogfooded PRD
   - `docs/why-graph.xml` — teaching-size graph
   - `docs/why-graph-principles.md` — portable authoring guide distilled from SPS3A and a separate TypeScript adopter
   - `docs/why-contracts-v1.md` — anchor spec with Python + TypeScript examples

Project-specific extensions (CI integration, observability, acceptance automation, runbooks) correctly sit on top of both layers in a project's own repo — not as a separate publishable tier.

**Why the minimal `AGENTS.md` did not change:**

The delta-layer principle and the anti-micromanagement stance both say the same thing here: the behavior layer must be portable and must not fill with repo-specific reading lists. An advisor proposal to add a Required Reading header to the core `AGENTS.md` was considered and rejected. Instead, that header is documented in `WHY-APPROACH.md` §8 as the **adopter-side** extension pattern — observed in both real adopters.

**What was rejected during v5:**

- Keeping the `STANDARD/` and `FULL/` folder split. Reason: visual duplication, unclear canonicity, adoption friction.
- Renaming `docs/WHY-APPROACH.md` to `docs/STANDARD.md`. Reason: the layer is the WHY approach, not a rung on a ladder.
- Editing `AGENTS.md` to require reading the WHY layer. Reason: would break drop-in portability and contradict `DESIGN.md` §5 (what NOT to add).
- Building validator tooling into v5 itself. Reason: the pattern is demonstrated; tooling is a v6 concern and language-specific.

**Reference adopters that shaped v5:**

- **SPS3A** — the richer variant. Python/FastAPI backend plus TypeScript frontend. Full relation vocabulary, class/method contracts, intent1st integration, validator scripts. Documented in `docs/SPS3A-ANALYSIS.md`.
- **A separate TypeScript adopter** — the simpler variant. Trimmed node families, adoption-notes doc that articulated the governance-graph vs. knowledge-graph distinction that `WHY-APPROACH.md` §5 now carries.

Neither adopter copied the other. Both carried the same idea. That convergence was the signal that the WHY layer was ready to be documented.

### v5.1 — External review integration (2026-04-17)

v5 went out to eight external agents for review (Claude Opus 4.7, GPT-5.4, Gemini 3.1, Grok 4.20, Kimi K2.5, Meta-Muse Spark, MiniMax M2.7, Qwen 3.6). Full handoffs live under `docs/handoffs/v5-review-*.md`.

**Accepted and landed in v5.1:**

- **Teaching-surface fixes (GPT-5.4):** fixed the `COVERS` relation direction in `why-graph-principles.md` §7 (now correctly placed on the `USECASE_*` node); unified `TARGET` syntax across principles and dogfood graph (pick one convention per repo); moved `why-graph.xml` scope disclaimer from the bottom of the file to the top.
- **Three-tier residue removal (GPT-5.4):** `ROADMAP.md` opening now says "two layers"; `PRD.md` §2 "two tiers" → "two layers"; open question in §10 dropped "FULL-layer" framing.
- **Graph staleness as first-class failure mode (MiniMax M2.7):** new `WHY-APPROACH.md` §6a names staleness explicitly and gives a recovery protocol, plus an honest adoption criterion: if your team cannot commit to running the validator regularly, the layer costs more than it saves.
- **Workflow-shape intensity (GPT-5.4, MiniMax M2.7):** `WHY-APPROACH.md` §3 and §6 no longer prescribe "graph first" as universal law. Distinguishes intent-changing/cross-cutting work (graph first) from local edits in well-mapped features (graph moves with code, same commit). §6 also distinguishes first-session onboarding, returning sessions, and delegated subagents.
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

## v5.1 → v6: Contract-and-signal release, validator MVP lands

**Era:** GPT-5.5 and Claude Opus 4.7 are the new frontier targets. The temptation is to add model-specific guidance to `AGENTS.md`. The decision was the opposite — strong agents need clearer contracts, not longer instructions.

**Primary agent:** Claude Opus 4.7

**Inputs that shaped v6:**

- `docs/handoffs/v6-handoff-gpt-5.5-pro.md` from GPT-5.5-pro, framed explicitly as a working TZ rather than another opinion.
- A subagent-led mapping of `harness-observatory`, a downstream adopter that already has a working stdlib(-ish) anchor validator with STATE-aware enforcement.
- The official OpenAI GPT-5.5 prompt-guidance and Anthropic Claude Opus 4.7 migration documents — both pushing toward outcome-first, contract-clear prompts and against carrying over legacy prompt stacks.

**v6 thesis:**

> Strong agents need clearer contracts, not longer instructions.

This is a contract-and-signal release plus a validator MVP. It is explicitly **not** a GPT-5.5 / Opus 4.7 edition. No model-specific knobs (reasoning effort, verbosity, adaptive thinking, sampling parameters) were added to `AGENTS.md`. Those belong to the model/harness layer.

**Accepted in v6:**

- **`AGENTS.md` §8 — Signal Discipline replaces "Do Not Stop at the First Weak Signal".** Adds the symmetric stop rule: do not stop at a weak signal; do stop at a sufficient signal. Preserves the v3/v4 anti-weak-signal insight while closing the ritual-over-checking failure mode that frontier agents now exhibit. Aligns with GPT-5.5 stopping-condition guidance without naming it. Strongest delta-layer-passing change in the GPT-5.5-pro handoff.
- **`AGENTS.md` §9 — one line on delegation optimization target.** Discovery and review delegations now state whether the job optimizes for coverage, precision, speed, or evidence depth. Closes a real silent-filtering failure mode: a subagent asked for "review" may optimize for precision and omit lower-confidence findings when the parent needed coverage. Operational, model-agnostic, one bullet.
- **`scripts/validate-why.py` — WHY validator MVP.** Stdlib-only Python (no `lxml` dependency on a docs-only protocol repo). Checks: XML parses, IDs unique, REL TYPE is in the documented vocabulary, REL TARGET resolves (family-qualified or bare), TARGET style consistent across the graph, ANCHOR shape if present, STATE-aware anchor enforcement (`PLANNED`/`DEPRECATED` skipped, `STARTED`/`DONE`/`IMPLEMENTED` enforced). Degrades to a warning, not a failure, when the graph has no anchors yet — the dogfooded graph is teaching-only on purpose. Output uses CDD-style problem reporting (Problem / Smallest fix). Passes on the current `docs/why-graph.xml` with the expected "no anchors" warning.
- **`docs/why-graph-principles.md` §8 + `docs/PRD.md` §6 + FEAT-WHY state** — one-line references to the validator command, no doc-cascade rewrites.

**Rejected or deferred in v6:**

- **§1 Role Contract candidate change A (GPT-5.5-pro).** Proposed adding bullets about task-contract clarity and an assume/ask rule for missing details. The compressed version still landed at five bullets where the original has three; the assume/ask rule partially duplicates §3 (Right to Disagree) and the §1 escalation language. Failed the bullet-count discipline test ("if §1 ends with more bullets than it started with, defer §1"). Bloating the most-read section of `AGENTS.md` to demonstrate the "clearer contracts, not longer instructions" thesis is self-undermining. Deferred until a wording exists that compresses, not grows.
- **`EVIDENCED_BY` relation (proposed in v5.1).** The validator MVP gives evidence-tracking teeth without expanding the relation vocabulary. Adding a relation just to wire validators into the graph would push the vocabulary past the "small and stable" target without changing what the validator actually checks. Deferred indefinitely; revisit only if a real downstream project finds the validator missing a check it can't add locally.
- **All model-specific API knobs in `AGENTS.md`.** Reasoning effort, verbosity, adaptive thinking, sampling parameters, hosted tools, prompt caching, `previous_response_id`, Claude `task_budget`, temperature/top_p/top_k advice, model-specific tool-use heuristics. All belong to the harness or model layer. If a project needs a model-specific note, it goes in `CLAUDE.md`, a project-local config, or `EVOLUTION.md` — not in the portable behavior layer.
- **A model-named v6 ("GPT-5.5 edition" / "Opus 4.7 edition").** Naming the version after the models that triggered the review would normalize model-coupled releases. Agent1st is provider-agnostic by constitution.

**v6 acceptance criteria, per the GPT-5.5-pro handoff §14:**

- ✅ `AGENTS.md` remains minimal and model-agnostic.
- ✅ Every `AGENTS.md` change passes the delta-layer test.
- ✅ No model/API parameter added to `AGENTS.md`.
- ✅ Signal Discipline replaces §8.
- ✅ §1 / §9 / §1 changes either compactly accepted or explicitly rejected with rationale.
- ✅ WHY validator MVP exists and runs deterministically.
- ✅ Validator output is grep-friendly and uses CDD-style problem reporting.
- ✅ This file records accepted, rejected, and deferred decisions.
- ✅ `why-graph-principles.md` §8 mentions the validator command.
- ✅ Final completion claim includes evidence (validator run output, exit code).

**Evidence:**

```
$ python scripts/validate-why.py
WHY validator: nodes=18 relations=13 anchors_validated=0 anchors_skipped=0 errors=0 warnings=1
- [warning] <graph>
  Problem: no ANCHOR elements found
  Smallest fix: acceptable for a docs-only dogfood graph; add anchors when adopting this layer in a code repo
WHY validator: OK
exit=0
```

**Process note:** The harness-observatory mapping was delegated to an Explore subagent rather than done by the primary agent. The 600-word report came back in under a minute and gave the validator-design pattern (STATE-aware enforcement) without burning primary-agent context on raw exploration. This is the v6 example for §9's new optimization-target line: the delegation explicitly said "decision-grade signal, not a tour" — the deliverable was framed for evidence depth, not coverage.

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
