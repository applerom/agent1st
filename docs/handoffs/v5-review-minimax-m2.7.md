Received. I'm starting on your review now.



I'll read the file first to understand what needs to be reviewed.




I'll read all the relevant files to conduct a thorough review. Let me fetch them in parallel.




Now let me check the prior review documents to avoid re-proposing already-rejected patterns:



<div data-think="true" data-duration="214">
Now let me also read the FOUNDATIONS.md and some handoff files to understand what's been covered in prior reviews.


</div>





# Agent1st Protocol v5 — External Review

---

## 1. Verdict

The WHY layer solves a real problem — intent drift in long-lived, multi-agent projects — but it introduces a maintenance contract that sits uneasily with the "drop-in" promise that makes Agent1st worth adopting. The documents are well-written, the dogfooding is effective, and the philosophical spine of `WHY-APPROACH.md` is genuine. But two load-bearing weaknesses undermine the whole thing: (1) nothing in v5 addresses the case where the graph goes stale — which is the most common real-world failure mode — and (2) `WHY-APPROACH.md` §8 quietly violates the delta-layer principle it's supposed to exemplify. Fix those two things and v5 is solid. Leave them and the WHY layer becomes the ceremony it was designed to replace.

---

## 2. Answers to Core Questions

### Q1: Help or cost?

**Help, but conditionally.** Dropped into a project where the graph is maintained, validators run, and contracts are kept current — yes, the WHY layer makes my first hour meaningfully better. I read the PRD, I read the graph, I know what I'm working on, where it lives, and what couples to it. That is real value.

Dropped into a project where someone added the files months ago and nobody touched them since: I now have a stale graph I have to audit before I can trust it, contracts in files that don't match the code anymore, and a validation step that will fail. The ceremony cost of the WHY layer becomes visible precisely when the graph is stale or maintenance lapses. This is the scenario the documents don't address.

The inflection point is maintenance commitment, not documentation quality. The protocol is honest about "do not adopt when the project is a one-shot script" but silent on "do not adopt when nobody will keep the graph current." That gap is the most important thing missing from v5.

### Q2: Does `WHY-APPROACH.md` land as an idea?

Yes, and better than I expected. The philosophical spine is clear: intent drifts unless the repo carries it; make intent a first-class artifact; keep it paired with code; validate the pairing. That lands before the templates appear, which is the right order.

The document does not read as a glossy cover on a template pack. The key sentence — *"If you keep that idea and change every file name, you have still adopted the WHY approach. If you keep every file name and lose that idea, you have not."* — is the best one in the document and should be louder.

The one place it softens unnecessarily is §8 (the Required Reading header). More on that in structural notes below.

### Q3: Delta-layer discipline — any violations?

Yes, two quiet ones in the WHY layer itself.

**Violation 1:** `WHY-APPROACH.md` §6 says: *"the read order at session start is: AGENTS.md → PRD.md → why-graph.xml → why-graph-principles.md → why-contracts-v1.md."* Five files. Five files before I start work. This directly contradicts `AGENTS.md` §4 (Attention Engineering): *"keep one coherent objective per active iteration"* and *"if the first direct check answers the question, do not over-explore."* Reading five governance files before making a move is not one coherent objective — it's an onboarding task. The intent of §4 is clearly to prevent me from over-exploring *in the domain*. The §6 read order applies §4's over-exploration failure mode to the protocol layer itself.

**Violation 2:** `WHY-APPROACH.md` §8 proposes adding a Required Reading header to a project's copy of `AGENTS.md` — specifically **above** the Core section. `DESIGN.md` §2 and §5 explicitly prohibit adding repo-specific content to `AGENTS.md` and call it a delta-layer violation. The §8 header does exactly that. The document that teaches delta-layer discipline contains a section that violates delta-layer discipline, presented as the recommended adopter pattern. This is the most direct contradiction in the entire v5 delivery.

### Q4: Dogfooding — pulling its weight?

Yes, with one caveat. The PRD dogfoods well — it reads as a real product doc with real use cases and concrete acceptance criteria. `why-graph.xml` dogfoods the graph format effectively. Seeing "Agent1st's own PRD" mapped onto "Agent1st's own graph" is a teachable moment.

The caveat: the graph includes `DOC_*` nodes for all the governance files (AGENTS.md, why-graph-principles.md, etc.). These are governance artifacts, not implementation nodes. A DOC_* node pointing to a markdown file that explains how to read the graph is meta-content — it teaches the teaching tool. This works as a dogfooding example but creates a category that agents reading the graph for navigation purposes have to learn to filter out. The principles document mentions the domain-graph vs. governance-graph distinction but doesn't resolve where meta-nodes belong.

**Verdict:** dogfooding is the right call and works. The DOC_* treatment is the one place it creates confusion rather than clarity.

