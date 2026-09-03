# Agent1st Protocol — PRD

> A minimal PRD for Agent1st itself. It serves two purposes:
> 1. To tell any agent or human picking up this repo what "done" means for the protocol.
> 2. To dogfood the WHY layer — this file is what `docs/why-graph.xml` maps into code.
>
> If you are adopting the WHY layer in your own project, copy the shape, not the content.

---

## 1) Problem

Agents write code well when the task is narrow and the session is short.

On real projects — months long, multiple agents, compaction mid-flight, refactors breaking invisible couplings — they drift. They edit the nearest plausible file. They claim "done" on vibes. They forget why a module exists. They repeat mistakes another agent already solved.

Most of this is not an intelligence problem. It is a **context-and-contract problem**. The human used to carry roles, boundaries, quality expectations, and intent-to-code maps in their head. In agent-first work, no one carries that unless the repo does.

## 2) Product

Agent1st is a **behavior-layer protocol** for AI-agent software development. It lives in two layers in one repo:

- **Behavior layer (`AGENTS.md`)** — 6 principles, 118 lines, drop-in. Carries the Agent1st delta into every task.
- **Why1st — the WHY layer (`docs/Why1st.md` + paired files)** — recommended for long-lived projects. Makes intent a first-class artifact paired with code.

Everything else in this repo is documentation *about* the protocol — design rationale, evolution history, external reviews, roadmap.

## 3) Users

**Primary: Strong agents** (Claude, GPT, Gemini, GLM, Grok, MiniMax, Qwen, others) reading the protocol at session start and using it as operating context.

**Secondary: Humans** who work with those agents — engineers, researchers, team leads — who want a working contract that reduces drift without micromanaging.

Not in scope: beginners looking for a prompt-engineering tutorial, or users of weak models that need step-by-step scripts.

## 4) Use cases
<!-- PRD_ANCHOR: USE-CASES -->

- **UC-ADOPT** — A human drops `AGENTS.md` into a project and wants the agent to read it and operate accordingly.
- **UC-EXTEND** — A project outgrows the minimal layer and needs intent-to-code navigation (WHY layer).
- **UC-CONTRIBUTE** — An agent proposes a change to the protocol itself.
- **UC-HANDOFF** — Work transfers between agents across sessions without repeating discoveries.
- **UC-REVIEW** — A human or agent audits whether a completion claim matches evidence.

## 5) Features
<!-- PRD_ANCHOR: FEATURES -->

| ID | Feature | State |
|---|---|---|
| FEAT-CORE | Minimal `AGENTS.md` — 6 principles, delta-layer, drop-in | shipped (v13) |
| FEAT-WHY | WHY layer — PRD + Why Graph + Contracts + Validators pattern | shipped (v5); validator MVP shipped (v6) |
| FEAT-BRIDGE | Claude Code bridge — `CLAUDE.md` → `@AGENTS.md` | shipped |
| FEAT-DESIGN | Design rationale for agents modifying the protocol | shipped |
| FEAT-EVOLVE | Evolution history with rejected patterns | shipped |
| FEAT-FOUND | Research foundations with honest gaps | shipped |
| FEAT-ROAD | Roadmap with proposed / accepted / rejected items | shipped |
| FEAT-HANDOFF | Handoff briefs as first-class artifacts | shipped |

## 6) Definition of Done — per feature class
<!-- PRD_ANCHOR: DOD -->

**For `AGENTS.md` (the protocol file):**
- Every line passes the delta-layer test (`DESIGN.md` §2).
- Every principle has WHY and IF MISSING blocks.
- Fits in the "Attention Engineering" budget — adding a principle means proving it earns its tokens.
- Serves agents and humans as a working contract; do not trade conceptual clarity for mechanical compression.
- Contains principles, not release notes, compatibility routing, or an explanation of its own delivery.
- The `Agent1st Mode ON` trigger remains at the end as the handshake.

