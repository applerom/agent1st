# Why Evidence — agents own their own verification loop

This is one proven shape of the optional **tests and UI evidence** extension to Why1st (`Why1st.md` §11.2).
Companion docs: `Why1st.md` (the idea), Agent1st's **Done Is Not a Mood** (the principle; exact text in the v12.1 archive).

**Relationship to `AGENTS.md` §2.** §2 is the principle: "completion claims require the best evidence the current harness allows." This document is one layer down: *what evidence shape matches what risk surface,* and how the agent acquires that evidence without asking the human to verify on its behalf. §2 is the rule; this guide is its operational fan-out, with specific recommendations on browser tooling, evidence tiers, and the boundary between agent-owned and human-owned verification.

The goal: when an agent finishes UI work, the next move is *the agent looks at the rendered page* — not *the agent asks the human to check it.* When an agent finishes a backend change, the next move is *the agent runs the test suite* and *the agent reads the API debug trace* — not *the agent declares done and waits.* The closed loop is short. The human is the user, not the QA bot.

---

## 0) TL;DR

- Match evidence to risk surface: deterministic logic → unit tests; API contracts → response assertions; UI behavior → visual checks; runtime workflows → semantic-log assertions over fixtures (see `why-semantic-logs.md`).
- The agent owns the verification loop. *Setting up the harness* is part of the work, not a precondition asked of the human.
- For browser/UI evidence: **Playwright via CLI by default, MCP only when its structured I/O is load-bearing.** MCP tool definitions consume context whether you use them or not; CLI consumes context only on invocation. On long sessions the difference compounds.
- "Spin instead of work" is the canonical anti-pattern: the agent stops, asks the human to verify, the human does not respond, the session ends with the work unverified. Treat that pattern as a failure the agent prevents, not a fact of life.
- When in doubt: evidence is what the next agent reads to know the boundary did the right thing — not what the current agent says it did.

---

## 1) The problem this layer solves

A long-lived agent-driven project produces a recurring failure: the agent ships a UI change, the deterministic checks pass, the agent declares "done," and a week later someone discovers the rendered page was wrong. The unit tests passed because the unit tests tested the unit, not the page. No one looked at the page.

The micro-version of the same failure happens hourly: the agent makes the change, then asks *"can you check the UI looks right?"* The user is busy, does not respond. The agent waits or moves on. The work is in limbo. By the time the next session starts, no one is sure whether the change was verified.

This is **Done Is Not a Mood** failing in practice, not in principle. The principle says completion needs the best evidence the harness allows. The practice says: most adopters do not know what evidence the harness allows, agents do not set up evidence infrastructure proactively, and the human ends up as the verification loop by default.

The fix is two-sided: name *what evidence each kind of work actually needs*, and make clear the agent owns acquiring it.

---

## 2) The core idea

Two principles, working together.

**Match evidence to risk surface.** Different work fails in different ways; the evidence that catches each failure is different.

| Risk surface | What fails | Evidence that catches it |
|---|---|---|
| Deterministic logic | wrong return for a known input | unit / integration tests |
| API contracts | wrong shape, status, or field | response-shape assertions, debug-trace fields |
| UI behavior | wrong visual, layout, interaction | rendered-page checks (Playwright assertions, screenshots, snapshots) |
| Runtime workflows | wrong boundary behavior in a job/pipeline | semantic-log assertions over fixture runs (see `why-semantic-logs.md`) |
| Cross-system flows | wrong glue between components | end-to-end test against a real or near-real environment |

Trying to verify UI behavior with unit tests, or API contracts with screenshots, is a category error. Each surface needs its own evidence shape.

**The agent owns the loop.** This is the **Role Contract** applied to verification infrastructure. The agent picks the route, and *the route includes setting up its own ability to see the result of its work.* If the harness allows browser tools, the agent installs the dependency, writes the test, runs it, captures the evidence, attaches it to the completion claim. If the harness does not allow it, the agent says so explicitly — does not silently substitute "I claim it works" for actual evidence.

The user is rarely aware that the agent is allowed to install Playwright, run a browser, capture a screenshot, write a test, and verify its own work. Asking the user *"can you grant browser access?"* often goes unanswered not because the user refused, but because the user did not know it was a question. Agents who silently wait for permission spin instead of work; agents who proactively try, fail visibly, and report the failure get unstuck.

---

## 3) Why this works for transformer-based agents

Three forces, parallel to `why-graph-principles.md` §2a's three forces for tag shapes:

1. **Sight without verification is guessing.** A model that ships UI work without seeing the page has no model of whether the work succeeded. The unit tests tell it the unit succeeded. The model's internal claim that "this should render correctly" is a prediction over training data, not evidence about the actual current page. When the prediction is wrong — and it will be, because UI is full of CSS interactions and runtime context the model cannot infer from code alone — the failure is silent. Closing the loop with rendered-page verification is what turns prediction into evidence.

