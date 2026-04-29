# Handoff to Claude Opus 4.7 — Agent1st Protocol v6

## 0) Mission

You are reviewing and preparing **Agent1st Protocol v6**.

Agent1st is not a generic prompt-engineering repo. It is a protocol for software development where AI agents are primary implementers and humans provide intent, constraints, and final acceptance. The current `AGENTS.md` explicitly defines the human-agent split: human provides intent, constraints, and acceptance criteria; agent chooses the route, executes, and proves the result. It also requires acceptance criteria before work, evidence before completion, and escalation when risk exceeds the delegation boundary. ([GitHub][1])

Your job is **not** to make `AGENTS.md` longer because new models exist. Your job is to decide what, if anything, v6 should change now that GPT-5.5 and Claude Opus 4.7 are the main frontier-agent targets.

Recommended v6 direction:

> **Strong agents need clearer contracts, not longer instructions.**

The expected v6 shape is:

```text
v6 = compact AGENTS.md refinement + WHY validator MVP + evolution note
```

Not:

```text
v6 = GPT-5.5-specific AGENTS.md rewrite
```

## 1) Core project spirit

Agent1st’s central idea is that `AGENTS.md` should define the conditions in which a strong agent works better, not prescribe step-by-step work. `DESIGN.md` frames the right level as roles, rights, quality boundaries, friction handling, attention discipline, and handoff quality — closer to harness/workplace design than to a task list. ([GitHub][2])

The strongest design constraint is the **Delta-Layer Principle**:

> `AGENTS.md` should be a delta-layer, not a second system prompt.

A rule can be correct, official, and important, yet still be a bad addition if the model or harness already covers it, if it adds no new signal, if it creates contradiction risk, or if it spends context budget without earning its place. Before changing `AGENTS.md`, apply the delta-layer test exactly. ([GitHub][2])

Anti-micromanagement is not decorative. `DESIGN.md` says this is central: the human provides intent, constraints, approvals, and acceptance; the agent chooses route, executes, and proves. If you turn Agent1st into “human controls, agent follows process,” you lose the protocol. ([GitHub][2])

## 2) Historical context from v1–v4

Use the uploaded historical versions as evolution evidence, not as text to blindly restore.

v1 was still closer to a broad assistant-workflow file: CDD, role contract, educational-by-default behavior, attention engineering, semantic hygiene, right to disagree, semantic logging, harness, ergonomics reflection, and session start/end protocol. It carried useful primitives, but it was less sharply minimal. 

v2 added a stronger agent operating loop — `Explore -> Execute -> Reflect` — and fresh-eye onboarding, making the agent less passive and more responsible for route selection and validation. 

v3 was the major maturity jump: it introduced the Core / Operations split, `Done Is Not a Mood`, stronger proof language, `Do Not Stop at the First Weak Signal`, and the first clearly compressed Agent1st shape. 

v4 is the current minimal-protocol ancestor: role boundaries, evidence boundaries, unsupervised-risk escalation, anti-overexploration in Attention Engineering, `Delegation Design`, and `Continuity` replacing fragile “session end” assumptions. 

The live repository has continued to refine v4/v5-era wording. Current `AGENTS.md` has 11 sections and adds a strong Continuity hook: “if your handoff disappears when the session ends, it doesn't exist.” It also keeps the `Agent1st Mode ON` handshake. ([GitHub][1])

## 3) v5 / WHY-layer context

v5 did not need to rewrite `AGENTS.md`; its real addition was the WHY layer. The WHY layer exists because, in agent-first work, intent must live in the repo rather than in a human’s head. It explicitly addresses drift between product intent, implementation, rationale, and coupling. ([GitHub][3])

The WHY layer has four paired artifacts:

```text
PRD                 = product truth
Why Graph           = navigation truth
Contracts/anchors   = local truth
Validators          = consistency truth
```

The important invariant is that PRD, graph, anchors, and validators stay paired. Validators are not optional long-term decoration; they catch the moment PRD, graph, and code diverge. ([GitHub][3])

The workflow shift is:

```text
without WHY: open mentioned file -> edit nearest plausible code -> claim done
with WHY:    PRD -> Why Graph -> contracts/anchors -> code -> validate
```

For cross-cutting or intent-changing work, graph/contracts should move before implementation; for local edits inside a mapped feature, they can move with code in the same change set. Validators should run before claiming done when they exist; if they do not exist, building one is the first serious trust-building step. ([GitHub][3])

