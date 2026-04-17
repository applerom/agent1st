# Verdict

v5 is mostly fine. The WHY layer delivers on its core promise: making intent a first-class artifact paired with code. The philosophical spine in `WHY-APPROACH.md` is clear, the dogfooding works, and the delta-layer discipline holds. However, two areas need tightening: the validator expectations in `why-graph-principles.md` are slightly over-specified for a portable spec, and the protocol lacks guidance on handling inherited code without anchors or safely retiring graph nodes. These are small fixes, not structural flaws.

---

# Answers to Core Questions 1–6

1. **Help or cost?** The WHY layer is a net help, but the inflection point is real. Hour 1 feels like ceremony if you're just reading code. Hour 2+ feels materially better when you're about to change behavior. The graph answers "what else must change with this?" before you edit. That's the payoff. If your project is a one-off script, skip it. If it will live months, the upfront cost pays back fast.

2. **Does `WHY-APPROACH.md` land as an idea?** Yes. The document leads with the problem (intent drift across sessions) before introducing any templates. The four-artifact pairing (PRD, graph, contracts, validators) is motivated by the workflow shift, not the other way around. It reads as philosophy with scaffolding, not a template pack with a glossy cover.

3. **Delta-layer discipline violations?** None that break the principle, but one edge case: `why-graph-principles.md` §6 says "Run your validators. If they don't exist yet, that's the next thing to build." This borders on prescribing workflow that could overlap with harness-level validation. It's defensible because it's about graph↔code consistency (not general testing), but the wording could be tighter to avoid delta-layer creep.

4. **Dogfooding — pulling its weight?** The PRD and graph describing Agent1st itself is a good teaching device. The project is simple enough to be legible but complex enough to show the pattern. A generic example would be more abstract and less memorable. The meta-content works because the constraints are genuine (drop-in, delta-layer, voice), not manufactured.

5. **Voice.** The voice holds up. The weakest file is `why-graph-principles.md` §11 ("Adapting the schema"), which gets slightly procedural and loses the provocative edge. Lines like "If you need something this guide does not cover..." read more like documentation than protocol. A sharper hook ("Stretch before inventing. If you must add, document why.") would restore the voice.

6. **Three-tier retirement.** This was the right call. The minimal/standard/full framing created visual duplication and unclear canonicity. The behavior-layer + WHY-layer distinction is cleaner: one defines how you work, the other what you work on. Nothing was lost that can't be recovered by project-specific extensions. The only thing lost was a mental model for "graduation," but that model was creating more friction than clarity.

---

# File-Specific Notes

- **`why-graph-principles.md`**: The relation vocabulary is mostly right-sized. `IMPACTS` and `WILL_TOUCH` feel slightly overlapping — both describe indirect connections. Consider merging or clarifying the distinction. Missing: a relation for `DEPRECATED_BY` or `REPLACES` to handle refactors safely.

- **`why-contracts-v1.md`**: Anti-patterns in §7 are spot-on. Both Python and TypeScript examples earn their tokens because they show language-specific idioms (comment style, anchor placement). One suggestion: add a brief note on handling inherited code without anchors — a common real-world scenario the spec doesn't address.

- **`why-graph.xml`**: Inline commentary teaches more than distracts. ~150 lines is the right teaching size — enough to show structure, not enough to overwhelm. The dogfooding works because the graph maps to real files in the repo.

- **`PRD.md`**: Reads as a real PRD. The dogfooding works because the constraints are genuine (drop-in, delta-layer, voice), not manufactured. The "Definition of Done" section is particularly strong.

---

# Concrete Rewrite Proposals

**File**: `why-graph-principles.md` §8  
**Current**:  
> "At minimum, the graph should be checked for: every `` points to a real `START_*` marker in a real file..."

**Proposed**:  
> "At minimum, check that every `` points to a real `START_*` marker. Add project-specific checks (feature→implementation edges, ID consistency) as your graph grows. Validators are a tool, not a law."

**File**: `why-graph-principles.md` §11  
**Current**:  
> "If you need something this guide does not cover: 1. Check whether an existing node family or relation fits, even loosely..."

**Proposed**:  
> "Stretch before inventing. If you must add a new element, document its purpose in a `WHAT` child and explain why existing relations don't fit. If it becomes a pattern, update this guide. If it's a one-off, keep it local."

**File**: `why-contracts-v1.md` §7 (add after anti-patterns)  
**Proposed addition**:  
> "**Inherited code without anchors**: When you encounter code that lacks contracts, add a module header on first touch. Don't retrofit everything at once. If the code is stable and rarely changed, it's fine to leave it unanchored — the graph should only reference what you actively govern."

---

# What You'd Reject / What You'd Add

**Reject**:  
- Over-specified validator expectations in `why-graph-principles.md` §8. Keep the minimal check portable; let projects add complexity as needed.  
- The `MODULE_MAP` field in `why-contracts-v1.md` §2 as "optional but recommended" — it's a maintenance burden for small files. Make it explicitly optional with a threshold note ("only worth adding for files with >5 public symbols").

**Add**:  
- A brief "retirement pattern" for graph nodes/anchors: how to deprecate safely without breaking references.  
- Guidance on handling inherited code without anchors (see proposal above).  
- A one-line hook in `why-graph-principles.md` §11 to restore the provocative voice.

---

# Take on the Three-Tier Retirement

Collapsing minimal/standard/full into behavior-layer + WHY-layer was the right call. The three-tier framing created an expectation of promotion gates and separate artifacts that confused adoption. The real distinction is between how you work (behavior) and what you work on (intent-artifacts). Projects can still have richer or simpler WHY-layer implementations without needing a tier label. The only thing lost was a mental model for "graduation," but that model was creating more friction than clarity. If anything, the two-layer model makes adoption easier: drop in `AGENTS.md`, then add the WHY layer when the project earns it. That's a clearer decision boundary than "when do I graduate from minimal to standard?"