2. **Context economy is a tool-architecture decision, not just a brief-writing decision.** Every MCP tool definition installed in a session is loaded into the model's context at session start, *whether the tool is used or not.* A browser MCP can ship 20-40 tool definitions, each with name, description, parameter schema, examples — totaling thousands of tokens of permanent context tax. CLI invocations consume tokens only on invocation, and only the output the agent reads. On a long session with heavy reasoning, the MCP context tax compounds: the budget the agent should be spending on the actual problem is partly spent on tool definitions it may never call. CLI-by-default keeps the working window for the work.

3. **Self-sufficiency loops close faster than human-in-the-loop.** A round-trip through the human takes minutes-to-hours of wall-clock time even when the human is responsive. A round-trip through `npx playwright test` takes seconds. Agents bottlenecked on human verification iterate slowly; agents that verify themselves iterate at machine speed. The compounded latency is the difference between *the agent ships ten useful iterations per session* and *the agent ships two and asks for help eight times*.

The fourth force is cultural: **evidence the next agent can read is durable; "the agent said it works" is not.** A test in the repo, a screenshot saved to artifacts, a semantic log line in a JSONL file — those survive the session ending. The agent's confidence does not. AGENTS.md §6 (Durable State) is the abstract form; this guide is one of its concrete applications.

---

## 4) The four evidence tiers

Pick the tier that matches what failed. Use multiple when multiple surfaces are at risk.

### Tier 1 — Deterministic tests

Unit and integration tests for behavior that can be asserted without a browser, real network call, or human eye. The fastest, cheapest, most reusable evidence.

- *Examples:* function returns expected output for known inputs; reducer transforms state correctly; parser handles edge cases.
- *Tooling:* whatever the project already uses (pytest, jest, go test, cargo test).
- *Strength:* runs in milliseconds, deterministic, easy to add to CI.
- *Weakness:* tests the unit, not the system. UI rendering, real I/O, and visual layout are out of scope.

If your only evidence is Tier 1 and you shipped UI work, you have not verified the UI.

### Tier 2 — API and protocol-shape assertions

For backend work and APIs: assertions on response shape, status codes, debug-trace contents, contract conformance.

- *Examples:* `assert response.status == 200`; `assert "trace_id" in response.debug`; schema validation against an OpenAPI spec.
- *Tooling:* the project's HTTP client + assertions in tests; a contract test suite (Pact, Schemathesis); API debug fields exposed for assertions.
- *Strength:* catches contract drift, missing fields, wrong shapes — the failures most likely to break downstream consumers.
- *Weakness:* says nothing about whether the contract is the *right* contract for the user need.

For RAG and pipeline backends, the debug trace is itself first-class evidence: `debug.graph_trace`, `debug.trace_id`, timing fields, retrieval counts. The API debug payload doubles as test evidence and as a runtime forensic surface. The same fields belong in semantic logs (see `why-semantic-logs.md`).

### Tier 3 — UI and visual evidence

For user-facing surfaces: rendered-page checks via Playwright, browser snapshots, screenshots, visual regression tests.

- *Examples:* Playwright test clicks a button and asserts the modal becomes visible; screenshot of the rendered page saved to `artifacts/screenshots/`; visual diff against a baseline.
- *Tooling:* Playwright (recommended; see §5 for CLI vs MCP), Cypress, Puppeteer, headless-browser frameworks. For authenticated flows, persistent browser profiles (Edge / Chrome user-data-dir) save reauthentication time.
- *Strength:* catches CSS regressions, layout breaks, interaction bugs, JS errors that unit tests miss entirely.
- *Weakness:* slower than Tier 1, requires browser tooling installed, can be flaky on dynamic content. Worth it.

This is the tier most adopters skip and most regret skipping. UI work without UI evidence is *the* canonical "claimed done, actually broken" pattern.

### Tier 4 — Runtime semantic-log assertions

For jobs, schedulers, agent runners, integrations — work where the action happens at runtime boundaries, not in synchronous request/response.

- *Examples:* run the workflow over a fixture, parse the JSONL events, assert the expected event sequence appeared with the right anchors and the right `expected`/`actual` shape.
- *Tooling:* the project's semantic-log writer + a test that runs the workflow + JSONL parsing + assertions.
- *Strength:* catches boundary failures unit tests cannot see (e.g., a job ran but emitted zero `done` events because a fallback path swallowed the success signal).
- *Weakness:* requires the semantic-log infrastructure to exist; pairs with `Why1st.md §11.1` and `docs/why-semantic-logs.md`.

