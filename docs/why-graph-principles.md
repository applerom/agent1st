# Why Graph — principles & authoring guide

File: `docs/why-graph.xml`
Companion docs: `Why1st.md` (the idea), `why-contracts-v1.md` (anchors and contracts).

This is a **reference, not a law.** It describes one proven shape of the Why Graph. Adapt it. If your project needs fewer node types, drop them. If it needs more, add them carefully — see §11.

---

## 0) TL;DR for agents

1. Ensure `docs/PRD.md`, `docs/why-graph.xml`, this file, and `docs/why-contracts-v1.md` are in context before substantial work (use your harness's pinning mechanism — e.g. `@path` in Claude Code — or include them in the initial prompt).
2. For intent-changing or cross-cutting work: update the graph **first**, then contracts/anchors, then code. For local edits inside an already well-mapped feature: update graph and contracts in the same change set, not necessarily before the first keystroke.
3. Every feature node should reach code through a surface, module, or artifact — no orphans.
4. Use anchors (`path#ANCHOR_NAME`), never line numbers.
5. Run your validators. If they don't exist yet, that's the next thing to build.

---

## 1) What the Why Graph is

A single XML file that maps product intent onto the repo.

It answers, for any change an agent is about to make:

- **What** use case is this for?
- **Which** feature carries that value?
- **Where** in the code does the feature live?
- **What else** touches the same value?

It is navigation truth. It is not:

- a domain knowledge graph
- an ontology of the business
- a replacement for the PRD
- a substitute for the repo README or build scripts

If your project also needs a domain graph, give it a different name and a different file. See `AGENTS.md` §5 (Semantic Hygiene).

---

## 2) Root and schema

```xml
<Why_Graph schema="0.8" project="YourProject">
  ...
</Why_Graph>
```

Keep one file per repo. Do not shard until the file visibly outgrows one canonical location — that almost never happens in practice.

`schema="0.8"` is the current stable shape. Bump only when structure changes, not when content changes.

---

## 3) Node families (common set)

These are XML element names. Use the ones your project actually has. Do not invent node families for concepts that don't exist yet.

| Family | Purpose | Typical ID prefix |
|---|---|---|
| `USECASE_*` | User or operator use cases | `UC-*` |
| `FEATURE_*` | Implementable, testable requirements | `FEAT-*` |
| `API_*` | Backend endpoints | `API-*` |
| `SURFACE_*` or `UI_*` | Operator-visible surfaces (tabs, routes, CLIs) | `SURFACE-*`, `UI-*` |
| `SCRIPT_*` | Runnable command entrypoints | `SCRIPT-*` |
| `MODULE_*` | Code modules, orchestrators, helpers | `MOD-*` |
| `DB_*` / `EMB_*` | Data stores, indices, embeddings | `DB:*`, `EMB:*` |
| `ARTIFACT_*` | Durable files consumed or produced by workflows | `ART-*` |
| `DOC_*` | Canonical governance docs | `DOC-*` |
| `MILESTONE` / `EPIC` | Planning scope (optional) | — |

Common optional attributes: `state`, `status`, `priority`, `freshness`, `tags`, `owner`.

**Naming:** UPPER_SNAKE_CASE, short, descriptive. For modules, prefix with path flavor when it helps (`BACKEND_APP_*`, `FRONTEND_WEB_*`).

---

## 4) Relations — a small, stable vocabulary

Relation `TYPE` values are UPPERCASE. Keep the list small. Add new types only when they add real clarity.

Common:

- `COVERS` — usecase covers a feature; epic covers a milestone. **Direction is parent→child:** place the `REL` on the `USECASE_*` (or `EPIC`) node, targeting the feature (or milestone). Do not reverse it.
- `EXPOSED_AS` — feature is exposed through an API
- `IMPLEMENTED_BY` — feature/requirement is implemented by a module or anchor
- `SURFACED_BY` — feature is visible through a UI surface
- `HOSTED_BY` — API is hosted by a specific route handler
- `DELEGATES_TO` — API delegates work to a service module
- `CALLED_BY` — API is called by a UI module
- `READS` / `WRITES` / `QUERIES` — module interacts with storage
- `BACKED_BY` — API or feature is backed by a DB/config/artifact
- `DEPENDS_ON` — explicit co-change coupling that is not implementation or ownership. Use when two features or modules must move together but neither implements the other. The graph's answer to "what else must change with this?"
- `IMPACTS` — feature changes the behavior of another node (API, surface, feature) without implementing it. Weaker than `IMPLEMENTED_BY`, distinct from `DEPENDS_ON` (the latter is about co-change; `IMPACTS` is about runtime effect).
- `WILL_TOUCH` / `WILL_CREATE` — planned-but-not-yet work during scoping. Use only for a bounded planning window (one milestone, one release) — if the edge is still `WILL_*` after that window, delete it or promote it. Distinct from `IMPACTS`: `WILL_*` is a promise, `IMPACTS` is a fact.

**TARGET syntax:** pick one convention per repo and keep it. Either bare IDs everywhere (`TARGET="FEAT-ASK"`) or family-qualified targets everywhere (`TARGET="FEATURE:FEAT-ASK"`). Do not mix styles in the same graph. This repo's dogfood uses the family-qualified form; small projects often use bare IDs. Either works — mixed does not.

When you use family-qualified targets, make the element family match the target family (`TARGET="MODULE:MOD-RAG"` should resolve to `<MODULE_RAG ...>` or another `MODULE_*` tag) unless your project validator explicitly knows your custom family mapping.

If you find yourself inventing a synonym for one of these, use the existing one. Semantic drift in relations is the fastest way to kill the graph.

---

## 5) Anchors — pointing the graph at code

Anchors are the bridge between the graph and source files.

- Shape: `<ANCHOR NAME="<ANCHOR_NAME>" COORD="<repo-relative-path>#<ANCHOR_NAME>"/>`
- Never use line numbers — they drift the moment someone edits the file.
- Anchor names must match a real `START_*` marker in the target file (see `why-contracts-v1.md`).
- One anchor per meaningful code region. Not per function. Not per line.

Example:

```xml
<MODULE_RAG ID="MOD-RAG" FILE="backend/app/rag/graph.py" TYPE="ORCHESTRATOR" STATE="IMPLEMENTED">
  <ANCHOR NAME="START_GRAPH_main" COORD="backend/app/rag/graph.py#START_GRAPH_main"/>
</MODULE_RAG>
```

---

## 6) Authoring workflow

In order. Skipping a step is how the graph becomes decoration.

1. **Start from value.** Add or update the `UC-*` the work serves.
2. **Name the feature.** Add or update a `FEAT-*` with `INTENT`, optional `ACCEPT` (acceptance criteria), and `PRD_REF` back to `docs/PRD.md`.
3. **Map it.** Connect the feature to APIs, surfaces, modules, and artifacts via `REL` edges.
4. **Add anchors.** In each touched file, add or confirm anchor names that match what the graph points to.
5. **Then implement.** Write code inside the anchored blocks.
6. **Validate.** Run the graph↔anchor validator before claiming done.
7. **Commit graph + code + contracts together.** Split commits break the invariant the graph exists to protect.

---

## 7) Small example

```xml
<USECASE_ASK ID="UC-ASK" NAME="Ask a question with sources">
  <INTENT>Operator asks a question, gets an answer with compact source list.</INTENT>
  <REL TYPE="COVERS" TARGET="FEATURE:FEAT-ASK"/>
</USECASE_ASK>

<FEATURE_CHAT ID="FEAT-ASK" PRIORITY="HIGH" STATE="PLANNED">
  <INTENT>History-aware chat with compact sources</INTENT>
  <PRD_REF>docs/PRD.md#UC-ASK</PRD_REF>
  <REL TYPE="EXPOSED_AS"     TARGET="API:API-ASK"/>
  <REL TYPE="IMPLEMENTED_BY" TARGET="MODULE:MOD-RAG"/>
</FEATURE_CHAT>

<API_ASK ID="API-ASK" PATH="/api/ask" METHOD="POST">
  <WHAT>RAG chat endpoint</WHAT>
</API_ASK>

<MODULE_RAG ID="MOD-RAG" FILE="backend/app/rag/graph.py" TYPE="ORCHESTRATOR" STATE="PLANNED">
  <ANCHOR NAME="START_GRAPH_main" COORD="backend/app/rag/graph.py#START_GRAPH_main"/>
</MODULE_RAG>
```

That is enough structure to tell an agent: this endpoint is here for UC-ASK, its implementation starts at that anchor, and the contract at that anchor is what to read next.

---

## 8) Validation expectations

At minimum, check that every `<ANCHOR ... COORD="path#ANCHOR">` points to a real `START_*` marker in a real file. That one check catches more drift than every other lint combined.

This repo ships a stdlib-only MVP: `python scripts/validate-why.py`. It verifies unique IDs, `REL TYPE` against the documented vocabulary, `REL TARGET` resolution, consistent TARGET style, and STATE-aware anchor enforcement (`PLANNED`/`DEPRECATED` skipped; `STARTED`/`DONE`/`IMPLEMENTED` enforced). On a graph with no anchors yet, it degrades to a warning instead of failing — adopt it as a starting point and tighten as your graph grows.

Add as your graph grows:

- every `FEAT-*` has at least one outgoing `REL` edge toward an implementation node
- every module/UI/API node with `STATE="IMPLEMENTED"` has at least one anchor
- ID prefixes match node families consistently
- no duplicate IDs

These are lint rules, not correctness proofs. They catch mechanical drift — graph edited, code not; code edited, anchor name stale — which is what kills graphs first. Validators are a tool, not a law. Project-specific checks sit on top.

---

## 9) Decision guidance for agents

- Prefer **few clear** `FEAT-*` nodes over many vague ones.
- An orphan feature (no implementation edge) is a drift signal, not a valid state.
- If an entrypoint or module has lost its value, **delete** it and remove its graph node. Stale nodes are worse than missing ones.
- Use `state` / `status` / `freshness` to mark what is implemented, partial, or planned. Agents read these to decide where to work.
- When a PRD change lands, the graph should move in the same commit, or the next one.
- **Retiring a node:** set `STATE="DEPRECATED"` and keep it for one release cycle so existing references don't break silently, then delete it in the commit that removes the last code edge pointing at it. Do not soft-delete forever — an `IMPLEMENTED` repo shouldn't carry a museum.
- **Inherited code without anchors:** don't retrofit. Leave untouched legacy as an untracked region. The first time an agent touches it, add a module contract and whatever block anchors help navigation — and add the graph node at the same commit. The graph should only reference what you actively govern.

---

## 10) What the graph is *not*

- Not the README or the build scripts — use `package.json` / `pyproject.toml` / `Makefile` for runnable commands.
- Not the changelog — use git.
- Not the roadmap — use `docs/ROADMAP.md` or whatever your project uses.
- Not a design doc — use `docs/PRD.md` and design docs as needed.

The graph is narrow on purpose. It is the map between intent and code. Nothing more.

---

## 11) Adapting the schema

Stretch before inventing. If the existing vocabulary covers your case even loosely, use it.

If you must add a new element:

1. Give it a clear `WHAT` child describing its purpose in one sentence.
2. Write down *why* existing node families or relations didn't fit — in the same commit, in this file (your project's copy of it).
3. If the addition becomes a pattern across features, keep it. If it stayed a one-off for one release cycle, delete it.
4. Resist adding nodes for concepts that don't yet exist in the repo. A graph that describes wishful thinking is a graph agents learn to ignore.

The graph format is a tool. If the tool fights the project, bend the tool.
