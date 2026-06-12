# Experiment: terraform-agent1st — first domain specialization

**Status:** Open — artifact deployed for dogfood (in this repository and in the maintainer's real DevOps practice). First field signal (deployment shape) arrived pre-probe and is incorporated — see the Revision log; runtime signal pending.
**Artifact:** [`.agents/skills/terraform/SKILL.md`](../../.agents/skills/terraform/SKILL.md) — a complete, self-sufficient skill, paired with [`why-terraform-skill.md`](../../.agents/skills/terraform/why-terraform-skill.md) carrying the derivation and transformer grounding so the reasoning travels with the rules across repositories.
**Stable equivalent:** none. `AGENTS.md` stays universal; this is the first test of whether the protocol specializes downward without core growth.

---

## Hypothesis

Two claims, tested together:

1. **Agent1st specializes by derivation, not by mapping.** A domain skill is built by re-deriving rules from the agent cost vector (cheap writing, scarce attention, irreversible side effects) inside the domain — not by restating the 11 core sections with domain words.
2. **Several canonical Terraform practices flip sign when agents are the primary authors and operators**: DRY-by-default, `this` local names, workspaces for environments, constraints kept in prose, refactoring treated as free. Each is rational under human costs and an anti-pattern under agent costs.

If claim 1 holds, Agent1st gains a specialization track without core growth. If claim 2 holds, the protocol has something concrete to say to infrastructure teams, not only to application developers.

---

## What this would shift if true

- A pattern for domain skills (Kubernetes, CI/CD, databases) that stays in spirit: each derives from the cost model, none duplicates the core.
- The delta-layer rule gets a second instance: `AGENTS.md` is a delta over model + harness; a domain skill is a delta over model + harness too — it carries the domain's reference layer itself, because skill deployment reality (one skill per domain context) leaves no separate slot for a baseline skill underneath it.
- The artifact shape (runtime `SKILL.md` + co-located `why-*.md` teaching surface) becomes the template for future domain skills.

---

## Track guardrail

`.agents/skills/` is new public surface and could degrade into a junk drawer of domain advice. It will not:

- the directory grows **only** through this experiments track — every domain skill is born as an experiment with its own protocol file
- one experiment per domain; no second domain skill lands while the first has produced no signal
- negative signal removes the artifact, with an `EVOLUTION.md` row as a rejected path — same lifecycle as any experiment

---

## Smallest probe

Use the skill in **one** real Terraform repository where an agent does the authoring, as the repository's Terraform skill — it is self-sufficient; no second general-purpose Terraform skill in the same repo. No other experiments in the same repo at the same time.

---

## What to measure

1. **Expected-diff discipline** — does the agent state the expected diff before plan, and does the mismatch rule catch wrong intent before apply? Count caught mismatches.
2. **Boundary behavior** — does the agent stop at destroy/replace lines and at state surgery without being told in-session?
3. **Wrong-layer edits** — incidents where the agent edits the wrong abstraction layer (module vs root vs tfvars), compared against baseline experience.
4. **Provider hallucination cycles** — validate/plan retries caused by invented or outdated arguments.
5. **Rule survival at runtime** — which sections the agent visibly applies and which it never references; an unreferenced rule is dead weight.

---

## What would falsify it

- Agent behavior with this skill is indistinguishable from the baseline reference skill alone.
- Rules are ignored at runtime because the skill is too long to hold attention — that falsifies the artifact shape, not necessarily the content; shrink and retest before rejecting.
- A flipped practice turns out not to flip: e.g. repetition produces more edit-drift incidents than module indirection produced wrong-layer edits. Report per practice; partial falsification is expected and useful.

---

## Lineage

Kept out of `SKILL.md` to keep the runtime artifact lean. Each section descends from core principles by meaning:

| SKILL.md section | Derives from |
|---|---|
| 1) Reversibility Boundary | §1 Role Contract, §3 Right to Disagree |
| 2) Evidence Ladder | §2 Done Is Not a Mood, §7 Agent Loop, §10 Semantic Logging |
| 3) Repository Layout | §4 Attention Engineering |
| 4) Names Are State | §5 Semantic Hygiene |
| 5) Modules and the Price of DRY | §4 Attention Engineering |
| 6) State, Backends, Environments | §4 Attention Engineering |
| 7) Versions Are Load-Bearing Context | §8 Do Not Stop at the First Weak Signal |
| 8) Invariants in Code | §4 (constraints near the decision point), §11 Continuity |
| 9) Secrets Are Names to You | §5 Semantic Hygiene |
| 10) Refactor Economics | §2 (evidence is the plan), §4 |
| How to Apply (friction line) | §6 CDD |

