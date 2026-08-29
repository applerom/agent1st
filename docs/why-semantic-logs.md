# Why Semantic Logs — runtime events as future agent context

This is one proven shape of the optional **semantic logs** extension to Why1st (`Why1st.md` §11.1).
Companion docs: `Why1st.md` (the idea), `why-graph-principles.md` (the graph), `why-contracts-v1.md` (contracts and anchors).

**Relationship to `AGENTS.md` §8 "Semantic Logging."** AGENTS.md §8 is the behavior principle ("logs are future context") that applies to *all* agent-produced records — chat handoffs, decision notes, runtime events. This document is the **runtime-events instantiation** of that principle: structured boundary events with anchors that bridge the Why1st chain. Same idea, narrower surface. A fresh agent who finds both does not need to choose between them — §8 is the rule, this guide is one of its applications.

The goal: when a future agent shows up after a job has run, a request has failed, or a workflow has produced an unexpected result, they should be able to read what happened **in the same vocabulary as the PRD, the Why Graph, and the code anchors** — without reconstructing intent from raw stdout, code archaeology, or chat history.

**Why this is not just "more logs."** Raw logs preserve detail. Semantic logs preserve meaning. The two are different artifacts, not competing ones — keep both. The thing that turns a structured log into agent context is one specific decision: the **anchor** field uses verbatim the same UPPER_SNAKE_CASE names that live in the Why Graph and in `START_*` code markers. A model in a fresh session can `grep FEATURE_LIVE_DEBUGGABILITY` and get hits in three artifacts — graph, code, log — and orient instantly. That cross-layer greppability is the load-bearing claim. Without it, semantic logs are just structured logs that help humans.

---

## 0) TL;DR

- Two streams: raw logs (detail) and semantic logs (meaning). Keep both.
- Required event fields: `ts`, `event`, `anchor`, `component`.
- The trio that turns events into evidence: `anchor + expected + actual`. Use it whenever the boundary has a check-able expectation.
- One workflow → 3-7 events at meaningful boundaries → one parsing test → one note pointing future agents at the file. Stop there until a real failure asks for more structure.
- Anchor names match what the Why Graph and code already use. Inventing a new vocabulary for logs breaks the whole point.

---

## 1) The problem this layer solves

A long-lived agent-driven project produces a recurring failure: an agent finishes a job, declares success, and a future agent (or a human, or a CI job) opens the codebase a week later and asks: **what actually happened on that run?**

Three usual answers, all bad:
- raw stdout: high detail, no semantics — every line is plausibly important, none is actually important.
- chat history: gone after compaction; pretends to be evidence and is not.
- "trust the green tests": tests prove the unit ran, not that the runtime boundary did what intent required.

Semantic logs are the fix for *this* failure mode, not a generalization of "logging." If your project does not have runtime boundaries that produce surprising outcomes, you do not need them.

---

## 2) The core idea

Record important runtime boundaries as compact structured events whose vocabulary matches the rest of the Why1st chain.

A boundary is a place where intent meets reality:
- a job transitions state (queued → running → done/failed)
- an external call returns (API, model, browser, CLI, database)
- a parser/adapter produces zero results when results were expected
- an HTTP route receives or rejects a request
- a state load completes or fails
- a fallback path is taken
- a user-visible artifact is written or rendered

Two streams, different jobs:

| Stream | Format | Question it answers |
|---|---|---|
| Raw logs | stdout/stderr, arbitrary text | "what was every byte that came out?" |
| Semantic logs | one JSON object per line | "what happened, in project vocabulary?" |

The bridge between semantic logs and the rest of the Why1st chain is a single field: **`anchor`**.

```
PRD intent
  -> Why Graph entity (FEATURE_*, USECASE_*, MODULE_*, ...)
  -> code anchor (START_FEATURE_CONTRACT: FEATURE_X / START_BLOCK_X)
  -> runtime semantic event {"anchor": "FEATURE_X", ...}
  -> test/visual/raw-log evidence
```

If your event's `anchor` is `FEATURE_LIVE_DEBUGGABILITY`, the same string lives in the graph as `<FEATURE_LIVE_DEBUGGABILITY ID="...">` and in code as `START_FEATURE_CONTRACT: FEATURE_LIVE_DEBUGGABILITY`. The agent does not need a documented index — the index is the vocabulary itself.

---

## 3) Why this works for transformer-based agents

Three forces, parallel to `why-graph-principles.md` §2a's three forces for tag shapes:

1. **Vocabulary stability creates an attention bridge.** A model in a fresh session has no project memory. When it sees `FEATURE_LIVE_DEBUGGABILITY` in a log, the token is salient if and only if the model has seen the same token elsewhere in current context (graph, code, contracts). Distinctive UPPER_SNAKE_CASE strings are exactly the kind of tokens that survive long contexts. Generic strings (`debug`, `state_loaded`, `api_call`) blend into training-data noise; identifiers do not.