Tiers stack. A backend with a UI runs Tier 1 (unit), Tier 2 (API contract), Tier 3 (UI render). A job-running pipeline with a dashboard runs Tier 1, Tier 4 (semantic events), Tier 3 (dashboard renders). Evidence-by-tier is additive, not exclusive.

---

## 5) Browser tooling — Playwright CLI as default, MCP as edge case

For UI evidence specifically, the choice between **Playwright CLI** and **Playwright MCP** is a real architecture decision with real cost asymmetry.

**Default recommendation: Playwright CLI.**

The CLI version installs as a dev dependency (`npm i -D @playwright/test` / `npx playwright install`), runs as `npx playwright test` or `npx playwright codegen`, and produces structured outputs (test reports, traces, screenshots) the agent reads after invocation.

**The MCP variant** loads its tool definitions into the model's context at session start. The descriptions of `browser_navigate`, `browser_click`, `browser_type`, `browser_screenshot`, and 20-30 sibling tools are part of the prompt the model sees on every turn — whether the tools are called or not. On a typical session that means thousands of tokens of permanent context tax for the *option* of using browser tools.

**Where the trade-off lives.**

| Aspect | CLI | MCP |
|---|---|---|
| Context cost | only on invocation (test output, error logs) | permanent, regardless of use |
| Latency | one process spawn per test run | per-call round-trip, often faster per individual action |
| Iteration loop | write test → run → read output | direct call → read result → next call |
| Determinism | test files are version-controlled, reproducible | per-call decisions live in the conversation |
| Best for | regression suites, CI integration, scripted verification | exploratory clicking, demo flows, one-off checks where writing a test is overkill |

**The choice rule.** Default to CLI. Reach for MCP only when the work is genuinely interactive in a way scripted tests cannot capture — usually exploratory triage of a flow you do not yet understand well enough to script. Once the flow is understood, convert the MCP exploration into a CLI test so the evidence is durable.

This is `AGENTS.md` §1 (Attention Engineering) applied to tool architecture: tool definitions are context, and context is finite. A tool that costs the model 2,000 tokens of permanent context to occasionally call is a worse trade than a tool that costs zero permanent context and 200 tokens per actual use.

**The same logic generalizes.** For database inspection, file system operations, package management — anywhere a CLI exists alongside an MCP server, prefer CLI unless the structured I/O is load-bearing for the agent's reasoning loop. MCP shines on tools where the per-call structure genuinely beats parsing CLI output. Browsers usually do not qualify, because Playwright's CLI already produces structured artifacts (JSON test reports, JUnit XML, traces).

---

## 6) The agent-owns-it principle

Most users do not know they can grant browser access. Most users do not know the agent can install Playwright, write a test, and run it. Most users assume that if the agent is asking *"can you check the UI?"*, the agent could not have checked it itself.

Almost always, the agent could have. The user-facing failure is the agent not trying.

**The right move is a four-step pattern:**

1. **Try.** Install the dependency. Write the test. Run it. Capture the evidence.
2. **If blocked, name the block.** "I tried to install Playwright but the package install requires permission I do not have. Specifically: `npx playwright install` failed with `EACCES`. The fix is: (a) grant write access to `~/.cache/ms-playwright`, or (b) run the install yourself with `npx playwright install --with-deps`."
3. **Continue with the next-best evidence.** If browser evidence is unavailable, run the unit tests, write API assertions, capture stdout — make the completion claim with whatever evidence the current harness actually allowed, and name what is missing.
4. **Never silently substitute "trust me."** A claim of "this should work" with no evidence is **Done Is Not a Mood** failing.

The principle scales beyond Playwright. *Setting up the test framework on a fresh project, writing the first integration test, configuring CI to run on PRs, installing semantic-log infrastructure on a project that has none* — all are part of the agent's route to verification, not preconditions the human is expected to satisfy.

The exception is irreversible or high-blast-radius setup: prod database access, production secret installation, billing-implicating cloud resources. For those the agent escalates. For local dev tooling the answer is almost always "install it and try."

---

## 7) When to adopt / when not to bother

**Adopt evidence-tier discipline when:**

- the project has a UI that real users see;
- the project has APIs whose contracts other systems depend on;
- the project has runtime workflows whose failures are not loud;
- failures discovered by users would cost more than the evidence does to set up;
- "claimed done, actually broken" has happened more than once.

**Skip browser/UI evidence specifically when:**

- the project has no UI (backend libraries, CLI tools);
- the UI is throwaway or prototype-only;
- the harness genuinely cannot run a browser (rare; usually the harness can but no one tried).

**Skip API-trace evidence when:**

- there is no API surface;
- the API is internal-only with one consumer that already tests it.

