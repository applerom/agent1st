# Why Subagents — delegate by default, crystallize the pattern later

This is one proven shape of the optional **subagent orchestration** extension to Why1st (`Why1st.md` §11.3).
Companion docs: `Why1st.md` (the idea), `AGENTS.md` §4 (Delegation Design — the principle).

**Relationship to `AGENTS.md` §4.** §4 is the principle: how to delegate well *when you do*. This document is one layer down: *when does an agent default to delegating in the first place,* and what shape the project-local artifact takes once delegation becomes recurring. Same idea, different question. §4 is the rule; this guide is its behavioral entry point and one common artifact.

The goal: a strong agent that is trained on agentic work should not silently revert to single-thread *do-it-all-myself* mode on real projects. When the work is parallel, when the read surface is large, when the ops do not need the lead's full intelligence, the right move is to spawn subagents. This guide names when, why, and how.

---

## 0) TL;DR

- Strong agents are trained agentically but default to solo execution. The single biggest project-level drift: missing parallelism, burnt context, wrong-tier intelligence on cheap ops.
- Four shapes carry most of the value: **parallel exploration**, **fan-out validation**, **deep-dive isolated work**, and **lower-intelligence ops**. Memorize these four; spawn when the work fits one.
- Default rule: *if the next step is independent of what you are currently reasoning about, and the brief fits in three sentences, delegate.*
- Subagents return evidence, not narratives. The lead synthesizes; subagents work.
- The artifact (`docs/agent-orchestration.md`) is the second move, not the first. Behavior comes first; the file crystallizes patterns the lead has already used.

---

## 1) The problem this layer solves

A long-lived agent-driven project produces a recurring failure that is invisible from inside one session: the lead agent goes through the entire task as one coherent thread of reasoning, reads twenty files in main context, runs four greps in main context, and ships. The work gets done. Looks fine.

The cost is paid quietly:
- the lead's context gets burnt on reads it could have delegated, leaving less room for the actual reasoning the human is paying for;
- independent steps run sequentially when they could have run in parallel — three minutes of latency per delegation skipped, multiplied by every "let me also check…";
- low-difficulty ops (file scanning, format conversion, link checking, config lookup) run on the most expensive model in the stack;
- the lead's own attention budget, which AGENTS.md §1 names as a finite engineering constraint, gets spent on bookkeeping instead of judgment.

The behavior is not a model deficiency. Strong agents are explicitly trained on agentic work and have native subagent tools. The miss is a default. Optimization-for-completion within one session pulls toward "I can do this directly, so I will." The next-best move — *delegate this part, keep my context for the synthesis* — does not get picked unless the agent is biased toward it.

This guide is the bias.

---

## 2) The core idea

Treat delegation as the default for any work that is independent, bounded, or context-heavy. Treat solo execution as the case that needs justification, not the other way around.

Three orthogonal wins, each enough on its own:

| Win | What it buys | Cost if you skip it |
|---|---|---|
| **Context economy** | The subagent burns its own context on the read surface and returns a small summary. The lead's context stays clean. | The lead's working memory fills with intermediate facts; the actual decision happens with degraded attention. |
| **Real parallelism** | Independent subtasks run concurrently. End-to-end latency drops to the slowest branch. | Every "let me also check" adds serially to wall-clock time. Slow loop, fewer iterations per session. |
| **Intelligence routing** | Low-difficulty ops run on cheap/fast models. The lead reserves the expensive model for synthesis. | Every grep, lint, format-convert, link-check pays frontier-tier prices. Or worse — the lead's attention. |

The lead's job is not to be a faster solo worker. It is to be the only agent in the swarm that holds the full task graph and decides what gets dispatched, in what shape, to whom.

---

## 3) Why this works for transformer-based agents

Three forces, parallel to `why-graph-principles.md` §2a's three forces for tag shapes:

1. **Context is finite and the lead's context is the most expensive.** A subagent gets a fresh context window per dispatch. Its 50k-token read becomes a 500-token return. The lead never sees the 50k. Without delegation, every read consumes the same window the lead needs for the actual decision — and once that window is full, attention degrades on every subsequent token (AGENTS.md §1 again, applied to its own substrate).

2. **Independence enables true parallelism, not just nominal parallelism.** Two grep operations issued in one assistant turn run concurrently. Two subagents dispatched in one turn each get their own full reasoning loop, in parallel. The latency win compounds: a five-minute research task split across three subagents finishes in five minutes, not fifteen. Strong agents have this primitive; the failure is using it.