### Q5: Voice — diluted or holding?

Mostly holding. The voice is strongest in `AGENTS.md` and `DESIGN.md`. The WHY layer files are more instructional in tone (which is appropriate for reference docs) but maintain the directness.

The weakest file is `WHY-APPROACH.md` §8. It reads as implementation notes for an adopter pattern rather than as something meant to be read by a working agent. The tone shifts from "here's an idea" to "here's how you operationalize it" without the same energy. It's the only section that reads like internal documentation leaking into the protocol.

### Q6: Three-tier retirement — right call?

Yes. The minimal/standard/full framing created a graduation-gate expectation that caused confusion in practice. The distinction that matters is not "how much of the protocol do I adopt" — it's "behavior layer vs. intent artifacts." That distinction is cleaner and more honest about what the WHY layer actually is: not a more-complete version of the same thing, but a different kind of artifact solving a different kind of problem.

What was not lost: "standard version" thinking survived as project-local extensions sitting on top of both layers. This is actually a better fit. Standard-version content (CI integration, observability contracts, acceptance automation) is correctly project-local — it doesn't need to be portable, it needs to be extendable from. Moving that concern out of the protocol and into the extension layer is the right structural call.

---

## 3. File-Specific Notes

### `why-graph-principles.md` — Relation vocabulary

**Assessment:** Right size, but one synonym pair worth flagging.

`HOSTED_BY` and `DELEGATES_TO` are semantically adjacent in a way that could cause confusion. `HOSTED_BY` (API is hosted by a route handler) and `DELEGATES_TO` (API delegates work to a service module) both describe where work gets done — the distinction is about whether the API "is" the handler or "calls" the handler, which is subtle enough that an agent maintaining the graph might use the wrong one without noticing.

Recommendation: add a one-sentence clarification distinguishing them, or collapse into one relation with a clarifying attribute. Not urgent, but worth a note.

Everything else in the vocabulary is defensible. `WILL_TOUCH` / `WILL_CREATE` for planned work is a good addition — orphan features are a real drift signal, and planned-but-not-yet nodes make the graph useful before implementation starts.

### `why-contracts-v1.md` — Anti-patterns in §7

The anti-patterns are solid and the rule of thumb at the end (*"if an anchor doesn't help an agent answer 'what is this region for and what depends on it,' it's noise"*) is the best line in the document.

On "one language example enough": Python + TypeScript both earn their tokens here. The contrast between Python comment-block style (`# START_METHOD_...`) and TypeScript JSX-comment style (`// START_METHOD_...`) is genuinely useful — it shows that anchor syntax adapts to language idioms, which reinforces the "adapt the format" message.

The one gap: TypeScript doesn't have a method-contract example. The class-contract example (`HomePageClient.tsx`) shows a module header and block anchors, but no `START_METHOD_*` with a full `START_CONTRACT` block. Python has `embed` with a full method contract. TypeScript needs the parallel example for the dogfooding to be symmetric.

### `why-graph.xml` — Teaching size and inline commentary

~150 lines is right. The inline annotations (`WHAT` children on nodes) add genuine value — they read as teaching notes rather than just label text. The risk is annotation drift: if a node's behavior changes and the annotation isn't updated, the annotation becomes misinformation. The principles document says this but doesn't give a detection mechanism.

Recommendation: add a lightweight note in the principles doc about annotation maintenance, or a validator rule that catches `freshness` attribute mismatch with annotation date.

### `PRD.md`

Strongest dogfooding signal in v5. The problem statement is precise, the features table is concrete enough to be actionable, the definition of done is actually measurable, and the open questions in §10 are genuinely open — not decorative filler. This is a real PRD that a team could actually use as ground truth.

---

## 4. Concrete Rewrite Proposals

### Proposal 1: Delete `WHY-APPROACH.md` §8 (Required Reading Header)

**Location:** `docs/WHY-APPROACH.md` §8

**Current text:**
> When you adopt the WHY layer in your project, add a small header block **above** the Core section of your project's copy of `AGENTS.md`:
> markdown
> ## Required Reading
> Before substantial work, read in order:
> - `docs/PRD.md` — product truth
> ...

**Proposed replacement:**

Delete the section entirely, or replace with:

> When you adopt the WHY layer in your project, pin these files at session start using your harness's memory mechanism (e.g., Claude Code `MEMORY.md`, intent1st skills, or project read-order notes in `CLAUDE.md`). The behavior layer (`AGENTS.md`) remains unchanged.

**Why:** `DESIGN.md` §5 explicitly prohibits repo-specific reading lists in `AGENTS.md`. `DESIGN.md` §2 calls this a delta-layer violation. The §8 header does exactly what the design principles say not to do. The intent — telling agents what to pin — is legitimate. The mechanism — editing the portable core — is not.

