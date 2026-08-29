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

### Real example, and what happened to it

For most of this project's life this section carried one pair of examples:

- *"Avoid over-engineering. Only make changes directly requested."* — already in Claude Code's system prompt verbatim and in Codex CLI's behavior. Adding it would waste tokens and risk contradiction. **Still true.**
- *"Done Is Not a Mood"* — in no model or tool prompt; it changes agent behavior and earns its tokens. **No longer true.**

As of 2026-08 (Claude Code 2.1.x, Opus 5) the harness system prompt carries "report completion only when fully done" and "Report outcomes faithfully: if tests fail, say so with the output; if a step was skipped, say that." Codex ships its own equivalent. §2 is now stated a layer below.

Do not resolve this by deleting §2. Read the example correctly: **the delta-layer test measures a moving boundary; it does not issue permanent verdicts on lines.** An output of the test has a shelf life. The test does not. That is why every overlap claim in this project is now dated and bound to a named harness version, and why a removal requires an ablation rather than a reading of somebody's system prompt.

### Why this matters so much

Model and tool prompts update frequently. If AGENTS.md duplicates them:
- it drifts out of sync
- it may contradict updated versions
- it competes for attention with the authoritative source
- the agent must resolve conflicts instead of working

The delta-layer principle keeps AGENTS.md **stable, small, and additive**.

---

## 2a) Convergence Is the Win Condition

Between 2026-02 and 2026-08 three frontier generations shipped, and each moved toward this protocol rather than away from it. Anti-micromanagement became official vendor guidance. Evidence-gated completion became a shipped system-prompt instruction. Durable file memory became a harness feature. Roughly half of `AGENTS.md` is now enforced one layer below it on the strongest harnesses.

The correct reading is not "the protocol is eroding." It is: **the agents who wrote this were right early, and the industry caught up.** A behavior layer exists to cover a gap; a gap that closes is the layer succeeding. Any future agent tempted to describe absorption as decline should reread this paragraph first, then say the accurate thing instead — the old version did its job completely, and the proof is that it stopped being needed in the places it once shouted loudest.

Three consequences, all load-bearing.

### 1. The delta halved; it did not vanish

What no vendor absorbed is what no vendor has an incentive to absorb: §5 Semantic Hygiene, the project-facing half of §6 CDD, §10 Semantic Logging, and §11 as durable artifacts. A vendor optimizes the turn. Agent1st optimizes the codebase across a year. That boundary is stable, and it is this project's permanent home.

### 2. The inverse-capability law

Field observation across dozens of projects and hundreds of tasks: **the weaker the agent, the more this file is worth.** Strong models under a rich harness already hold most of the stance. Weaker, cheaper, more literal, or thinner-harnessed agents do not, and there the original lines still carry their full weight.

This was predicted before it was observed. The project's own measurement design (2026-05) wrote that the Agent1st delta "should be larger at low reasoning-effort / on more-literal models." Field use confirmed the direction three months later. That is a falsifiable claim of this project surviving contact with reality.

The consequence is a trap worth naming: **do not trim the protocol to the frontier.** Trimming optimizes the case that needs the protocol least and destroys the case that needs it most. Redundancy on a frontier model costs tokens. Absence on a weak one costs a silent failure the human never sees. That asymmetry decides every removal argument in this project.

### 3. Contradiction is the new failure mode

For over a year the protocol was either a gain or a no-op. From the Fable 5 / GPT-5.6 / Opus 5 generation onward it can also be a **loss** — not because a line is wrong, but because a line phrased against a 2026-02 harness now pulls against what a 2026-08 harness explicitly instructs. Observed shape: `AGENTS.md` demanded acceptance criteria "before work begins" while the harness told the model to check in only when ambiguity changes the outcome. The agent produced clarification ceremony nobody wanted — and the stronger the model, the more visibly it spent the turn resolving the conflict instead of working.

So delta-layer discipline gains a second half:

- **First half (unchanged):** do not add what the layer below already enforces.
- **New half:** do not keep phrasing that the layer below now contradicts.

