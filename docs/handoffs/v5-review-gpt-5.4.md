**1. Verdict**

v5 is directionally right, and the two-layer model is better than the old ladder. The part that is still broken is not the idea; it is the teaching surface. The WHY layer sometimes presents its route as universal law, while its own examples are incomplete or internally inconsistent. The sharpest problems are: blanket session-start pinning that can become subagent context tax, a graph-first workflow stated too absolutely, one real relation-direction inconsistency in the graph guide, and a stale three-scope sentence that weakens the “retired three-tier” claim. ([GitHub][1])

**2. Core questions 1–6**

**1) Help or cost?**
It helps once I cross a very clear inflection point: the moment I cannot recover “why this exists” and “what else moves with it” cheaply from code alone. Your own adoption test is basically right: longer than one feature cycle, more than one agent, refactors, handoffs, or forgotten couplings. In that zone, PRD + graph materially improves the first hour. Below that zone, it is overhead. The problem is that the docs sometimes describe the route as if every governed task should pay the full entry fee, even though the repo’s own graph example admits there are no validators yet and no real `START_*` markers in the markdown artifacts. That means the current teaching package sells a full chain while demonstrating a partial chain. ([GitHub][2])

**2) Does `WHY-APPROACH.md` land as an idea?**
Mostly yes. The document earns belief before it shows machinery: it opens with drift, explains the four-artifact pairing, and only then moves into workflow and rollout. That is the right order. Where it starts to feel closer to a template pack is later, when session-start read order and the adopter-side `AGENTS.md` header become fairly prescriptive. So: the philosophical spine lands, but the back half edges toward installation manual territory. ([GitHub][2])

**3) Delta-layer discipline.**
I do not see a major quiet duplication of model or harness behavior in the new WHY files. The more serious issue is different: route over-specification. `why-graph-principles.md` says to pin four docs “at session start,” and `WHY-APPROACH.md` says, for any substantial edit, graph first, contracts first, then code. That is not a delta-layer violation in the narrow sense; it is a context-and-process tax risk. It clashes with the repo’s own sensitivity to multi-agent startup cost: `EVOLUTION.md` explicitly rejects fresh-eye startup scans because subagent cost scales linearly with agent count. The same critique applies here if every delegated worker is expected to pin the full WHY pack. ([GitHub][1])

**4) Dogfooding — pulling its weight?**
Yes, keep it. A generic example would be cleaner and weaker. The repo PRD and graph prove that this is not just a template bundle; it is a pattern the project is willing to apply to itself. That matters. The catch is that Agent1st is mostly docs, so the dogfooded graph demonstrates governance mapping more than real code navigation. The XML comments admit there are no validators yet, no real markers in these markdown files, and no API/UI/module families because the repo has no code. So the dogfood is useful, but it teaches the skeleton better than the hard operational middle. ([GitHub][3])

**5) Voice.**
The voice mostly holds. `WHY-APPROACH.md`, `VISION.md`, and the README keep the direct / memorable / slightly provocative stance that `DESIGN.md` explicitly wants. The weakest new file is `why-contracts-v1.md`: useful, disciplined, but flatter than the rest. That is partly acceptable because it is a mini-spec, but it has the least Agent1st “edge” of the v5 additions. It reads competent rather than distinctive. ([GitHub][4])

**6) Three-tier retirement.**
Yes, this was the right call. `EVOLUTION.md`, `DESIGN.md`, and `VISION.md` all make the same correct point: the real distinction is behavior vs. intent artifacts, not a staircase of minimal / standard / full. You removed duplicate-folder ambiguity and preserved portability. What you did lose is a short public label for the stuff that sits above the WHY layer in adopter repos; now it is described more diffusely as project-specific extensions, runbooks, CI integration, observability contracts, and so on. That is acceptable, but the cleanup is incomplete: `ROADMAP.md` still opens with “all three scopes,” and `PRD.md` says “two tiers” rather than “two layers.” ([GitHub][5])

**3. File-specific notes**

**`why-graph-principles.md`**
Relation vocabulary is about the right size. I would not add much. But I would fix two clarity bugs before adding anything else. First, `COVERS` is defined as “usecase covers a feature,” and the repo XML follows that direction, but the small example reverses it by putting `COVERS` on the feature node targeting the use case. Second, the example uses bare `TARGET` IDs like `UC-ASK` and `MOD-RAG`, while the repo XML uses qualified targets like `FEATURE:FEAT-CORE` and `ARTIFACT:ART-AGENTS-MD`. That is not a small stylistic difference; it is teaching drift. Pick one direction and one target convention, then make every example obey it. ([GitHub][1])