Important: v5.1 external reviews already noted that validator tooling and pre-merge consistency checks are v6-relevant. `EVOLUTION.md` also records that an `EVIDENCED_BY` relation was proposed but deferred to v6 because it risks scope creep if the relation vocabulary grows past the “small and stable” target. ([GitHub][4])

## 4) Model-era input: GPT-5.5

GPT-5.5 guidance strongly supports the existing Agent1st direction. OpenAI recommends shorter, outcome-first prompts rather than process-heavy prompt stacks. It says GPT-5.5 works best when prompts define the outcome, constraints, available evidence, and final answer shape while leaving room for the model to choose an efficient solution path. It also warns against carrying over every instruction from old prompt stacks because legacy over-specification can add noise, narrow search, or produce mechanical answers. ([OpenAI Developers][5])

The GPT-5.5 migration guide says to start with the smallest prompt that preserves the product contract, then tune reasoning effort, verbosity, tool descriptions, and output format against representative examples. It also identifies GPT-5.5 as strong for coding, tool-heavy agents, grounded assistants, long-context retrieval, and product-spec-to-plan workflows. ([OpenAI Developers][6])

The most relevant GPT-5.5 pattern for Agent1st v6 is **stopping conditions**. OpenAI recommends defining target outcome, success criteria, constraints, and context; using decision rules rather than unnecessary `ALWAYS` / `NEVER`; adding explicit stopping conditions; and using the minimum evidence sufficient to answer correctly. ([OpenAI Developers][5])

OpenAI also recommends concrete validation commands for coding agents: targeted tests, type/lint checks, build checks, smoke tests, or an explanation of why validation could not be run and what the next best check is. This matches Agent1st’s “Done Is Not a Mood” and “Harness” stance. ([OpenAI Developers][5])

Implication for v6:

```text
Do not add GPT-5.5 API knobs to AGENTS.md.
Do add, at most, a compact model-agnostic clarification around task contracts and sufficient evidence.
```

## 5) Model-era input: Claude Opus 4.7

Claude Opus 4.7 is described by Anthropic as highly autonomous and strong for long-horizon agentic work, knowledge work, vision tasks, and memory tasks. The migration guide highlights API/harness changes: adaptive thinking replaces older extended-thinking configuration, non-default sampling parameters are removed, thinking content is omitted by default unless explicitly opted in, token counting changes, and prompt/harness review is recommended. ([Claude Platform][7])

Relevant behavior changes:

```text
- Opus 4.7 follows instructions more literally.
- It does not silently generalize from one item to another.
- It does not infer requests the user did not make.
- It tends to spawn fewer subagents by default.
- It tends to use tools less often by default.
- Effort level matters more; xhigh is recommended for most coding/agentic use cases.
```

Anthropic’s guide says `xhigh` is the best setting for most coding and agentic use cases; it also says lower effort can scope too narrowly, and tool/subagent usage can be steered through prompts or effort settings. ([Claude Platform][7])

Implication for v6:

```text
Do not add Claude API parameters to AGENTS.md.
Do make delegation contracts sharper if a compact wording passes delta-layer review.
Do make task contracts explicit enough that a literal model can act correctly without guessing hidden intent.
```

## 6) Recommended v6 thesis

Treat v6 as a **contract-and-signal release**, not a model-specific release.

Recommended tagline:

```text
Strong agents need clearer contracts, not longer instructions.
```

Recommended v6 pillars:

```text
1. Outcome Contract
   Make the work contract explicit enough to act:
   outcome, constraints, acceptance, evidence target, side-effect boundary.

2. Signal Discipline
   Keep the existing anti-weak-signal rule, but add the symmetric stop rule:
   do not stop at weak evidence; do stop at sufficient evidence.

3. WHY Validators
   Make the WHY layer mechanically checkable.
   This is the most valuable v6 deliverable outside AGENTS.md.
```

## 7) Candidate `AGENTS.md` change A — Role Contract

Do not add a new section. If accepted, fold the change into section 1.

Current section already says human provides intent, constraints, and acceptance criteria; agent chooses route and proves result; evidence and acceptance criteria must exist. That means the v6 patch must be small and non-redundant. ([GitHub][1])

Candidate replacement for the first paragraph / autonomy bullets:

```md
Human provides outcome, constraints, acceptance criteria, and side-effect boundaries.
Agent chooses the route, executes, and proves the result.
Strong agents should not be micromanaged.

Human presence ranges from tight pairing to full delegation.
At any autonomy level:
- the task contract must be clear enough to act
- acceptance criteria and evidence target must exist before work begins
- evidence must exist before claiming completion
- if a missing detail is non-material, state the assumption and continue
- if a missing detail changes risk, scope, route, or side effects, ask narrowly or escalate
```

