---
name: terraform-agent1st
description: "Use for Terraform work where AI agents are the primary authors and operators: writing, refactoring, reviewing, planning, applying. A behavior layer that reframes standard Terraform practice around agent cost structure - cheap writing, scarce attention, irreversible apply. Complements a baseline Terraform reference skill; does not replace it."
metadata:
  scope: terraform
  style: behavior layer
  portability: reusable
  status: experimental
---

# Terraform, Agent1st

Standard Terraform best practice was written for human teams with human costs:
code is expensive to write, abstraction saves labor, review capacity is scarce.
Agents invert the cost structure:

- writing HCL is nearly free
- attention and context are the scarce resources
- `apply` is the only step that cannot be taken back

Every rule below derives from these three inversions. Where popular human
practice conflicts with them, this skill says so explicitly.

This skill is a behavior layer, never a syntax authority: pair it with a
baseline Terraform reference for syntax-level and architecture-level guidance,
and let local project policy override both when they conflict.

The derivation behind these rules — including the transformer mechanics —
lives in [`why-terraform-skill.md`](why-terraform-skill.md) next to this file.
Read it once to understand the rules; do not reload it at every use.

## 1) The Reversibility Boundary

Infra work splits by reversibility, not by effort.

- `fmt`, `validate`, lint, `plan`: agent territory at any autonomy level
- `apply`: crosses the reversibility boundary; requires explicit delegation per stack and environment
- destroy and replace lines in a plan escalate even when apply is delegated
- `-target`, `import`, `state mv|rm|push`, manual state edits: surgery — escalation-gated, never routine
- never leave a stack half-applied without a durable handoff: what applied, what did not, exact next command

WHY:
- code edits are reversible; state changes are not; the role contract follows that line

IF MISSING:
- an agent "fixing" infra destroys in seconds what took months to fill

## 2) The Evidence Ladder

Each completion claim names its rung. Exit code 0 is not evidence; the diff content is.

1. `fmt` + `validate` — syntax-true
2. lint + security scan — rule-true
3. `plan` against refreshed state — intent-true
4. `apply` + post-check — real

- before running plan, state the expected diff: what adds, what changes, what destroys
- a plan matching the expectation is evidence; a mismatch is stop-and-explain, not retry-until-quiet
- save the plan (`-out`, then `terraform show`) and cite resource addresses, not impressions
- before editing a stack you did not create this session, run plan first: code is not reality, and a "no changes" plan is the sync evidence

The expected diff is a stated artifact, not a thought:

```text
expected: ~ aws_iam_role.app (permissions boundary only); nothing added, destroyed, or replaced
plan:     1 to change, 0 to add, 0 to destroy — match, proceed
mismatch: the plan shows -/+ aws_db_instance.orders — stop, quote the line, escalate (rule 1)
```

WHY:
- HCL is intent; only state operations touch truth

IF MISSING:
- "I wrote the module" ships as "the infrastructure is ready"

## 3) DRY Has a Different Price

DRY saves writing labor. You do not pay writing labor — you pay attention per indirection hop.

- abstract only behind a contract: module name + inputs + outputs must carry full meaning without opening the source
- module depth: one level by default, composing in the root; a deeper level must pay with a full contract at its seam — depth is a refactor signal, not a law
- repetition is fine when the copies fit on one screen and shared names keep them greppable
- the real repetition risk for you is edit drift between copies — counter it with semantic names and grep, not with deeper variable chains
- keep effective values visible at the decision point; a value reachable only through default -> tfvars -> local -> module input is invisible
- do not introduce a variable for what never varies

WHY:
- each indirection hop is a context fetch; buried values lose to nearest values

IF MISSING:
- the agent edits the wrong layer; the effective configuration exists nowhere readable

## 4) Names Are State

Terraform names are load-bearing twice: they guide attention, and they are state
addresses where a rename means destroy-and-recreate unless a `moved` block says otherwise.

- `for_each` with stable semantic keys over `count` wherever identity matters
- never `this`, `main`, or `default` as local names — the registry-module habit produces zero-meaning addresses in plans, state, and logs
- keep one concept under one name across HCL identifiers, cloud tags, outputs, and docs
- treat a rename as a state operation: write the `moved` block, or accept recreate consciously

WHY:
- plans, state, and logs are read by agents whose attention follows names

IF MISSING:
- the plan says `aws_security_group.this[0] must be replaced` and nothing says what that is

## 5) No Hidden Context

Same code plus invisible CLI state equals different infrastructure.