2. **Same-string grep is the cheapest tool a model has.** Models are good at one thing humans underuse: literal string search across files. `grep FEATURE_LIVE_DEBUGGABILITY` works only when the same identifier really is in three artifacts. Keeping vocabulary identical between layers is what makes that grep land. Translating between layers ("the `agent_job` log corresponds to the `AgentJob` graph node which is in `src/jobs/` somewhere") is a translation tax the agent pays every time, in tokens and in error rate.

3. **Attention is finite (AGENTS.md §4).** A semantic log line carries one main signal — what happened at this boundary, in known vocabulary. Agents reading 200 such lines will spend their attention on the events that matter (warnings, errors, expected≠actual cases) because the wrappers are predictable and the deltas are not. A free-text log mixes signal and decoration; the agent has to re-read every line.

The primary audience of semantic logs is the **future agent**, not the present human. Humans benefit too. But if a format helps humans and not agents, the format failed.

---

## 4) When to adopt / when not to bother

**Adopt** when the project has:
- background or scheduled jobs;
- agent-run workflows where the agent is the actor;
- external integrations (APIs, CLIs, browsers, model calls) that fail in non-obvious ways;
- multi-step pipelines (queue → process → render);
- recurring "what happened on that run?" questions across sessions.

**Do not bother** when the project is:
- a pure CLI that computes and exits;
- a library without runtime surface;
- a static site;
- a throwaway prototype.

Adding semantic logs to a project that does not have a runtime surface is the canonical way to make Why1st feel like ceremony. The `Why1st.md` §11.1 "When NOT to bother" line is a real check, not a politeness.

---

## 5) Minimum useful event shape

Use JSONL/NDJSON (one JSON object per line) unless your project already has a better structured sink.

**Required fields:**

| Field | Type | Notes |
|---|---|---|
| `ts` | ISO timestamp string | `2026-04-29T12:00:00Z`. Stable name across the project. |
| `event` | snake_case string | `state_load_completed`, `external_call_failed`. Stable vocabulary. |
| `anchor` | string | Why Graph entity name, or code anchor name (`FEATURE_X`, `START_BLOCK_STATE_LOADING`). Use the same strings the graph and code already use. |
| `component` | string | Module/service/surface that owns the boundary (`ApiServer`, `RefreshJob`, `RAGAdapter`). |

**Conditional fields — use when they apply, omit when they don't:**

| Field | Use when |
|---|---|
| `expected` | The boundary has a definable expectation (state present, list non-empty, status 2xx). |
| `actual` | Always paired with `expected`. Together they form the evidence trio with `anchor`. |
| `correlation_id` | Events span boundaries (a job, a request, a trace). Common names: `job_id`, `request_id`, `trace_id`. |
| `level` | The downstream sink filters by level. `info` / `warn` / `error`. |
| `next` | One short hint for the next agent reading this event. One sentence, not a paragraph. |
| `metadata` | Compact structured details specific to this boundary. Not a free-form dump. |

**Example — one good event:**

```json
{
  "ts": "2026-04-29T12:00:00Z",
  "level": "warn",
  "event": "rag_returned_zero_results",
  "anchor": "FEATURE_LIVE_DEBUGGABILITY",
  "component": "RAGAdapter",
  "request_id": "req_4f2a",
  "expected": {"results_min": 1},
  "actual": {"results_count": 0},
  "metadata": {"query_len": 217, "filters": ["scope=team"]}
}
```

The trio `anchor + expected + actual` is what a future agent will scan for. If your event has a check-able expectation and you don't write the trio, you are leaving the load-bearing field empty.

---

## 6) What to log / what not to log

**Log boundaries, not steps.** A boundary has a before/after that matters; a step is internal flow.

**Good events** (representative, not exhaustive):
- job/workflow state transitions (queued, running, done, failed)
- external call started / returned / failed
- state load started / completed / failed
- parser/adapter returned zero artifacts when artifacts were expected
- route received / rejected / authenticated
- fallback path used
- user-visible write completed / failed
- snapshot/screenshot saved

**Bad events** (do not log):
- every loop iteration
- raw prompt or response body dumps
- secrets, tokens, OTPs, credentials, full HTTP headers
- huge data payloads (truncate or summarize)
- vague free text ("processing complete", "something happened")
- "success" without expected vs actual

If you find yourself writing `event: "tick"` or `event: "step_3"`, you are in step territory, not boundary territory. Stop and reconsider what the actual boundary is.

---

## 7) Where logs live

Pick the simplest durable local sink that works.