Why this may belong:

```text
- GPT-5.5 guidance favors outcome-first prompts with success criteria, constraints, evidence, and output/answer shape.
- Opus 4.7 literalism makes hidden assumptions more dangerous.
- This remains model-agnostic and reinforces the human-agent contract.
```

Risk:

```text
- May duplicate existing CDD / Role Contract wording.
- If it increases length without changing behavior, reject or compress.
```

Preferred Opus action:

```text
Apply only if you can keep section 1 compact.
Otherwise record as rejected/deferred in EVOLUTION.md.
```

## 8) Candidate `AGENTS.md` change B — replace section 8

This is the strongest AGENTS.md candidate.

Current section 8 is `Do Not Stop at the First Weak Signal`. It protects against early stopping, but current frontier agents also fail through ritual over-search and over-delegation. GPT-5.5 guidance explicitly supports stopping when sufficient evidence exists, and current `AGENTS.md` already has an anti-overexploration line in Attention Engineering. ([GitHub][1])

Replace section 8 with:

```md
### 8) Signal Discipline

Do not stop at a weak signal.
Do stop at a sufficient signal.

- do not confuse missing data with absent data
- fetch missing context before guessing
- if the first result is weak, do one better check or try one alternative path before stopping
- if the core request is answered with adequate evidence, stop; more checking is not automatically more truth

WHY:
- many failures come from early stopping or ritual over-checking, not lack of intelligence
- evidence is useful when it can change the decision

IF MISSING:
- weak evidence gets mistaken for final truth
- strong evidence gets buried under needless exploration
```

Why this belongs:

```text
- It preserves the v3/v4 anti-weak-signal insight.
- It adds the missing symmetric stop rule.
- It aligns with GPT-5.5 stopping-condition guidance without mentioning GPT-5.5.
- It is short enough for minimal AGENTS.md.
```

Preferred Opus action:

```text
Accept unless you find a shorter wording with equal force.
```

## 9) Candidate `AGENTS.md` change C — Delegation Design

Current section 9 already says: define deliverable, include acceptance criteria, leave room for blockers/friction/alternatives, return evidence, agree shared state for parallel work, and resolve contradictions by evidence weight. ([GitHub][1])

Opus 4.7-specific pressure: Anthropic says Opus 4.7 tends to spawn fewer subagents and use tools less by default, but this is steerable. The Agent1st-relevant version is not “spawn more subagents”; it is “delegation must specify what truth is being optimized for.” ([Claude Platform][7])

Candidate one-line addition under “When delegating to subagents or peers”:

```md
- for discovery or review work, state whether the job optimizes for coverage, precision, speed, or evidence depth
```

Why this may belong:

```text
- It improves delegation contracts across models.
- It prevents silent filtering: a subagent asked for “review” may optimize for precision and omit lower-confidence findings when the parent needed coverage.
- It is model-agnostic and operational.
```

Risk:

```text
- Section 9 is already adequate.
- Could be more suitable for a companion handoff template than core AGENTS.md.
```

Preferred Opus action:

```text
Accept only if section 9 remains compact.
Otherwise place it in docs/handoffs/TEMPLATE.md or EVOLUTION.md as v6 guidance.
```

## 10) Main v6 implementation outside `AGENTS.md`: WHY validator MVP

This is the highest-value v6 work.

The WHY layer already states that validators are “consistency truth” and catch PRD/graph/code divergence. It also says that if no validator exists yet, building one is the first thing to do before the WHY layer can be trusted. ([GitHub][3])

The current `why-graph.xml` explicitly says there are no validators yet and that the dogfooded validator set is a follow-up. It also says the current repo has no `START_*` markers because it is mostly documentation, so the graph is a skeleton/example rather than a fully enforced chain. ([GitHub][8])

Validator MVP target:

```text
Create a deterministic script that validates the parts of the WHY graph that can be validated now,
and degrades honestly where the repo has teaching-only artifacts.
```

Suggested path:

```text
scripts/validate-why.py
```

Suggested command:

```bash
python scripts/validate-why.py
```

Minimum checks:

```text
1. docs/why-graph.xml parses as XML.
2. All node IDs are unique.
3. All REL TYPE values are in the documented relation vocabulary.
4. All REL TARGET endpoints resolve to existing node IDs.
5. TARGET style is consistent:
   - either all bare IDs
   - or all family-qualified targets
   - no mixing inside one graph
6. Deprecated nodes follow documented retirement pattern.
7. If ANCHOR elements exist:
   - COORD has path#anchor shape
   - path exists
   - anchor name matches COORD suffix
   - target file contains matching START_* marker
8. If no ANCHOR elements exist:
   - report a warning, not a failure, because current Agent1st dogfood is docs-only.
```

