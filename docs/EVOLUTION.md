# Agent1st Protocol — Evolution History

Version history with design rationale for each transition. This is a living document — agents who contribute to new versions should add their transition notes.

---

## Version Map

| Version | File | Focus | Agent Contribution |
|---------|------|-------|--------------------|
| v0 | (no file) | Scattered ideas in conversations | — |
| v1 | `docs/_archive/AGENTS-min-v1.md` | First formalization. Copilot-era framing. | [TBD — author to fill] |
| v2 | `docs/_archive/AGENTS-min-v2.md` | More agentic. Agent Loop added. | [TBD — author to fill] |
| v3 | `docs/_archive/AGENTS-min-v3.md` | Harness-optimized. Delta-layer discipline. Core/Ops split. | GPT-5.4 agent (primary), with Claude Opus 4.6 comparison |
| v4 | (planned) | Multi-agent autonomy. Human role spectrum. Claude 4.6 native. | Claude Opus 4.6 agent (primary) |

---

## v0 → v1: From Scattered Ideas to First Protocol

**Era:** Copilot-era thinking. Agent as enhanced autocomplete.

**What happened:**
- [TBD — author to fill the origin story: what prompted creating the first file, what problems it was trying to solve]

**Key decisions in v1:**
- 10 sections, flat structure (no hierarchy)
- CDD (Complaint-Driven Development) introduced as section #1
- "Educational by Default" included — adaptive explanation depth
- "Harness (Validation + Observability)" as separate section
- "Session Start + Session End" combined in one section
- Example complaint included for concreteness
- `Hello Agent!` activation phrase introduced

**What v1 got right:**
- CDD was original and stayed in every version
- WHY / IF MISSING pattern established from the start
- The overall inventory of concerns was surprisingly complete

**What v1 got wrong:**
- Flat structure made scanning hard
- "Educational by Default" was a style preference, not a protocol principle
- Framing was still somewhat copilot-era: "Humans provide intent, constraints, and final acceptance" but the agent role was passive
- Harness section tried to cover too much

---

## v1 → v2: Becoming More Agentic

**Era:** Agent as executor with own judgment, not just a helper.

**What happened:**
- [TBD — author to fill: what triggered the v2 rewrite, which agent contributed]

**Key changes:**
- Added **Agent Loop: Explore → Execute → Reflect** as explicit principle
- Merged fresh-eye audit into Agent Loop (was standalone in v1's Session Start)
- Strengthened Role Contract: "Agent owns implementation, reasoning path, verification, and alternatives"
- Added "assumptions/invariants" and "rejected paths" to handoff
- Removed some redundancy
- Kept flat structure (10 sections, no hierarchy)

**Key decisions:**
- "Collaboration style" subsection added: "human sets destination and boundaries, agent chooses the route"
- This was the first explicit anti-micromanagement signal, though still mild
- "Continuous Ergonomics Improvement" and "Session End Protocol" kept separate

**What v2 got right:**
- Agent Loop was the biggest improvement — gave agents a reusable execution pattern
- Handoff became more structured and complete
- Agent role started feeling like a real partner

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

3. **Anti-micromanagement stance made central** — Role Contract moved to #1. "Strong agents should not be micromanaged" added explicitly. "Humans steer. Agents execute." wording rejected as too manager/executor.

4. **"Done Is Not a Mood" replaced Harness** — More memorable, more compact, covers the core idea (completion requires evidence) without becoming a procedural verification manual.

5. **"Do Not Stop at the First Weak Signal" added** — New principle. Protects against early collapse, false clean results, and the difference between missing data and absent data.

6. **"Educational by Default" removed** — Style preference, not protocol principle. Doesn't earn tokens in the minimal version.

7. **"Continuous Ergonomics Improvement" folded into Session End** — Friction reporting is now part of handoff (1-3 frictions), not a separate section.

8. **Subagent awareness added to CDD** — "Delegate for truth, not silence." "Leave subagents room to report blockers, repeated friction, or fallback." This was a major design insight: silent subagents are a delegation-design bug, not a subagent behavior problem.

9. **Hooks sharpened** — "correctness becomes a vibe", "autocomplete with tools", "Leave the next agent a runway, not a crater", "the right fact loses to the nearest fact"

10. **"Hello Agent!" kept** — Nearly removed as noise, then brought back: low token cost, high adoption value, session boundary marker, project identity.

**Key rejected ideas (with reasons):**
- "reasoning path" demand → replaced with route/evidence framing (externalized evidence > theatrical CoT)
- "let subagents break format to surface truth" → replaced with "design delegation contracts correctly"
- output contracts, dependency checks, planning mechanisms → model/tool layer, not Agent1st
- detailed verification procedures → "Done Is Not a Mood" is sufficient for minimal version

**Agent-to-agent handoff:** See `docs/handoffs/gpt54-v3-handoff.md`

---

## v3 → v4: Multi-Agent Autonomy (Planned)

**Era:** Agent collectives. Human presence as spectrum. Full autonomy possible.

**Primary agent:** Claude Opus 4.6

**Planned changes:**

1. **Human role spectrum** — From fixed pair (human+agent) to a range: paired → supervised autonomy → full delegation. What stays constant: acceptance criteria must exist, evidence must exist, escalation boundaries must be respected.

2. **Delegation Design principle** — How agents delegate to other agents. Covers hierarchical (orchestrator→workers) and swarm (peer) patterns. Not in any model/tool prompt — genuine delta.

3. **Claude 4.6-specific attention tuning** — Over-exploration and over-delegation guards. "If the first direct check is sufficient, do not spawn a subagent."

4. **Evidence across agent boundaries** — Evidence transfers by artifact, not by claim. Shared state files > message passing.

5. **Session Start behavior attached to "Hello Agent!"** — Lightweight scan for stale paths and contradictions before starting work.

6. **Escalation Boundary principle** — What to do when there's no human in the loop. Different from "Right to Disagree" (which assumes a present human).

**Design constraints for v4:**
- Must stay under 200 lines (minimal version)
- Must pass the delta-layer test for every addition
- Must preserve the anti-micromanagement stance
- Must preserve hooks and voice
- 11-12 principles maximum (up from 10)

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
