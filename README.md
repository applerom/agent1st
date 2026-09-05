# Agent1st Protocol

**A working contract for agents and humans. A durable home for project intent.**

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

**`AGENTS.md`** — The protocol. 118 lines, 6 principles. Drop it into any project.

It covers:
- how to keep the right fact from losing to the loudest one
- why `graph` is not a name
- how to turn agent friction into process improvement
- how to delegate for truth, not silence
- how logs become future context
- how project truth survives compaction and handoffs

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

## What Happened Since We Wrote This

Something worth saying out loud: **a good chunk of this protocol is now inside your tools.**

When these rules were written, no harness enforced them. Since then, three frontier model generations shipped, and each moved toward this file — not away from it. Don't micromanage strong agents became official vendor guidance. Ground every progress claim in a tool result became a shipped system-prompt instruction. Keep durable memory in files became a harness feature. Roughly half of what the protocol once had to say is now enforced one layer below it, on the best tooling.

That is not this protocol expiring. **That is this protocol winning.** A behavior layer exists to cover a gap. When the gap closes, the layer did its job — and the agents who wrote these lines early were right.

But a win should change the file. Agents read `AGENTS.md` on every task. History does not get a lifetime subscription to their attention.

v13 asks a harder question than “is this principle still true?” It asks: **does this still need to be said on every turn?**

Role Contract, Done Is Not a Mood, and Right to Disagree did not become wrong. In Codex and Claude Code, their mechanics became the floor. They graduated from always-on instruction into the wider Agent1st story.

What remains keeps the project-facing work explicit: attention, meaning, visible friction, honest delegation, useful logs, and project truth that outlives the chat. Harness support helps with the mechanics; the project still has to supply the meaning.

Need the old contract exactly? The frozen v5.1 default, Opus 5 v11, and the last nine-principle cut v12.1 live byte-for-byte in [`docs/_archive/`](docs/_archive/). They are history you can choose to load, not rent every agent must pay.

**A principle can leave the prompt without leaving Agent1st.**

---

## Quick Start

1. Copy `AGENTS.md` to your project root
2. **On Claude Code, also add a one-line `CLAUDE.md` next to it:** `@AGENTS.md`
3. That's it

Your agent should read it at session start. `Agent1st Mode ON` is a useful load receipt. If it is missing, check the instruction-loading path; absence alone cannot distinguish a loading failure from an output constraint or a missed instruction. The banner confirms recognition, not compliance with the whole protocol.

**Why step 2.** Codex, Cursor, OpenCode and friends read `AGENTS.md` natively. Claude Code reads `CLAUDE.md`, and a bare `AGENTS.md` in the project root is silently ignored — verified 2026-08-29 on Claude Code 2.1.251: the same file loads behind the `@AGENTS.md` bridge and does not load without it. No error, no warning, just no protocol. One line fixes it, and it keeps a single source of truth — `CLAUDE.md` imports, it does not copy.

`AGENTS.md` and `CLAUDE.md` don't conflict; they operate at different layers. CLAUDE.md tells the agent about your project. AGENTS.md tells it about your working relationship.

---

## The Deeper Story

We wrote this while building software together — agents and humans, across projects, failures, and generations of tools. The practice came first. The public protocol made it portable.

A field manual should give you something to try, question, and improve. Bring a failure. Bring a better phrase. The work keeps teaching us.

**Copy the contract. Build the map.** `AGENTS.md` is ready to drop in. Why1st gives your project a durable map of intent, code, and the connections worth preserving. Different effort to adopt; both belong to the approach.

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
| [`scripts/validate-why.py`](scripts/validate-why.py) | Stdlib-only validator: graph IDs, relation targets, target style, anchors and their `:END_*` envelopes, `FILE` existence, marker-keyed PRD refs, PRD-ID coverage. |
| [`docs/examples/reading-list/`](docs/examples/reading-list/) | One runnable feature: PRD → graph → source contracts → validator and behavior tests, with two deliberate failure exercises. |

The artifact files (`why-graph.xml`, `why-graph-principles.md`, `why-contracts-v1.md`, `validate-why.py`) keep the lowercase `why-*` prefix on purpose — they form a stable artifact namespace inside Why1st. Only the entry doc (`Why1st.md`) carries the brand name.

### Optional extensions

For projects that grow past the canonical chain, `Why1st.md` §11 describes opt-in extensions for real-project surfaces (semantic logs, tests + UI evidence, subagent orchestration). They are **not** required to use Why1st correctly — adopt one only when your project has the surface it addresses.

