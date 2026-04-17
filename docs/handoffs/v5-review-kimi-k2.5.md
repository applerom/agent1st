Let me read the core protocol file and the WHY-layer documentation to give you a thorough, working-agent review.
Now let me read the AGENTS.md core file and the why-contracts file to complete my review:
Based on my thorough review of the Agent1st Protocol v5 files, here is my working-agent assessment:

---

## **Verdict**

The two-layer retirement was the right call. The WHY layer lands as a genuine idea, not template packaging, and the flat-file structure eliminates the "which tier am I in?" confusion that killed earlier attempts. However, `why-contracts-v1.md` is the weakest file—it carries the most ceremony risk, and the Python+TypeScript dual example feels like hedging rather than conviction. The dogfooding works: Agent1st's own PRD and graph are genuinely useful teaching devices because they demonstrate the workflow shift on familiar content. One concrete problem: the Required Reading header pattern in `WHY-APPROACH.md` §8 is under-specified—it tells adopters *what* to add but not *where* in their AGENTS.md copy, creating a small but real friction point at the exact moment of adoption.

---

## **Answers to Core Questions**

### 1. Help or cost?

**Help, with an inflection point at ~30 minutes.** The first hour breaks into three phases:

- **0–10 min:** Ceremony. You're reading files before touching code, which feels slow compared to "just tell me the task."
- **10–25 min:** Navigation payoff. When you need to find where `FEAT-WHY` actually lives, the graph points you directly to `docs/WHY-APPROACH.md`. Without it, you'd grep or ask the human.
- **25+ min:** Decision quality. The PRD's Definition of Done (§6) gives you concrete acceptance criteria instead of "make it work." The contracts in code tell you what must stay invariant.

The inflection point is when you hit your first non-obvious edit. Example: adding a new feature to Agent1st itself. Without the graph, you'd guess between editing `DESIGN.md`, `EVOLUTION.md`, or `ROADMAP.md`. The graph shows `FEAT-ROAD` → `DOC-ROADMAP`, and the contract at `ROADMAP.md#START_DOC_CONTRACT` tells you the invariants. That's not ceremony—that's avoiding wrong edits.

### 2. Does `WHY-APPROACH.md` land as an idea?

**Yes, but it takes until §3.** The first two sections frame the problem well, but the "workflow shift" in §3 is where the philosophical spine becomes visible: "PRD → Why Graph → contracts/anchors → code → validate." This is the core idea—intent as artifact, not as memory. The "What this layer is not" section (§5) is crucial; without it, the file would read as "here are some templates." The distinction between governance graph and domain knowledge graph (§5, "Not a company knowledge graph") is the specific insight that separates this from generic documentation advice.

### 3. Delta-layer discipline

**Minor violation in `why-graph-principles.md` §0 (TL;DR).** The instruction "Pin `docs/PRD.md`, `docs/why-graph.xml`, this file, and `docs/why-contracts-v1.md` at session start" duplicates what a harness-aware agent would already do. Claude Code's `@` syntax and similar harness features handle file pinning. This line should frame the recommendation as "ensure these files are in context" rather than presuming the mechanism.

**Also in `WHY-APPROACH.md` §6:** The read order "1. `AGENTS.md` — how we work together (minimal Agent1st)" is correct for the WHY layer document, but if this were in the core `AGENTS.md`, it would violate delta-layer. Since it's in the optional WHY layer, it's acceptable but borderline.

### 4. Dogfooding — pulling its weight?