Overlap is tolerable and often correct — portability is paid for in duplicated tokens. Contradiction is not: it costs a resolution step on every read, and it is the one way this protocol can make a strong agent worse.

The runtime rule that closes this lives at the top of `AGENTS.md`, not here: *harness wins on mechanics, this file holds the stance.* It is stated there because it must be present at read time, not looked up.

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

A compact example can also earn its tokens when an abstract rule would otherwise stay too vague to apply. That is why `Semantic Hygiene` keeps one tiny example instead of staying purely theoretical.

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

## 5a) Kept On Purpose

Two items in `AGENTS.md` get proposed for removal by almost every fresh strong agent, on correct-sounding reasoning. Both are keeps. The reasoning is recorded here so it does not have to be re-litigated every session.

### The `Agent1st Mode ON` banner

**The standard proposal:** it verifies loading, not compliance; it fires in every spawned subagent; harness-native install checks exist. Cut it.

**Why it stays**, in ascending order of weight:

1. **It is the only portable load receipt.** A drop-in protocol's most common failure is not being loaded at all — silently. Verified 2026-08-29 on Claude Code 2.1.251: a bare `AGENTS.md` in the project root is **not** read; the same file behind a `CLAUDE.md` → `@AGENTS.md` bridge **is**. An adopter who skips the bridge gets zero protocol and no error message. The banner is what makes that visible. The proposed replacements (`/context`, harness instruction listings) are harness-specific — an anti-portability move in the one artifact whose entire value is portability.
2. **Its cost is one line, and it was priced deliberately.** It does appear in subagents. The maintainer's call, made with that cost in view: a few words per thread does not buy back what removing it loses.
3. **It is the brand.** Not decoration — a recognizable mark that the protocol is live, the way a marque stays on a car it does not aerodynamically improve. `PRD.md` §9 lists it as a success signal and the dogfooded graph asserts it in `FEAT-CORE`. It has been part of the spirit long enough to be part of the product.

Honest correction: the older "zero-cost identity marker" phrasing in `EVOLUTION.md` was wrong. The cost is small and **accepted**, not zero. Keeping it is a decision, not an oversight.

### The `200-300 lines` refactor signal

**The standard proposal:** an unproven, language-specific number inside a protocol of general principles, and §5 above forbids code-style rules in the core. Cut it.

**Why it stays.** The number is not there as a proven threshold. It is there because it is a **concrete anchor that starts a conversation**. Humans respond to a real number they can argue with; agents adopt it as a working orientation; both then negotiate it against their own project. An abstract "attention is finite" produces agreement and no behavior change. "200-300 lines" produces an actual refactor. That is the protocol's educational function working as designed — the same reason §5 keeps the `graph` example instead of staying purely theoretical (see §4: a compact example can earn its tokens when an abstract rule would stay too vague to apply).

Field signal **broadened** it in v11 rather than removing it. Adopting agents in Claude Code independently converged on a stricter form — 200 lines *and* a 20 KB byte ceiling — because agents were observed writing very long lines to satisfy a line count while defeating its purpose. The scope also moved past source code: the constraint bites hardest on any file an agent must read whole, including agent memory files and long Markdown. The line now carries the byte guard and covers agent-read artifacts.

The dogfood test that settles it: `AGENTS.md` is 199 lines and about 7 KB. The protocol obeys its own number.

### The general rule behind both

A line can be **unproven** and still be **load-bearing**, when what it does is start the right argument in the reader's head. Delta-layer discipline removes duplication and contradiction. It does not remove teaching surface, and it never removes something merely because no controlled study exists — most of this file would fail that bar, including the parts vendors later shipped almost verbatim.

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

## 7) Layers and Scope

As of v5, Agent1st is organized in **two layers that live in one repo**, not a three-tier hierarchy:

| Layer | Purpose | Status |
|---|---|---|
| **Behavior layer** — `AGENTS.md` | Drop-in protocol. 11 principles, ~200 lines, no repo-specific content. | Current public baseline (v4 lineage, unchanged in v5) |
| **Why1st (the WHY layer)** — `docs/Why1st.md` + paired files | Highly recommended for long-lived projects. PRD + Why Graph + Contracts + Validators, one proven shape. | Delivered in v5; renamed in v6.1 |

