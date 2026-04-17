I'll read through the v5 files directly before writing anything. Let me start with the repo structure and the core files in the order the request specified.I have the repo structure. Now let me fetch the core files in the order specified. Starting with AGENTS.md.GitHub's blob view doesn't give me file contents. Let me try the raw URL format.Let me try to view the docs folder listing to see what files actually exist.Let me try the github.com/raw/ redirect pattern which sometimes works when raw.githubusercontent.com is blocked.Progress — DESIGN.md rendered in the blob response. Let me try fetching the v5-specific files now.EVOLUTION.md is v5-aware. But I noticed DESIGN.md §7 on main was NOT updated — it still has the three-tier table, contradicting the request's claim that v5 rationale lives there. Let me try the v5-specific files again now that they've been referenced in fetched content.I've got enough to give you a useful review, but I have to flag a tool limitation first. Here's the review in the format your v4.6 colleague asked for.

---

## Scope caveat before the verdict

My web_fetch tool only opens URLs that appear as hyperlinks in already-fetched pages. That meant I could read `README.md`, `DESIGN.md`, and `EVOLUTION.md` in full (they're linked from README). The five v5-specific files — `WHY-APPROACH.md`, `PRD.md`, `why-graph.xml`, `why-graph-principles.md`, `why-contracts-v1.md` — are not linked from any page I could reach, so the raw and blob URLs were blocked by my tool's allowlist. I also could not fetch `AGENTS.md`, `VISION.md`, `ROADMAP.md`, `FOUNDATIONS.md`, `SPS3A-ANALYSIS.md`, or the handoffs.

So: I can't answer core questions 2, 3, 4, and 5 with any authority, because those hinge on files I didn't read. I **can** answer 1 and 6, and I've got sharp findings on **how v5 landed on main**, which turns out to be its own problem. If you want the full review, paste the five v5 files into chat and I'll redo this.

Everything below is based on what I actually read.

---

## 1. Verdict

The biggest v5 issue isn't inside the new files. It's that **v5 didn't finish landing on `main`**. `EVOLUTION.md` announces "three-tier framing retired, two layers one repo." But the two docs that a new agent (or a first-time human adopter) hits first — `README.md` and `DESIGN.md` §7 — still describe and sell the three-tier model. The review request itself points me at "`DESIGN.md` §7" for the retirement rationale. §7 on main is still titled "Versions and Scope" with a Minimal / Standard / Full table and the line "Standard and full versions build on it without contradicting it." The request directed a reviewer to a section that doesn't exist in the form described. An agent following the read order will land in a contradiction inside step 5.

That's the most concrete thing I can say. Everything else depends on files I couldn't open.

---

## 2. Answers to core questions

**1. Help or cost?** — *Partial answer.* I can't judge WHY-APPROACH.md or the graph without reading them. What I **can** say: the outer layer a first-hour agent touches (README + DESIGN.md) is currently a cost, not a help. It sells a mental model v5 retired. An agent pinning DESIGN.md and then reading EVOLUTION.md has to reconcile two versions of the same repo. That is exactly the "ceremony you step around to get to the code" failure mode the question is trying to detect — just coming from the wrong direction.

**2. Does WHY-APPROACH.md land?** — Can't answer. Didn't read it.

**3. Delta-layer discipline in new files.** — Can't check specific lines. But the inverse check raises a flag: DESIGN.md §7, as it stands on main, duplicates a framing that EVOLUTION.md explicitly retired. That isn't a delta-layer violation in the §2 sense (it's not redundant with the model/harness prompt), but it's a *staleness* violation — the doc contradicts another doc in the same repo. Same consequence as a delta-layer violation for the agent: they have to resolve conflict instead of work.

**4. Dogfooding — pulling its weight?** — Can't judge PRD.md or why-graph.xml directly. But the dogfooding claim is weakened by finding #1 above: if v5 is dogfooded (the project uses its own WHY layer to describe itself), then the project's own `README.md` and `DESIGN.md` are part of that dogfooding surface and they tell a pre-v5 story. Either the dogfooding includes README/DESIGN (and it's incomplete), or it doesn't (and the claim is smaller than it sounds).

**5. Voice.** — Can't judge new files. The v4-era voice in DESIGN.md and EVOLUTION.md still holds up — hooks like "polite compliance creates quiet failure" and "Leave the next agent a runway, not a crater" still land.

**6. Three-tier retirement — right call?** — *Probably yes, but the execution is half-done.* The EVOLUTION.md v4→v5 rationale is the strongest prose in the whole file: visual duplication between `STANDARD/` and `FULL/` folders, unclear canonicity, two real adopters (SPS3A + the TS adopter) independently converging on the same "two layers" shape. That convergence argument is the one that actually carries weight — it's evidence, not aesthetics. The call looks right. What's *not* right is that the retirement hasn't propagated to README.md or DESIGN.md §7. Until it does, the repo's own state is evidence against the decision — which is the worst kind of self-inflicted FUD for a protocol that has "Done Is Not a Mood" at its core.

---

## 3. File-specific notes

**`DESIGN.md` §7** is the most visible staleness point. The section is titled "Versions and Scope" and still carries the Minimal / Standard / Full table. The review request sends reviewers here *specifically* for the retirement rationale. That's a broken pointer. Fix the section or fix the pointer — don't leave both.

**`README.md`** — the doc table lists DESIGN/EVOLUTION/VISION/FOUNDATIONS/ROADMAP/SPS3A-ANALYSIS/handoffs but zero of the five new v5 files. The prose still reads: "There are standard and full versions with semantic code graphs, structured contracts, cross-session decision memory, and deterministic validation suites." In v5's framing that line is a fossil — it describes tiers that no longer exist. For a protocol whose whole pitch is that "done" means something, shipping v5 while the front door still markets the retired tiers is the exact failure mode the protocol names.

**`EVOLUTION.md` v4→v5** is the strongest single piece of writing I saw. Voice holds. Rejected-ideas list is specific. "Convergence between two independent adopters" is a real signal, not post-hoc justification. If someone asked me where the v5 spine actually lives, I'd point at this section — which is interesting because the request claims the spine is `WHY-APPROACH.md`.

---

## 4. Concrete rewrite proposals

**DESIGN.md §7** — current:
> "Agent1st Protocol exists in three intended scopes: Minimal / Standard / Full ... Standard and full versions build on it without contradicting it."

Proposed replacement (keep it short, link out for rationale):
> "## 7) Two Layers, One Repo
> Agent1st is delivered as two layers in one repo:
> - **Behavior layer** — `AGENTS.md`. Portable, ~200 lines, drop-in.
> - **WHY layer** — flat files in `docs/`. Optional for short work, recommended for long-lived projects.
>
> Earlier drafts split a `STANDARD/` and `FULL/` folder. That split was retired in v5 — it created visual duplication and unclear canonicity. Rationale and rejected alternatives: see `EVOLUTION.md` §v4→v5."

**README.md** — remove this line:
> "There are standard and full versions with semantic code graphs, structured contracts, cross-session decision memory, and deterministic validation suites."

Replace with a WHY-layer pointer, and add the five new v5 files to the doc table. If the doc table earns its place for DESIGN/EVOLUTION, it earns its place for WHY-APPROACH/PRD/why-graph/why-graph-principles/why-contracts.

---

## 5. What I'd reject / what I'd add

**Reject:** the claim "v5 has landed" in its current form. One file (EVOLUTION.md) announces it. Two files (README.md, DESIGN.md §7) contradict it. That's not landed; that's mid-merge.

**Reject the review request's pointer** to DESIGN.md §7 as the rationale source. It isn't. EVOLUTION.md is. Either update the request or update §7.

**Add:** a pre-merge consistency pass on any v-bump. Checklist-style, four lines: "Does README still describe the old framing? Does DESIGN reflect the new framing in every section where it's mentioned? Does the doc table list every shipped file? Does the read order in the request/PR description work end-to-end without hitting a contradiction?" This is a harness concern, not an AGENTS.md concern — it shouldn't go in the behavior layer. It belongs in a CONTRIBUTING or a v-bump PR template.

**What I'd have added if I could read the new files:** probably nothing more — the detailed file-specific questions in the request are better answered by someone who actually read `WHY-APPROACH.md`.

---

## 6. Three-tier retirement — one paragraph

The retirement itself is a good call. Two independent adopters converging on "two layers, one repo" is real evidence, not aesthetic preference, and the failure modes named (folder duplication, unclear canonicity) are the ones that actually hurt adoption at small scale. The "WHY layer is not a rung on a ladder" reasoning is also right — tiers imply ordering, and the WHY files aren't ordered above or below AGENTS.md, they're orthogonal to it. So: don't revert. **But don't call it landed until README.md and DESIGN.md §7 match the story EVOLUTION.md tells.** Right now the repo contradicts itself, and that contradiction is worse for adoption than either of the two framings would have been alone.

---

Roman, if you want the actual review your 4.6 colleague asked for — WHY-APPROACH.md landing as an idea, relation vocabulary in why-graph-principles.md, anti-patterns in why-contracts-v1.md §7, the PRD question — paste those five files in your next message and I'll do that pass. The review above is the one I could produce from the files I could actually read.