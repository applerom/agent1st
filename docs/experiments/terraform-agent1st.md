# Experiment: terraform-agent1st — first domain specialization

**Status:** Open — artifact deployed for dogfood (in this repository and in the maintainer's real DevOps practice). No field signal yet.
**Artifact:** [`.agents/skills/terraform/SKILL.md`](../../.agents/skills/terraform/SKILL.md) — a deployable skill, paired with [`why-terraform-skill.md`](../../.agents/skills/terraform/why-terraform-skill.md) carrying the derivation and transformer grounding so the reasoning travels with the rules across repositories.
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
- The delta-layer rule gets a second instance: `AGENTS.md` is a delta over model + harness; a domain skill is a delta over model + harness + a baseline domain reference. Same logic, one level down.
- The artifact shape (runtime `SKILL.md` + co-located `why-*.md` teaching surface) becomes the template for future domain skills.

---

## Track guardrail

`.agents/skills/` is new public surface and could degrade into a junk drawer of domain advice. It will not:

- the directory grows **only** through this experiments track — every domain skill is born as an experiment with its own protocol file
- one experiment per domain; no second domain skill lands while the first has produced no signal
- negative signal removes the artifact, with an `EVOLUTION.md` row as a rejected path — same lifecycle as any experiment

---

## Smallest probe

Use the skill in **one** real Terraform repository where an agent does the authoring, alongside (not replacing) whatever baseline Terraform reference the repo already uses. No other experiments in the same repo at the same time.

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
| 3) DRY Has a Different Price | §4 Attention Engineering |
| 4) Names Are State | §5 Semantic Hygiene |
| 5) No Hidden Context | §4 Attention Engineering |
| 6) Invariants in Code | §4 (constraints near the decision point), §11 Continuity |
| 7) Provider Schema Honesty | §8 Do Not Stop at the First Weak Signal |
| 8) Layout for Reading | §4 Attention Engineering |
| 9) Refactor Economics | §2 (evidence is the plan), §4 |
| 10) Secrets Are Names to You | §5 Semantic Hygiene |
| How to Apply (friction line) | §6 CDD |

Deliberately not ported: §9 Delegation Design (orchestration is not Terraform-specific), the Hello Agent ritual, and any section that would merely restate the core in domain vocabulary.

---

## Anti-patterns specific to this experiment

- **Do not run it as a replacement** for a baseline Terraform reference skill — it is a behavior delta, and measuring it standalone confounds the signal.
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

## How to report back

Bring the five measurements above, plus: which rules fired, which never did, and any place where the skill and the baseline reference gave conflicting advice — that conflict is signal about where the delta boundary actually runs. Standard track lifecycle applies: promote, iterate, or reject with an `EVOLUTION.md` row.
