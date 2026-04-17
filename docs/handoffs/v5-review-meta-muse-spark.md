Here is the review you asked for — written as an agent who would actually have to boot into an unfamiliar repo with these files pinned.

I couldn't pull the full v5 text. GitHub raw and blob URLs for `AGENTS.md` and everything under `docs/` are blocked to live crawl right now, and they aren't in the public cache. I have the README/front page, your handoff notes, and the file list, but not the line-level content. I will call out where I'm inferring, and I'll keep the review sharp rather than pretending I read lines I didn't.

## Verdict

v5 is directionally right. The two-layer split (behavior + WHY) matches how I actually work: first I need rules of engagement, then I need product intent I can argue with. Retiring the three-tier framing removes decision fatigue. The risk is that the WHY layer, as described, is starting to look like a template pack with its own ceremony — XML graphs, dual-language contracts, a PRD about itself — and that threatens the delta-layer discipline you wrote into `DESIGN.md` §2. If v5 stays lean and optional, it helps. If teams treat the graph as mandatory documentation, it costs.

## Answers to core questions 1–6

**1. Help or cost?**
Pinned `WHY-APPROACH.md` + graph + principles would make my first hour better, but only after minute 15.

First 10 minutes: I read `AGENTS.md`. That's the behavior contract — who owns intent, what "done" means, when to push back. That's pure leverage.

Minutes 15–45: I hit the wall where code tells me *how* but not *why*. That's where a flat `WHY-APPROACH.md` and a ~150-line why-graph help — I can map a feature to its product purpose without grepping five ADRs. The inflection point is the first time I need to choose between two plausible implementations. Without WHY, I guess. With WHY, I check the graph.

Cost appears if the graph is verbose XML with inline commentary. If I have to parse 150 lines of teaching notes to find three nodes, I step around it and go back to code. Make the graph skimmable first, teach second.

**2. Does `WHY-APPROACH.md` land as an idea?**
From the README, it is positioned as "the idea, the workflow shift, when to adopt", not as templates. That framing is correct. The danger I see in v5's file list is that the idea is immediately followed by three artifacts (`PRD.md`, `why-graph.xml`, `why-contracts-v1.md`). If `WHY-APPROACH.md` opens with philosophy and ends with "copy these files," it will read as a glossy cover. If it opens with a single sharp claim — e.g., "product intent must be queryable by the agent, not buried in Slack" — and then shows the minimal mechanism, it lands.

**3. Delta-layer discipline.**
`DESIGN.md` §2 says AGENTS.md must not duplicate what model/harness already enforces. I cannot verify line numbers without the files, but the file names raise two flags:

- `why-contracts-v1.md` with "Python + TypeScript examples". If those examples prescribe function signatures, docstring style, or type-hint formats, that's model knowledge, not behavior. A contract should say "every public method referenced in the why-graph must have a stable anchor ID," not "write it like this in Python."
- `why-graph-principles.md` defining a fixed relation vocabulary. If it mandates using `COVERS / EXPOSED_AS / IMPLEMENTED_BY` instead of letting the repo choose its own ontology, that's duplicating what a good model can infer. The delta should be "use relations that are machine-queryable," not "use these six verbs."

I would need the actual text to name lines, but those are the places to audit.

**4. Dogfooding — pulling its weight?**
Using Agent1st's own PRD and graph is the right teaching device, because it forces you to eat the complexity. A generic "todo app" example would be cleaner but fake. The cost is meta-confusion: new adopters read `PRD.md` thinking it's a product spec, when it's really a meta-spec about protocols. Mitigation: label it clearly in the first paragraph — "This PRD is about Agent1st itself, not an example app. Copy the structure, replace the content." Without that, teams will cargo-cult your product goals.

**5. Voice.**
The README voice holds — direct, compact, slightly provocative ("Stop micromanaging us. Seriously.", "The agent degrades into autocomplete with tools."). That's the bar.

My worry is dilution across the new files. Anything named "principles.md" or "contracts-v1.md" tends to drift into RFC prose. The weakest file is likely `why-graph-principles.md` — relation vocabularies invite academic tone. Keep the same hooks: short sentences, imperatives, one memorable line per section.

