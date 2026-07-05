# Experiment: openspec-why1st — a change-lifecycle for long-lived specs

**Status:** Open — design complete, first field trial dispatched to one long-lived brownfield adopter. N=1 (texture, not significance).
**First field signal (2026-07-05, probe refined):** the maintainer reviewed OpenSpec's generated `opsx` skill/command prompts against primary source (`src/core/templates/workflows/`, e.g. `explore`, `propose`) and found them micromanagement-heavy: persona coaching, scripted dialogue with fixed phrasings, prescribed routes and named harness tools, ~80-85% failing the delta-layer test — incompatible with the Role Contract ("agent chooses the route") and actively harmful for strong models via nearest-example imitation. OpenSpec is two separable layers: the **artifact/lifecycle layer** (`specs/` + `changes/` + dated archive, CLI, `validate --strict`) — mechanical, spirit-compatible, and still the thing under test — and the **generated prompt layer**, which is not. The probe now runs layer 1 only: do not install (or delete) the generated `opsx` skills and replace them with thin pointers — a few lines each carrying only the delta an agent cannot guess (the CLI contract: `status --json` field semantics, `instructions <artifact-id>`, `context`/`rules` are constraints-not-content) plus acceptance = validators green. Count the generated prompt surface under measurement #5 (net ceremony delta). This also honestly revises H1's economics: "maintained tool, lower maintenance cost" holds for the lifecycle layer only — the thin pointers are a small local prompt surface an a1w1 adopter must own.
**Artifact:** this design, plus a forked OpenSpec schema (`a1w1`) and an extended `validate-why.py`, composed over an adopter's existing Why1st chain. Nothing in stable changes.
**Stable equivalent:** none. The canonical chain (PRD → Why Graph → contracts → validator) is unchanged. This tests an **optional change-lifecycle layer** for the one case the chain does not yet cover: a spec that has outgrown agent attention.

> `a1w1` = Agent1st + Why1st (the paired approach). Used throughout this file.

---

## The problem this experiment exists to test

Field signal from long-lived brownfield work, reached independently by more than one adopter: **a structurally-valid spec can become attention-invalid.** As a project accretes product eras, old layers keep equal visibility, equal naming weight, and equal navigational authority. The old context is *correct*, so an agent does not reject it — it over-attends to it. Correct-but-stale context is harder to demote than wrong context, because validators stay green the whole time.

Why1st made intent durable, navigable, and validated. It did **not** give intent a *change lifecycle* — a way to keep current truth separable from history without losing either. The canonical chain has one canonical Why Graph and "do not shard until the file visibly outgrows one location — that almost never happens." This experiment is the honest counter-case: on a long-lived brownfield project, it *did* happen.

The tempting in-house fix is a bespoke routing layer (profiles / slices / status axes / a renderer tool). That works, but it is project-local machinery that must itself be built, validated, and maintained — and it tends to grow the very monolith it fights (a "current" profile becomes the next monolith). This experiment asks whether a **maintained, popular SDD tool** supplies the same attention fix as a structural property, so adopters do not each hand-build a routing system.

---

## Lead principle — the success bar

**Success is net-fewer competing truth surfaces. Not "OpenSpec adopted."**

If a project finishes with PRD + OpenSpec `specs/` + Why Graph + a bespoke slice system all live, the experiment has *added* a surface and made the disease worse — even with every validator green. The headline acceptance criterion, against which every other measure is secondary:

> After the change, there are **fewer** places an agent could mistake for current truth than before.

This is the criterion that turns "the cure carried the disease" from a risk into a falsifier.

---

## Hypothesis

Three claims, tested together:

1. **(H1) OpenSpec's compiled-current-view + dated-archive solves brownfield attention-overload at least as well as a bespoke profile/slice system — at lower maintenance cost.** Cleanest single test: *can a pre-existing bespoke slice system be retired without an attention regression?* That binary is better evidence than a fuzzy time-to-locate number.
2. **(H2) The OpenSpec⇄Why1st seam holds without double-bookkeeping.** OpenSpec `specs/` carries product truth (*what*, with a change lifecycle); the Why Graph carries intent→code navigation **plus the coupling/relations graph OpenSpec refuses to hold by design** (it excludes internal class/function names and code links on purpose). They stay in sync through a title-as-key reference that the validator checks. If they drift into two hand-maintained truths, H2 is false.
3. **(H3) OpenSpec's native scenarios give BDD's acceptance *form* for free, but evidence still has to be earned.** OpenSpec requirements already carry Gherkin-style `#### Scenario:` WHEN/THEN blocks — so the acceptance-criteria shape is free. Turning a scenario into *evidence-before-done* still requires binding it to a deterministic check. Bound as **OpenSpec scenario → Why Graph feature anchor → project eval row**, it delivers BDD's value without Gherkin/Cucumber tooling sprawl.