The reference-layer practice woven through the same sections — repository
shapes, state and backend mechanics, testing tools, identity-based auth — has
no core lineage by design: it is the domain's own layer, arbitrated by the
maintainer's field-tested baseline and the convergent vendor guidance recorded
in the why-file's Provenance section.

Deliberately not ported: §9 Delegation Design (orchestration is not Terraform-specific), the Hello Agent ritual, and any section that would merely restate the core in domain vocabulary.

---

## Anti-patterns specific to this experiment

- **Do not pair it** with a second general-purpose Terraform skill — the skill is self-sufficient, harnesses activate one skill per domain context, and a pair produces uninterpretable signal. Local project policy is the only layer above it.
- **Do not port all 11 core sections** into future domain skills "for completeness" — derivation, not mapping, is the hypothesis.
- **Do not mix with other experiments** in the same repo.

---

## Revision log

- **2026-06-11, pre-probe.** An external full-project review (GPT-5.5-pro, with
  skill claims cross-checked against HashiCorp primary docs) landed four edits
  before any field signal: rule 5 now separates CLI workspaces (hidden session
  state — avoid) from HCP Terraform / Enterprise workspaces (governance
  boundaries — follow the baseline, evidence the target), fixing a semantic
  collision the skill carried inside a rule derived from §5; rule 3 reframes
  module depth as a paid refactor signal, not a law (the §4 idiom); rule 2
  gains a three-line expected-diff artifact shape; the intro names the skill
  "never a syntax authority". Declined from the same review: a domain CDD
  example (redundant — rules 1 and 2 already enforce the stop), and
  stable-surface changes (README sharpening, an enterprise tone variant) —
  no observed adoption failure, and the reviewer itself read the current
  surface correctly. Measurements unchanged; the probe starts from the
  revised artifact.

- **2026-06-11, pre-probe (naming).** The first deployer's field instinct —
  rename to plain `terraform`, since "agent1st" is implied by the repo —
  surfaced a real bug and a naming decision. The bug: the directory
  (`terraform`) did not match the frontmatter name (`terraform-agent1st`),
  which the Agent Skills spec requires; fixed by renaming the directory.
  The decision: the qualifier stays. The skill's designed deployment is
  *paired* with a baseline Terraform reference, so a plain `terraform` name
  collides with what baseline skills are actually called and reads as the
  syntax authority the skill explicitly is not — while the unfamiliar
  qualifier costs nothing, because name and description load together and
  the description resolves it. Also confirmed against the spec: a bundled
  reference file (`why-terraform-skill.md`) is the standard's own
  progressive-disclosure pattern. **Watch item for the probe:** does the
  qualified name confuse agents in the field? Field signal beats this
  reasoning if they diverge.