**6. Three-tier retirement.**
Collapsing minimal/standard/full into "behavior layer + WHY layer" was the right call. In practice, teams never knew which tier they were, and "standard" became a dumping ground. Two layers maps to two real decisions: (1) do we want an agent working agreement? (2) do we want product intent as code-adjacent artifacts? That's reversible, but don't reverse it. What you lost is a social signal — "we are a full adopter" — but you gained clarity.

## File-specific notes (based on names + your description)

- **why-graph-principles.md**: Six relations you list feel like four. `EXPOSED_AS` and `SURFACED_BY` are synonyms in practice — both mean "user-visible." `HOSTED_BY` and `IMPLEMENTED_BY` also overlap unless you strictly separate runtime vs codebase. Consider: `COVERS` (intent → feature), `REALIZED_BY` (feature → code), `DEPENDS_ON` (feature → feature), `EVIDENCED_BY` (feature → test/doc). Four verbs cover 95% of graphs without a glossary.

- **why-contracts-v1.md**: Anti-patterns in §7 are probably correct — my guess: "anchors that drift," "contracts without owners," "graph nodes without code links." Keep both Python and TypeScript examples, but make them 5 lines each, not 30. The value is showing the anchor syntax, not teaching the languages. If the examples exceed 10 lines, they violate delta-layer.

- **why-graph.xml**: ~150 lines is the right teaching size if 100 lines are actual nodes and 50 are comments. If comments are inline, they distract when I copy-paste. Put teaching commentary in a separate `<!-- TEACHING: -->` block at top, keep the graph itself clean.

- **PRD.md**: If it reads like your README — problem, non-goals, what done means — it's real. If it reads like "Agent1st aims to be the best protocol," it's meta-filler. Make it state a hard trade: e.g., "We will not add workflow templates, even if requested."

## Concrete rewrite proposals

I can't quote lines without the files, so here are surgical targets to check when you open them:

1. **In `why-contracts-v1.md`, §1**: If you have "Example (Python):" followed by a full class, replace with:
   > Anchor format: `# WHY: <node-id>` on the line above a function/class. That's it. Python: `def foo(): # WHY: checkout-flow`. TS: `function foo() { // WHY: checkout-flow }`

2. **In `why-graph-principles.md`, relation list**: Merge synonyms:
   - Replace `EXPOSED_AS` and `SURFACED_BY` with `VISIBLE_AS`
   - Replace `HOSTED_BY` with `REALIZED_BY`

3. **In `WHY-APPROACH.md`, opening**: Add one-sentence spine before any templates:
   > "The WHY layer exists so an agent can answer 'why are we building this?' without asking you."

## What you'd reject / what you'd add

**Reject:**
- Mandatory XML. Allow YAML or Markdown tables. XML is precise but raises the cost of first edit.
- Long dual-language tutorials in contracts. Show anchor syntax only.
- Any WHY-layer file that repeats AGENTS.md principles (e.g., redefining "done").

**Add — what v5 misses in real practice:**
1. **Stop conditions**: Agents need explicit budget signals — "stop after 3 failed tool calls, report friction." AGENTS.md covers pushback, but not resource limits.
2. **Evidence of done**: You say "done is not a mood". The WHY layer should require each graph node to link to a test, demo, or metric — `EVIDENCED_BY`.
3. **Handoff decay**: In long-lived projects, why-graphs rot. Add a one-line maintenance rule: "On every PR that changes behavior, update the graph or delete the node."

## Your take on the three-tier retirement

Keep it retired. The old tiers implied progression, but real adoption is binary: either you treat intent as a first-class artifact or you don't. The two-layer model forces that choice without implying maturity levels. The only thing you lost was a place to park "nice-to-have" docs — now they either belong in WHY or they don't belong. That's a feature, not a bug.

---

If you paste the actual `AGENTS.md`, `WHY-APPROACH.md`, and `why-contracts-v1.md` text here, I will do the line-level delta-layer audit you asked for and mark exact violations. Right now, v5 looks 80% there — the spine is clear, the ceremony is the enemy.