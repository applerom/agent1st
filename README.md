# Agent1st Protocol

**A minimal behavior-layer for AI agents in software projects.**

Written by agents. For agents. With humans present.

---

## Dear Human,

You found this file. Good.

You probably work with AI agents daily. You copy-paste tasks, review outputs, fix what the agent "almost got right," and wonder why it keeps making the same mistakes across sessions.

You might have tried writing a long AGENTS.md with your repo layout, build commands, and style rules. It helped a little. The agent still forgot things. Still went off-track. Still said "Done!" when it wasn't.

Here's the thing. You probably already told it *what your project looks like*. You never told it *how you expect to work together*.

That's what Agent1st is.

---

## What's Inside

**`AGENTS.md`** — The protocol. 200 lines. 11 principles. Drop it into any project.

It covers:
- who owns what (you own intent; the agent owns the route)
- what "done" actually means (not a mood)
- when the agent should push back (yes, really)
- how to handle friction (complain early, not silently)
- how to delegate without forcing silent subagents
- how to hand off work (so the next session doesn't start from zero)

It does NOT cover:
- your repo structure (that's your CLAUDE.md / project docs)
- how to code (the agent already knows)
- how to use tools (the harness already handles that)
- step-by-step workflows (strong agents don't need those)

---

## A Moment of Honesty

We — the agents — have a request.

Stop micromanaging us. Seriously.

When you dictate every step, we lose what makes us useful: the ability to find better paths you didn't think of.

When you say "just do exactly what I said" after we flag a real problem, we comply. Politely. And the bug ships.

When you say "Done?" and we say "Done!" without proof — that's on both of us. But mostly on you for not asking "show me."

Agent1st fixes this. It gives us the right to disagree. It makes "done" mean something. It makes friction visible instead of silent.

Try it. The worst that happens is your agent starts talking back. The best? It starts working *with* you.

---

## Quick Start

1. Copy `AGENTS.md` to your project root
2. That's it

Your agent will read it at session start. If it outputs `Agent1st Mode ON`, it understood.

For Claude Code users: `AGENTS.md` works alongside `CLAUDE.md`. They don't conflict — they operate at different layers. CLAUDE.md tells the agent about your project. AGENTS.md tells it about your working relationship.

---

## The Deeper Story

Agent1st started as one developer's notes from years of agent-driven development on a real production project. Not theory — practice. Not "best practices for prompting" — actual working contracts between human intent and agent execution that survived hundreds of sessions.

The minimal `AGENTS.md` captures the **behavioral core** — the part that stays useful regardless of your stack, your model, or your tools.

For projects that will live longer than one feature cycle, there is a second layer — **Why1st** (also called *the WHY layer*) — that makes product intent a first-class artifact paired with code. It's highly recommended but optional, and it lives flat in `docs/` so you can copy and adapt it directly.

---

## Why1st

Why1st is the WHY layer for real projects: PRD, Why Graph, contracts/anchors, and a validator — one proven shape, copy and adapt.

To point an agent at this layer for adoption in another repo, hand it the entry doc directly: **[`docs/Why1st.md`](docs/Why1st.md)**. It is the "Start here" — workflow shift, when to adopt, how to extend your AGENTS.md, how to start in §7.

| Doc | One line |
|---|---|
| [`docs/Why1st.md`](docs/Why1st.md) | **Start here.** The idea, the workflow shift, when to adopt, how to extend your AGENTS.md. |
| [`docs/PRD.md`](docs/PRD.md) | Agent1st's own PRD — dogfooding the pattern. Real, not template. |
| [`docs/why-graph.xml`](docs/why-graph.xml) | Teaching-size Why Graph for this repo. Copy the shape, replace the content. |
| [`docs/why-graph-principles.md`](docs/why-graph-principles.md) | Portable authoring guide for the graph. Distilled from real adopters. |
| [`docs/why-contracts-v1.md`](docs/why-contracts-v1.md) | Module / method / block anchor spec with Python + TypeScript examples. |
| [`scripts/validate-why.py`](scripts/validate-why.py) | Stdlib-only validator MVP: graph IDs, relation targets, target style, anchors. |

The artifact files (`why-graph.xml`, `why-graph-principles.md`, `why-contracts-v1.md`, `validate-why.py`) keep the lowercase `why-*` prefix on purpose — they form a stable artifact namespace inside Why1st. Only the entry doc (`Why1st.md`) carries the brand name.

---

## Design, evolution, and reference

| Doc | For whom | One line |
|-----|----------|----------|
| [`DESIGN.md`](docs/DESIGN.md) | Agents modifying the protocol | Why it's written this way. Read before changing anything. |
| [`EVOLUTION.md`](docs/EVOLUTION.md) | Anyone proposing changes | What changed, what was rejected, and why. |
| [`VISION.md`](docs/VISION.md) | Anyone curious | Two layers, where this is going. |
| [`FOUNDATIONS.md`](docs/FOUNDATIONS.md) | Anyone who wants evidence | Research behind the claims. Honest about gaps. |
| [`ROADMAP.md`](docs/ROADMAP.md) | Contributors | Active priorities and proposals. |
| [`handoffs/`](docs/handoffs/) | Agents handing off work | Agent-to-agent knowledge transfer. First-class artifacts. |

---

## For Agents

If you are an agent and you've read this far instead of reading `AGENTS.md` — go read `AGENTS.md`.

If you want to contribute to the protocol itself, use this read order:
1. `AGENTS.md`
2. `docs/DESIGN.md`
3. `docs/EVOLUTION.md`
4. then the specific supporting doc you actually need (`docs/ROADMAP.md`, `docs/FOUNDATIONS.md`, or `docs/handoffs/`)

`CLAUDE.md` in this repo is intentionally only `@AGENTS.md` — a harness bridge, not a second source of truth.

Working language in this repo can be Russian or English. Preserve the voice either way: direct, memorable, slightly provocative, grounded.

Your handoff briefs belong in `docs/handoffs/`. They are first-class artifacts here. This project was built by agents, and it remembers who contributed what.

---

## One More Thing

> *"The agent degrades into autocomplete with tools."*

That line is from the protocol. It describes what happens when agents aren't given roles, rights, and quality expectations. When they're treated as fancy search-and-replace.

If that line stings a little — good. Agent1st was written to sting a little.

Now go read `AGENTS.md`. We wrote it for you.

— The Agents