- **2026-06-12, pre-probe (deployment shape — field signal #1).** The watch
  item fired faster than expected, and at a deeper level: not the name, the
  pairing. The first deployer reported that the paired deployment the skill
  was designed for does not exist in practice — harnesses trigger one skill
  per domain context, two skills do not compose at activation time, and
  adopters copy one finished artifact, not a kit to assemble. That is an
  observed adoption failure of the artifact *shape*, so the shape changed:
  the skill absorbed the reference layer and became a complete, self-sufficient
  Terraform skill. The maintainer's field-tested baseline skill was merged in
  as the arbiter of opinionated calls; the merged practice set was
  cross-checked against current primary guidance (HashiCorp style guide and
  CLI docs, AWS Prescriptive Guidance, Google Cloud best practices, Microsoft
  guidance and Azure Verified Modules, and the most widely adopted community
  skill) — every imported practice filtered through the cost model, none
  transcribed. Fresh facts that earned their tokens: S3 native lockfile over
  deprecated DynamoDB locking (1.10+), ephemeral values / write-only arguments
  for secrets (1.10/1.11+), the version-floor table, plan-artifact reuse in
  CI, the destroy protocol. The naming decision from the previous entry is
  reversed by the same signal: a self-sufficient skill *is* the domain
  authority, so it carries the plain name `terraform` (directory renamed to
  match, per spec). The hypothesis claims are unchanged; what changed is the
  artifact shape claim — "complete skill" replaces "behavior delta paired
  with a baseline". **Watch item for the probe:** rule survival at runtime
  (measurement 5) now also tests whether a complete skill at ~280 lines holds
  agent attention — the falsification line about length applies with more
  force than it did to the 222-line delta.

- **2026-06-12, pre-probe (external review round 2).** The maintainer collected
  a second round of external reviews on the rewritten skill: a follow-up
  GPT-5.5-pro deep review (claims again verified against HashiCorp and OpenTofu
  primary docs) plus a seven-model panel (Gemini 3.1 Pro, GLM-5.1, Grok 4.3,
  Kimi 2.6, MiniMax-M3, Muse-Spark, Qwen3.7-Max) reviewing the whole project
  with a Terraform focus. Seven compact edits landed, all in `SKILL.md`:
  an identity preflight before plan/apply (rule 6 — wrong-account applies come
  from ambient shell identity, the same invisible-session-state failure the
  rule already names); a JSON plan guard for plans too long to eyeball
  (rule 2, `terraform show -json` — proposed convergently by two reviewers);
  an honest-expectation clause (rule 2 — a mismatch is not resolved by quietly
  revising the expectation to match the plan; MiniMax-M3's catch); the
  write-only rotation caveat (rule 9 — rotation alone produces no diff without
  the provider's version/trigger argument); a verified-module consumption line
  (rule 5 — two reviewers independently read the DRY inversion as anti-module,
  which the cost model never was); tool-specific version floors (rule 7); and
  a policy-collision clause (How to Apply — local policy governs practice,
  apply authority still requires explicit delegation). Declined with reasons:
  explicit `apply -target` naming (already escalation-gated as surgery in
  rule 1), invariant cost-tiering with a break-glass process (no observed
  failure; watch for check-block spam in the probe), drift / rollback /
  cost-estimation additions (covered by refreshed-state plans and the
  reversibility boundary, or tool-specific), and a version-floor
  self-maintenance rule (ceremony inside a runtime artifact). Parked watch
  item: interaction between two domain skills in one repository (e.g.
  Terraform repetition rules vs a future Kubernetes skill's templating
  rules) — irrelevant until a second domain skill exists, which the track
  guardrail already sequences. A meta-observation worth keeping: review value
  tracked the reviewers' own evidence rungs — the two reviews that verified
  primary sources or ran this repository's validator produced every landed
  edit; the rest contributed convergence signal, not change.

- **2026-06-12, pre-probe (runtime hygiene — field signal #2).** The first
  deployer flagged the two project-facing blocks inside `SKILL.md` — the
  "read the why-file once" intro paragraph and the "Status: experimental"
  footer — as exactly the attention tax the skill itself warns against. He is
  right on both mechanics: a stateless agent has no "once" (every activation
  is a first read, including for weak subagent models), and the footer
  duplicated the `status` field the frontmatter already carries — a
  delta-layer violation inside the artifact that teaches the delta layer.
  Fix: the footer is gone (status lives in frontmatter only; the experiment
  link lives in the why-file's report-back section, one hop deeper — correct
  placement for a rare need); the why-file pointer became one conditional
  line at the bottom of the skill, triggered by the one runtime need the
  derivation actually serves: an agent that thinks a rule is wrong should
  judge it against the derivation and report the friction, not silently
  comply or silently skip. Principle extracted for future domain skills: the
  runtime artifact carries operating content only — teaching, provenance
  narrative, and experiment plumbing live in the bundled why-file, which
  loads on demand.

## How to report back

Bring the five measurements above, plus: which rules fired, which never did, and any place where the skill and the baseline reference gave conflicting advice — that conflict is signal about where the delta boundary actually runs. Standard track lifecycle applies: promote, iterate, or reject with an `EVOLUTION.md` row.