**`why-contracts-v1.md`**
The anti-patterns are the right ones. I would keep them. Python + TypeScript both earn their tokens because the point is not only syntax; it is placement. Python comments above classes/methods and TS/TSX block markers inside JSX are different enough that one-language examples would invite bad cargo-culting. No issue here. ([GitHub][6])

**`why-graph.xml`**
The inline commentary mostly teaches rather than distracts. ~150 lines is a good teaching size. My only complaint is placement: the most important disclaimer is late. The file only tells me near the bottom that there are no validators yet and no real markers in the markdown artifacts. That caveat should appear near the top comment block, because it changes how I interpret the example. ([GitHub][7])

**`PRD.md`**
It reads enough like a real internal PRD to do its job. It is not meta-filler. The only slightly soft area is that the feature / DoD sections blur product truth with authoring policy. That is unavoidable here because the “product” is itself a protocol-plus-docset. I would keep it. ([GitHub][3])

**4. Concrete rewrite proposals**

**A. `docs/WHY-APPROACH.md` §6**
Current: “For any substantial edit: touch the graph before the code; touch contracts before the code; run validators before claiming done.” ([GitHub][2])
Proposed replacement:

> For intent-changing, cross-cutting, or poorly mapped work: update the graph and any needed contracts before implementation.
> For local edits inside an already well-mapped feature: update graph/contracts in the same change set, not necessarily before the first keystroke.
> Run validators before claiming done when validators exist.

**B. `docs/why-graph-principles.md` §4 / §7**
Current: `COVERS — usecase covers a feature` plus example `<REL TYPE="COVERS" TARGET="UC-ASK"/>`. ([GitHub][1])
Proposed replacement:

> `COVERS` is parent→child only. Use it from `USECASE_*` to `FEATURE_*`, and from `EPIC` to `MILESTONE`. Do not reverse it in examples.
> `TARGET` syntax must be consistent within one repo. Use either bare IDs everywhere or family-qualified IDs everywhere; do not mix styles in teaching material.

**C. `docs/ROADMAP.md` opening**
Current: “tracking the protocol’s evolution across all three scopes (minimal, standard, full).” ([GitHub][8])
Proposed replacement:

> tracking the protocol’s evolution across its two public layers — behavior and WHY — plus project-local extensions that sit on top of them.

**5. What I’d reject / what I’d add**

Reject:

* Blanket “pin these four docs at session start” as default behavior for every agent. Primary agent: yes. Every subagent: no. ([GitHub][1])
* “Graph first, contracts first, code later” as a universal law for every substantial edit. It should be the default for intent-changing work, not a ritual for every bounded fix. ([GitHub][2])
* Leaving relation direction and `TARGET` style inconsistent across the guide and the dogfooded graph. That is the one thing I would call genuinely broken. ([GitHub][1])

Add:

* One sentence distinguishing primary-agent onboarding from delegated-agent minimal context.
* One canonical note on edge direction and `TARGET` syntax in the graph guide.
* One earlier disclaimer that the repo’s graph is a structural teaching example, not yet an end-to-end enforced validator setup. ([GitHub][1])

**6. Your take on the three-tier retirement**

Keep the retirement. The old ladder was conceptually neat and operationally muddy. “Behavior layer + WHY layer” is the cleaner mental model, and the repo’s own rationale for the switch is persuasive. The only real problem is residue: a few docs still speak in tier language or scope language, which makes the simplification feel less finished than it is. Fix that residue, and the new framing will look deliberate instead of transitional. ([GitHub][5])

[1]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/why-graph-principles.md "agent1st/docs/why-graph-principles.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[2]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/WHY-APPROACH.md "agent1st/docs/WHY-APPROACH.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[3]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/PRD.md "agent1st/docs/PRD.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[4]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/DESIGN.md "agent1st/docs/DESIGN.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[5]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/EVOLUTION.md "agent1st/docs/EVOLUTION.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[6]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/why-contracts-v1.md "agent1st/docs/why-contracts-v1.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[7]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/why-graph.xml "agent1st/docs/why-graph.xml at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
[8]: https://github.com/applerom/agent1st/blob/ceff3c7/docs/ROADMAP.md "agent1st/docs/ROADMAP.md at ceff3c7be43715e2a8e215d6c0617567de5fb6f0 · applerom/agent1st · GitHub"
