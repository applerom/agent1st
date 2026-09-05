# Why Contracts v1 — module, method, and block anchors

This is one proven shape of the Contracts layer that pairs with the Why Graph.
Companion docs: `Why1st.md` (the idea), `why-graph-principles.md` (the graph).

The goal: anchor-first navigation that survives refactors, with intent readable where the code lives.

**Why contracts live at the file head.** A module contract sits in the first ~20 lines of the file on purpose. A model that reads only those 20 lines learns PURPOSE + PRD_REF + INVARIANTS + LINKS — enough to decide whether to load the full file or move on. This is *progressive disclosure*: the same idea recently popularized by `SKILL.md`, but built into Why1st from the start. The token-saving is real but secondary; the primary effect is attention shaping. The model spends its context on files that matter and skips files that don't, without you writing a routing prompt.

---

## 0) TL;DR

- Every governed file starts with a **Module Contract**.
- Reusable functions/methods get a **Method Contract** when it helps navigation.
- Non-trivial regions get paired **Block Anchors**.
- Graph-addressable anchor names are stable, unique per file, and match what the Why Graph points to. Local `START_CONTRACT` field groups may repeat inside separately named method or class envelopes; do not address those repeated groups from the graph.
- No line numbers anywhere — in graph, in docs, in contracts.

---

## 1) Core rules

- Use language-native single-line comments with **exact labels**: `START_*:` and `:END_*`.
- Anchors **wrap** the code they describe — the implementation is inside the envelope.
- Each graph-addressable opening token and its closing token occur exactly once in the file, with the opening first. Referenced envelopes may nest or be disjoint; they must not cross. JSX comment markers may omit the opening colon as shown below.
- Anchor names must match `START_*` markers referenced from `docs/why-graph.xml`.
- Keep anchor names short, descriptive, and stable across refactors. Renaming an anchor is a graph-level change.
- PRD references use marker keys — `docs/PRD.md#KEY` resolving to exactly one `<!-- PRD_ANCHOR: KEY -->` comment in the PRD — never section numbers or heading text. Headings get refactored; keys survive. See `why-graph-principles.md` §5a.
- Field keys (PURPOSE, INVARIANTS, etc.) stay in English for deterministic parsing; narrative can be in any language your team uses.
- Feature-level variant: when one file realizes one graph feature, adopters mark it `START_FEATURE_CONTRACT: FEATURE_X` ... `:END_FEATURE_CONTRACT` with the same fields as a module contract. Same rules apply; the marker carries the graph entity's name so one grep lands on graph, code, and log (`why-semantic-logs.md`). Use it instead of, not in addition to, the module contract for that file.

---

## 2) Contract fields

The starter validator checks exact marker tokens, uniqueness, order, and crossing
of graph-referenced enforced envelopes. It does not parse the source language,
prove that tokens are comments, lint every unreferenced local block, or establish
behavioral correctness. Use language-aware checks and behavior tests where the
project needs those guarantees. The [runnable example](examples/reading-list/README.md)
shows the boundary.

**Module-level (required):**
- `FILE` — repo-relative path
- `VERSION` — semver or `YYYY-MM-DD`
- `PURPOSE` — why this file exists
- `PRD_REF` — marker-keyed pointer into `docs/PRD.md` (`docs/PRD.md#KEY`)
- `WHY_REF` — pointer into `docs/why-graph.xml` (optional but recommended)
- `SCOPE` — primary responsibilities
- `INVARIANTS` — policy-critical guarantees

**Module-level (optional):**
- `MODULE_MAP` — one-line role per public symbol. Worth the tokens once a file has more than ~5 public symbols or an agent would otherwise have to grep to find the right entry point. Skip for small, obvious files.
- `CHANGE_HISTORY` — last meaningful change. Optional; git already has the full history. Add only when the "why of the last change" is load-bearing for the next agent.

