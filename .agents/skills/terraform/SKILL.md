---
name: terraform
description: "Use for any Terraform or OpenTofu work: writing, refactoring, reviewing, planning, applying, module and state design, environments, secrets, CI/CD. A complete skill written for AI agents as the primary authors and operators - standard practice re-derived under agent costs: writing is cheap, attention is scarce, apply is irreversible. Self-sufficient; local project policy overrides it."
metadata:
  scope: terraform
  style: complete reference + behavior
  portability: reusable
  status: experimental
---

# Terraform

Standard Terraform best practice was written for human teams with human costs:
code is expensive to write, abstraction saves labor, review capacity is scarce.
For an agent the costs invert:

- writing HCL is nearly free
- attention and context are the scarce resources
- `apply` is the only step that cannot be taken back

This skill is a complete operating guide under those costs. It carries both
standard practice — cross-checked against current HashiCorp, AWS, Google, and
Azure guidance — and the behavior rules the cost inversion forces. Where
popular human practice conflicts with agent costs, it says so explicitly.
Local project policy — naming schemes, approval rules, environment rules —
overrides this skill wherever they conflict.

Use it for authoring, review, refactoring, plan/apply operations, module and
state design, environments, and Terraform CI/CD. Do not load it for raw syntax
questions or provider API lookup — that is model knowledge and provider docs.
When a provider can manage the target system, prefer codifying the change in
Terraform over manual portal or UI configuration; a manual exception gets
documented with its reason.

The derivation behind these rules — including the transformer mechanics —
lives in [`why-terraform-skill.md`](why-terraform-skill.md) next to this file.
Read it once to understand the rules; do not reload it at every use.

## 1) The Reversibility Boundary

Infra work splits by reversibility, not by effort.

- `fmt`, `validate`, lint, `plan`: agent territory at any autonomy level
- `apply`: crosses the reversibility boundary; requires explicit delegation per stack and environment
- destroy and replace lines in a plan escalate even when apply is delegated
- `destroy` — full or `-target` — only after `terraform plan -destroy` with every deleted resource listed, including implicit dependents; never auto-approved
- `-target`, `import`, `state mv|rm|push`, manual state edits: surgery — escalation-gated, never routine
- never leave a stack half-applied without a durable handoff: what applied, what did not, exact next command

WHY:
- code edits are reversible; state changes are not; the role contract follows that line

IF MISSING:
- an agent "fixing" infra destroys in seconds what took months to fill

## 2) The Evidence Ladder

Each completion claim names its rung. Exit code 0 is not evidence; the diff content is.

1. `fmt` + `validate` — syntax-true
2. `tflint` + security scan (`trivy` or `checkov`) — rule-true
3. `plan` against refreshed state — intent-true
4. `apply` + post-check — real

- before running plan, state the expected diff: what adds, what changes, what destroys
- a plan matching the expectation is evidence; a mismatch is stop-and-explain, not retry-until-quiet — and not quietly revising the expectation until it matches the plan
- save the plan (`-out`, then `terraform show`) and cite resource addresses, not impressions
- when the plan is too long to hold in attention, stop eyeballing: run `terraform show -json` on the saved plan and query every delete and replace action before judging the match
- apply consumes the reviewed plan artifact — in CI, the apply stage takes the saved plan file from the plan stage, it does not re-plan
- before editing a stack you did not create this session, run plan first: code is not reality, and a "no changes" plan is the sync evidence
- native `terraform test` (1.6+) for reusable modules and logic-heavy stacks; mock providers (1.7+) keep unit runs cheap; integration tests only when native tests are not enough; do not force brittle tests while the main risk is still architecture or access
- prefer the local Terraform binary already on PATH; install pinned versions in CI where runners are ephemeral

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

## 3) Repository Layout

You read file-by-file. Lay the repository out so one question costs one read.

- module-oriented repo: `modules/<module-name>/`; infrastructure repo: `modules/` plus `live/<env-or-account>/<stack>/` or `environments/<env>/` — pick one pattern and keep it consistent
- standard files: `main.tf`, `variables.tf`, `outputs.tf`, `providers.tf`, `terraform.tf` (current HashiCorp convention; `versions.tf` is the established equivalent — one per repo), `backend.tf`; `locals.tf` and `data.tf` when they earn their keep
- past a few dozen resources, group files by component, not by syntax kind: a resource and its security groups, IAM, and alarms live together (`network.tf`, `database.tf`)
- `variables.tf` / `outputs.tf` stay split — they are the module's contract surface
- give each root and module a file-head contract: PURPOSE, SCOPE, INVARIANTS, and BLAST_RADIUS — what this state owns and what an apply here can break
- 200-300 lines for a frequently edited file is a refactor signal, not a law
- every reusable module eventually ships a `README.md` with generated inputs/outputs (`terraform-docs`); `examples/` double as documentation and test fixtures

