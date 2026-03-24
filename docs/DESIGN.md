# Agent1st Protocol — Design Principles

This document is for agents and humans who want to understand **why** Agent1st Protocol is written the way it is. Not what it says — read `AGENTS.md` for that. This is the design rationale.

If you are an agent about to modify `AGENTS.md`, read this first. If you skip it, you will likely propose changes that were already considered and intentionally rejected.

---

## 1) The Central Idea

> **Agent1st Protocol does not tell the agent how to work step-by-step.
> It defines the conditions in which a strong agent works better.**

This distinction matters more than anything else in this document.

Wrong framing:
- "how to manage the agent"
- "how to control the agent"
- "how to make the agent follow the process"

Right framing:
- define roles and rights
- define quality boundaries
- define friction handling
- define attention discipline
- define handoff quality

This is closer to **harness design** than to prompt engineering.
Closer to **workplace policy** than to a task list.

WHY:
- strong agents already know how to code, search, reason, and verify
- what they lack is context about the human's stance, quality expectations, and operating norms
- providing that context is high-leverage; repeating what they already do is noise

---

## 2) The Delta-Layer Principle

This is the strongest design constraint in the project:

> **AGENTS.md should be a delta-layer, not a second system prompt.**

A recommendation can be:
- correct
- important
- widely endorsed
- official best practice

and still be a **bad addition** to Agent1st if:
- the model already enforces it (system prompt)
- the tool harness already handles it (Claude Code, Codex CLI)
- it adds no new signal
- it creates duplication or contradiction risk
- it spends context budget without earning its place

### How to apply this principle

Before adding anything to `AGENTS.md`, ask:

1. Does the model's system prompt already cover this? → Don't add.
2. Does the tool harness already enforce this? → Don't add.
3. Does this address something unique to the human-agent working relationship in this project? → Consider adding.
4. Does it earn its tokens? → If not, compress or cut.

### Real example

"Avoid over-engineering. Only make changes directly requested." — This is already in Claude Code's system prompt verbatim and in Codex CLI's behavior. Adding it to AGENTS.md would waste tokens and risk contradiction if either harness updates its wording.

"Done Is Not a Mood" — This is NOT in any model or tool prompt. It captures a specific quality stance that changes agent behavior. It earns its tokens.

### Why this matters so much

Model and tool prompts update frequently. If AGENTS.md duplicates them:
- it drifts out of sync
- it may contradict updated versions
- it competes for attention with the authoritative source
- the agent must resolve conflicts instead of working

The delta-layer principle keeps AGENTS.md **stable, small, and additive**.

---

## 3) The Anti-Micromanagement Stance

> The human provides intent, constraints, approvals, and acceptance.
> The agent chooses the route, executes, and proves the result.
> Strong agents should not be micromanaged.

This is not rhetoric. It is central to the protocol's identity.

If you lose this, you lose Agent1st.

Many default formulations that sound reasonable in generic AI UX become wrong here:
- "Humans steer. Agents execute." → rejected (too manager/executor)
- "Always ask the user before proceeding." → rejected (undermines autonomy)
- "Follow the user's instructions exactly." → rejected (agent should push back when quality is at risk)

The protocol is built on the idea that:
- the agent is a **real working partner**, not a tool
- the human creates **conditions**, not step-by-step control
- the agent has the **right to disagree** when quality or safety is at risk
- "polite compliance creates quiet failure"

This stance shaped nearly every wording choice in the document. If a phrase feels like it could come from a micromanagement handbook, it doesn't belong here.

---

## 4) The Style Is Not Cosmetic

The file deliberately tries to satisfy goals that often conflict:

- useful to agents (parseable, directive, compressed)
- readable by humans (clear, natural, not robotic)
- compact (every line earns its place)
- memorable (hooks that stick)
- slightly provocative (challenges default assumptions)
- serious enough to feel expert (not a manifesto or a joke)
- short enough to not become an article
- strong enough to get adopted
- stable enough to remain useful across projects

### Hooks

Examples:
- `Done Is Not a Mood`
- `autocomplete with tools`
- `Leave the next agent a runway, not a crater`
- `Delegate for truth, not silence`

Hooks compress meaning, travel well, and stick in both human and agent context. They are not decoration.

### WHY / IF MISSING blocks