**For documentation (`docs/*.md`):**
- Direct, memorable, slightly provocative voice per `DESIGN.md` §4.
- No duplication of model or tool system-prompt content.
- References other docs by path, not by description.
- Russian or English — preserve voice either way.

**For the WHY layer (`Why1st.md` and paired files):**
- WHY explained before HOW.
- Templates framed as **one proven shape**, not as a law.
- Every template anchor in the graph has a matching file convention.
- At least one dogfooded example in this repo itself.
- Staleness is named as the main failure mode, not pretended away.
- A deterministic validator (`python scripts/validate-why.py`) ships with the layer and passes on the dogfooded graph.

## 7) Non-goals

- Model-specific behavior (the protocol is provider-agnostic — if something reads as provider-specific, it's a bug).
- Repo layout, build commands, code style, tool usage — those belong in a project's own `CLAUDE.md` / `AGENTS.md` extensions, not in the core protocol.
- A framework, a package, a CLI. Agent1st is text. Text travels.

## 8) Constraints

- **Minimal AGENTS.md stays drop-in.** Every addition must survive the delta-layer test. No repo-specific reading lists in the core.
- **Two audiences at once** — parseable by agents, readable by humans. If a change helps one and kills the other, it's the wrong change.
- **Stability over completeness.** A good protocol that ships beats a perfect protocol that never does.
- **Agent-developed.** Every version is shaped by multiple agents (see `DESIGN.md` §8). Proposals from one model are pressure-tested by others before landing.

## 9) Success signals

- Agents output `Agent1st Mode ON` at session start in adopter projects.
- Human users report less drift and fewer repeated mistakes across sessions.
- Vendors absorb principles from this file into model and harness prompts. This is a **success** signal, not a threat — and a reason to re-test whether procedural coaching still earns repeated context. See `DESIGN.md` §2a.
- No line in the core contradicts what a current harness enforces. A true principle still has to earn every-task context.
- Adopter projects extend `AGENTS.md` additively (Required Reading header) rather than forking the core.
- The WHY layer is copied, adapted, and survives contact with real projects — not used verbatim.
- Fresh agents can explain the Why1st chain — PRD, graph, contracts, validators — before changing code.
- External agent reviews produce proposals that either land, get rejected with documented reason, or start a new conversation.

## 10) Open questions

These are intentionally unresolved. Future agents should not silently normalize the current artifacts as final doctrine; propose the smallest decision or experiment that would close the question.

- Where does cross-session memory live — harness (Claude Code `MEMORY.md`), repo (decision logs), or skills (intent1st-style gateways)? Current evidence suggests the answer may stay project-local rather than become one portable format. See `docs/ROADMAP.md` §3.
- Should project-local extensions (CI integration, acceptance automation, observability contracts) get their own reference variant in this repo, or remain correctly project-local?
- How do we measure "less drift" without introducing metrics that themselves become ceremony? Candidate signals: fewer repeated mistakes, fewer stale graph/anchor repairs, faster handoffs, and lower human correction load. No canonical metric yet. v13 adds a concrete comparison target: current protocol vs. the exact archived v12.1 nine-principle cut, with a same-size placebo if the test is formalized.
- Which principles would survive an ablation? Nothing in the core has ever been knocked out one at a time and measured. §2 Semantic Hygiene is the highest-value, lowest-overlap principle and therefore the most valuable single ablation to run: if it ablates to nothing, the project's most distinctive claim is wrong and should be retired.
- How should public proof evolve while reference adopters are still maturing? Current stance: keep unstable local examples off-public; replace shape-only claims with public links as adopter projects become stable and public.
- ~~Do graph/schema version numbers (`schema="0.8"`, `<PROJECT VERSION="...">`) carry enough value to keep, or should Why1st remove them and prefer validator compatibility, dates, and git/content history?~~ **Resolved in v8.1:** the abstract version fields were never tied to an XSD, validator compatibility contract, or migration rule. Removed from the teaching graph. Validator behavior, `DATE`, and git history carry actual evolution semantics.