- **Default:** `artifacts/logs/<workflow>.jsonl` or `live-sessions/*.jsonl` — JSONL files, one per workflow or per day, append-only.
- **Per-job correlation:** one global JSONL filtered by `job_id` for query, **or** one file per job under `artifacts/jobs/<id>/events.jsonl` if the job's lifecycle is bounded.
- **API/RAG:** include the relevant events in the API debug payload **and** persist to JSONL. The debug payload is for the immediate caller; the JSONL is for the future agent.
- **DB:** only when JSONL provably hits a real limit — concurrent writers across processes, retention policy, complex query needs. Choose a DB to solve a measured problem, not to look serious.

**Never:** semantic logs only in chat. If the session disappears, the log disappeared.

---

## 8) Implementation slice — the smallest useful version

A new adopter should start here and stop here until the next failure teaches them more is needed.

1. **Pick one workflow.** A refresh job, a `/api/ask` route, app startup, a scheduled task. One. Not all of them.
2. **Write a tiny appender.** Function takes an event dict, ensures the parent directory exists, appends one JSON line. ~15 lines of code in any language. No framework.
3. **Emit 3-7 events at real boundaries.** Cover one happy path and one failure/empty-result path at minimum. Reuse `anchor` strings that already exist in your graph or code.
4. **Pair with raw logs.** Do not delete or hide raw stdout/stderr. Semantic events summarize; raw logs prove.
5. **Add one test.** Run the workflow over a fixture, parse the JSONL, assert the required fields are present and the expected event sequence appeared. Do not over-validate. The goal is "the writer works"; the validator can catch deeper issues later.
6. **Tell the next agent where to look.** One sentence in the project's adopter addendum or per-workflow doc: *"Semantic events for `<workflow>` live in `artifacts/logs/<workflow>.jsonl`. Each line is one JSON object with at least `ts`, `event`, `anchor`, `component`."*

That is the entire first slice. Resist the urge to design a schema, choose a vendor, build a dashboard, or define an event taxonomy. Add structure when a real failure shows the current shape is too loose.

---

## 9) What semantic logs are *not*

Keep these layers separate. Conflating them is the most common way semantic logs become noise.

- **Not decision memory.** Logs answer *what happened.* They do not answer *why we decided X.* Durable rationale belongs in PRD, graph, or a project-local decision artifact — not in a fatter event. If you find yourself writing prose into `metadata`, you are in the wrong layer.
- **Not raw logs.** A semantic event is a summary at a known boundary. The raw stream still exists and still matters; semantic events do not replace it. Lose neither.
- **Not test evidence on their own.** A green semantic-event sequence proves the appender ran; it does not prove the boundary did the right thing. Pair with assertions on `expected`/`actual`, with raw-log diffing, or with the `Why1st.md §11.2` evidence path (UI/snapshots/Playwright) for surfaces that semantic events cannot describe.
- **Not graph-staleness signal.** Graph staleness asks "does the graph still reflect PRD intent?" Logs ask "did this run match the boundary's expectation?" Different question, different artifact.

---

## 10) Anti-patterns

If you find yourself writing these, stop:

- log lines that are free-text strings instead of structured objects;
- emitting "success" with no `expected`/`actual`;
- inventing a separate vocabulary for logs that does not match the graph/code;
- camelCase or PascalCase event names (`event: "stateLoadCompleted"`); use snake_case for stable identifiers and reserve UPPER_SNAKE_CASE for the `anchor` field;
- hiding raw logs because semantic logs exist;
- choosing a database before JSONL has demonstrably failed;
- adding 12 fields when 5 carry the meaning;
- per-line metadata blobs that are unbounded or contain secrets;
- requiring every adopter to copy one reference project's exact filenames and field names — what is portable is the *shape*, not the labels.

---

## 11) Validator — optional, not required

A future addition to `scripts/validate-why.py` could lint that anchors emitted in semantic events resolve to real graph entries or code markers. This is **not** part of the canonical chain and is not shipped today; it is a candidate in `docs/ROADMAP.md` waiting on adoption signal. Until then, treat the event-anchor relationship as a discipline, not a checked invariant.

If you implement this lint locally, keep it as a warning, not an error. A new event that points at a not-yet-graphed anchor is often a useful signal that the graph needs an entry, not that the log is wrong.

---

## 12) Where this fits in the rest of the chain

Semantic logs sit in a specific spot:

```
PRD            -> what users need
Why Graph      -> how intent maps to surfaces and code
Contracts      -> intent at the file head
Code anchors   -> intent at the block
Semantic logs  -> what happened at runtime, in the same words
Tests + UI     -> what the system actually does (Why1st.md §11.2)
```

Each layer has one job. If a layer takes on a second job, it loses the first.

The chain works because the same vocabulary survives all of it. Break the vocabulary at any layer and the chain becomes a stack of independently-correct artifacts that no agent can navigate as one structure. The semantic log is the runtime instance of the same Why1st rule that makes the graph and contracts work in the first place: **carry intent in tokens that distinct enough to grep across the whole project.**