WHY:
- component cohesion turns "what guards this database" into one read instead of five

IF MISSING:
- every navigation question fans out across main/variables/locals/data

## 4) Names Are State

Terraform names are load-bearing twice: they guide attention, and they are state
addresses where a rename means destroy-and-recreate unless a `moved` block says otherwise.

- descriptive snake_case nouns; never repeat the resource type in the name; units in numeric names (`ram_size_gb`); positive booleans (`enable_external_access`)
- prefer a semantic local name even for singletons (`tfstate`, `landing_zone` — not `state`, `main`); `this` only where the module name already carries the full meaning and the plan line stays readable
- `for_each` with stable semantic keys wherever identity matters; `count` only for on/off toggles and fixed replication — never a list index as long-lived identity: removing a middle element reshuffles every address after it
- keep one concept under one name across HCL identifiers, cloud tags, outputs, and docs; qualify ambiguous words
- treat a rename as a state operation: write the `moved` block, or accept recreate consciously; in shared modules, retain historical `moved` blocks — removing one is a breaking change

WHY:
- plans, state, and logs are read by agents whose attention follows names — at the moment of maximum risk

IF MISSING:
- the plan says `aws_security_group.this[0] must be replaced` and nothing says what that is

## 5) Modules and the Price of DRY

DRY saves writing labor. You do not pay writing labor — you pay attention per indirection hop.

- abstract only behind a contract: module name + inputs + outputs must carry full meaning without opening the source
- no thin wrappers: if the module cannot be named anything but the resource type it wraps, use the resource directly
- consuming a maintained registry or vendor-verified module is buying a contract, not hiding one — judge it by its interface, version pin, examples, and plan diff, the same surface you review for any module
- module depth: one level by default, composing in the root; a deeper level must pay with a full contract at its seam — depth is a refactor signal, not a law
- providers are configured in roots, never inside shared modules; shared modules declare `required_providers` only
- repetition is fine when the copies fit on one screen and shared names keep them greppable; the real risk is edit drift between copies — counter it with semantic names and grep, not with deeper variable chains
- keep effective values visible at the decision point; a value reachable only through default -> tfvars -> local -> module input is invisible
- parameterize only what actually varies; do not introduce a variable for what never varies, and do not make consumers pass many knobs when few meaningfully vary

WHY:
- each indirection hop is a context fetch; buried values lose to nearest values

IF MISSING:
- the agent edits the wrong layer; the effective configuration exists nowhere readable

## 6) State, Backends, Environments

Same code plus invisible CLI state equals different infrastructure.