---

## The architecture — three layers that fill each other's holes

| Layer | Brings | Lacks (filled by another) |
|---|---|---|
| **OpenSpec** | change lifecycle, compiled current view (`specs/`), dated archive | intent→code links, code-aware validation (none, by design) |
| **Why1st** | stable anchors, intent→code map, coupling graph, validators | a change lifecycle / archive |
| **BDD (via OpenSpec scenarios)** | acceptance form (WHEN/THEN) tied to requirements | a runner — evidence comes from binding to the project's eval |

Composed chain (experimental, over the canonical one — it does not replace it for other adopters):

```
OpenSpec specs/      →  Why Graph          →  anchors in code  →  validators (git/CI)        →  scenarios as evidence
(current product        (intent→code map +    (local truth)       (anchors resolve; every       (each requirement's
 truth; old eras        coupling/relations;                       live requirement has a        WHEN/THEN bound to a
 archived out)          OpenSpec won't hold)                      Why Graph node; refs           Why Graph anchor +
                                                                  point to real requirement      a deterministic eval row)
                                                                  titles)
```

**Why both Why Graph and OpenSpec `specs/` exist** (state this plainly or a future agent will read duplication and collapse them wrong): `specs/` answers *what the product does now and how that changed over time*. The Why Graph answers *where that intent lives in code and what moves with it* — the navigation and coupling layer OpenSpec deliberately omits. The seam is **title-as-key**: a Why Graph node references an OpenSpec requirement by its exact `### Requirement: <title>` text (OpenSpec has no stable IDs — the title *is* the key). A `RENAMED` op in OpenSpec must propagate to the Why Graph reference; the validator catches a reference pointing at a title that no longer exists in `specs/`.

---

## What this would shift if true

- Why1st gains a **brownfield change-lifecycle** without inventing one: current truth in `openspec/specs/`, in-flight work in `openspec/changes/<name>/`, history in `openspec/changes/archive/<date>-<name>/` — three structurally-separated attention zones.
- Adopters with an over-grown spec get a **maintained tool** instead of a hand-built routing layer to maintain forever.
- The evidence story gets concrete: acceptance criteria are authored as scenarios, bound to anchors and to a deterministic eval — "Done Is Not a Mood" with a wired loop.

---

## Smallest probe

On **one** long-lived brownfield project, take **one** current strategic change:

1. `openspec init --tools <harness> --profile core` (scaffolds four empty dirs; imports nothing).
2. Fork the schema: `openspec schema fork spec-driven a1w1` — add artifact instructions that tell the agent to update the Why Graph and anchors as part of the change, and to demote superseded prose in the same change.
3. Express the current change as an OpenSpec change folder (`proposal.md` carries the WHY/"so that"; delta-specs carry requirements + scenarios; `tasks.md` includes the Why-Graph/anchor updates).
4. **Demote in the same change:** mark the PRD/section the new requirement supersedes as `legacy-reference` and repoint or retire its references — one capability, one current home.
5. Archive the change → deltas merge into `openspec/specs/`; the folder moves to `changes/archive/`.
6. Wire the live requirements to the Why Graph (title-as-key) and run the validators.
7. Measure (below). Run no other experiment on this project at the same time.

---

## What to measure

1. **Truth-surface count, before vs after.** The headline. How many places could a cold agent mistake for current truth? The number must go down.
2. **Can the bespoke slice/profile system be retired** without an attention regression? (Direct H1 test — the cleanest falsifier.)
3. **Double-bookkeeping / drift incidents** between `specs/` and the Why Graph over the trial (direct H2 test). Count every time they disagreed and a human/agent had to reconcile.
4. **Time-to-locate current truth** for a cold agent, and **wrong-era edits** (edits made against an archived/superseded layer). Texture, not significance.
5. **Net ceremony delta.** Did the integration remove more attention load than the OpenSpec + forked-schema + extended-validator machinery added? If it is net-heavier, it fails minimalism regardless of the other numbers.

