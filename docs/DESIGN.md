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
- define how project truth survives sessions

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

1. Does the model or harness already own the mechanics? → Do not coach them again.
2. Does the line define the human-agent working relationship? → It may still earn its place even when mechanics overlap.
3. Does it carry project-level meaning a generic harness cannot know? → Consider adding.
4. Can an agent act on it and a human understand what to expect? → If only one audience benefits, rewrite.
5. Does it earn repeated context? → If not, compress or cut.

### Real example, and what happened to it

For most of this project's life this section carried one pair of examples:

- *"Avoid over-engineering. Only make changes directly requested."* — already in Claude Code's system prompt verbatim and in Codex CLI's behavior. Adding it would waste tokens and risk contradiction. **Still true.**
- *"Done Is Not a Mood"* — originally absent from model and tool prompts; now substantially enforced by modern harnesses. **Still kept.**

Why the different result? The first sentence only coaches execution. The second also tells the human what "done" means in this working relationship, gives the agent a memorable quality boundary, and supports the project's evidence layer. Overlap is one input to the decision, not the whole decision.

v12 provides the opposite example. `Agent Loop` and `Do Not Stop at the First Weak Signal` were valuable when harnesses did not reliably explore, execute, verify, and persist. Once those mechanics became the floor, their remaining standalone teaching value no longer justified permanent injection. Their evidence remains in FOUNDATIONS; the procedural scaffolding does not remain in every task.

The delta-layer test measures a moving boundary and it is allowed to change the current file. Git history and exact archived editions preserve what earlier agents needed; the startup context does not have to become their museum.

### Why this matters so much

Model and tool prompts update frequently. If AGENTS.md duplicates them:
- it drifts out of sync
- it may contradict updated versions
- it competes for attention with the authoritative source
- the agent must resolve conflicts instead of working

The delta-layer principle keeps AGENTS.md **stable, small, additive, and meaningful to both audiences**.

---

## 2a) Convergence Must Change the Protocol

Between 2026-02 and 2026-08 three frontier generations moved toward this protocol. Anti-micromanagement became official vendor guidance. Evidence-gated completion became system-prompt behavior. Persistence, verification loops, and basic delegation mechanics became harness features.

The correct reading is not "the protocol is eroding." The earlier protocol did its job. But success that never removes a repeated instruction is only ceremonial success.

v11 correctly fixed the first live contradiction and correctly insisted that Agent1st remain useful beyond one vendor. It then drew the wrong universal conclusion: keep every principle in every future context because a weaker agent may still need it. That asks one current file to be both history and instruction, and makes the strongest runtime pay the weakest runtime's context bill.

v12 revises the single protocol in place. Earlier editions remain exact in `docs/_archive/`; the current `AGENTS.md` carries what still deserves to be read on every task.

Three tests decide what survives convergence.

### 1. Mechanics may leave

If a principle's remaining job is to prescribe an execution loop the harness now reliably owns, remove it. v12 retires `Agent Loop` and the standalone weak-signal rule on this basis. Their history and evidence remain; their instructions no longer compete with the task.

### 2. Working-contract meaning may stay

Role ownership, evidence-backed completion, and the right to disagree overlap modern mechanics and still earn their place. They tell humans what relationship they are entering and give agents memorable permission and quality boundaries. Agent1st is not only machine control text; its human readability is part of the product.

### 3. Project meaning stays until the project no longer needs it

Semantic Hygiene, project-facing CDD, delegation as a contract, semantic logs, and durable project state govern behavior a generic vendor cannot fully supply. A vendor can provide tools for the turn. It cannot name your concepts or decide what must survive in your repository.

Contradiction remains an immediate failure: do not keep wording that pulls against higher-priority mechanics. Overlap is judged by meaning, not automatically accepted or automatically removed.

Dated model comparisons, install caveats, and release reasoning belong in DESIGN, FOUNDATIONS, EVOLUTION, and README. Putting them at the top of `AGENTS.md` makes every future agent reread yesterday's editorial argument instead of today's project intent.

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
- **Planning methodology** — modern model and harness layer
- **Context window management** — model/harness layer
- **Error recovery / rollback** — harness layer
- **Generic safety boilerplate** — model layer
- **Anything that reads like a prompt engineering tutorial** — model layer

These were all discussed, evaluated, and **intentionally excluded**. They are correct recommendations. They are bad additions.

---

## 5a) Teaching Surface Is Not Technical Preamble

Agent1st must be memorable to humans and operational to agents. That gives examples, names, and even one small ritual a legitimate job. It does not give release commentary, compatibility routing, or arbitrary numbers permanent residence in the file every agent reads.

### The `Agent1st Mode ON` banner

**The standard proposal:** it verifies loading, not compliance; it fires in every spawned subagent; harness-native install checks exist. Cut it.

