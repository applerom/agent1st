# Experiment: why-graph-sharding — router + capability shards for an outgrown graph

**Status:** Open — design complete, no field trial dispatched yet. Deliberately sequenced after (or beside, on a different adopter than) `openspec-why1st.md`: the two experiments must never run on the same project at the same time.
**Artifact:** this design, plus a ~150-line extension to `validate-why.py` (multi-file resolution, edge-home rule, budget warnings). Nothing in stable changes.
**Stable equivalent:** none. Canonical Why1st keeps one graph file and the guidance "do not shard until the file visibly outgrows one canonical location." This experiment defines what *outgrows* means and what to do when it happens — it does not move the default. Small and mid-size adopters should ignore this file.

---

## The problem this experiment exists to test

Same field signal that motivated `openspec-why1st.md`, reached independently by more than one long-lived brownfield adopter: **a structurally-valid spec becomes attention-invalid at scale.** That experiment gives the *spec* a change lifecycle (compiled current view, dated archive). It leaves the Why Graph itself as one monolithic file, pinned into the context of every lead agent and pushed at every subagent whose brief says "read PRD + why-graph."

Why a monolithic graph fails mechanistically, not just aesthetically:

1. **Attention is a normalized competition.** Every pinned token takes budget from every other, on every reasoning step, in every agent — even when "ignored" (Context Rot; see `docs/FOUNDATIONS.md`).
2. **The graph is its own worst distractor.** Stale entities share tag families, attribute shapes, relation vocabulary, and near-duplicate names with current ones — maximally similar distractors for the graph's own queries. Retrieval degrades far faster with similar distractors than with raw length.
3. **Prompt-XML salience is contrastive and saturates.** Distinctive UPPER_SNAKE tags anchor attention against prose; with hundreds of sibling entities they no longer discriminate entity-from-entity. The format's working range is tens of entities per loaded surface.
4. **Stale nodes are active templates.** Agents copy the nearest in-context example over the remote spec (a documented field failure). A status marker does not remove a node from the imitation pool; absence does.

One sentence carries the design: **markers are a soft prior; absence is the only hard demotion.**

The equally documented counter-risk: naive sharding hides exactly what Why1st exists to reveal — "what else must change with this?" A sharding design is only acceptable if cross-cutting coupling becomes *more* visible, not less.

---

## Lead principle — the success bar

Same bar as `openspec-why1st.md`: **net-fewer competing truth surfaces, and net-fewer pinned tokens per session.** If the project ends with the monolith *and* shards *and* a bespoke slice system alive, the experiment failed regardless of green validators. Sharding without a changed load rule is file management theater.

---

## Hypothesis

1. **(H1)** On a project past the size threshold (below), router + capability shards cut pinned graph-context per session by ≥2× for leads and more for subagents, without an increase in wrong-era / wrong-capability edits.
2. **(H2)** The **edge-home rule** (intra-capability edges live in the shard; cross-capability edges live only in the router) holds under real work without double-bookkeeping — drift incidents ≈ 0 with the validator enforcing both directions — and makes inter-capability coupling *more* visible than the monolith did, because it now sits in the one small always-pinned file.
3. **(H3)** Marker-keyed PRD references (`PRD_REF` → an explicit `<!-- PRD_ANCHOR: ... -->` marker instead of §-numbers/heading text) make demotion and restructuring cheap enough that stale sections actually get demoted — attacking accumulation at its cause. This part is independently valuable: if sharding is falsified, keep the markers.

---

## The architecture

```
docs/why-graph.xml              <- the ROUTER: small, budget-capped, pinned (same path adopters already pin)
docs/why-graph/<capability>.xml <- capability shards: full vertical slice each, edited directly, nothing generated
```

- **Capability** = a coherent product/system area with its own vertical slice (usecases → features → APIs/surfaces → modules → anchors). If a local profile/slice system already exists, its *stabilized* profiles are the revealed shard boundaries.
- **Router** holds exactly: the `<PROJECT>` header; one `<CAPABILITY_*>` entry per shard (`ID="CAP-*"`, `SHARD="<file>"`, `ROLE`, one-sentence `<INTENT>`); and **all cross-capability edges**, as `<REL SOURCE="..." TARGET="..."/>` children of the source capability's entry.
- **`ROLE`** ∈ `CURRENT` (default working set) / `REFERENCE` (stable contract, load when touched) / `LEGACY` (still running, skipped by default; every inbound edge is named modernization debt and warned). `ROLE` exists **only on router entries**, never on nodes — nodes keep the canonical two-value `STATE` practice.
- **Shards** are unchanged Why1st inside: same families, relations, anchors, authoring workflow. Root tag `<Why_Graph_Shard project="..." CAPABILITY="CAP-...">` so any file self-identifies.
- **Load rule** (the actual intervention — put it in Required Reading): pin the router; load the shard your task names; load a second shard only when the router's cross-edges say your change touches it; subagents get shards or subtrees only; global lookups via `grep -r`; whole-directory reads only for graph-wide refactors.
- **No compiler, nothing generated.** The extended validator parses router + shards into one in-memory table: global ID uniqueness, cross-file target resolution, edge-home rule both directions, `SHARD` paths exist, no orphan shards, budget warnings. Monolith graphs (no `CAPABILITY_*` entries) validate exactly as before.
- **History:** deprecated nodes still get deleted after one cycle (git is the archive); a still-running off-strategy capability goes `ROLE="LEGACY"`; a deleted capability's shard is deleted with its code. Intent history is the spec layer's job, not the navigation layer's.
- **Budgets** (defaults from field texture — a 16-element working set succeeded where a 78-element one re-monolithed): shard warns at 30 elements, split-or-justify at 50; router warns at 12 capabilities or 40 cross-edges. A router past budget means merge capabilities or question boundaries — never build a second router.