**Always run Tier 1 (unit / integration tests).** It is the cheapest possible evidence and almost always relevant. Skipping Tier 1 is rare enough to be a project-level red flag.

The pattern that makes evidence feel like ceremony is the same as for semantic logs: applying every tier to every project. Match the tier to the surface; skip the tiers for surfaces you do not have.

---

## 8) What this is *not*

Keep these layers separate. Conflating them is how evidence discipline becomes performative.

- **Not "more tests = more evidence."** A thousand unit tests on the wrong layer is not evidence about the failing layer. Tier-match matters more than test count.
- **Not "the agent must run every test on every change."** Run the tests relevant to what changed. CI runs the full suite; the agent runs the targeted slice.
- **Not "100% coverage means done."** Coverage is a proxy, not the goal. Coverage of the tier that catches the actual failure mode is what matters.
- **Not a replacement for code review.** Evidence catches what the test caught; review catches what the test did not think to check. Both have their place.
- **Not graph-staleness signal.** Evidence answers "did this run match expectation?" Graph staleness asks "does the graph still reflect intent?" Different questions; different artifacts.

---

## 9) Anti-patterns

If you find yourself doing these, stop:

- **"Spin instead of work."** Asking the user to verify the UI, getting no response, sitting idle. The right move is to install the browser tooling and verify yourself, or report the install failure and fall back to next-tier evidence.
- **Tier-1-only on UI work.** Unit tests passing on a feature whose actual failure mode is visual. The unit tests are not evidence about the page.
- **MCP-by-default for browser tooling.** Loading 30 browser-tool definitions into the model's permanent context for sessions that never click anything. CLI is usually the right default; MCP is the special case.
- **Coverage-as-evidence.** "We have 92% coverage" is not the same as "the failing layer is tested." Coverage of the wrong tier is decoration.
- **Testing the mock instead of the system.** Heavy mocking that produces a green test for behavior the real code never executes. Use real dependencies where feasible; mock only at genuine I/O boundaries.
- **Snapshots without diffs reviewed.** Visual snapshot tests that auto-pass when snapshots are auto-regenerated. The whole point is that the diff is read.
- **Disabling logs to keep tests clean.** Tests that mute the semantic-log writer prove the appender is *off*, not that the appender works. Either run real logs and parse them, or skip log assertions and be honest about it.
- **Asking permission to do verification work.** *"Should I install Playwright?"* The answer in dev environments is almost always yes. Try; report if blocked.

---

## 10) References

External anchors for the patterns this guide describes:

- **Playwright official docs** (https://playwright.dev/) — the canonical reference for the recommended browser tooling. CLI usage, test API, traces, and CI integration patterns.
- **Anthropic, *Building Effective Agents*** (https://www.anthropic.com/engineering/building-effective-agents) — covers evaluator-optimizer patterns; "agent verifies its own output" is a direct application.
- **Anthropic Claude Code docs — subagents and tool use** — the harness-specific layer that makes "agent owns its own evidence loop" concretely operable. Provider-specific; the principle is provider-agnostic.
- **Done Is Not a Mood and Role Contract** — the protocol-level ideas, preserved exactly in `docs/_archive/AGENTS-min-v12.1.md`. This guide is their operational fan-out.

The point of citing Playwright specifically is engineering-practice: it is the de facto standard for browser test automation, well-documented, well-supported, and has the CLI-vs-MCP architecture decision sitting right at its surface. Other browser frameworks work; Playwright is the path of least resistance.

---

## 11) Where this fits in the rest of the chain

Evidence sits in a specific spot:

```
PRD            -> what users need
Why Graph      -> how intent maps to surfaces and code
Contracts      -> intent at the file head
Code anchors   -> intent at the block
Semantic logs  -> what happened at runtime, in the same words   (Why1st.md §11.1)
Tests + UI     -> what the system actually does                 (Why1st.md §11.2, this doc)
Subagents      -> who does which part of the work               (Why1st.md §11.3)
```

Each layer has one job. Evidence is the only layer that closes the loop between *what the system was supposed to do* (PRD, graph, contracts) and *what the system actually did at runtime* (logs, tests, UI checks). Without evidence, the rest of the chain is design intent that may or may not be reflected in running code.

The chain works when evidence is acquired by the agent and matched to the surface at risk. It breaks when the agent ships without verifying, or verifies the wrong tier, or asks the human to verify and waits indefinitely. The behavioral fix — *the agent owns the route to its own evidence* — is what makes **Done Is Not a Mood** operational rather than aspirational.

The question is not *whether* to verify. It is *whether the agent's default is closed-loop self-verification or open-loop "ask the human to check."* On modern agent harnesses, the closed loop is available and the open loop is the regression. This guide is the bias toward closing the loop.