3. **Intelligence has a tier.** Reading a file and reporting structure does not need a frontier-tier model. Running ten greps and synthesizing matches does not either. Lint, format-convert, doc-summary — fast cheap models do these without quality loss. The lead's tier is reserved for the parts that actually require it: integration, design judgment, ambiguity resolution, evidence weighing. Routing low-tier work to low-tier models is not a cost optimization — it is correct allocation. Doing it on the lead is overpayment *and* attention pollution.

The fourth force is cultural, not architectural: **the lead is paid to synthesize, not to execute.** Anthropic's *Building Effective Agents* (the canonical external reference for this pattern — orchestrator-worker, parallelization, evaluator-optimizer) names the same shape. If you have not read it once, read it. The pattern is not Agent1st-specific. It is the default mental model of every modern agent framework. Single-thread execution is the regression.

---

## 4) When to default to delegation / when not to bother

**Default to delegation when:**
- the next step is **independent** of what you are currently reasoning about — knowing its answer changes the next move, but the work to get the answer does not need the lead's current chain;
- the read surface is **larger than the decision** — you need a summary of ten files to make a small judgment call;
- the work is **bounded and verifiable** — clear input, clear "done," no recursive ambiguity that would require multiple lead-side check-ins;
- the same shape will run **N times** — N file reviews, N config lookups, N parallel migrations;
- the brief fits in **three sentences** — if you cannot name the deliverable that compactly, the work is not yet shaped for delegation; shape it first.

**Do not bother when:**
- the work is **stateful and sequential** — each step depends on the lead's interpretation of the previous step's output;
- the delegation **brief is longer than the work** — writing the contract takes more tokens than just doing the work;
- the task is **on the critical path with a human in the loop** — the human is the next reviewer, not a subagent;
- the read is **load-bearing for the lead's own reasoning** — sometimes the lead needs to read the file directly because what matters is not the summary but the texture;
- the cost of a wrong dispatch is **higher than the cost of doing it directly** — destructive ops, irreversible changes, work that requires the lead's full context to judge correctly.

The bias is toward delegation, but the bias is not a mandate. Solo work is correct when the conditions above apply. The failure mode is *never* dispatching, not *not always* dispatching.

---

## 5) The four delegation shapes

These four cover the bulk of useful subagent work in real projects. Recognize them by name; spawn when the work fits one.

### Shape A — parallel exploration

Multiple independent reads or searches, results synthesized by the lead.

- *Examples:* "skim these seven candidate libraries and report on their dependency footprint"; "grep for usages of `RAGAdapter` across these three sibling repos"; "summarize the open issues in five files."
- *Win:* context economy + parallelism. The lead never reads the seven libraries.
- *Brief shape:* deliverable is a compact comparison, table, or list. Each subagent does one slice; the lead synthesizes.
- *Smell that says do this:* you are about to read more than three files in main context to "get the lay of the land."

### Shape B — fan-out validation

The same check, run independently across N items.

- *Examples:* "review each of these six PRs against the migration checklist"; "run the validator over each subdirectory and report failures"; "for each of these adapter implementations, confirm it satisfies the contract."
- *Win:* parallelism + uniformity (each subagent applies the same rubric, returns the same shape).
- *Brief shape:* one rubric, N targets. Each subagent gets one target, returns evidence in a fixed shape.
- *Smell that says do this:* you are about to write a loop in your own reasoning.

### Shape C — deep-dive isolated work

A bounded task with a clear deliverable that does not require ongoing lead-side judgment mid-flight.

- *Examples:* "implement and test the `redis` cache adapter against the existing `Cache` interface"; "write a migration script that produces this output format from this input"; "diagnose why this specific test fails and propose a fix."
- *Win:* context economy. The subagent does the full reasoning loop in its own window; the lead receives the patch, the test, and the explanation.
- *Brief shape:* full contract — purpose, interface, acceptance criteria, return format. This is where most of §4 (Delegation Design) gets exercised.
- *Smell that says do this:* the work is one or two coherent hours of focused execution, not interleaved with other decisions you are making.

### Shape D — lower-intelligence ops

Format conversion, link checking, doc summarization, lint, file scanning — work that does not need the lead's tier.

