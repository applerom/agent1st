# Why Contracts v1 — module, method, and block anchors

This is one proven shape of the Contracts layer that pairs with the Why Graph.
Companion docs: `WHY-APPROACH.md` (the idea), `why-graph-principles.md` (the graph).

The goal: anchor-first navigation that survives refactors, with intent readable where the code lives.

---

## 0) TL;DR

- Every governed file starts with a **Module Contract**.
- Reusable functions/methods get a **Method Contract** when it helps navigation.
- Non-trivial regions get paired **Block Anchors**.
- Anchor names are stable, globally unique per file, and match what the Why Graph points to.
- No line numbers anywhere — in graph, in docs, in contracts.

---

## 1) Core rules

- Use language-native single-line comments with **exact labels**: `START_*:` and `:END_*`.
- Anchors **wrap** the code they describe — the implementation is inside the envelope.
- Anchor names must match `START_*` markers referenced from `docs/why-graph.xml`.
- Keep anchor names short, descriptive, and stable across refactors. Renaming an anchor is a graph-level change.
- Field keys (PURPOSE, INVARIANTS, etc.) stay in English for deterministic parsing; narrative can be in any language your team uses.

---

## 2) Contract fields

**Module-level (required):**
- `FILE` — repo-relative path
- `VERSION` — semver or `YYYY-MM-DD`
- `PURPOSE` — why this file exists
- `PRD_REF` — pointer into `docs/PRD.md`
- `WHY_REF` — pointer into `docs/why-graph.xml` (optional but recommended)
- `SCOPE` — primary responsibilities
- `INVARIANTS` — policy-critical guarantees

**Module-level (optional):**
- `MODULE_MAP` — one-line role per public symbol
- `CHANGE_HISTORY` — last meaningful change

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
# PRD_REF: docs/PRD.md §...
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
# - PRD: docs/PRD.md §...
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
# - PRD: docs/PRD.md §...
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
# PRD_REF: docs/PRD.md §9
# WHY_REF: docs/why-graph.xml
# SCOPE: embeddings; chat; error translation
# INVARIANTS:
# - provider errors are translated to ProviderError before leaving this module
# :END_MODULE_CONTRACT

# START_CLASS_OpenAIProvider:
# START_CONTRACT:
# PURPOSE: OpenAI-backed embeddings and chat provider.
# LINKS:
# - PRD: docs/PRD.md §9
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
// PRD_REF: docs/PRD.md §4
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
// - PRD: docs/PRD.md §4
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
4. Keep patches small. For frequently edited modules, ~200–300 lines is a refactor signal (AGENTS.md §4).
5. Run your validators before claiming done:
   - anchor linter (every `START_*` has a matching `:END_*`)
   - graph↔anchor checker (every `<ANCHOR TARGET="...">` resolves)
   - whatever project-specific checks you've added

---

## 6) Rationale

- **High-contrast anchors** reduce context entropy — agents find the right region without parsing the whole file.
- **Contracts front-load intent and invariants** — the "why" is where the code is.
- **Anchor-first retrieval** is robust to refactors; line-number references rot on first edit.
- **Stable field keys** allow deterministic validation with simple scripts.

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

---

## 8) Rollout policy (adapt per project)

How much of this to apply at once is a project decision. One pattern that works:

1. All **new files** in governed directories start with a module contract.
2. **Touched high-value entrypoints** gain block anchors immediately.
3. **Reusable functions** gain method contracts when files are refactored or stabilized.
4. Do **not** retrofit the whole repo at once. Every touched file upgrades. Orphan untouched legacy until it's being changed anyway.

The graph and contracts grow together. A file without a contract that the graph doesn't reference is fine. A file the graph references without matching anchors is a bug.