## Size threshold — when this experiment applies at all

Any two of: graph > ~100 elements or ~8k tokens; recurring CDD complaints about graph size or stale-layer distraction; a local routing layer (profiles/slices/context maps) already invented; capability clusters nameable without looking at the graph. Below the threshold, stop reading — stable guidance applies.

---

## Smallest probe

On **one** long-lived brownfield adopter past the threshold (and *not* running `openspec-why1st` concurrently):

1. **PRD anchors first** (H3, structure-neutral): add `<!-- PRD_ANCHOR: ... -->` markers, repoint `PRD_REF`s, extend the validator to check them. Validators green.
2. Extend the project's `validate-why.py` port: multi-file resolution + edge-home rule + budgets.
3. Carve out **one shard — the current strategic capability** (it benefits most). Move its vertical slice verbatim; move its cross-edges to the router with explicit `SOURCE=`; validate; commit.
4. Strangler-repeat per capability, one commit each, validators green throughout. The monolith shrinks until it *is* the router.
5. Rewrite the load rule in the project's Required Reading / context map; **delete** the "pin the full graph" instruction (two contradictory load rules is a truth-surface regression).
6. Retire any bespoke slice/profile system that now duplicates shard boundaries.

---

## What to measure

1. **Pinned graph-tokens per session**, lead and subagent separately, before vs after (headline for H1).
2. **Truth-surface count** before vs after — monolith gone, slices retired, one load rule (the shared bar).
3. **Wrong-era / wrong-capability edits** — must not increase (coupling-visibility check on H1/H2).
4. **Edge-home violations and router↔shard drift incidents** over the trial (direct H2 signal; the likeliest failure).
5. **Router growth curve** across N changes — the monolith-#2 detector.
6. **Demotions actually performed** after PRD anchors land vs the prior era (H3 signal).

---

## What would falsify it

- **Coupling dominance:** honest boundaries still leave cross-capability edges > ~⅓ of all edges — the project does not decompose; sharding is the wrong tool for it.
- **Router monolith:** the router blows its budget and resists capability merging — the design fails its own math.
- **Load rule ignored:** agents demonstrably keep loading all shards — attention unchanged, file count up; the binding constraint was behavioral, not structural.
- **Double bookkeeping:** recurring edge-home drift despite the validator — the invariant is too expensive in practice.
- **No measurable win** on tokens, wrong-era edits, or time-to-locate, on a project that genuinely crossed the threshold.

---

## Anti-patterns specific to this experiment

- **Sharding below the threshold.** This design is overhead for any project that fits in one attention surface — which is most projects.
- **Sharding by node family or by lifecycle-into-files.** Both were considered and rejected in design: family shards force every task to load everything; the graph needs no archive files because deleted code leaves the graph (git is the archive) and still-running legacy is capability-shaped (`ROLE="LEGACY"`).
- **A compiler / generated monolith.** The validator reads a directory; "full view" is concatenation on demand. Generated views reintroduce the edit-policy machinery this design exists to avoid.
- **Keeping the old load rule.** Shards plus "pin the full graph" is strictly worse than the monolith.
- **A router for the router.** Automatic reject; merge capabilities instead.
- **Running concurrently with `openspec-why1st`** on the same project.

---

## Rollback

Concatenate the shards back into `docs/why-graph.xml` (drop `SOURCE=` edges back into their source nodes), delete `docs/why-graph/`, restore the previous load-rule text. The validator's monolith mode still passes; anchors and contracts are untouched. Keep the PRD anchor markers regardless — they are independently justified. Record the negative signal as an `EVOLUTION.md` rejected-path row.

---

## How to report back

Bring the six measurements, headlined by pinned-tokens-per-session and truth-surface count. Report edge-home drift incidents plainly (H2 is the likeliest failure), whether the load rule was actually followed or quietly bypassed, and any place the router+shard split felt heavier than the monolith it replaced. N=1 is texture and a worked example, not proof — the proof bar remains a clean comparison per `MEASURING-EFFECTIVENESS` discipline.