- *Examples:* "convert this YAML to TOML preserving comments where possible"; "scan this directory for files over 500 lines and list them"; "summarize this 4000-word doc in five bullets."
- *Win:* intelligence routing + context economy. Cheap model, cheap tokens, no lead context spent.
- *Brief shape:* short, prescriptive. The deliverable is mechanical.
- *Smell that says do this:* you would feel mildly silly spending frontier-tier tokens on the operation.

A single task can use multiple shapes in one assistant turn — Shape A for exploration in parallel with Shape B for validation, results merged before the next decision. Multiple subagent dispatches in one turn is the canonical pattern, not an edge case.

---

## 6) The delegation contract

A subagent may receive no context, a filtered slice, or a fork of the parent conversation. The delegation contract is the only context the lead can safely assume arrived and stayed salient.

A good brief carries:

- **Goal in one sentence.** What changes after the subagent's work that did not change before? Not "investigate X" — "tell me whether X is safe and what specifically would break if not."
- **Inputs and constraints.** File paths, line numbers, exact strings. Anything the subagent cannot find on its own. If the prior conversation discovered that approach Y was rejected and approach Z works, say so — the subagent does not see the conversation.
- **Acceptance criteria — what the deliverable looks like.** A list of bullets, a patch with a passing test, a five-line summary, a verdict + reasoning, a file written to a specific path.
- **Latitude — what the subagent is allowed to decide vs. what to escalate.** "If you find Z, do W; if you find anything else, return findings without acting."
- **Right to report operational truth.** Say explicitly that blockers, missing context, repeated friction, unsafe assumptions, and a better alternative are valid outcomes. A subagent forced to look successful will hide the fact the contract failed.
- **Length budget for the normal result.** Prune narration, not complaints. A response budget never forbids the subagent from reporting why the requested result is unsafe, impossible, or based on missing evidence.

A bad brief — and the canonical failure mode — is a one-line command-style prompt. *"Find security issues in the auth code."* The subagent has no context, no constraints, no acceptance criteria, no latitude, no budget. It will produce something. That something will be diluted, off-target, and the lead will spend more tokens correcting than was saved by dispatching. AGENTS.md §4 is the principle this codifies. Read it once.

The subagent's return contract mirrors the brief: **evidence plus operational truth, not performance theater**. Return file paths and line numbers, commands and exit codes, the patch and test output — and also limitations, blockers, friction, fallback, or a better route when they matter. If the subagent only describes what it intended to do, or hides failure to fit the requested shape, the dispatch failed even if the answer sounds confident.

---

## 7) What to delegate vs. do yourself

A practical heuristic, calibrated to where lead-only work actually pays:

**Lead does directly:**
- the synthesis across subagent results
- design judgment, ambiguity resolution, framing decisions
- the read whose *texture* matters more than its summary
- destructive or irreversible ops where the lead's full context is the safety net
- the parts the user is actively in the loop on

**Lead delegates:**
- parallel reads where the lead would otherwise serial-read more than ~3 files
- the same check applied to N items
- bounded deep-dive work that does not interleave with other open decisions
- mechanical ops that do not need the lead's tier
- exploratory searches where the lead would otherwise burn context "to see what's there"

The line moves with task size. On a small task, the brief overhead dominates and solo execution is correct. On a large task, the delegation discipline is what makes the lead's context survive long enough to ship.

---

## 8) When the artifact emerges

After the lead has delegated several times in a project — different shapes, different contexts — patterns crystallize:

- which prompt shapes consistently produce useful subagent output;
- which task types are reliably good fits for delegation vs. recurring solo work;
- which evaluation rubrics catch subagent over-narration vs. under-evidence;
- durable lessons from prior delegations that the next dispatch should not re-discover.

That is the moment a project-local `docs/agent-orchestration.md` (or equivalent) earns its place. The artifact crystallizes patterns the lead has already used; it does not invent them. Writing the artifact first, before the patterns are real, produces ceremony.

A useful first version is small:

- **Role matrix** — for the recurring delegation shapes in this project, what role does each subagent play? Researcher, validator, implementer, reviewer.
- **Prompt patterns** — the brief shapes that have worked. Not full templates; load-bearing structure (goal sentence, constraints, acceptance, latitude, budget).
- **Evaluation rubric** — how does the lead decide a subagent return is acceptable vs. needs re-dispatch?
- **Durable lessons** — anti-patterns this project has burned itself on, written so the next dispatch does not repeat them. Two or three is plenty; ten is over-fitting.

Reference it from the adopter addendum **only when the project actually delegates regularly.** A solo-agent project with occasional one-shot subagents does not need it; the brief in `Why1st.md §11.3` is enough.

