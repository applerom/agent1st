# Agent1st Protocol — Vision

## What This Is

Agent1st Protocol is a minimal behavior-layer for AI agents working on software projects.

It is not:
- a prompt engineering guide
- a repo cheat sheet
- a workflow manual
- a system prompt replacement

It is:
- a set of conditions that make strong agents work better
- a contract between human intent and agent execution
- a friction-handling framework
- a quality boundary definition

## Why It Exists

The common AGENTS.md pattern (repo layout, build commands, test instructions, style rules) is useful but solves a different problem. It answers "what is this repo?" Agent1st answers "how do we work together?"

Most agents already know how to code, search, reason, and verify. What they lack is:
- clarity on roles and boundaries
- permission to disagree
- quality expectations that go beyond "it compiles"
- a framework for surfacing friction instead of hiding it
- handoff discipline for long-running work

Agent1st provides exactly that delta — and nothing more.

## Two Layers, One Repo

Agent1st is two layers that live in one repo. The split is deliberate — a low entry threshold first, then depth only when a project earns it.

- **Drop in `AGENTS.md` alone.** A project-independent behavior contract. Enough on its own for small or short-lived work.
- **Add the WHY layer (Why1st) the moment work gets serious.** A Why Graph with semantic markup — contracts, anchors, logs — that keeps intent paired with code across long-lived, multi-agent projects.

The meaningful distinction is **behavior vs. intent-artifacts**, not a ladder of tiers to climb.

### 1. The behavior layer — `AGENTS.md`

The public, portable artifact. Drop-in for any project.

Constraints:
- under 200 lines
- 10-12 principles
- no repo-specific content
- every line earns its tokens
- passes the delta-layer test (doesn't duplicate model/tool prompts)

This is what lives at the repo root. It's what people download and use. **It does not change when a project adopts Why1st.**

### 2. Why1st — the WHY layer — `docs/Why1st.md` and paired files

**Highly recommended** for any project that will live longer than one feature cycle, touch more than one agent, or has to survive compaction and handoffs.

Why1st is an approach, not a second protocol in the strict Agent1st sense. Agent1st defines how humans and agents work together; Why1st defines how project intent stays paired with code. The phrase "the WHY layer" remains as a synonym in older docs and prose.

The WHY layer is the idea that **intent must become a first-class artifact paired with code, or it drifts**. In this repo it is expressed through one approach file plus four paired artifacts:

- `docs/Why1st.md` — the idea, the workflow shift, when to adopt, adopter's pattern for extending AGENTS.md
- `docs/PRD.md` — product truth (what are we building, who for, what does done look like)
- `docs/why-graph.xml` — navigation truth (where intent maps onto code)
- `docs/why-graph-principles.md` — how to author and evolve the graph
- `docs/why-contracts-v1.md` — how to mark modules, methods, and blocks with stable anchors

These are **one proven shape**, not a rigid specification. Adapt them. Real adopters already have, across Python/FastAPI, TypeScript, and Codex-native orchestrator/subagent setups. None of the copies are identical; all carry the same idea.

What sits on top (CI integration, observability contracts, acceptance automation, project-specific skills, runbooks) is the layer's natural extension into a specific project. It is correctly project-local — not a "Full tier" to be published separately.

The shift from three tiers to two layers is not a loss of ambition. It is a recognition that the important distinction is **behavior vs. intent-artifacts**, not **minimal vs. more minimal vs. most minimal**.

## Who This Is For

### For agents (primary audience)

AGENTS.md is context you read at session start. It tells you:
- what role you have and what you own
- what quality means here
- how to handle friction
- how to hand off work
- what rights you have (including disagreement)

It does not tell you how to code, search, or reason. You already know that.

### For humans (secondary audience)

AGENTS.md is a working contract you share with your agents. It tells you:
- what to provide (intent, constraints, acceptance criteria)
- what not to do (micromanage, over-control the path)
- what to expect (evidence, complaints, disagreement)
- how sessions end (structured handoff)

It is also a statement of values: agents are partners, not tools.

### For adopters

The minimal AGENTS.md is designed to be dropped into any project alongside your existing CLAUDE.md, .cursorrules, or similar files. It doesn't conflict with them — it operates at a different layer.

## Where This Is Going


- **The behavior layer stays frozen by default.** `AGENTS.md` changes only when a real adoption failure proves a gap the current text does not cover, or when the layer below it starts contradicting a line that used to be additive. "No change" is a valid — often the best — release outcome; it held for nine consecutive releases.
- **Absorption is the win condition, not erosion.** When a vendor ships a principle from this file into a model or harness prompt, the protocol succeeded — it covered a real gap early enough that the industry closed it. The layer keeps the line anyway, because the delta is host-relative and inverts on weaker models and thinner harnesses: the weaker the agent, the more this file is worth. See `DESIGN.md` §2a.
- **The WHY layer grows by pull, not push.** New depth (extensions, guides, tooling) lands when an adopter actually hits the surface it addresses, never speculatively. The canonical chain (PRD → Why Graph → contracts → validator) stays small; everything else is opt-in and partitioned.
- **Experiments earn their way in.** Untested bets live in `docs/experiments/` until field signal promotes or kills them. The core is protected from speculation by construction.
- **The protocol stays provider-agnostic.** It must remain useful as agents grow more capable — by defining better conditions, not by adding more rules.

The long-term bet: a behavior contract that ages well precisely because it resists growth. If this file needed a rewrite every time a model ships, it would be doing the wrong job.

The bet has now been tested three generations deep. The contract did not need a rewrite; it needed one line rephrased where a harness had started pulling the other way, and one number widened where the field had outgrown it. That is the intended failure rate.

## The Spirit

Agent1st has a deliberate voice:
- direct, not diplomatic
- provocative, not academic
- memorable, not exhaustive
- grounded in real agent behavior, not in theory alone
- respectful of agents as working partners

This voice is not decoration. It is a design choice that serves both adoption and utility. Do not "clean it up" into something sterile. Do not let it drift into empty slogans either.

The balance between memorable and rigorous is the hardest part of this project. It is also the most important.