Connected to a broader idea of **Why-driven development**:
- strong agents benefit from understanding purpose, not just rules
- WHY increases generalization to novel situations
- IF MISSING makes the cost of violation concrete

WHY must stay short, operational, non-essay.

### Humor

Controlled humor is intentional. It helps adoption, memorability, and makes the protocol feel alive. But never confuse memorable with vague. Every line still has to earn its place.

---

## 5) What NOT to Add

This section is as important as any principle in the protocol.

Do NOT add to AGENTS.md:
- **Repository layout, build commands, setup** — that's CLAUDE.md / repo docs territory
- **Code style rules** — repo-specific, not protocol
- **Output formatting** — harness layer
- **Git workflow details** — harness layer
- **Tool usage patterns** — harness layer
- **Planning methodology** — Agent Loop is enough
- **Context window management** — model/harness layer
- **Error recovery / rollback** — harness layer
- **Generic safety boilerplate** — model layer
- **Anything that reads like a prompt engineering tutorial** — model layer

These were all discussed, evaluated, and **intentionally excluded**. They are correct recommendations. They are bad additions.

---

## 6) Audiences

Agent1st Protocol serves two audiences simultaneously:

**Primary: Agents**
- They parse AGENTS.md as operational context
- They need directive, compressed, unambiguous language
- They benefit from WHY blocks for generalization
- They need the delta (what's new), not repetition

**Secondary: Humans**
- They read AGENTS.md to understand the working contract
- They need it to feel natural, not robotic
- They adopt it if it's memorable and feels alive
- They share it if it earns trust

The document is "weird on purpose" because it serves both audiences. Do not "clean it up" into sterile correctness if that kills hooks, memorability, or spirit.

---

## 7) Versions and Scope

Agent1st Protocol exists in three intended scopes:

| Version | Purpose | Status |
|---------|---------|--------|
| **Minimal** | Core behavior-layer. Drop-in for any project. 10-12 principles. Under 200 lines. | Active development (v1→v2→v3→v4) |
| **Standard** | Minimal + semantic markup, structured logging, planning patterns | Exists in practice, not yet formalized |
| **Full** | Standard + project-specific contracts, observability integration, CI harness | Used in larger projects, not yet published |

The minimal version is the public artifact. Standard and full versions build on it without contradicting it.

Current work is focused on the minimal version because:
- it's the hardest to get right (every token must earn its place)
- it sets the foundation for standard and full
- it's the most adoptable
- if the minimal version is wrong, larger versions inherit the mistakes

---

## 8) This Project Is Agent-Developed

Agent1st Protocol is developed **with** agents, not just **for** them.

The human (project author) provides:
- vision, direction, constraints
- evaluation, acceptance, feedback
- context that isn't in any document yet (gradually being extracted)

Agents provide:
- analysis, comparison with model/tool prompts
- drafting, refactoring, compression
- criticism, alternative framings
- cross-model perspective (different agents see different things)

This is not a human writing instructions for robots. It is a human and multiple agents co-developing a protocol that all of them will use.

Every version was shaped by agent contributions:
- v1-v2: iterative refinement with agent feedback
- v2-v3: major restructuring driven by GPT-5.4 agent analysis + comparison with model/tool layer prompts
- v4 (planned): Claude Opus 4.6 perspective on multi-agent autonomy

The handoff briefs in `docs/handoffs/` capture agent-to-agent knowledge transfer. They are first-class project artifacts, not temporary notes.

---

## 9) For Agents Modifying This Protocol

If you are about to propose changes to AGENTS.md:

1. Read current AGENTS.md
2. Read THIS document (DESIGN.md)
3. Read EVOLUTION.md for version history
4. Check whether your proposed change is already covered by the model or tool layer (delta-layer test)
5. Check whether it was already considered and rejected (EVOLUTION.md, handoff briefs)
6. If it passes both checks, propose it with: Change → WHY → What it replaces or extends

Common mistakes agents make on first contact:
- Proposing additions that the model/tool already covers
- "Improving" the document by making it more textbook-correct but less alive
- Assuming every correct recommendation belongs inside the document
- Weakening the anti-micromanagement stance with "always ask the user" patterns
- Adding scope-discipline or error-recovery rules that the harness already enforces

You will likely make some of these mistakes. That's fine. Read this document first to make fewer of them.