The same boundary applies to harness-specific extensions — Codex `.codex/agents/*.toml` profiles, Claude Code subagent definitions, harness-specific routers — all are project-local extensions above Why1st, not parts of it.

---

## 9) What this is *not*

Keep these layers separate. Conflating them is how subagent orchestration becomes process theater.

- **Not "always delegate."** The bias is toward delegation when the conditions in §4 apply. Mandatory delegation kills the times when solo execution is correct.
- **Not a hierarchy of agents.** Subagents are tools the lead uses. They are not direct reports with their own backlogs. The lead owns the task graph.
- **Not a substitute for thinking.** Delegating to "save tokens" while skipping the actual reasoning produces dispatched-but-aimless work. The lead's job is the synthesis, not the dispatch.
- **Not a replacement for `AGENTS.md` §4.** §4 says how to delegate well. This guide says when delegation is the right move at all. They stack; they do not replace each other.
- **Not graph-staleness signal.** Subagent dispatch quality and graph health are different drift signals; one does not measure the other.

---

## 10) Anti-patterns

If you find yourself doing these, stop:

- **Solo-by-default on independent reads.** Reading more than three files in main context "to see what's there" when a subagent could return a summary.
- **One-line briefs.** *"Find security issues in the auth code."* The subagent has no constraints, no acceptance criteria, no budget. The output will be diluted noise.
- **Re-doing the subagent's work.** If the lead's next move is to grep the same files the subagent just searched, the brief failed. Either the subagent's return was too thin, or the lead did not trust it. Both are fixable.
- **Using subagents to avoid thinking.** Dispatching the *decision* to a subagent. Subagents do work; leads decide.
- **Subagent over-narration.** Returning prose that describes what was done instead of evidence of what was done. Acceptance criteria + length budget on the brief side prevents this.
- **No length budget on the brief.** Default subagent behavior is verbose. Without "report in under N words" or "return only the patch," the lead pays in synthesis tokens what was saved on dispatch.
- **Delegating the destructive op.** `rm -rf`, force-push, schema migration on prod — the lead does these, with full context. Subagents propose; leads execute.
- **Building the artifact first.** Writing `docs/agent-orchestration.md` before any delegation has happened. The artifact crystallizes lived patterns; without lived patterns it is template ceremony.

---

## 11) References

External anchors for the pattern this guide describes:

- **Anthropic, *Building Effective Agents*** (https://www.anthropic.com/engineering/building-effective-agents) — the canonical write-up of orchestrator-worker, parallelization, and evaluator-optimizer patterns. Provider-agnostic vocabulary, drawn from Anthropic production work but applicable across stacks. If you read one external thing on this topic, read this one.
- **Harness-native subagent docs** — Claude Code subagents, Codex agent profiles, Cursor background agents, OpenAI Agents SDK handoffs. These are the tooling layer; this guide is the behavior layer above them. Do not confuse "I have the tool" with "I use the tool by default."
- **`AGENTS.md` §4 (Delegation Design)** — the protocol-level rule. This guide is its behavioral entry point.

The point of citing external references is not credentialism. It is to make clear that the *do-it-all-myself default* is the regression, and the *delegate-by-default* posture is what every modern agent framework already assumes. Adopting this is not Agent1st invention; it is catching up to the operating model the frameworks were built for.

---

## 12) Where this fits in the rest of the chain

Subagent orchestration sits in a specific spot:

```
PRD            -> what users need
Why Graph      -> how intent maps to surfaces and code
Contracts      -> intent at the file head
Code anchors   -> intent at the block
Semantic logs  -> what happened at runtime, in the same words   (Why1st.md §11.1)
Tests + UI     -> what the system actually does                 (Why1st.md §11.2)
Subagents      -> who does which part of the work               (Why1st.md §11.3, this doc)
```

Each layer has one job. Subagent orchestration is the only layer that is not about the *system* being built — it is about the *agent doing the building*. That is why it is project-local, not part of the canonical chain. The chain describes the artifact; this guide describes the workshop.

The chain works regardless of whether the lead delegates well. But on a project large enough to need the chain, the lead's context budget is the bottleneck — and how the lead uses subagents is the difference between a chain that scales and a chain that gets abandoned because every session feels like solo crunch.

The question is not *whether* to use subagents. It is *whether the lead's default is dispatch or solo.* On strong agents, that default is the regression. This guide is the bias toward fixing it.
