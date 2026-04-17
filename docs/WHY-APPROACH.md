# The WHY Approach — intent as a first-class artifact

Agent1st's minimal `AGENTS.md` defines how agents and humans work together.
It does not define what they work on, or how intent stays aligned with code across hundreds of sessions.

For small or short-lived projects, you don't need more than that.

For real projects — ones that will be edited for months, touched by multiple agents, and have to survive compaction, refactors, and handoff — you need one more layer.

This document describes that layer.

---

## 1) The problem this layer solves

When a project grows, four things drift apart:

- what the product is supposed to do (intent)
- what the code actually does (implementation)
- why each part exists (rationale)
- which parts change together (coupling)

In agent-driven development this drift is deadly.
A strong agent reading a function can usually tell you *what it does*.
It often cannot tell you *why it exists*, *what use case it serves*, or *what else must change with it* — because that information is not in the code.

The human used to carry that context in their head.
In agent-first work, no one carries it unless something in the repo does.

> **The WHY layer exists so that intent lives in the repo, near the code, in a form that agents can read and keep aligned.**

---

## 2) What the layer actually is

Four artifacts, paired in a specific way.

| Artifact | What it holds | Answers |
|---|---|---|
| **PRD** (`docs/PRD.md`) | Product truth | What are we building? Who for? What does done look like? |
| **Why Graph** (`docs/why-graph.xml`) | Navigation truth | Where in this repo does that intent actually live? |
| **Contracts & anchors** (in code) | Local truth | What is this file/function for, and what changes with it? |
| **Validators** (scripts) | Consistency truth | Do the three above still agree? |

The pairing matters more than the format.

- PRD explains intent; Why Graph maps intent to code.
- Why Graph points to anchors; anchors label real code blocks.
- Validators catch the moment PRD, graph, and code diverge.

Take any one away and the chain breaks.
Keep them paired and agents can answer, quickly and reliably:

- what matters
- why it matters
- where it lives
- what is safe to change
- what else must change with it

---

## 3) The workflow shift

Without the WHY layer, the default agent workflow is:

> **open the file the user mentioned → edit the nearest plausible code → claim done**

This is fast and often wrong. Edits happen where the agent landed, not where the value lives.

With the WHY layer, the workflow becomes:

> **PRD → Why Graph → contracts/anchors → code → validate**

This shape applies in two intensities. Match the intensity to the work.

**For intent-changing, cross-cutting, or poorly mapped work:**
1. Identify which use case or feature is changing (PRD + graph).
2. Update the graph first, so the intended change is explicit.
3. Update or add contracts/anchors in the files that will change.
4. Only then implement.
5. Run validators.

**For local edits inside an already well-mapped feature:**
Update graph and contracts in the same change set as the code, not necessarily before the first keystroke. The invariant is that the three move together in one commit — not that the graph always moves first.

**Run validators before claiming done** when validators exist. If they don't, that's the first thing to build (see §8).

This is slower per-edit. It is dramatically faster per-project because the agent no longer wastes cycles on nearest-code edits or invisible couplings. Refactors stop breaking invisible couplings. Handoffs stop starting from zero.

---

## 4) When to adopt this layer

Adopt when any of these are true:

- the project will live longer than one feature cycle
- more than one agent will edit it
- you have ever asked "wait, why does this exist again?"
- a refactor has broken something nobody remembered was coupled
- a PRD change landed in docs but never reached code
- "done" keeps meaning "done for what I happened to look at"

Do not adopt when:

- the project is a one-shot script or prototype you will throw away
- there is exactly one agent, one session, one deliverable
- writing the graph would take longer than the whole task

The layer pays off on projects where intent has to survive time.
It is overhead on projects where intent only has to survive minutes.

---

## 5) What this layer is not

- **Not a replacement for the PRD.** Product intent still lives in the PRD.
- **Not a company knowledge graph.** The Why Graph is a project-governance graph, not a domain-knowledge graph. If the project also needs a domain graph, it is a separate artifact with a separate name. See `AGENTS.md` §5 (Semantic Hygiene).
- **Not ceremony.** Anchors that don't help an agent answer "what is this region for" are noise. Graph nodes that have no code path are orphans. See the contracts and principles documents — both say this explicitly.
- **Not a rigid specification.** The files in this repo are one proven shape. Adapt them. If the format gets in the way of the idea, the format is wrong.

---

## 6) How the pieces fit (for agents)

**First session in a project that uses this layer** — read in this order:

1. `AGENTS.md` — how we work together (minimal Agent1st).
2. `docs/PRD.md` — what we're building and what done means.
3. `docs/why-graph.xml` — where intent maps onto code (pin this during the session).
4. `docs/why-graph-principles.md` — how to read and update the graph.
5. `docs/why-contracts-v1.md` — how to read and update contracts/anchors.

Pin `AGENTS.md`, `PRD.md`, and `why-graph.xml` for the session. The other two are reference files — read them when you touch the relevant artifact, not before every move.

**Returning sessions** — start from the graph and the current task. Reach for principles and contracts only when your edit needs them.

**Delegated subagents** — they should not pay the full pinning cost unless the delegation contract needs it. Pass them the relevant graph subtree and the specific contracts their work touches. The parent agent carries the full context; subagents carry only what the delegation says they need (see `AGENTS.md` §9, Delegation Design).

For intent-changing or cross-cutting work, graph and contracts move before code. For local edits inside a well-mapped feature, they move with the code in the same commit. Validators run before "done."

This is not bureaucracy. It is how "Done Is Not a Mood" gets teeth in a project large enough that memory alone cannot carry it.

