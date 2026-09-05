# Why1st — intent as a first-class artifact

`AGENTS.md` defines how we work together. **Why1st** keeps what we are building
connected to why it exists.

Copy the contract; build the map. The first is easy to adopt. The second must
fit your project. Small, short-lived work may need only the contract. Work that
survives sessions, agents, and refactors needs its intent to survive too.

A better agent still cannot recover a decision nobody recorded.

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
| **Validators** (scripts) | Consistency checks | Do the declared references and constraints still hold? |

The pairing matters more than the format.

- PRD explains intent; Why Graph maps intent to code.
- Why Graph points to anchors; anchors label real code blocks.
- Validators catch broken declared references and mechanically checkable constraints. Behavior tests and review establish whether the implementation satisfies intent.

**One word, four jobs — qualify "anchor" whenever the sentence is ambiguous.** A *code anchor* is a `START_*` / `:END_*` marker pair in a source file. A *PRD anchor* is a `<!-- PRD_ANCHOR: KEY -->` comment in the PRD. A *log anchor* is the `anchor` field of a semantic-log event, carrying a graph or code anchor name. An *attention anchor* is the transformer-side reason the first three work: a distinctive string a model can still find in saturated context (`why-graph-principles.md` §2a). The same string across the first three is the load-bearing trick; the fourth is why it works. (`AGENTS.md` §2 applied to this layer's own vocabulary.)

The explanatory docs in this repo (`Why1st.md`, `why-graph-principles.md`, and `why-contracts-v1.md`) exist so agents understand the pattern before they maintain it. The live project chain is simpler:

> **PRD -> Why Graph -> anchors/contracts -> validators**

Take any one away and the chain breaks.

**Before you write the graph, read `why-graph-principles.md` §2a.** The Why Graph is `.xml` for tooling reasons but is not classical XML and not a graph-DB schema — its tag shapes are engineered for transformer attention, not for parser elegance. Strong agents who skip §2a tend to silently simplify the format to `<?xml ?> + <nodes><node id="..." kind="..."> + <relations>` — which parses, validates, and quietly fails the actual job (the format becomes invisible to the model in long context). §2a explains the choice with side-by-side good/bad examples so the rationale lands before the format gets simplified away.
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

**Run validators before claiming done.** This repo ships a starter validator (`python scripts/validate-why.py`). Adopter projects should run that or their project-specific equivalent. If no validator exists yet, build the smallest graph-to-anchor check before trusting the layer.

The extra work per edit is meant to save repeated discovery across the project:
fewer nearest-code edits, visible couplings, and handoffs with a usable map.
That is the practical lesson behind the layer, not a guarantee that every
refactor will be safe or every project faster. A stale map can do the opposite.

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

The first version does not need to be grand. In real projects, the useful start is often one `docs/PRD.md`, one `docs/why-graph.xml`, one governed file with a module contract, and one validator that catches broken anchor references.

---

## 5) What this layer is not

- **Not a replacement for the PRD.** Product intent still lives in the PRD.
- **Not a demand for many docs.** Starting with one `docs/PRD.md` that also carries early design notes, roadmap, and plan is a valid choice. Split out `DESIGN.md`, `ARCHITECTURE.md`, or status files only when the split reduces drift more than it creates maintenance overhead.
- **Not a company knowledge graph.** The Why Graph is a project-governance graph, not a domain-knowledge graph. If the project also needs a domain graph, it is a separate artifact with a separate name. See `AGENTS.md` §2 (Semantic Hygiene).
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

**Delegated subagents** — they should not pay the full pinning cost unless the delegation contract needs it. Pass them the relevant graph subtree and the specific contracts their work touches. The parent agent carries the full context; subagents carry only what the delegation says they need (see `AGENTS.md` §4, Delegation Design).

For intent-changing or cross-cutting work, graph and contracts move before code. For local edits inside a well-mapped feature, they move with the code in the same commit. Validators run before "done."

This is not bureaucracy. It is how "Done Is Not a Mood" — the Agent1st lesson that strong harnesses now enforce as floor behavior — gets teeth in a project large enough that memory alone cannot carry it.

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

**If no validator exists yet:** that is the first thing to build, before anything else in the WHY layer can be trusted. Even a script that checks every `<ANCHOR ... COORD="path#ANCHOR">` resolves to a real `START_*` marker in a real file is enough to start. Without it, the graph will rot silently. In this repo, start from `python scripts/validate-why.py`.

**Honest adoption criterion:** if your team cannot commit to running the validator regularly and updating the graph alongside code changes, the WHY layer will cost more than it saves. Re-read §4 before adopting.

A stale graph is not the end of the WHY layer. It is the moment the WHY layer proves its value — the validator catches what would otherwise silently diverge.

---

## 7) How to start (one proven shape)

For a runnable first encounter, follow [one reading-list feature](examples/reading-list/README.md)
through its PRD, graph, code contracts, validator, and behavior tests. It includes
both a broken-reference exercise and a behavior bug that structural checks cannot catch.

The fastest path that has actually worked in production:

1. **Write a minimal PRD.** One or two pages. Use case, features, DoD, early roadmap, and any design constraints that would otherwise live only in your head. Don't try to be complete; try to be real. Put a `<!-- PRD_ANCHOR: KEY -->` marker under each section the graph will reference — the graph points at keys, never at section numbers or heading text, so the PRD stays refactorable from day one. See `docs/PRD.md` in this repo as an example.
2. **Sketch a Why Graph.** Start with three to five `FEATURE_*` nodes for the things that matter today. Link each to an API, surface, or module. It is normal for the first version to be half wrong.
3. **Add a contract to one touched file.** Pick the next file you'd edit anyway. Add a `START_MODULE_CONTRACT:` header with PURPOSE, PRD_REF, INVARIANTS. See `docs/why-contracts-v1.md`.
4. **Add anchors where they help navigation.** Not everywhere — where an agent would otherwise have to guess.
5. **Add a validator, even a trivial one.** A script that checks every `<ANCHOR ... COORD="path#ANCHOR">` in the graph points to a real `START_*` marker in a real file is enough to start.
6. **Grow from there.** Every touched file upgrades. Do not retrofit the whole repo at once.

The shape you'll arrive at after a few iterations won't be identical to this repo's. That is the correct outcome.

For an existing codebase, do the same thing in reverse: pick the next feature you are about to touch, add its PRD entry, map only that feature into the graph, add contracts to only the files you touch, run the validator, then repeat. Retrofitting the whole repository before useful work begins is how the graph becomes a tax.

For orchestrator/subagent work, the parent agent carries the full PRD and graph. Subagents should receive a bounded graph subtree, the files or modules they own, acceptance criteria, and the evidence format they must return.

---

## 8) Adopter's pattern — telling your agents what to pin

Agent1st's canonical `AGENTS.md` is drop-in and protocol-only on purpose. Do not modify the protocol body.

The question this section answers: when an adopter repo uses the WHY layer, how do its agents learn to pin the right files at session start?

**Prefer harness-native mechanisms first.** They cost no protocol drift and travel cleanly across tools:

- **Claude Code:** put a `Required Reading` list in `CLAUDE.md` (which already imports `@AGENTS.md`), or use `MEMORY.md`.
- **Codex / Cursor / OpenCode:** use the harness's project-context file for the reading list.
- **Skill-based harnesses:** pin via the skill's own pointers to the canonical files.
- **Any harness:** a short `docs/session-context.md` that your harness is told to pin at session start.

**If your harness only reads `AGENTS.md`** and you cannot add a second context file, you can add a short adopter header to your project's copy of `AGENTS.md` — **above** the Core section, clearly project-specific:

```markdown
<!-- Adopter addendum — project-specific. Agent1st Core below is unmodified. -->
## Required Reading

Before substantial work, ensure these files are in context.

**Pin always (during the session):**
- `docs/PRD.md` — product truth
- `docs/why-graph.xml` — intent-to-implementation map

**Reference on demand (read when you touch them):**
- `docs/Why1st.md` — the layer's idea
- `docs/why-graph-principles.md` — graph authoring guide
- `docs/why-contracts-v1.md` — contract and anchor rules
- `scripts/validate-why.py` — validator (run before claiming done)
- `<any project-specific docs that matter>`

## Harness exceptions

Anything project-specific — Hello Agent handshake tweaks, output-contract exceptions, harness-specific role names — goes here, **above** the separator. Do not edit them into the Core.

The Core section below is the Agent1st protocol, byte-identical to canonical. Editing the Core directly breaks the upgrade path and creates audit noise across versions.
---
```

The addendum is yours. The Core is Agent1st's. Keep them visibly separate.

**Pin vs reference matters.** Real cold-start adopters have pinned 8+ files and turned the graph layer into context tax. The list is not "pin everything that exists"; it is "pin what answers *what are we building and where does it live*." Everything else opens on demand.

**Don't edit the Core.** A common adoption mistake is editing the canonical protocol body "just slightly" — usually around the `Hello Agent` handshake or to add a strict-output exception. The rationale is always good. The cost is real: future Agent1st upgrades will conflict with your local edits, and a future agent reading your `AGENTS.md` cannot tell which rules are protocol and which are local. Put the local part in the addendum above the separator. If a tweak feels load-bearing enough to belong in the Core, raise it as a protocol change, not as a local edit.

**Smoke test for adoption:** after you add one module contract and your reading-list mechanism, a fresh agent should be able to answer *"what is this file for, and what else moves with it?"* from the contract and the graph alone — without reading the code. If that fails, your contract is noise.

Real adopters have shipped this in Python/FastAPI, TypeScript, and Codex-native orchestrator/subagent setups. They differ in format and strictness. They share the same invariant: PRD, graph, contracts, and validators move together.

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

---

## 11) Optional extensions for real-project surfaces

Some projects need more than the canonical chain. The patterns below are **opt-in**. They are **not** part of the canonical Why1st chain (PRD → Why Graph → contracts/anchors → validator). The chain stays small on purpose.

Adopt an extension only when your project actually has the surface it addresses. If you don't need it, ignore it — the protocol does not require it.

### 11.1 Semantic logs as future agent context

When a project has runtime workflows (jobs, integrations, scheduled tasks, agent runners), important boundaries should emit compact structured events that a future agent can read.

A useful minimum event shape: `ts`, `event`, `anchor`, `component`, plus `expected` / `actual` when the boundary has a check-able expectation, plus a correlation id when events span boundaries.

The load-bearing trick: **the `anchor` field uses the same names as your Why Graph and code anchors.** A model can grep the same string across logs ↔ graph ↔ code and orient instantly. Without that link, semantic logs are just structured logs — they help humans, but they do not pull their weight as agent context.

Keep separate from rationale memory. Semantic logs answer *what happened.* They do not answer *why we decided X.* If your project needs durable rationale beyond what PRD and graph carry, that is a separate artifact, not a fatter log.

When NOT to bother: small projects with no runtime surface; CLIs that compute and exit; throwaway scripts. Adding semantic logs to a project that does not need them is the canonical way to make Why1st feel like ceremony.

**Implementation guide:** see `docs/why-semantic-logs.md` for event shape, where logs live, the smallest useful first slice, and anti-patterns. The guide is opt-in; this paragraph is enough for projects that just need the principle.

### 11.2 Tests and UI evidence — agents own their own verification loop

Agent1st's **Done Is Not a Mood** lesson (graduated from `AGENTS.md` in v13; exact text in `docs/_archive/AGENTS-min-v12.1.md`) says completion needs "the best evidence the current harness allows." Match the evidence to the risk surface: deterministic logic → unit tests; API contracts → response-shape assertions; UI behavior → visual checks (Playwright, screenshots); runtime workflows → semantic-log assertions over fixtures (see §11.1).

**The behavior most adopters miss.** When the agent finishes UI work, the next move should be *the agent looks at the rendered page,* not *the agent asks the human to check it.* Most users do not know they can grant browser access. Agents who silently wait for permission spin instead of working. If your harness allows browser tools, install them, write the tests, capture the evidence, attach it to the completion claim. This is the **Role Contract** lesson applied to verification: the agent owns the route, including the route to its own evidence. The depth doc (cross-link below) covers the four evidence tiers, the **Playwright CLI vs MCP** trade-off (default to CLI; MCP definitions consume context whether you use them or not), and the agent-owns-it pattern.

When NOT to bother: backend-only libraries; pure-CLI projects; throwaway prototypes.

**Implementation guide:** see `docs/why-evidence.md` for the four evidence tiers, the CLI-over-MCP position with reasoning, the agent-owns-it pattern, and anti-patterns. The guide is opt-in; this paragraph is enough for projects that just need the principle.

### 11.3 Subagent orchestration — delegate by default, crystallize the pattern later

The behavior most adopters miss: strong agents are trained on agentic work but default to single-thread *do-it-all-myself* mode. Independent reads, fan-out validation, context-heavy exploration, and lower-intelligence ops are usually faster, cheaper, and better when delegated to subagents — but the lead has to pick that route. `AGENTS.md` §4 (Delegation Design) is the rule; the question this section answers is *when does an agent default to delegation in the first place*.

When delegation becomes recurring (parallel exploration, fan-out validation, large refactors split across subagents), a project-local artifact like `docs/agent-orchestration.md` crystallizes the pattern: role matrix, prompt shapes, evaluation rubric, durable lessons. The artifact is the second move, not the first.

This is **not** Agent1st core and **not** part of the canonical Why1st chain. The same applies to Codex-style `.codex/agents/*.toml` profiles, harness-specific subagent routers, and decision-context maps — they are project-local extensions above Why1st, not parts of it.

**Implementation guide:** see `docs/why-subagents.md` for when to default to delegation, the four common delegation shapes, what to delegate vs do yourself, anti-patterns, and the artifact shape that emerges. The guide is opt-in; this paragraph is enough for projects that just need the principle.

---

### Hard partition — please do not blur

Every extension above is opt-in. If you adopt all three you have not adopted "more Why1st" — you have built a project-local extension stack on top of Why1st. Mark them as such in your repo so the next agent can tell what is canonical (the chain) from what is yours (the extensions).

A project that has only the canonical chain is using Why1st correctly. A project that has the extensions and skips the chain is not using Why1st at all.