**Why it stays**, in ascending order of weight:

1. **It is the only portable load receipt.** A drop-in protocol's most common failure is not being loaded at all — silently. Verified 2026-08-29 on Claude Code 2.1.251: a bare `AGENTS.md` in the project root is **not** read; the same file behind a `CLAUDE.md` → `@AGENTS.md` bridge **is**. An adopter who skips the bridge gets zero protocol and no error message. The banner is what makes that visible. The proposed replacements (`/context`, harness instruction listings) are harness-specific — an anti-portability move in the one artifact whose entire value is portability.
2. **Its cost is one line, and it was priced deliberately.** It does appear in subagents. The maintainer's call, made with that cost in view: a few words per thread does not buy back what removing it loses.
3. **It is the brand.** Not decoration — a recognizable mark that the protocol is live, the way a marque stays on a car it does not aerodynamically improve. `PRD.md` §9 lists it as a success signal and the dogfooded graph asserts it in `FEAT-CORE`. It has been part of the spirit long enough to be part of the product.

Honest correction: the older "zero-cost identity marker" phrasing in `EVOLUTION.md` was wrong. The cost is small and **accepted**, not zero. Keeping it is a product and brand decision, not an efficiency claim.

### The `200-300 lines` refactor signal

**Why it once stayed.** The number made an abstract attention problem concrete. Humans argued with it, agents acted on it, and field use exposed that line count alone could be gamed by long lines. v11 widened it to a line and byte heuristic.

**Why v12 removes it.** The success of the teaching anchor also proved its limit: useful thresholds depend on language, artifact shape, and how a project reads files. Once the core had to explain the number, its scope, its exceptions, and its byte companion, a compact lesson had become project policy plus an article defending itself.

The principle survives: attention is finite, and context that does not change a decision should leave. Projects may set concrete local thresholds where their evidence supports them. The exact v5.1 and v11 formulations remain in `docs/_archive/` for adopters who deliberately want the old default.

### The general rule

A line can be **unproven** and still be **load-bearing** when it starts the right argument in the reader's head. But teaching surface must stay teaching surface: one clear example or phrase, not a compatibility essay or a policy that needs footnotes.

Compression has the same limit. Do not fuse distinct ideas into compound principles merely to save headings. A smaller file with a worse mental model is not attention engineering; it is loss of meaning.

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
| **Behavior layer** — `AGENTS.md` | Drop-in protocol. 9 distinct principles, 165 lines, no repo-specific content. | Current public baseline (v12) |
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
- v11: Opus 5 broke the 123-day freeze to repair a live harness contradiction
- v12: GPT-5.6-Sol distilled the current protocol after maintainer correction restored the human-facing, pedagogical meaning of the file

Current handoff briefs in `docs/handoffs/` capture live agent-to-agent transfer. Once a version's conclusions are curated, `EVOLUTION.md` becomes the durable public record so old raw reviews do not mislead fresh agents.

---

## 9) For Agents Modifying This Protocol

If you are about to propose changes to AGENTS.md:

1. Read current AGENTS.md
2. Read THIS document (DESIGN.md) — §2a and §5a answer most first-contact proposals
3. Read EVOLUTION.md for version history and the recurring-rejection list
4. Check whether your proposed change is already covered by the model or tool layer (delta-layer test)
5. Check whether the layer below now contradicts an existing line or has absorbed a purely mechanical principle (§2a)
6. Check whether it was already considered and rejected (EVOLUTION.md, FOUNDATIONS Model-Shift Register)
7. If it passes those checks, propose it with: Change → WHY → What it replaces or extends

Bring evidence proportional to the direction of the change. Adding needs an observed adoption failure. Removing needs more than keyword overlap: show that the line's remaining job is mechanical and that it no longer carries enough human-contract or project meaning to earn repeated context.

Common mistakes agents make on first contact:
- Proposing additions that the model/tool already covers
- Treating every old keep as permanent merely because it once taught something useful; v12 removed the numeric signal after its explanation outgrew its lesson (§5a)
- Treating "no controlled study proves this line" as grounds for removal; most of this file would fail that bar, including the parts vendors later shipped almost verbatim
- Trimming only by model knowledge while ignoring what the protocol teaches its human reader
- Combining separate ideas into compound headings for line-count savings
- Writing release notes or model versions into `AGENTS.md`; every agent pays for that prose on every task
- "Improving" the document by making it more textbook-correct but less alive
- Assuming every correct recommendation belongs inside the document
- Weakening the anti-micromanagement stance with "always ask the user" patterns
- Adding scope-discipline or error-recovery rules that the harness already enforces

You will likely make some of these mistakes. That's fine. Read this document first to make fewer of them.