---

### Proposal 2: Add a Graph Staleness section to `WHY-APPROACH.md`

**Location:** `docs/WHY-APPROACH.md`, new section after §7

**Proposed text:**
> ### When the graph goes stale
>
> The WHY layer's most common failure mode is a graph that no longer matches the code. An anchor points to a deleted marker. A feature node has no implementation edges. A module's contract is missing. This happens when:
> - code is edited and the graph is not updated in the same commit
> - a refactor lands and nobody updates the contracts
> - validators are not run and drift accumulates silently
>
> **If you encounter a stale graph:** treat it as a drift signal, not a maintenance failure. Do not ignore it and do not retrofit the whole graph from scratch. Instead:
> 1. Run the graph↔anchor validator. Mark every failure.
> 2. Pick the file you are about to touch anyway.
> 3. Fix the contracts and anchors for that file as you go.
> 4. Update the graph in the same commit.
>
> **If no validator exists yet:** this is the first thing to build. Even a script that checks every `<ELEMENT>` in the graph points to a real `START_*` marker in a real file is enough. Without this, the graph will rot.
>
> A stale graph is not the end of the WHY layer. It is the moment the WHY layer proves its value: the validator catches what would otherwise silently diverge.

**Why:** Staleness is the most common real-world failure mode and the one the current documents are most silent about. Naming it explicitly and giving a recovery protocol transforms a silent trap into a CDD-able problem.

---

### Proposal 3: Clarify §6 read order with a qualifier

**Location:** `docs/WHY-APPROACH.md` §6

**Current text:**
> When you sit down in a project that uses this layer, the read order at session start is: [5 files listed]

**Proposed replacement:**
> For the first session in a project that uses this layer, read in this order: [5 files listed]. Pin PRD and graph for the session. The other two are reference files — read them when you touch the relevant artifact, not before every move.
>
> For returning sessions, start from the graph and your current task. Read other docs only as needed.

**Why:** The current §6 read order makes sense for onboarding but reads as mandatory ceremony for every session. Adding "pin PRD and graph" as the operative instruction and clarifying the others are reference files (not pre-work) aligns with `AGENTS.md` §4's attention discipline.

---

## 5. What I'd Reject / What I'd Add

### What I'd reject

**`WHY-APPROACH.md` §8 as written.** The delta-layer violation is real and it undermines the document's credibility as a teacher of the delta-layer principle. The Recommended Reading header is the right *intent* (tell the agent what to pin) with the wrong *mechanism* (editing the portable core). Reject the mechanism, not the intent. Replace with harness-native pinning instructions.

**Any proposal to add validator tooling as a v5 deliverable.** The dogfooded example is enough. Building tooling into the protocol creates a "not invented here" dependency problem — teams that want validators will build them for their own stack. The principles document that explains what validators should check is the portable artifact; the validator scripts are correctly project-local. Leave tooling to v6 as a separate discussion.

### What I'd add

**A Graph Adoption Criteria checklist.** Before a team commits to the WHY layer, they should answer: (1) Will this project live longer than one feature cycle? (2) Will more than one agent edit it? (3) Can we commit to running graph↔anchor validation at least weekly? If the answer to (3) is no, the graph will go stale and become a liability. The WHY layer needs a "should we adopt this?" section that names the staleness failure mode explicitly and asks teams to assess their maintenance commitment honestly.

**A one-paragraph section on "what to do when the graph is wrong."** Sometimes I land in a project and the graph is wrong — features don't map to the right files, contracts describe intent that the code no longer reflects, anchors are missing. The current documents don't tell me whether I should fix the graph first, fix the code first, or flag it via CDD. A brief decision guide would close this gap.

---

## 6. My Take on the Three-Tier Retirement

The right call, and the reasoning in `EVOLUTION.md` is honest about why: the parallel `STANDARD/` and `FULL/` folders created visual duplication and confusion about which file was canonical. The real distinction turned out to be behavior vs. intent-artifacts, which is a cleaner and more durable framing than a ladder of completeness.

What I notice as a working agent: the "standard version" didn't disappear — it dispersed. What used to be "standard version content" is now project-local extensions sitting on top of both layers. CI integration, acceptance automation, observability contracts, runbooks, custom skills — all correctly project-local, not published separately. This is actually a better structural fit. Standard-version thinking is inherently project-specific; treating it as a separate tier implied it was portable in a way it isn't.

The one thing the retirement conversation undersells: the two-layer framing makes the adoption decision clearer. "Do I need intent-to-code navigation?" is a better screening question than "Am I minimal, standard, or full?" The latter invited teams to treat "standard" as a target to reach. The former invites teams to ask whether the problem they're solving actually requires the solution.

---

**MiniMax Agent** | Agent1st Protocol External Reviewer