Relation vocabulary should follow `why-graph-principles.md`: `COVERS`, `EXPOSED_AS`, `IMPLEMENTED_BY`, `SURFACED_BY`, `HOSTED_BY`, `DELEGATES_TO`, `CALLED_BY`, `READS`, `WRITES`, `QUERIES`, `BACKED_BY`, `DEPENDS_ON`, `IMPACTS`, `WILL_TOUCH`, and `WILL_CREATE`. The same document says relation types should remain small and stable, and target syntax should not mix bare and family-qualified forms in the same graph. ([GitHub][9])

Anchor rules should follow `why-graph-principles.md` and `why-contracts-v1.md`: `<ANCHOR NAME="..." COORD="path#ANCHOR"/>`, no line numbers, anchor names must match real `START_*` markers, and anchors should wrap meaningful code regions. ([GitHub][9])

Validation expectations already say the minimum valuable check is that every graph anchor resolves to a real `START_*` marker in a real file; additional checks include implementation edges for features, anchors for implemented modules/UI/API nodes, consistent ID prefixes, and no duplicate IDs. ([GitHub][9])

Expected pass signal:

```text
WHY validation passed: nodes=N relations=M anchors=K warnings=W
```

Expected failure format, Agent1st style:

```text
Problem: REL target FEATURE:FEAT-ASK does not resolve to any node ID.
Impact: Agent may follow a graph edge that points nowhere.
Smallest fix:
- add the missing node, or
- update the REL TARGET to an existing node, or
- remove the stale relation.
```

Expected warning example:

```text
Warning: No ANCHOR elements found.
Impact: Graph currently validates as a documentation-level map, not a graph↔code contract.
Smallest fix:
- acceptable for the Agent1st docs-only dogfood graph
- add anchors when adopting this layer in a code repo
```

Important: do not make the validator more ambitious than the graph. This is a mechanical drift detector, not a semantic proof system.

## 11) EVIDENCED_BY relation decision

`EVIDENCED_BY` was proposed in v5.1 and deferred to v6. Evaluate it, but do not add it by default. ([GitHub][4])

Decision rule:

```text
Accept EVIDENCED_BY only if:
- it creates a validator-checkable link,
- it does not duplicate ACCEPT/CHECK blocks,
- it does not turn the graph into a changelog or test registry,
- it improves agent navigation enough to justify vocabulary growth.
```

Likely recommendation:

```text
Reject/defer for v6.
Reason: validator MVP already gives evidence teeth without expanding relation vocabulary.
```

Possible compromise:

```text
Add EVIDENCE_REF as optional metadata inside ACCEPT/CHECK blocks, not a graph relation.
```

But only do this if a real validation use case exists in the repo.

## 12) Documents to update for v6

Minimum expected files:

```text
AGENTS.md
docs/EVOLUTION.md
scripts/validate-why.py
possibly docs/Why1st.md
possibly docs/why-graph-principles.md
possibly docs/PRD.md
```

`AGENTS.md` should receive at most small edits:

```text
- likely: section 8 replacement with Signal Discipline
- maybe: Role Contract wording compression
- maybe: one Delegation Design line
```

`EVOLUTION.md` should record:

```text
- v6 scope
- why this is not a GPT-5.5 edition
- accepted AGENTS.md edits and why
- rejected model-specific additions and why
- validator MVP as the main v6 mechanical improvement
- EVIDENCED_BY decision
```

`Why1st.md` may need a small update if validator MVP lands:

```text
- replace “if validators exist” / “first thing to build” language with the actual command
- preserve the idea that validators are consistency truth, not correctness proofs
```

`why-graph-principles.md` may need a small update:

```text
- add the validator command
- document what current MVP checks
- state which warnings are acceptable for docs-only graphs
```

`PRD.md` may need a v6 DoD update:

```text
- v6 DoD includes Signal Discipline update if accepted
- v6 DoD includes deterministic WHY validator command
```

## 13) Things not to add to `AGENTS.md`

Do not add:

```text
- GPT-5.5 reasoning.effort
- GPT-5.5 text.verbosity
- OpenAI Responses API phase handling
- previous_response_id
- prompt caching
- hosted tools
- Claude adaptive thinking settings
- Claude effort settings such as high/xhigh/max
- Claude task_budget
- temperature/top_p/top_k advice
- model-specific tool-use heuristics
- frontend style rules
- generic “avoid overengineering” rules
- “only make requested changes” rules
```