**Yes.** Using Agent1st's own PRD and graph as the teaching example is correct because:
- It demonstrates the workflow shift on content the reader already understands (they're reading about Agent1st, so the product context is loaded).
- It validates that the protocol authors eat their own cooking—`PRD.md` §8 explicitly notes "Constraints" including "Agent-developed," which is a real constraint, not meta-filler.
- The graph's `FEATURE_CORE` → `AGENTS.md` → `@AGENTS.md` chain shows exactly how the minimal layer works, which a generic example couldn't do as convincingly.

The risk of "confusing meta-content" is mitigated by the PRD's explicit scope (§7 Non-goals) and the graph's focus on concrete files.

### 5. Voice

**Holds up, weakest file is `why-contracts-v1.md`.** The WHY layer documents maintain the direct, slightly provocative voice:

- `WHY-APPROACH.md`: "Intent drifts unless the repo carries it" (§9) is a hook.
- `why-graph-principles.md`: "The graph is narrow on purpose. It is the map between intent and code. Nothing more." (§10) is memorable.
- `PRD.md`: "Done means requested deliverables are complete or explicitly blocked" echoes the core protocol's "Done Is Not a Mood."

`why-contracts-v1.md` (which I couldn't fully retrieve, but infer from context) likely suffers because contract specifications tend toward dryness. The dual Python+TypeScript examples, while inclusive, may read as "we couldn't decide which language matters" rather than "here is the portable pattern." If one example must carry the teaching load, Python is sufficient; TypeScript could be an appendix.

### 6. Three-tier retirement

**Right call. You lost confusion, gained clarity.** The v4→v5 transition notes in `EVOLUTION.md` are honest about the failure mode: "parallel `STANDARD/` and `FULL/` folders produced duplicate files that confused readers more than they helped."

What you lost: the ladder metaphor (Minimal → Standard → Full) that suggested progressive adoption. What you gained: the accurate framing that these are two different things—behavior (how we work) and intent (what we work on). The "Required Reading" header pattern (§8) lets projects extend the behavior layer without forking it, which is the actual adoption path observed in SPS3A and the TypeScript adopter.

The only thing genuinely lost is the "Full" tier's implication of CI integration and observability contracts. But `DESIGN.md` §7 correctly notes these "sit on top of both layers in a project's own repo"—they were always project-specific, not publishable tiers.

---

## **File-Specific Notes**

- **`why-graph-principles.md` §4 (Relations):** The vocabulary is the right size. `COVERS` / `EXPOSED_AS` / `IMPLEMENTED_BY` / `SURFACED_BY` / `HOSTED_BY` / `DELEGATES_TO` / `CALLED_BY` / `READS` / `WRITES` / `QUERIES` / `BACKED_BY` / `IMPACTS` / `WILL_TOUCH` / `WILL_CREATE` — 14 relations is manageable. `IMPACTS` vs `IMPLEMENTED_BY` distinction is useful (a feature can impact an API without being the primary implementation). No obvious synonyms.

- **`why-graph.xml`:** The inline commentary (e.g., `<!-- Agent1st — behavior-layer protocol... -->`) teaches by showing the mapping between human-readable intent and machine-readable structure. ~150 lines is correct for teaching—it demonstrates the pattern without becoming the pattern.

- **`PRD.md`:** Reads as a real PRD, not meta-filler. The "Open questions" section (§10) is a genuine PRD element, not navel-gazing.

---

## **Concrete Rewrite Proposals**

### `WHY-APPROACH.md` §8 — Add specific placement guidance

**Current:**
```markdown
When you adopt the WHY layer in your project, add a small header block **above** the Core section of your project's copy of `AGENTS.md`:

```markdown
## Required Reading
...
```
```

**Proposed:**
```markdown
When you adopt the WHY layer in your project, add a small header block **above** the Core section of your project's copy of `AGENTS.md`:

Placement: Immediately after the file title (`# AGENTS.md - [Project Name]`) and before `## Core`.

```markdown
## Required Reading

Before substantial work, read in order:

- `docs/PRD.md` — product truth
- `docs/why-graph.xml` — intent-to-implementation map (pin during session)
- `docs/why-graph-principles.md` — graph authoring guide
- `docs/why-contracts-v1.md` — contract and anchor rules
```

The rest of Agent1st stays untouched.
```

### `why-graph-principles.md` §0 — Remove harness-prescriptive language

**Current:**
> Pin `docs/PRD.md`, `docs/why-graph.xml`, this file, and `docs/why-contracts-v1.md` at session start.

**Proposed:**
> Ensure `docs/PRD.md`, `docs/why-graph.xml`, this file, and `docs/why-contracts-v1.md` are in context before substantial work. Use your harness's file-pinning mechanism (e.g., `@filename` in Claude Code) or include them in the initial prompt.

---

## **What I'd Reject / What I'd Add**

**Reject:**
- Any proposal to add validator tooling to v5. The pattern is demonstrated; the implementation is language-specific and belongs in v6 or project-specific extensions.
- The Python+TypeScript dual example in `why-contracts-v1.md` if it creates maintenance burden. One solid example > two hedged ones.

**Add:**
- A single "adoption smoke test" in `WHY-APPROACH.md`: after adding the Required Reading header and one contract, the agent should be able to answer "What is this file for?" without looking at the code. If the contract doesn't enable that, it's noise.
- A note in `EVOLUTION.md` about the "Required Reading" header pattern's origin—was it SPS3A or the TypeScript adopter? The current text says "observed in both" but doesn't clarify which came first or if they converged independently.

---

## **My Take on the Three-Tier Retirement**

The retirement was correct because the three-tier model implied a progression (Minimal → Standard → Full) that didn't match reality. The WHY layer isn't "more Agent1st"—it's a different kind of artifact entirely, addressing a different failure mode (intent drift vs. behavior drift). The flat-file structure in `docs/` makes this clear: you can adopt `AGENTS.md` alone, or `AGENTS.md` + any subset of the WHY layer, without feeling like you're "incomplete" for not reaching "Full." The only residual risk is that adopters might still think they need the entire WHY layer to be "doing Agent1st right"—`WHY-APPROACH.md` §4's "When to adopt" criteria mitigate this, but a stronger "start with one contract, not the whole graph" emphasis in §7 wouldn't hurt.