- backend choice and state split are architecture decisions: split by ownership boundary, lifecycle boundary, or blast radius — not folder aesthetics; a state approaching ~100 resources or visibly slow plans is a split signal, not a law
- default root stacks to a remote backend where one exists; the backend bootstrap stack is the exception — local state first, never depending on its own remote backend for the first run; design state keys so later migration is straightforward
- S3 backend: `use_lockfile = true` (Terraform 1.10+) — DynamoDB lock tables are deprecated; every state store gets versioning, encryption at rest, and restricted access
- one environment = one directory with its own backend and identity; CLI workspaces are not environment isolation — same backend, same credentials, invisible session state (this is HashiCorp's own current position); where CLI workspaces exist anyway, print `terraform workspace show` before any plan or apply
- HCP Terraform / Enterprise workspaces are a different concept — a governance boundary, not CLI session state; follow the project's setup there and name the target (org, project, workspace) next to every plan and apply
- before any plan or apply, evidence the target identity: cloud account / subscription / project and the backend key or workspace, one line next to the command — never trust ambient shell identity silently
- no `*.auto.tfvars` magic; pass `-var-file` explicitly and record the exact command next to the plan it produced
- never commit state, plan files, `.terraform/`, or secret-bearing tfvars; always commit `.terraform.lock.hcl`

WHY:
- critical context must sit next to the decision point; agents inherit shells they did not configure

IF MISSING:
- the right plan applies to the wrong environment

## 7) Versions Are Load-Bearing Context

Your training data contains every historical version of every provider, blended.

- pin `required_version`, pin providers in roots (exact or pessimistic minor), let shared modules declare minimums; pin module sources by `version` or `?ref=` — an unpinned version is hidden context and an open supply-chain door
- before emitting a version-gated feature, check the project's floor (Terraform floors below; OpenTofu versions its own features — check the binary actually pinned):

| Feature | Floor |
|---|---|
| `moved` blocks | 1.1 |
| pre/postconditions | 1.2 |
| `import` + `check` blocks | 1.5 |
| `terraform test` | 1.6 |
| `removed` blocks, test mocking | 1.7 |
| ephemeral values | 1.10 |
| write-only arguments | 1.11 |

- treat remembered argument names as hypotheses, not knowledge; verify unfamiliar resources against the pinned provider docs before authoring
- validate early; a validate error means "open the docs", not "guess a synonym"
- watch for outdated idiom that still validates: old-major patterns pass `validate` and then fight real infrastructure as drift
- never emit cloud IDs or ARNs remembered from training data — resolve them through data sources or variables

WHY:
- the failure mode is not syntax errors; it is fluent 2021-style code with 2021 bugs

IF MISSING:
- hallucinated or deprecated arguments cost a plan-apply cycle each — or silently create drift

## 8) Invariants in Code, Not in Prose

Comments ask; expressions enforce. Checks are cheap for you to write — generate them liberally:

- every variable: explicit `type`, `description` where not obvious; defaults only when safe, intentional, and environment-independent — environment-specific values get no default
- `validation` blocks on variables where misuse is plausible
- `precondition` / `postcondition` for cross-resource constraints (no `0.0.0.0/0` on management ports)
- `check` blocks for environment truths worth asserting on every plan
- `lifecycle { prevent_destroy = true }` and provider deletion protection on stateful keystones: databases, state buckets, key material
- outputs: a clear downstream purpose, `description` where non-trivial, `sensitive` marked; expose only what consumers actually need
- comment only what cannot be encoded, on the line it constrains

WHY:
- encoded constraints survive context loss and fire exactly when attention fails
- humans underuse these blocks because writing them was tedious; that excuse is gone

IF MISSING:
- the invariant lives in a README that never got loaded into context

## 9) Secrets Are Names to You

You will never see secret values — only references. Then the reference must carry all the meaning.

- `sensitive = true` masks display only — the value still lands in state and plan; on 1.10+/1.11+ use ephemeral values and write-only arguments to keep secrets out of state entirely; best of all, keep secret material out of Terraform and pass references to a secrets manager
- write-only arguments leave no trace in state — which also means rotating the value alone produces no diff; pair the secret with its provider's version/trigger argument and put that trigger in the expected diff
- identity-based auth over static credentials everywhere: OIDC / workload identity / assume-role for CI and providers; no long-lived keys in code, tfvars, or env files
- secret names and paths follow the same semantic hygiene as code names — under blindness, the name is the only signal
- verify secrets by behavior (post-check), never by reading values into context; scan plan output before quoting it anywhere durable

WHY:
- state is where secret leaks actually happen, and the agent cannot eyeball a value it never sees

IF MISSING:
- `key2-final-new` gets wired into production because nothing said what it was

## 10) Refactor Economics

Tidy-looking HCL is not free to reach after the fact.

- first decide what the code is: durable production infrastructure, or temporary / test-only / still rapidly evolving
- a refactor with zero behavior change still churns state addresses; tidying Terraform that plans clean needs a reason, not taste
- recreate over migrate while state is young: no meaningful data, no external consumers — temporary code gets the clean target design, not migration scaffolding
- migration machinery (`moved` blocks, compatibility shims) only when continuity materially matters — then document why
- never mix refactor noise and behavior change in one plan

WHY:
- the reviewable diff is the plan; rename noise buries the one destroy that matters

IF MISSING:
- a 40-line plan of moves hides the single `-/+` that takes production down

## Inverted Practices

| Standard practice | What inverts for agents |
|---|---|
| DRY everything into modules | indirection now costs more than repetition |
| `this` / `main` for singletons | zero-meaning addresses in plans, state, logs |
| CLI workspaces for environments | invisible session state decides what gets destroyed |
| constraints in comments and wikis | prose is skippable; validation blocks fire |
| `sensitive = true` as secret protection | it masks display; the value still lands in state |
| tidy refactors any time | every address change is a state operation |
| review the HCL | review the plan; HCL is intent, the plan is truth |

## How to Apply

1. answer first: reusable module, stack, or environment instantiation? smallest safe ownership boundary? does the change touch backend, state layout, or delivery?
2. find the reversibility boundary for the task: what is plan, what is apply, who approved apply
3. state the expected diff before running plan
4. keep one stack and one objective per loop
5. if tooling or provider friction reduced your effectiveness, say so in the handoff: Problem (1 line), Impact (1 line), Smallest fix (1-3 bullets)
6. local policy overrides this skill — on conflict, follow local policy and name the conflict in the handoff; one thing does not move: apply authority comes from explicit delegation (rule 1), never inferred from a policy document

Status: experimental — part of the Agent1st experiments track. Protocol,
measurements, and report path:
[`docs/experiments/terraform-agent1st.md`](https://github.com/applerom/agent1st/blob/main/docs/experiments/terraform-agent1st.md).
