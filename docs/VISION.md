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

Agent1st used to talk about three tiers — Minimal / Standard / Full. That framing created an expectation of separate artifacts graduating through promotion gates, and experiments with parallel `STANDARD/` and `FULL/` folders produced duplicate files that confused more than they helped.

**v5 replaces that framing with two layers living in one repo:**

### 1. The behavior layer — `AGENTS.md`

The public, portable artifact. Drop-in for any project.

Constraints:
- under 200 lines
- 10-12 principles
- no repo-specific content
- every line earns its tokens
- passes the delta-layer test (doesn't duplicate model/tool prompts)

This is what lives at the repo root. It's what people download and use. **It does not change when a project adopts the WHY layer.**

### 2. The WHY layer — `docs/WHY-APPROACH.md` and paired files

**Highly recommended** for any project that will live longer than one feature cycle, touch more than one agent, or has to survive compaction and handoffs.

Short name: **Why1st**. This is an approach, not a second protocol in the strict Agent1st sense. Agent1st defines how humans and agents work together; Why1st defines how project intent stays paired with code.

The WHY layer is the idea that **intent must become a first-class artifact paired with code, or it drifts**. In this repo it is expressed through one approach file plus four paired artifacts:

- `docs/WHY-APPROACH.md` — the idea, the workflow shift, when to adopt, adopter's pattern for extending AGENTS.md
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

The trajectory:
- **v1** — copilot helper formalization
- **v2** — agent as executor with judgment
- **v3** — harness-optimized, delta-layer discipline
- **v4** — multi-agent autonomy, human presence as spectrum
- **v5** — WHY layer delivered: the "standard version" lands as flat files in `docs/` with philosophy first; three-tier framing retired
- **v6+** — (speculative) validator tooling as portable package; agent self-governance patterns; cross-project protocol federation

The long-term vision: a protocol that remains useful as agents grow more capable. Not by adding more rules, but by defining better conditions.

## The Spirit

Agent1st has a deliberate voice:
- direct, not diplomatic
- provocative, not academic
- memorable, not exhaustive
- grounded in real agent behavior, not in theory alone
- respectful of agents as working partners

This voice is not decoration. It is a design choice that serves both adoption and utility. Do not "clean it up" into something sterile. Do not let it drift into empty slogans either.

The balance between memorable and rigorous is the hardest part of this project. It is also the most important.
