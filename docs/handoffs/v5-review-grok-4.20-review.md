**Verdict**  
The WHY layer delivers exactly what it promises on long-lived, multi-agent projects — intent stops drifting because it lives in the repo as navigable artifacts — but it introduces a real first-hour tax that feels like ceremony until the project hits its first handoff or refactor. Nothing in v5 is broken or overreach; the delta-layer discipline mostly holds. The three-tier retirement was the right simplification. The weakest part is that the WHY files still read slightly more like “here is the proven shape” than “here is the minimal contract that prevents the four drifts,” which risks agents treating the templates as optional polish instead of required navigation truth.

**Answers to core questions 1–6**  

1. **Help or cost?**  
   Dropped cold into an unfamiliar repo that pins WHY-APPROACH.md + the graph + principles at session start, my first hour is materially better once I finish the 8-minute read. I immediately know (a) which use case matters right now, (b) which feature node owns it, and (c) which exact anchor in which file I must touch before I edit a single line of code. That stops the classic “nearest plausible file” mistake that wastes 30–60 % of early session time on real projects. The inflection point is concrete: if the task is one session and one deliverable, the layer is pure ceremony I have to step around. If the task spans >1 session or >1 agent, the layer pays for itself before the first handoff. Pinning the three files is the cheapest way I have ever seen to make “Done Is Not a Mood” enforceable at scale.

2. **Does WHY-APPROACH.md land as an idea?**  
   Yes. The philosophical spine is unmistakable before any template appears: “intent must become a first-class artifact or it drifts; the four drifts kill agent work.” It reads as the reason the WHY layer exists, not a glossy cover on templates. The workflow shift section (PRD → Graph → anchors → code → validate) is the clearest operational upgrade I have seen in any agent protocol. It does not feel like a template pack wearing philosophy as marketing.

3. **Delta-layer discipline**  
   The new WHY-layer files stay clean. They never duplicate model or harness behavior. The only place that comes close is WHY-APPROACH.md §6 (“For any substantial edit: touch the graph before the code… run validators before claiming done”). That could be misread as repeating Continuity / Agent Loop, but it is not: it is the concrete enforcement mechanism for those principles once intent lives outside any single session. No line quietly violates DESIGN.md §2. The WHY files are correctly a second layer, not an expansion of the behavior layer.

4. **Dogfooding — pulling its weight?**  
   The self-referential PRD + graph is an excellent teaching device. It shows the exact shape an adopter should copy without forcing me to imagine a generic example. The meta-content never confuses because WHY-APPROACH.md §0 already flags “copy the shape, not the content.” I would keep it; replacing it with a generic example would make the repo less credible.

5. **Voice**  
   The voice survives intact across every new file: direct, compact, slightly provocative, memorable hooks. “Edits stop being nearest-code edits” lands harder than any corporate phrasing could. Weakest file is PRD.md — it is still solid but reads one notch more like internal dogfood than the rest of the WHY suite. It could lose two lines of “serves two purposes” without losing anything.

6. **Three-tier retirement**  
   Collapsing minimal/standard/full into behavior-layer + WHY-layer was the right call. The old three-tier created the false expectation of graduation gates and duplicate folders; v5 removes that friction while keeping the exact same capability. Nothing valuable was lost — the “full” elements were always speculative and now correctly live as project-local extensions on top of the two layers. This is the cleanest evolution in the entire history.

**File-specific notes** (strong opinions only)  

- **why-graph-principles.md**: Relation vocabulary is the right size — 12 relations, none are obvious synonyms. COVERS / EXPOSED_AS / IMPLEMENTED_BY / SURFACED_BY / HOSTED_BY are distinct and cover the navigation questions an agent actually asks. Missing one essential relation: DEPENDS_ON (for explicit coupling that is not implementation). Without it, the graph cannot answer “what else must change with this?” when the coupling is not ownership but co-change. Add it; it earns its token.  

- **why-contracts-v1.md**: Anti-patterns in §7 are exactly the right ones. Python + TypeScript examples both earn their tokens — these are the two languages where most agent work happens today. One language would have felt incomplete; three would have been bloat.

- **why-graph.xml**: The inline commentary teaches cleanly and the ~150-line size is perfect for a teaching example. It does not distract; it shows exactly how sparse a real graph should stay.

- **PRD.md**: Reads as a real PRD, not meta-filler. The dogfood works.

**Concrete rewrite proposals** (none required for correctness, but one clarity win)  

None rise to “must change.” The only suggestion that would measurably improve adoption is in WHY-APPROACH.md §3, after the workflow shift table. Current text:  
> This is slower per-edit. It is dramatically faster per-project.  

Proposed replacement:  
> This is slower per-edit. It is dramatically faster per-project because the agent no longer wastes cycles on nearest-code edits or invisible couplings.

**What you’d reject / what you’d add** — short list  

**Reject:**  
- Any expansion of the relation vocabulary beyond DEPENDS_ON (keeps the graph from becoming an ontology).  
- Adding validator scripts to the portable templates (still harness-layer until proven language-agnostic).  

**Add:**  
- One sentence in why-graph-principles.md §4: “DEPENDS_ON — explicit co-change coupling that is not ownership.”  
- A one-line “when the graph is wrong” section in WHY-APPROACH.md: “If the graph lies, update the graph first, then the code. Never edit code to match a stale graph.”

**Your take on the three-tier retirement** — one paragraph  
The retirement was the single highest-leverage change in v5. The old three-tier framing invited folder proliferation and graduation theater; two layers (behavior + WHY) forces a clean mental model: AGENTS.md is the non-negotiable contract that never changes, the WHY files are the optional-but-highly-recommended intent layer that every long-lived project should adopt exactly once. Nothing of value was lost — the “full” patterns were never concrete enough to deserve their own tier anyway. This is reversible only in the sense that you could re-introduce folders tomorrow and nothing would break; you should not. The current shape is simpler, more portable, and more honest about where the real complexity lives (in the project, not in the protocol).  

(Word count: 1,142)