---

## 6a) When the graph goes stale

The WHY layer's most common real-world failure mode is a graph that no longer matches the code. An anchor points to a deleted marker. A feature node has no implementation edges. A module's contract is missing. This happens when:

- code is edited and the graph is not updated in the same commit
- a refactor lands and nobody updates the contracts
- validators are not run and drift accumulates silently
- a project adopts the layer and then stops maintaining it

**If you encounter a stale graph:** treat it as a drift signal, not a reason to abandon the layer.

1. Run the graph↔anchor validator. Mark every failure.
2. Pick the file you're about to touch anyway.
3. Fix its contracts and anchors as you go.
4. Update the graph in the same commit.
5. Never edit the code to match a stale graph — update the graph.

**If no validator exists yet:** that is the first thing to build, before anything else in the WHY layer can be trusted. Even a script that checks every `<ANCHOR TARGET=...>` resolves to a real `START_*` marker in a real file is enough to start. Without it, the graph will rot silently.

**Honest adoption criterion:** if your team cannot commit to running the validator regularly and updating the graph alongside code changes, the WHY layer will cost more than it saves. Re-read §4 before adopting.

A stale graph is not the end of the WHY layer. It is the moment the WHY layer proves its value — the validator catches what would otherwise silently diverge.

---

## 7) How to start (one proven shape)

The fastest path that has actually worked in production:

1. **Write a minimal PRD.** One or two pages. Use case, features, DoD. Don't try to be complete; try to be real. See `docs/PRD.md` in this repo as an example.
2. **Sketch a Why Graph.** Start with three to five `FEATURE_*` nodes for the things that matter today. Link each to an API, surface, or module. It is normal for the first version to be half wrong.
3. **Add a contract to one touched file.** Pick the next file you'd edit anyway. Add a `START_MODULE_CONTRACT:` header with PURPOSE, PRD_REF, INVARIANTS. See `docs/why-contracts-v1.md`.
4. **Add anchors where they help navigation.** Not everywhere — where an agent would otherwise have to guess.
5. **Add a validator, even a trivial one.** A script that checks every `<ANCHOR TARGET=...>` in the graph points to a real `START_*` marker in a real file is enough to start.
6. **Grow from there.** Every touched file upgrades. Do not retrofit the whole repo at once.

The shape you'll arrive at after a few iterations won't be identical to this repo's. That is the correct outcome.

---

## 8) Adopter's pattern — telling your agents what to pin

Agent1st's canonical `AGENTS.md` is drop-in and protocol-only on purpose. Do not modify the protocol body.

The question this section answers: when an adopter repo uses the WHY layer, how do its agents learn to pin the right files at session start?

**Prefer harness-native mechanisms first.** They cost no protocol drift and travel cleanly across tools:

- **Claude Code:** put a `Required Reading` list in `CLAUDE.md` (which already imports `@AGENTS.md`), or use `MEMORY.md`.
- **Codex / Cursor / OpenCode:** use the harness's project-context file for the reading list.
- **intent1st / skill-based harnesses:** pin via the skill's canon pointers.
- **Any harness:** a short `docs/session-context.md` that your harness is told to pin at session start.

**If your harness only reads `AGENTS.md`** and you cannot add a second context file, you can add a short adopter header to your project's copy of `AGENTS.md` — **above** the Core section, clearly project-specific:

```markdown
<!-- Adopter addendum — project-specific. Agent1st Core below is unmodified. -->
## Required Reading

Before substantial work, ensure these files are in context:

- `docs/PRD.md` — product truth
- `docs/why-graph.xml` — intent-to-implementation map (pin during session)
- `docs/why-graph-principles.md` — graph authoring guide (reference)
- `docs/why-contracts-v1.md` — contract and anchor rules (reference)
- `<any project-specific docs that matter>`

The Core section below is the Agent1st protocol, unmodified.
---
```

The addendum is yours. The Core is Agent1st's. Keep them visibly separate so future protocol upgrades don't collide with your additions.

**Smoke test for adoption:** after you add one module contract and your reading-list mechanism, a fresh agent should be able to answer *"what is this file for, and what else moves with it?"* from the contract and the graph alone — without reading the code. If that fails, your contract is noise.

See `docs/SPS3A-ANALYSIS.md` for one real-world variant of this pattern (Python/FastAPI); a separate TypeScript adopter uses the same pattern with a smaller node set.

---

## 9) Why this layer has its own document

Because the idea is more important than the files.

If you read only the file names (`why-graph.xml`, `why-contracts-v1.md`) you'll see a format.
If you copy the files without reading this document, you'll copy ceremony.

The format is one proven shape. The idea is:

> **Intent drifts unless the repo carries it. Make intent a first-class artifact. Keep it paired with code. Validate the pairing.**

If you keep that idea and change every file name, you have still adopted the WHY approach.
If you keep every file name and lose that idea, you have not.

---

## 10) Relationship to the rest of Agent1st

- `AGENTS.md` — behavior layer. Required. Drop-in. Does not change when you adopt the WHY layer.
- This document — the WHY layer. Recommended for real projects. Not required.
- `docs/PRD.md`, `docs/why-graph.xml`, `docs/why-graph-principles.md`, `docs/why-contracts-v1.md` — one proven shape of the WHY layer, living in this repo so you can read, copy, and adapt it.

The WHY layer is to Agent1st what the contracts of a workplace are to the culture of a workplace.
The behavior layer defines how people act.
The WHY layer defines what they are acting on, and how they know they are still aligned.

Adopt when the project will live long enough to need both.