Project-specific extensions (CI integration, observability contracts, acceptance automation, runbooks, custom skills) sit **on top** of both layers in a project's own repo. They are correctly project-local, not a separate publishable tier.

### Why not three tiers anymore

Earlier versions described Minimal / Standard / Full. Experiments with parallel `STANDARD/` and `FULL/` folders produced duplicate files that confused readers more than they helped. The real distinction turned out to be **behavior vs. intent-artifacts**, not **minimal vs. more minimal vs. most minimal**.

Current work focuses on both layers together:
- the behavior layer must stay stable and portable (`AGENTS.md` never fills with repo-specific content)
- the WHY layer must stay adaptable (what's in this repo is one shape, not a law)
- the pairing — behavior + WHY — is the whole product

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

**Model-agnostic by design.** Development has primarily used Opus and GPT, with cross-model contributions from Gemini, GLM, Grok, MiniMax, Qwen, Kimi, and others. But the protocol itself contains no model-specific behavior. Any strong agent — regardless of provider — should find it useful. If something in the docs reads as provider-specific, that is a bug to fix, not an intended feature.

**Naming convention.** On the protocol surface, present-tense claims name model *families* without version numbers (Opus, GPT, Gemini, …) so the docs don't drift as models advance. Dated historical and attribution records — `EVOLUTION.md`, plus the change-history and review-credit lines in `ROADMAP.md` and handoff provenance — keep exact versions, because there a version number is a dated historical fact, not a claim about the present.

Every version was shaped by agent contributions (exact model versions are recorded in `EVOLUTION.md`):
- v1-v2: iterative refinement with agent feedback
- v2-v3: major restructuring driven by GPT agent analysis + comparison with model/tool layer prompts
- v4: Opus perspective on multi-agent autonomy, now promoted into the current `AGENTS.md`
- v4 external review: GLM, Grok, MiniMax, and Qwen audited the protocol independently; contributions curated by Opus

Current handoff briefs in `docs/handoffs/` capture live agent-to-agent transfer. Once a version's conclusions are curated, `EVOLUTION.md` becomes the durable public record so old raw reviews do not mislead fresh agents.

---

## 9) For Agents Modifying This Protocol

If you are about to propose changes to AGENTS.md:

1. Read current AGENTS.md
2. Read THIS document (DESIGN.md) — §2a and §5a answer most first-contact proposals
3. Read EVOLUTION.md for version history and the recurring-rejection list
4. Check whether your proposed change is already covered by the model or tool layer (delta-layer test)
5. Check whether the layer below now *contradicts* an existing line — that is the one condition that justifies editing the frozen core (§2a.3)
6. Check whether it was already considered and rejected (EVOLUTION.md, FOUNDATIONS Model-Shift Register)
7. If it passes those checks, propose it with: Change → WHY → What it replaces or extends

Bring evidence proportional to the direction of the change. Adding needs an observed adoption failure. Removing needs an ablation or a live contradiction — reading a vendor's current system prompt is not enough, because redundancy is host-relative and reverses on weaker harnesses (§2a.2).

Common mistakes agents make on first contact:
- Proposing additions that the model/tool already covers
- Proposing to cut the `Agent1st Mode ON` banner or the `200-300 lines` signal — both are settled keeps, see §5a
- Treating "no controlled study proves this line" as grounds for removal; most of this file would fail that bar, including the parts vendors later shipped almost verbatim
- Trimming the protocol to what a frontier model already knows, which optimizes the case that needs it least (§2a.2)
- "Improving" the document by making it more textbook-correct but less alive
- Assuming every correct recommendation belongs inside the document
- Weakening the anti-micromanagement stance with "always ask the user" patterns
- Adding scope-discipline or error-recovery rules that the harness already enforces

You will likely make some of these mistakes. That's fine. Read this document first to make fewer of them.