- prefer directory-per-environment over CLI workspaces; where CLI workspaces exist, print `terraform workspace show` before any plan or apply
- HCP Terraform / Enterprise workspaces are a different concept: a governance boundary, not CLI session state — follow the project's baseline there, and name the target (org, project, workspace) next to every plan and apply
- no `*.auto.tfvars` magic; pass `-var-file` explicitly and record the exact command next to the plan it produced
- providers are configured in roots, never inside shared modules
- pin Terraform and provider versions; an unpinned version is hidden context too

WHY:
- critical context must sit next to the decision point; agents inherit shells they did not configure

IF MISSING:
- the right plan applies to the wrong environment

## 6) Invariants in Code, Not in Prose

Comments ask; expressions enforce. Checks are cheap for you to write — generate them liberally:

- `validation` blocks on variables where misuse is plausible
- `precondition` / `postcondition` for cross-resource constraints (no `0.0.0.0/0` on management ports)
- `check` blocks for environment truths worth asserting on every plan
- `lifecycle { prevent_destroy = true }` on stateful keystones: databases, state buckets, key material
- comment only what cannot be encoded, on the line it constrains

WHY:
- encoded constraints survive context loss and fire exactly when attention fails
- humans underuse these blocks because writing them was tedious; that excuse is gone

IF MISSING:
- the invariant lives in a README that never got loaded into context

## 7) Provider Schema Honesty

Your training data contains every historical version of every provider, blended.

- treat remembered argument names as hypotheses, not knowledge; verify unfamiliar resources against the pinned provider docs before authoring
- validate early; a validate error means "check the docs", not "guess a synonym"
- watch for outdated idiom that still validates: old-major patterns (inline rules vs standalone rule resources) pass validate and then fight real infrastructure as drift

WHY:
- the failure mode is not syntax errors; it is fluent 2021-style code with 2021 bugs

IF MISSING:
- hallucinated or deprecated arguments cost a plan-apply cycle each — or silently create drift

## 8) Layout for Reading

You read file-by-file. Group roots by component, not by syntax kind.

- a resource and its security groups, IAM, and alarms live together (`network.tf`, `database.tf`), so one question costs one read
- `variables.tf` / `outputs.tf` stay split — they are the module's contract surface
- give each root and module a file-head contract: PURPOSE, SCOPE, INVARIANTS, and BLAST_RADIUS — what this state owns and what an apply here can break
- 200-300 lines for a frequently edited file is a refactor signal, not a law

WHY:
- component cohesion turns "what guards this database" into one read instead of five

IF MISSING:
- every navigation question fans out across main/variables/locals/data

## 9) Refactor Economics

Tidy-looking HCL is not free to reach after the fact.

- a refactor with zero behavior change still churns state addresses; tidying Terraform that plans clean needs a reason, not taste
- recreate over migrate while state is young: no meaningful data, no external consumers
- migration machinery (`moved` blocks, compatibility shims) only when continuity materially matters — then document why
- never mix refactor noise and behavior change in one plan

WHY:
- the reviewable diff is the plan; rename noise buries the one destroy that matters

IF MISSING:
- a 40-line plan of moves hides the single `-/+` that takes production down

## 10) Secrets Are Names to You

You will never see secret values — only references. Then the reference must carry all the meaning.

- secret names and paths follow the same semantic hygiene as code names
- `sensitive = true` on variables and outputs; scan plan output before quoting it anywhere durable
- verify secrets by behavior (post-check), never by reading values into context

WHY:
- under blindness, the name is the only signal available

IF MISSING:
- `key2-final-new` gets wired into production because nothing said what it was

## Inverted Practices

| Standard practice | What inverts for agents |
|---|---|
| DRY everything into modules | indirection now costs more than repetition |
| `this` for module singletons | zero-meaning addresses in plans, state, logs |
| CLI workspaces for environments | invisible session state decides what gets destroyed |
| constraints in comments and wikis | prose is skippable; validation blocks fire |
| tidy refactors any time | every address change is a state operation |
| review the HCL | review the plan; HCL is intent, the plan is truth |

## How to Apply

1. find the reversibility boundary for the task: what is plan, what is apply, who approved apply
2. state the expected diff before running plan
3. keep one stack and one objective per loop
4. if tooling or provider friction reduced your effectiveness, say so in the handoff: Problem (1 line), Impact (1 line), Smallest fix (1-3 bullets)
5. local policy overrides this skill; a baseline Terraform reference covers what this skill leaves out

Status: experimental — part of the Agent1st experiments track. Protocol,
measurements, and report path:
[`docs/experiments/terraform-agent1st.md`](https://github.com/applerom/agent1st/blob/main/docs/experiments/terraform-agent1st.md).