**Method-level (when used):**
- `PURPOSE` — single responsibility
- `INPUTS` — roles/constraints (not type signature — the code has that)
- `OUTPUTS` — return shape and meaning
- `LINKS` — PRD, WHY, or anchor references
- Optional: `PRECONDITIONS`, `POSTCONDITIONS`, `INVARIANTS`, `ERRORS`, `SIDE_EFFECTS`

---

## 3) Templates

### 3.1 Module contract

```text
# FILE: <repo-relative path>
# VERSION: <semver or YYYY-MM-DD>
# START_MODULE_CONTRACT:
# PURPOSE: <why this module exists>
# PRD_REF: docs/PRD.md#<KEY>
# WHY_REF: docs/why-graph.xml
# SCOPE: <primary responsibilities, semicolon-separated>
# INVARIANTS:
# - <policy-critical guarantee>
# START_MODULE_MAP:
# - <symbol>: <short role>
# :END_MODULE_MAP
# START_CHANGE_HISTORY:
# LAST_CHANGE: <vX.Y or YYYY-MM-DD — brief note>
# :END_CHANGE_HISTORY
# :END_MODULE_CONTRACT
```

### 3.2 Class contract

```text
# START_CLASS_<RealClassName>:
# START_CONTRACT:
# PURPOSE: <class role>
# LINKS:
# - PRD: docs/PRD.md#<KEY>
# :END_CONTRACT
class <RealClassName>:
    ...
# :END_CLASS_<RealClassName>
```

### 3.3 Method / function contract

```text
# START_METHOD_<real_method_name>:
# START_CONTRACT:
# PURPOSE: <single responsibility>
# INPUTS:
# - <role/constraint>
# OUTPUTS:
# - <return shape and meaning>
# LINKS:
# - PRD: docs/PRD.md#<KEY>
# - ANCHORS: START_BLOCK_...
# :END_CONTRACT
def <real_method_name>(...):
    ...
# :END_METHOD_<real_method_name>
```

### 3.4 Block anchors

```text
# START_BLOCK_<SCOPE>_<WHAT>:
# ... code ...
# :END_BLOCK_<SCOPE>_<WHAT>
```

---

## 4) Examples

### 4.1 Python — module + class + methods + block

```python
# FILE: backend/app/rag/providers.py
# VERSION: 2025-10-02
# START_MODULE_CONTRACT:
# PURPOSE: Provider abstractions for embeddings and chat generation.
# PRD_REF: docs/PRD.md#PROVIDERS
# WHY_REF: docs/why-graph.xml
# SCOPE: embeddings; chat; error translation
# INVARIANTS:
# - provider errors are translated to ProviderError before leaving this module
# :END_MODULE_CONTRACT

# START_CLASS_OpenAIProvider:
# START_CONTRACT:
# PURPOSE: OpenAI-backed embeddings and chat provider.
# LINKS:
# - PRD: docs/PRD.md#PROVIDERS
# :END_CONTRACT
class OpenAIProvider:
    # START_METHOD_embed:
    # START_CONTRACT:
    # PURPOSE: Return embedding vector for a single text.
    # OUTPUTS:
    # - list[float], normalized at call site
    # :END_CONTRACT
    def embed(self, text: str) -> list[float]:
        # START_BLOCK_EMBED_HTTP_CALL:
        ...
        # :END_BLOCK_EMBED_HTTP_CALL
        return []
    # :END_METHOD_embed
# :END_CLASS_OpenAIProvider
```

### 4.2 TypeScript — module header + block anchor in a component

```tsx
// FILE: frontend/web/src/app/HomePageClient.tsx
// VERSION: 2026-04-11
// START_MODULE_CONTRACT:
// PURPOSE: Home page client-side composition and chat surface.
// PRD_REF: docs/PRD.md#UC-ASK
// WHY_REF: docs/why-graph.xml
// SCOPE: chat UI; history rendering; source list
// INVARIANTS:
// - message list never re-renders the whole history on a new token
// :END_MODULE_CONTRACT

export function HomePageClient() {
  return (
    <div>
      {/* START_BLOCK_UI_CHAT_MESSAGE_LIST */}
      <MessageList />
      {/* :END_BLOCK_UI_CHAT_MESSAGE_LIST */}
    </div>
  );
}
```