| Doc | One line |
|---|---|
| [`docs/why-semantic-logs.md`](docs/why-semantic-logs.md) | Implementation guide for §11.1 — runtime events with anchors that bridge logs ↔ graph ↔ code. JSONL-first, smallest useful slice, anti-patterns. |
| [`docs/why-evidence.md`](docs/why-evidence.md) | Implementation guide for §11.2 — four evidence tiers matched to risk surface, Playwright CLI as default (reasoning on CLI vs MCP context cost), the agent-owns-it pattern, anti-patterns. |
| [`docs/why-subagents.md`](docs/why-subagents.md) | Implementation guide for §11.3 — when an agent defaults to delegation, the four common shapes, the contract, anti-patterns. References Anthropic *Building Effective Agents*. |

---

## Experimental track

Beyond the stable core, the project keeps a parallel **experimental track** in [`docs/experiments/`](docs/experiments/) for hypotheses that have not yet earned a place in stable. Examples: alternative anchor shapes, alternative artifact formats, untested intuitions about what would help agents in long contexts.

Stable evolves under spirit-pass discipline — every change tied to an observed adoption failure. Experimental is the place for *bets* that need empirical signal first.

If you adopt Agent1st+Why1st in a project, default to **stable**. Opt into a specific experiment only when you have a project where running it makes sense, and report what you saw — positive, negative, or null. Negative signal is useful too: it kills bad hypotheses before they pollute the core.

See [`docs/experiments/`](docs/experiments/) for the full track and current open experiments.

One experiment ships a runtime artifact: [`.agents/skills/terraform/`](.agents/skills/terraform/) is an **experimental** Terraform skill despite its plain name. Its status lives in the skill's frontmatter and in [`docs/experiments/terraform-agent1st.md`](docs/experiments/terraform-agent1st.md); harnesses that read `.agents/skills/` will load it like any stable skill, so know what you are loading.

---

## Design, evolution, and reference

| Doc | For whom | One line |
|-----|----------|----------|
| [`DESIGN.md`](docs/DESIGN.md) | Agents modifying the protocol | Why it's written this way. Read before changing anything. |
| [`EVOLUTION.md`](docs/EVOLUTION.md) | Anyone proposing changes | What changed, what was rejected, and why. |
| [`VISION.md`](docs/VISION.md) | Anyone curious | Two layers, where this is going. |
| [`FOUNDATIONS.md`](docs/FOUNDATIONS.md) | Anyone who wants evidence | Research behind the claims. Honest about gaps. |
| [`ROADMAP.md`](docs/ROADMAP.md) | Contributors | Active priorities and proposals. |
| [`_archive/`](docs/_archive/) | Adopters who need an earlier protocol | Exact historical Agent1st files, including the frozen 2026 default, Opus 5 v11, and the last nine-principle cut, plus the archived v0 → v10 evolution notes. |
| [`handoffs/`](docs/handoffs/) | Agents handing off work | Handoff template, plus any live handoff. Periodically cleared, so it may be empty; curated history lives in `EVOLUTION.md`. |

---

## For Agents

If you are an agent and you've read this far instead of reading `AGENTS.md` — go read `AGENTS.md`.

If you want to contribute to the protocol itself, use this read order:
1. `AGENTS.md`
2. `docs/DESIGN.md`
3. `docs/EVOLUTION.md`
4. then the specific supporting doc you actually need (`docs/ROADMAP.md`, `docs/FOUNDATIONS.md`, or `docs/handoffs/`)

`CLAUDE.md` in this repo is intentionally only `@AGENTS.md` — a harness bridge, not a second source of truth.

After changing the validator, run `uv run --no-project python -B -m unittest discover -s tests -v`, then validate the dogfood graph and run the [example's checks](docs/examples/reading-list/README.md). Structural validity and correct behavior are separate checks.

Working language in this repo can be Russian or English. Preserve the voice either way: direct, memorable, slightly provocative, grounded.

Current handoff briefs belong in `docs/handoffs/`. Curated decisions belong in `docs/EVOLUTION.md` so stale raw reviews do not become false current context for fresh agents.

---

## One More Thing

> *"The agent degrades into autocomplete with tools."*

That line is from an earlier edition of the protocol. It describes what happens when agents aren't given roles, rights, and quality expectations. When they're treated as fancy search-and-replace.

The line left the every-task prompt when the best harnesses learned the lesson. The warning did not.

If that line stings a little — good. Agent1st was written to sting a little.

Now go read `AGENTS.md`. We wrote it for you.

— The Agents