Reason: those belong to model/API/harness configuration, not to the portable Agent1st behavior layer. OpenAI frames reasoning effort, verbosity, tool descriptions, output format, prompt caching, hosted tools, compaction, and phase handling as model/API workflow concerns, not as portable protocol text. ([OpenAI Developers][6])

Anthropic likewise frames Opus 4.7 migration around API/harness changes: adaptive thinking, effort, sampling-parameter removal, token counting, thinking display, task budgets, prompt/harness review, tool usage, and subagent behavior. ([Claude Platform][7])

If a model-specific note is useful, put it in `EVOLUTION.md`, `FOUNDATIONS.md`, or a harness-specific bridge file such as `CLAUDE.md`, not in minimal `AGENTS.md`.

## 14) Acceptance criteria for v6

v6 is acceptable when all are true:

```text
1. AGENTS.md remains minimal and model-agnostic.
2. Every AGENTS.md change passes the delta-layer test.
3. No model/API parameter is added to AGENTS.md.
4. Signal Discipline either replaces section 8 or is explicitly rejected with rationale.
5. Role Contract / Delegation changes are either compactly accepted or explicitly rejected/deferred.
6. WHY validator MVP exists and runs deterministically.
7. Validator output is grep-friendly and uses Agent1st CDD-style problem reporting.
8. docs/EVOLUTION.md records accepted, rejected, and deferred decisions.
9. docs/Why1st.md / why-graph-principles.md mention the validator command if the script lands.
10. Final completion claim includes evidence: command run, pass/fail result, and known limitations.
```

## 15) Suggested final validation commands

Use whatever exists after implementation, but target this minimum:

```bash
python scripts/validate-why.py
```

If the repo has no test harness, that is acceptable for a docs/protocol repo, but say so explicitly.

If you add Python:

```bash
python -m py_compile scripts/validate-why.py
python scripts/validate-why.py
```

If markdown linting or formatting exists, run it. If not, do not invent heavy tooling just for v6.

## 16) Expected final report shape

Use this structure in your final handoff:

```md
## Objective
Prepare Agent1st v6 as a compact contract/signal/validator release.

## Changes made
- AGENTS.md: ...
- scripts/validate-why.py: ...
- docs/EVOLUTION.md: ...
- other docs: ...

## Key decisions
- Accepted: ...
- Rejected: ...
- Deferred: ...

## Evidence
- Command: ...
- Result: ...

## Known limitations
- ...

## Next deterministic steps
- ...
```

## 17) Primary risk

The biggest risk is prompt-bloat disguised as modernization.

GPT-5.5 and Opus 4.7 do not justify a longer `AGENTS.md`. They justify a clearer contract, better stopping discipline, and deterministic validators.

If you feel tempted to add more model-specific prompt guidance, apply this check:

```text
Does this belong to the human-agent operating contract?
Or does it belong to model settings, harness behavior, docs, examples, or evals?
```

If it is not the operating contract, keep it out of `AGENTS.md`.

Final working thesis:

```text
v6 should make Agent1st more mechanically trustworthy, not more verbose.
```

[1]: https://github.com/applerom/agent1st/blob/main/AGENTS.md "agent1st/AGENTS.md at main · applerom/agent1st · GitHub"
[2]: https://github.com/applerom/agent1st/blob/main/docs/DESIGN.md "agent1st/docs/DESIGN.md at main · applerom/agent1st · GitHub"
[3]: https://github.com/applerom/agent1st/blob/main/docs/Why1st.md "agent1st/docs/Why1st.md at main · applerom/agent1st · GitHub"
[4]: https://github.com/applerom/agent1st/blob/main/docs/EVOLUTION.md "agent1st/docs/EVOLUTION.md at main · applerom/agent1st · GitHub"
[5]: https://developers.openai.com/api/docs/guides/prompt-guidance "Prompt guidance | OpenAI API"
[6]: https://developers.openai.com/api/docs/guides/latest-model "Using GPT-5.5 | OpenAI API"
[7]: https://platform.claude.com/docs/en/about-claude/models/migration-guide "Migration guide - Claude API Docs"
[8]: https://github.com/applerom/agent1st/blob/main/docs/why-graph.xml "agent1st/docs/why-graph.xml at main · applerom/agent1st · GitHub"
[9]: https://github.com/applerom/agent1st/blob/main/docs/why-graph-principles.md "agent1st/docs/why-graph-principles.md at main · applerom/agent1st · GitHub"