---

## What would falsify it

- **H2 drifts:** `specs/` and the Why Graph become two hand-maintained truths that disagree. Then the seam is wrong — consider generating one view from the other, or subsuming.
- **Agents still drown** despite the compiled current view — the archive alone does not fix attention, which would vindicate a routing/slice layer after all.
- **Net more ceremony:** the machinery costs more attention than it saves. On a small or mid-size project this is the expected outcome — the experiment is scoped to large brownfield only.
- **The slice system cannot be retired** without regression — H1 false; the two mechanisms are not substitutes.

---

## Operational seam — verified against OpenSpec v1.4.1 (read from package source, 2026-06-28)

These facts shaped the design; an implementing agent must honor them:

- **No requirement IDs.** `### Requirement: <title>` is the key, matched whitespace-insensitively at archive. Renames need the explicit `## RENAMED Requirements` op. The Why Graph seam piggybacks on this title-key — do not invent a parallel ID scheme.
- **No native spec↔code link, no plugin/hook/CI API.** Anchors are net-new (Why1st's job). The validator plugs in **externally**: gate archive in git/CI on `openspec validate --all --strict` (OpenSpec's structural check — document-only, zero code awareness) **plus** the extended `validate-why.py`. OpenSpec will not call your checker; `--no-validate` can bypass even its own structural gate, so the CI gate is the real one.
- **`/opsx:verify` is expanded-profile-only, optional, heuristic, and unenforced.** Do not rely on it as the evidence gate. Evidence = scenarios bound to eval + the validators.
- **`openspec archive` is deterministic** (merge order RENAMED → REMOVED → MODIFIED → ADDED, matched by exact header) and is the only place the compiled `specs/` view materializes — there is no `diff`/preview command.
- **Scenario pitfall:** `#### Scenario:` needs **exactly four hashtags** or it fails silently; every requirement needs ≥1 scenario; `MODIFIED` must carry the full updated requirement, not a fragment.
- **Schema fork** (`openspec schema fork`) and `config.yaml` `context:`/`rules:` inject **LLM-level guidance, not enforcement** — they carry the a1w1 discipline into the prompt; the hard gate stays in CI.

---

## Anti-patterns specific to this experiment

- **Big-bang PRD migration.** OpenSpec imports nothing and grows one change at a time; a brownfield PRD with reference anchors and heading-dependent validators must be migrated capability-by-capability, validators green throughout. Forcing a wholesale move is how you break the contract web the field note warned about.
- **Two live truths for one capability.** Landing a capability in `specs/` while its old prose still reads as current is the disease, not the cure. Demote in the same change.
- **"BDD for free" overreach.** The *form* is free; the *evidence* is not. A scenario with no bound deterministic check is documentation, not proof.
- **Keeping the slice system "just in case."** If the compiled current view works, retiring the bespoke layer is the point — an unretired parallel system means the surface count did not drop.
- **Mixing with other experiments** on the same project.

---

## Rollback

OpenSpec is `openspec/` (four dirs) + generated per-harness command files (e.g. `.claude/commands/opsx/`). To back out cleanly if H2 drifts or ceremony proves net-negative: stop using the slash commands, delete the `openspec/` tree and the generated command files, restore any PRD section demoted during the trial. The Why Graph, anchors, and `validate-why.py` are unaffected — they predate the experiment. Negative signal removes the experiment with an `EVOLUTION.md` rejected-path row.

---

## How to report back

Bring the five measurements, with #1 (truth-surface count) and #2 (could the slice system be retired) as the headline. Plus: every drift incident between `specs/` and the Why Graph (H2 signal), and any place the integration felt net-heavier than the problem it solved. Standard track lifecycle: promote, iterate, or reject with an `EVOLUTION.md` row. N=1 means this is texture and a worked example — not proof. The proof bar is a clean comparison run per `MEASURING-EFFECTIVENESS` (placebo arm, blind judge), which this trial explicitly is not.