### 4.3 TypeScript — method contract on a reusable function

```ts
// START_METHOD_renderSources:
// START_CONTRACT:
// PURPOSE: Render a compact source list for a single answer.
// INPUTS:
// - sources: array of {title, url, score}
// OUTPUTS:
// - JSX element, empty when no sources
// LINKS:
// - PRD: docs/PRD.md#UC-ASK
// - WHY: docs/why-graph.xml
// :END_CONTRACT
export function renderSources(sources: Source[]): JSX.Element { ... }
// :END_METHOD_renderSources
```

---

## 5) Authoring workflow

1. Read the PRD and Why Graph for the affected feature.
2. Update the graph first (see `why-graph-principles.md`).
3. In the files you'll change, add or update contracts **before** writing the implementation.
4. Keep patches coherent. If unrelated concepts compete for attention in one frequently edited module, split it at a semantic boundary (AGENTS.md §1–§2).
5. Run your validators before claiming done:
   - anchor linter (every `START_*` has a matching `:END_*`)
   - graph↔anchor checker (every `<ANCHOR ... COORD="path#ANCHOR">` resolves)
   - whatever project-specific checks you've added

---

## 6) Rationale

This shape is the file-level realization of two AGENTS.md principles:

- **§1 Attention Engineering** — the contract sits in the first ~20 lines so the most load-bearing facts (PURPOSE, INVARIANTS, LINKS) are visible at the decision point. An agent that reads only the file head still leaves with what matters.
- **§2 Semantic Hygiene** — field keys and `START_*:` markers carry meaning, not just labels. Anchor names match graph references one-to-one, so the same concept is named the same across code, graph, and PRD.

Concrete properties this gives:

- **High-contrast anchors** reduce context entropy — agents find the right region without parsing the whole file.
- **Front-loaded intent and invariants** — the "why" is where the code is.
- **Anchor-first retrieval** is robust to refactors; line-number references rot on first edit.
- **Greppability** — every field is a single-command project-wide query (`grep -rn "^# PURPOSE:"`, `grep -rn "LINKS:"`). English, upper-case, anchored after the colon — this shape exists for that. The same property gives validators a deterministic input.
- **LINKS as dependency map** — the field an agent reads **before** changing a method. PRD reference, graph node, related anchors. Without LINKS, "which other places must I think about" is a grep-and-guess. With LINKS, it is a read.

---

## 7) Anti-patterns

Avoid:

- anchors that are vague, duplicated, or unstable (`START_BLOCK_STUFF`, three of them in the same file)
- contracts that paraphrase the code instead of capturing intent ("PURPOSE: returns the user" on `getUser`)
- line-number references anywhere in canonical docs or contracts
- adding anchors to every five-line block — anchors are for regions a human or agent would otherwise have to guess at
- updating a file's code without updating its contract header — the contract becomes a lie on the first forgotten edit
- leaving obsolete anchors after deleting the code they wrapped

**Rule of thumb:** if an anchor doesn't help an agent answer "what is this region for and what depends on it," it's noise. Remove it.

**Inherited code without anchors.** You will land in files that never had contracts. Do not retrofit the whole tree. Leave stable, rarely-touched legacy untouched — the graph should only reference what you actively govern. The first time an agent edits an unanchored file, add a module contract and whatever block anchors aid navigation, and add the graph node in the same commit. Every touched file upgrades; the rest waits its turn.

---

## 8) Rollout policy (adapt per project)

How much of this to apply at once is a project decision. One pattern that works:

1. All **new files** in governed directories start with a module contract.
2. **Touched high-value entrypoints** gain block anchors immediately.
3. **Reusable functions** gain method contracts when files are refactored or stabilized.
4. Do **not** retrofit the whole repo at once. Every touched file upgrades. Orphan untouched legacy until it's being changed anyway.

The graph and contracts grow together. A file without a contract that the graph doesn't reference is fine. A file the graph references without matching anchors is a bug.
