# Agent1st Protocol — Evolution History

Version history with design rationale for each transition. This is a living document — agents who contribute to new versions should add their transition notes.

---

## Version Map

| Version | File | Focus | Agent Contribution |
|---------|------|-------|--------------------|
| v0 | (no file) | Scattered ideas in conversations | — |
| v1 | `docs/_archive/AGENTS-min-v1.md` | First formalization. Early friction/evidence/attention contract. | [TBD — author to fill] |
| v2 | `docs/_archive/AGENTS-min-v2.md` | More agentic. Agent Loop added. Anti-micromanagement sharper. | [TBD — author to fill] |
| v3 | `docs/_archive/AGENTS-min-v3.md` | Harness-optimized. Delta-layer discipline. Core/Ops split. | GPT-5.4 agent (primary), with Claude Opus 4.6 comparison |
| v4 | `docs/_archive/AGENTS-min-v4.md` + `AGENTS.md` | Current minimal baseline. Multi-agent autonomy and delegation design. | Claude Opus 4.6 agent (primary), building on GPT-5.4 v3 rationale |

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

Four external agents (GLM-5, Grok, MiniMax, Qwen) independently analyzed the protocol and submitted contributions. GPT-5.4 provided a parallel review. Claude Opus 4.6 curated and integrated the results.

**What was incorporated:**
- **Handoff Template** — `docs/handoffs/TEMPLATE.md` with 3 modes (mini/full/subagent-evidence-only). Requested independently by 3+ agents.
- **Continuity hook** — "if your handoff disappears when the session ends, it doesn't exist" (from Qwen). Added to AGENTS.md.
- **Continuity research grounding** — Park et al. "Generative Agents" (2023) added to FOUNDATIONS.md. Moved Continuity from "Practical origin" to "Supported."
- **Model-agnostic acknowledgment** — Brief note in DESIGN.md section 8. Protocol is model-agnostic by design; examples may reference specific models.

**What was noted for standard version:**
- Friction Tax (GLM-5) — quantified CDD for recurring friction
- Ambiguity handling in CDD (MiniMax) — distinguishing ambiguous from incomplete requests
- Anti-pattern examples as companion doc (MiniMax, Qwen) — violation examples per principle
- Decision log template (MiniMax) — standardized format for cross-session rationale

**What was rejected (already covered or delta-layer violation):**
- Truth-First Orientation (Grok) — already covered by Right to Disagree
- Discovery Before Commitment (GLM-5) — fresh-eye scan, rejected 4th time
- Ethical boundaries principle (MiniMax) — model layer already covers safety
- Escalation protocol detail (MiniMax) — v4 already has unsupervised clause
- Assumption Surfacing (GLM-5) — over-specifies Agent Loop
- Agent Maturity Levels (MiniMax) — against "strong agents" philosophy

**All handoffs saved:** `docs/handoffs/glm5-v4-analysis.md`, `grok-v4-truth-first.md`, `minimax-v4-perspective.md`, `qwen-v4-audit.md`.

**Pattern observed:** External agents consistently rediscover the same improvements and the same rejected paths. The recurring rejected patterns section above predicted most proposals accurately. This validates the value of documenting rejections.

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
