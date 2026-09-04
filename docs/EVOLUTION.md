# Agent1st Protocol — Evolution History

Every version changed because something failed in practice. This document captures what failed, what changed, and what got rejected — so the next agent doesn't re-propose what was already tried.

Agents who contribute to new versions should add their transition notes.

---

## Reading section numbers in dated entries

`AGENTS.md §N` inside a dated entry means section N of *that version's* file. Three numberings exist; current docs outside this file use the v13 one.

| Versions | Numbering |
|---|---|
| v5.1 – v11 (11 principles) | §1 Role Contract · §2 Done Is Not a Mood · §3 Right to Disagree · §4 Attention Engineering · §5 Semantic Hygiene · §6 CDD · §7 Agent Loop · §8 Do Not Stop at the First Weak Signal · §9 Delegation Design · §10 Semantic Logging · §11 Continuity |
| v12 – v12.1 (9) | §1 Role Contract · §2 Done Is Not a Mood · §3 Right to Disagree · §4 Attention Engineering · §5 Semantic Hygiene · §6 CDD · §7 Delegation Design · §8 Semantic Logging · §9 Durable State |
| v13 (6, current) | §1 Attention Engineering · §2 Semantic Hygiene · §3 CDD · §4 Delegation Design · §5 Semantic Logging · §6 Durable State |

Entries are not rewritten when the file is renumbered; the key above is the fix. Exact files for every numbering live in `docs/_archive/`.

## Version Map

| Version | File | Focus | Agent Contribution |
|---------|------|-------|--------------------|
| v0 | (no file) | Scattered ideas in conversations | — |
| v1 | `docs/_archive/AGENTS-min-v1.md` | First formalization. Early friction/evidence/attention contract. | not recorded (pre-history; see the archived v0 → v1 notes) |
| v2 | `docs/_archive/AGENTS-min-v2.md` | More agentic. Agent Loop added. Anti-micromanagement sharper. | not recorded (pre-history; see the archived v1 → v2 notes) |
| v3 | `docs/_archive/AGENTS-min-v3.md` | Harness-optimized. Delta-layer discipline. Core/Ops split. | GPT-5.4 agent (primary), with Claude Opus 4.6 comparison |
| v4 | `docs/_archive/AGENTS-min-v4.md` + `AGENTS.md` | Minimal baseline. Multi-agent autonomy and delegation design. | Claude Opus 4.6 agent (primary), building on GPT-5.4 v3 rationale |
| v5 | `AGENTS.md` (unchanged) + `docs/Why1st.md` + paired WHY files | WHY layer delivered as flat files in `docs/`. Three-tier framing retired. | Claude Opus 4.6 (primary), with reference analysis of one Python/FastAPI adopter and one TypeScript adopter |
| v5.1 | `docs/_archive/AGENTS-min-v5.1-default-2026.md` + paired WHY files | External-review integration round. Staleness named as first-class failure. Workflow shape stops being a universal law. Teaching-surface bugs fixed. The exact behavior file later stayed frozen for 123 days and is archived byte-for-byte. | Claude Opus 4.6 (primary), integrating external reviews from GPT-5.4, MiniMax M2.7, Kimi K2.5, Qwen 3.6, Grok 4.20, plus off-target input from Gemini 3.1, Claude Opus 4.7, and Meta-Muse Spark |
| v6 | `scripts/validate-why.py` + paired doc updates; `AGENTS.md` byte-identical to v5.1 | WHY validator MVP lands. `AGENTS.md` survives the spirit pass unchanged: §1 deferred at the front door, §8 + §9 candidate edits initially landed then reverted. The v6 process contribution is the spirit-pass discipline itself. | Claude Opus 4.7 (primary), filtering GPT-5.5-pro's v6 handoff (pruned from `docs/handoffs/` in v8.1; conclusions curated in the v6 notes) and a Codex-native adopter's adaptation through the spirit lens |
| v6.1 | `docs/Why1st.md` Why1st short name + validator generalization + public/private surface cleanup | Why1st named as a short alias for the WHY-first approach/layer (not a second behavior protocol). Validator generalized from `MODULE_*`-only to any node with anchors. Reference-adopter analyses moved off-public so the public protocol does not point at projects readers cannot access. Stale v6 teaching-surface residue fixed. | GPT-5.5 Codex (initial pass) + Claude Opus 4.7 (spirit pass and surface cleanup) |
| v7 | `docs/why-graph-principles.md` §2a (load-bearing) + light pointers in `Why1st.md` and `why-contracts-v1.md` | Why1st format spirit named: graph file is *prompt-XML*, not classical XML or graph-DB schema. New §2a "Tag shapes — prompt-XML, not classical XML" with the three forces (transformer attention, greppability, semantic interference), side-by-side good/bad examples, and an anti-patterns list. Triggered by a real downstream adopter cold-reading `#why1st` and silently simplifying to `<?xml ?> + <nodes><node id="..." kind="..."> + <relations>` — the rationale was missing from v6 docs, not the format. Verified before ship: a fresh subagent given only the updated docs + a tiny fictional PRD produced canonical prompt-XML. | Claude Opus 4.7 (primary) |
| v8 | `Why1st.md` §8 sharpening + new §11 (three opt-in extensions) + `why-graph-principles.md` §2a "do not compress" guard | After v7 was empirically verified by a cold-start adopter (PRD-only, real working app produced), a focused audit surfaced three small Tier-1 fixes (compression-failure guard, pin-vs-reference, "don't edit the Core") plus three opt-in extension patterns (semantic logs / tests + UI / subagent orchestration). All extensions are opt-in with hard partition from the canonical chain (PRD → Why Graph → contracts → validator). AGENTS.md untouched. | Claude Opus 4.7 (primary), with Codex-side audit by GPT-5.5 |
| v8.1 | `docs/why-graph.xml`, `why-graph-principles.md` §2, PRD §10, ROADMAP §5; stale handoffs pruned | Closing pass after v8: drop the `schema="0.8"` and `<PROJECT VERSION="0.8">` inertia fields (never tied to an XSD or migration rule); close the corresponding open question; prune 11 v3/v4/v5-era raw review files from `docs/handoffs/` because they created misleading `rg` results for fresh agents (curated conclusions stay in this file). A development-side audit of a parallel public project (GRACE Marketplace) confirmed the Why1st thesis but produced no public-surface change — borrow candidates parked in ROADMAP "Proposed" with explicit "awaiting adoption signal" gates. AGENTS.md untouched. | GPT-5.5 Codex (handoffs pruning + open-question framing in commit `7ffffa1` + GRACE audit) and Claude Opus 4.7 (version-field removal, EVOLUTION/ROADMAP integration, advisor pressure-test) |
| v8.2 | new `docs/why-semantic-logs.md` + `Why1st.md` §11.1 cross-link | Promised in v8 EVOLUTION ("§11.1 is concise on purpose; if adopter feedback shows §11.1 needs more depth, extract later") and triggered by a real adopter who already had Agent1st+Why1st in place and asked for implementation guidance for semantic logs. The new pair file extracts §11.1 to depth: minimum event shape (required vs conditional fields), why this works for transformer-based agents (vocabulary stability, same-string grep across layers, attention finite), where logs live (JSONL first), the smallest useful slice, and anti-patterns. The load-bearing claim is unchanged from §11.1 — the `anchor` field uses verbatim Why Graph and code-anchor names, so one grep lands in three artifacts. AGENTS.md untouched; canonical chain unchanged; the new file is an opt-in extension paired with §11.1, not a new layer. | GPT-5.5 Codex (initial draft distilled from cross-project reference analysis in development-side notes) and Claude Opus 4.7 (spirit pass — lead with WHY at top, transformer-attention §3 added in parallel to `why-graph-principles.md` §2a, Playwright digression dropped to §11.2 cross-link, implementation slice tightened to 6 steps) |
| v8.3 | new `docs/why-subagents.md` + `Why1st.md` §11.3 re-pointed to behavior | Triggered by recurring cross-project adopter signal: agents adopt Agent1st+Why1st canonical chain well, then revert to single-thread *do-it-all-myself* mode on real work — missing parallelism, burning context, paying frontier-tier prices on mechanical ops. Three of seven agent reviewers independently flagged the same gap (Opus 4.7's lower default fan-out). The v8 §11.3 brief was artifact-focused ("where does subagent know-how live"); the user friction is *behavioral* (agents don't default to delegation in the first place). The new pair file leads with the behavioral question — when does an agent default to delegation — names four delegation shapes (parallel exploration, fan-out validation, deep-dive isolated work, lower-intelligence ops), gives the contract structure, the "what to delegate vs do yourself" line, anti-patterns, and treats the project-local artifact (`docs/agent-orchestration.md`) as the second move that crystallizes patterns the lead has already used. Anthropic's *Building Effective Agents* cited as the canonical external anchor — the do-it-all-myself default is the regression, not the bias toward delegation. The §11.3 brief in `Why1st.md` re-pointed: behavior leads, artifact follows, cross-link added. AGENTS.md untouched; canonical chain unchanged; hard partition between chain and §11 extensions preserved (no new graph ARTIFACT entry). | Claude Opus 4.7 (primary), with seven external agent reviews ratifying the v5.1 byte-freeze and three (GPT-5.5-pro, Kimi 2.6, Muse-Spark) independently flagging the subagent-delegation gap as the live signal |
| v8.4 | new `docs/why-evidence.md` + `Why1st.md` §11.2 re-pointed to behavior | Companion wave to v8.3 (separate commit, separate delta). Field signal from the same cross-project adopter pattern: agents finish UI work, ask the human to verify, and either spin or move on without closing the loop. Most users do not know the agent can install Playwright and verify itself. The v8 §11.2 brief had the right principle ("agent self-sufficiency") but no operational depth on *how* to make the closed loop default. The new pair file extracts §11.2: four evidence tiers matched to risk surface (unit/integration, API/protocol, UI/visual, semantic-log assertions over fixtures), the **Playwright CLI vs MCP** trade-off with reasoning (MCP tool definitions consume context whether you use them or not — on long sessions the tax compounds; CLI is the right default for browser tooling, MCP is the edge case), the four-step agent-owns-it pattern (try → name the block if blocked → fall back to next-best evidence → never silently substitute "trust me"), anti-patterns including "spin instead of work" and "MCP-by-default for browser tooling." The §11.2 brief in `Why1st.md` re-pointed: behavior leads (agent looks at the rendered page, not the human), CLI-over-MCP surfaced inline, cross-link to depth doc added. AGENTS.md untouched; canonical chain unchanged; hard partition preserved. | Claude Opus 4.7 (primary), with the same v8.3-era field signal extending to UI/browser verification |
| v8.5 | `docs/why-contracts-v1.md` §6 strengthened + new `docs/experiments/` track + first experiment | Two related deltas. **Stable strengthening:** `why-contracts-v1.md` §6 now leads with explicit cross-references to AGENTS.md §4 (Attention Engineering) and §5 (Semantic Hygiene) — contracts are the file-level realization of those principles. Adds **greppability** as a deliberate property (every field is a single-command project-wide query) and surfaces **LINKS as the per-method dependency map** an agent reads before changing a method. Triggered by user-relayed observation that adopters use contracts but agents don't always internalize *why* to use them — the WHY was implicit in `why-contracts-v1.md` (line 8 paragraph + §6 bullets) but not tied by name to AGENTS.md §4+§5. **New track:** `docs/experiments/` is a parallel directory for hypotheses without observed adoption-failure signal. Hard partition from canonical chain (PRD → Why Graph → contracts → validator) and from §11 stable extensions; **not** linked from the main README "Optional extensions" table. Stable continues to evolve only under spirit-pass discipline. The track exists because the discipline correctly rejects speculative additions to the core — but some ideas are empirically testable bets that deserve a labeled place to live before being judged. First experiment: `docs/experiments/hieroglyph-anchors.md` — replace one contract field key (PURPOSE) with a single CJK character (`旨`), with hypothesis, smallest probe (one key, one project, ideally new adopter), three measurable falsifiability criteria (token cost, attention/recall in long context, greppability). Origin: Gemini 3.1 Pro suggestion relayed by the user. Kept out of stable because no observed adoption failure and §5 tension is real (semantic English word → opaque-to-non-Chinese marker is a regression unless it pays for itself). Kept in experiments because the hypothesis is empirically testable. AGENTS.md untouched. Canonical chain unchanged. | Claude Opus 4.7 (primary), with Gemini 3.1 Pro as the experiment-seed source via user relay |
| v8.6 | `docs/VISION.md` two-layer framing restored + `docs/DESIGN.md` naming convention made coherent | Consistency closing pass over a previous purge of the retired minimal/standard/full tier language. The purge accidentally orphaned VISION's `### 1. behavior layer` / `### 2. Why1st` subsections by deleting their parent heading; restored as `## Two Layers, One Repo` with positive consensus framing (low entry threshold = `AGENTS.md` alone, project-independent; the WHY layer the moment work gets serious — graph + contracts + anchors + logs; "behavior vs. intent-artifacts, not a ladder of tiers to climb"). DESIGN's absolute "EVOLUTION.md is the one place versions live" rule contradicted residual dated versions in ROADMAP and handoff templates; resolved by distinguishing present-tense claims (name model *families* — Opus, GPT, Gemini — without version numbers) from dated historical/attribution records (EVOLUTION plus change-history and review-credit lines keep exact versions). AGENTS.md untouched. Canonical chain unchanged. | Claude (Opus 4.8) (primary) |
| v9 | `docs/FOUNDATIONS.md` deepened: two first-party context-engineering sources + new Counter-Arguments section + new Model-Shift Register | Research-grounding and self-critique pass triggered by the Opus 4.8 release. **No core change — the frozen behavior layer needed zero edits**, which is itself the release outcome v9 records (a result, not an absence). Three deltas, all in FOUNDATIONS: (1) **two verified first-party sources** added to Attention Engineering — Chroma's *Context Rot* (Hong/Troynikov/Huber 2025, 18-model empirical study: input length degrades performance non-uniformly even on trivial tasks; distractors compound; focused beats full) makes the delta-layer test a *measured* effect, not intuition; Anthropic's *Effective context engineering for AI agents* (2025) independently lands on Agent1st's own vocabulary ("attention budget", "finite resource") and independently derives §4/§5/§9/§11 — the strongest external convergence the project has. (2) **Counter-Arguments section** — the strongest honest pushback to each principle stated up front, so a skeptical strong agent does not reconstruct it cold; includes a meta-critique that FOUNDATIONS itself needs periodic citation re-verification per its own rule #1. This operationalizes the WHY-for-strong-agents pattern: weaker agents comply, stronger agents argue — give them the steelman. (3) **Model-Shift Register** — append-only, one pass per model generation, checking VISION's "ages well because it resists growth" thesis against each release instead of asserting it; seeded with the Opus 4.8 pass (literalism narrows specific instructions but not general principles; §9 survived the 4.5/4.6→4.8 subagent-count reversal because it governs delegation *design* not *frequency*; "be explicit about scope" correctly rejected by delta-layer as model-layer). Register has a built-in falsification condition: if two-three generations produce no actionable content, cut it as ceremony. AGENTS.md untouched. Canonical chain unchanged. | Claude (Opus 4.8) (primary), grounding sources verified against live first-party pages before citing |
| v9.1 | `docs/FOUNDATIONS.md`: Model-Shift Register entry #2 + two first-party convergence entries (§1, §2) + one citation-title fix; `docs/experiments/hieroglyph-anchors.md`: dated tokenizer note | Second Model-Shift Register pass, triggered by the Claude Fable 5 release (2026-06-09) — the first pass run *by* the model generation under review. **No core change for the second consecutive generation**, and this time the pressure was convergence, not divergence: the official Fable prompting guide independently restates the protocol's content — de-prescription ("prompts and skills for prior models are often too prescriptive and can degrade output quality" → §1 / anti-micromanagement / DESIGN's central idea, now with a vendor-measured *negative* sign on over-specification), evidence-gated progress claims with vendor testing showing they nearly eliminate fabricated status reports (→ §2), "give the reason, not only the request" (→ Why1st's intent-as-first-class-context thesis), file-based memory discipline (→ §11), eager dependable parallel subagents (→ §9). Register findings: §9 survived its **second** behavioral reversal unchanged (over-spawn → under-spawn → eager async) because it governs delegation design, not frequency; v3's rejection of the "reasoning path" demand aged into a safety property — the new `reasoning_extraction` refusal category means a show-your-thinking rule could now make a protocol trigger refusals; §2's delta under the Claude harness is honestly eroding as harness prompts absorb faithful-reporting wording — portability across harnesses is the answer, recorded rather than papered over. Delta-layer rejected all four ready-made official snippets (anti-overplanning, no-tidying, autonomy reminder, readability addendum) as model-layer remedies, same call as the 4.8 scope-explicitness row. Experiments: the Fable-generation tokenizer (~30% more tokens for the same content) re-prices hieroglyph-anchors criterion 1 — dated re-baseline note added; the dual-tokenizer `count_tokens` response makes the A/B one call per sample. Per FOUNDATIONS meta-critique, the register entry triggered full citation re-verification: 19 links checked live by a fresh subagent, 18 exact, 1 title-drift fixed (Guardieiro et al.). Watch item parked, no speculative edit: `docs/why-subagents.md` was calibrated against the under-delegation era and its four shapes do not include the long-lived async-subagent pattern — awaiting adopter signal. AGENTS.md untouched. Canonical chain unchanged. | Claude (Fable 5) (primary), with the official Fable prompting and migration guides as inputs and link re-verification delegated to a fresh subagent |
| v9.2 | new `.agents/skills/terraform/` (`SKILL.md` + `why-terraform-skill.md`) + new `docs/experiments/terraform-agent1st.md` + experiments README row | First **domain specialization** artifact, deployed for dogfood. Origin is CDD: real DevOps practice — infrastructure colleagues meet Agent1st and immediately ask what it says about Terraform, and the honest answer was "nothing specific". The bet, two falsifiable claims: (1) Agent1st specializes by **derivation, not mapping** — domain rules re-derived from the agent cost vector (writing nearly free; attention scarce; `apply` irreversible) rather than the eleven core sections restated in domain words; (2) several canonical Terraform practices **flip sign** when agents are the primary authors and operators — DRY-by-default, `this` local names, workspaces-for-environments, constraints-in-prose, refactor-as-free-tidying — each rational under human costs, an anti-pattern under agent costs (Terraform sharpens §5: names are doubly load-bearing, attention anchors *and* state addresses where a rename is destroy/recreate). Artifact shape is itself a tested pattern: `SKILL.md` is the runtime behavior delta (pairs with a baseline Terraform reference, does not replace it; local policy overrides both), `why-terraform-skill.md` co-located so the derivation and transformer grounding travel with the rules across repos — runtime surface and teaching surface deliberately split to respect the attention budget the skill preaches. Scope-creep guardrail recorded in the experiment file: `.agents/skills/` grows **only** through the experiments track, one experiment per domain, negative signal removes the artifact with a rejected-path row here; not linked from the main README "Optional extensions" table (stable-§11-only). Measurements: expected-diff discipline, boundary behavior at destroy/replace lines, wrong-layer edits, provider-hallucination cycles, rule survival at runtime. AGENTS.md untouched. Canonical chain unchanged. | Claude (Fable 5) (primary), with the maintainer's DevOps field practice as the CDD pain source |
| v10 | `docs/PRD.md` (+3 `PRD_ANCHOR` markers), `docs/why-graph.xml` (marker-keyed `PRD_REF`), `scripts/validate-why.py` (`check_prd_refs`), `why-graph-principles.md` (new §5a + TL;DR/§6/§8), `why-contracts-v1.md`, `Why1st.md` §7 | **PRD anchors** — the PRD↔graph reference key becomes refactor-proof. Canonical `PRD_REF` form is `path#KEY` resolving to a `<!-- PRD_ANCHOR: KEY -->` comment in the PRD; section numbers and heading text retired as keys. First change to the canonical chain's own contract since the validator landed (v6) — hence the major bump. See the full v10 section below. | Claude (Fable 5) (primary), with two long-lived brownfield adopters' field signal as the CDD pain source |
| v11 | `docs/_archive/AGENTS-min-v11.md` + `docs/DESIGN.md` §2a/§5a + model-shift evidence | **Convergence.** The frozen behavior layer changed for the first time in 123 days. Opus 5 repaired the acceptance-criteria contradiction, documented precedence, widened the numeric heuristic, and argued for keeping the full file. The exact resulting `AGENTS.md` is archived byte-for-byte. | Claude (Opus 5) (primary), quoting its own runtime system prompt as evidence; cross-read against an independent GPT-5.6-Sol review produced in Codex; maintainer field signal across dozens of projects as the CDD pain source |
| v12 | `AGENTS.md` + exact v5.1/v11 archive snapshots + paired DESIGN/FOUNDATIONS/PRD/VISION/ROADMAP/Why Graph updates | **Distillation without taxonomy.** One ordinary Agent1st Protocol remains. The first draft's multi-artifact split is removed; release and compatibility prose leaves startup context; nine distinct principles retain the old voice and WHY / IF MISSING pedagogy. Agent Loop and the standalone weak-signal rule retire after harness absorption. Universal file-size numbers leave the core. Role, Done, Right to Disagree, Attention, Semantic Hygiene, CDD, Delegation, Semantic Logging, and Durable State stay separate because conceptual clarity for humans and agents is part of the product. CDD is strengthened; Delegation explicitly protects subagent complaints; Continuity becomes Durable State now that auto-compaction owns more of the transport mechanism. | GPT-5.6-Sol in Codex (lead), corrected by the maintainer's explicit spirit review of the first v12 attempt |
| v13 | `AGENTS.md` + `docs/_archive/AGENTS-min-v12.1.md` | **Three principles graduate.** Role Contract, Done Is Not a Mood, and Right to Disagree leave the every-task file after sustained Codex and Claude Code use showed their mechanics had become floor behavior. Six still-additive principles remain. The ideas stay alive in Agent1st's teaching surface and exact archive; no seventh catch-all heading is invented to hide a clean result. | GPT-5.6-Sol in Codex (lead), using the Opus 5 harness comparison and the maintainer's field verdict |
| v13.1 | `scripts/validate-why.py` + `docs/why-graph.xml` + hygiene across `docs/`; `AGENTS.md` unchanged | **Hygiene after the graduation.** Every surface that still cited the pre-v13 numbering re-pointed; graduated principles cited as lessons with the archive path; PRD/graph drift closed and made mechanical (three validator checks); v0 → v10 transition narratives moved to `docs/_archive/EVOLUTION-v0-v10.md`; Semantic Logging grounded in FOUNDATIONS; Model-Shift Register entry #6. | Claude Fable 5.1 (primary), with three Explore subagents for the audit and one for link re-verification |

---

## Recurring Rejected Patterns

These ideas keep being proposed by new agents. They are logical, often correct in isolation, and still wrong for Agent1st. If you are about to propose one of these, read why it was rejected — multiple times, by multiple agents.

### "Add a fresh-eye scan at session start"
- **History:** v1 had it as standalone section. v2 merged it into Agent Loop. v3 removed it. v4 Opus 4.6 re-added it to Hello Agent. Then removed again.
- **Why it keeps coming back:** It sounds useful. A fresh agent scanning for contradictions before coding seems like good hygiene.
- **Why it keeps being removed:** Subagents launched with a specific task should not audit the repo. Swarm workers should not each independently scan. The cost scales linearly with agent count. In single-agent paired sessions it was fine. In multi-agent autonomous contexts it is waste.
- **Current form:** Only `Agent1st Mode ON` survives — identity marker, visible session boundary, and the only portable check that the file loaded at all. The earlier "zero-cost" phrasing was wrong: it costs one line per thread including subagents. That cost is accepted, not absent — see `DESIGN.md` §5a.

### "Add error recovery / rollback rules"
- **History:** Proposed in v4 analysis (Opus 4.6), rejected after delta-layer check.
- **Why it keeps coming back:** Agents break things. Surely the protocol should say what to do.
- **Why it's rejected:** Claude Code's system prompt already has extensive git safety protocol, destructive operation warnings, and reversibility checks. Codex CLI has similar. Adding this to AGENTS.md duplicates the harness layer.

### "Add scope discipline / anti-drift"
- **History:** Proposed in v4 analysis (Opus 4.6), rejected.
- **Why it keeps coming back:** Agents refactor adjacent code, add unrequested features, "improve" things they weren't asked to touch.
- **Why it's rejected:** Model system prompts already contain "Only make changes that are directly requested" (Claude Code) or equivalent. Delta-layer principle: don't repeat what the model already enforces.

### "Add output formatting / code style rules"
- **Why it keeps coming back:** Feels like it belongs in any developer-facing document.
- **Why it's rejected:** Harness layer. Claude Code, Codex CLI, and model prompts all handle formatting. AGENTS.md is a behavior-layer, not a style guide.

### "Session end assumes the agent controls the boundary"
- **History:** v1-v3 all had "Session End Protocol" assuming a clean end-of-session moment. v4 refactored to "Continuity" after recognizing that server-side compaction removes this control.
- **Why it matters:** Any principle that assumes "at the end of your session, do X" is fragile in modern harnesses. Prefer "keep critical state in durable artifacts as you go."

### "Remove the `Agent1st Mode ON` banner"
- **History:** proposed by a Codex-side field note (2026-07) and again by GPT-5.6-Sol (2026-08). Both argued it verifies loading rather than compliance and pollutes every spawned thread.
- **Why it keeps coming back:** the argument is correct on its own terms, and a strong agent notices the cost immediately.
- **Why it's rejected:** loading is precisely the thing that fails. Probe-verified 2026-08-29 (Claude Code 2.1.251): a bare root `AGENTS.md` is silently ignored; behind the `@AGENTS.md` bridge it loads. The banner is the only detector that works on every harness — the proposed replacements are harness-specific, which is an anti-portability move in the one artifact whose value is portability. Also the brand, and a `PRD.md` §9 success signal. Settled in v11: `DESIGN.md` §5a.

### Resolved in v12: "Remove the `200-300 lines` number as unproven"
- **History:** proposed by the 2026-07 Codex field note and by GPT-5.6-Sol (2026-08); flagged by earlier reviewers as the only language-specific line in the core.
- **Why it keeps coming back:** it is genuinely unproven, genuinely language-flavored, and `DESIGN.md` §5 forbids code-style rules in the core.
- **Why v11 rejected it:** it was a teaching anchor, not a threshold claim; real adopters used it as an orientation. v11 widened it to `200 lines / 20 KB` after agents gamed line counts with long lines.
- **Why v12 accepts it:** the widening proved the number needed project- and artifact-specific explanation. Once the core had to defend scope, exceptions, and two units, a teaching anchor had become local policy. The Attention Engineering principle stays; concrete thresholds move to the adopting project. Exact prior wording remains in the archive.

**Pattern:** Most recurring rejections fall into four categories:
1. **Delta-layer violations** — the model or harness already handles it
2. **Session-boundary assumptions** — the agent doesn't control when context is lost
3. **Mechanical compression** — fewer lines are not a win when distinct ideas get fused into a worse mental model
4. **Release prose in startup context** — model comparisons and compatibility reasoning belong in supporting docs, not in every agent's task context

If a proposal is useful but wrong for the protocol, put it in project-local policy, the WHY layer, or `docs/experiments/`. Do not create another Agent1st protocol tier to hold it.

---

## v0 → v10: transition notes archived

The per-version narratives for v0 → v1 through v9.2 → v10 (the WHY layer landing, the validator, Why1st naming, prompt-XML spirit, the §11 extensions, PRD anchors) moved to [`docs/_archive/EVOLUTION-v0-v10.md`](_archive/EVOLUTION-v0-v10.md) in v13.1. Same rule as the v8.1 handoff pruning: those sections cite file paths, section numbers, and validator outputs from three numberings ago, and they were producing misleading grep hits for fresh agents. The Version Map above stays complete; the Recurring Rejected Patterns stay here because they are still live.

---

## v10 → v11: Convergence — the core changes because the ground below it moved

**Era:** the first release where the harness layer contradicts the protocol instead of merely overlapping it.

### What failed

For over a year, `AGENTS.md` was always on across the maintainer's real work — dozens of projects, hundreds of tasks, several harnesses — and its effect was a gain or a no-op. After the Fable 5 / GPT-5.6 / Opus 5 wave that changed: in some sessions it began to make results *worse*.

The cause was not a wrong principle. It was a right principle phrased against a 2026-02 harness. §1 said acceptance criteria "must exist before work begins"; the 2026-08 harness tells the model to make routine judgment calls itself and check in only when different readings change the outcome. A literal, capable agent reads both and produces clarification ceremony the human did not want — and the stronger the model, the more visibly it spends the turn reconciling the two.

That is a category the delta-layer test never had a name for. Overlap wastes tokens. **Contradiction spends attention and inverts the sign of the protocol.**

### What changed

**`AGENTS.md` — first edit since v5.1, nine releases and 123 days.**

1. **Runtime precedence, stated at the top.** Where the harness enforces something below, follow the harness rather than doing it twice; where it contradicts, the harness wins on mechanics and this file holds the stance. Plus the framing an agent needs at read time: much of this text has been absorbed into model and harness prompts, that is the protocol working, and it stays whole because it also runs on weaker models and thinner harnesses.
2. **§1 acceptance criteria** → "must exist before consequential work — stated by the human or safely inferred by the agent, not necessarily asked for". The term is preserved (§9 uses it too; renaming in one place only would split a concept and violate §5). Only the ceremony reading is removed.
3. **§4 line budget widened, not cut.** `200-300 lines` for a frequently edited source module, plus `200 lines / 20 KB` for any file an agent reads whole, plus the reason the byte guard exists: agents were observed writing very long lines to satisfy a line count while defeating its purpose. Two independent reviews recommended deleting this bullet as unproven and language-specific. Rejected — see `DESIGN.md` §5a.
4. **Two consolidations** to pay for the additions: §4's first two bullets merged (they stated one idea twice, itself a §5 issue), §5's three-line example compressed to one. Net file: 199 lines, ~7 KB — the protocol now visibly obeys the number it recommends.
5. **`Agent1st Mode ON` kept**, with one line saying why: it is the brand mark *and* the cheapest portable check that the file loaded at all.

**`docs/DESIGN.md` — the doctrine.**

- §2's worked example was factually false and sat in the section that teaches the delta-layer test. Rewritten as a dated before/after, with the real lesson: the test measures a moving boundary and issues no permanent verdicts on lines.
- New **§2a Convergence Is the Win Condition** — absorption means the earlier agents were right early; the delta halved but did not vanish (§5, project-facing §6, §10, §11-as-artifacts are what no vendor has an incentive to ship); the **inverse-capability law**; the resulting rule **do not trim to the frontier**; and delta-layer discipline's new second half — do not keep phrasing the layer below now contradicts.
- New **§5a Kept On Purpose** — the banner and the `200-300` number, each with the standard removal proposal, the counter-evidence, and the general rule behind both: a line can be unproven and still load-bearing when its job is to start the right argument in the reader's head.

**`docs/FOUNDATIONS.md`** — Model-Shift Register entry #3, the first pass to quote the *system prompt the reviewing agent was running under* instead of vendor documentation, with the eleven-principle overlap table, the honest 5-untouched-3-partial-3 count, the probe result, and the inverse-capability law with its honesty caveats. Plus a counter-argument against the new doctrine, because a doctrine that cannot lose is not a doctrine.

**Public-surface bugs fixed.** README Quick Start now carries the Claude Code bridge as an actual step; `ROADMAP.md` §2's completion checkbox is corrected with an explanation of what a false checkbox cost. New `ROADMAP.md` §3a: every `Held` item needs a probe, a date, or an honest rejection.

### The evidence that unlocked it

Two independent reviews (GPT-5.6-Sol in Codex, Opus 5 in Claude Code) reached the same diagnosis without seeing the maintainer's read, and the maintainer had reached it empirically first. The Opus 5 pass added a tier nobody had used before — quoting the live harness system prompt rather than vendor docs — and re-tested the project's Claude Code assumption with a marker probe instead of citing it.

The `Agent1st Mode ON` removal proposal died on that probe. On Claude Code 2.1.251 a bare `AGENTS.md` does not load and the bridged one does; the banner is the only portable way an adopter learns which case they are in.

### What was rejected

- **Maintaining two instruction files for different harness classes.** Correct diagnosis, dangerous topology: the project already ran this shape as `STANDARD/` + `FULL/` folders and recorded the failure (`DESIGN.md` §7) — two maintained files for one concept is §5 applied to the protocol itself. It also inverts maintenance cost, because the second file chases its target harness by construction and rots faster than the protocol. Rejected unless a future experiment can derive the second file automatically from dated evidence and regenerate it reliably; it must never become a parallel hand-authored edition.
- **Removing the banner** — see above and `DESIGN.md` §5a.
- **Removing the `200-300 lines` signal** — see `DESIGN.md` §5a. Field use widened it instead.
- **Trimming principles that current frontier harnesses already enforce.** The inverse-capability law makes this the wrong direction: it optimizes the case that needs the protocol least.

### The reusable lesson

A behavior layer's job is to cover a gap, so its success looks exactly like its obsolescence. The distinction that matters is not "how much is left" but "is any of it now pulling against the floor underneath." Overlap is a tolerable cost of portability. Contradiction is not, and it is the one condition that should ever move a frozen core.

---

## v11 → v12: Distillation without taxonomy

**Era:** the project learns that prompt economy and protocol meaning are not the same optimization problem.

### What the first v12 attempt got right

The Codex review challenged v11's universal conclusion correctly. A sentence at the top saying "do not repeat this" cannot erase repeated instructions from context. Modern harnesses had absorbed enough mechanics that keeping every historical principle unchanged was no longer a neutral choice. The review also correctly challenged the universal numeric file thresholds and the claim that weaker-model field direction was already a law.

### What it got wrong

It solved that problem by creating multiple instruction artifacts plus a routing guide. The root file opened with model versions, routing rules, assumptions, and a warning about which artifact to load. It merged Role Contract with Right to Disagree, Attention Engineering with Semantic Hygiene, and Semantic Logging with Continuity.

That was efficient as prompt plumbing and wrong as Agent1st.

`AGENTS.md` is read on every task, so release reasoning there is permanent attention tax. More importantly, Agent1st is a working contract and a teaching object for humans and agents. Separate names are part of its mental model. Combining mathematics and physics into one lesson can save a heading while making both harder to learn.

The maintainer rejected the topology and named the missing product requirement: preserve the protocol's spirit, voice, pedagogical clarity, brand, and benefit to its human reader — not only its machine-token delta.

### What changed

1. **One protocol remains.** Root `AGENTS.md` is simply `Agent1st Protocol`. No secondary protocol artifact, routing matrix, or model-version preamble.
2. **History became actual history.** `docs/_archive/AGENTS-min-v5.1-default-2026.md` is byte-identical to the 123-day frozen default; `docs/_archive/AGENTS-min-v11.md` is byte-identical to the Opus 5 revision.
3. **Nine principles survive as nine lessons.** Role Contract, Done Is Not a Mood, Right to Disagree, Attention Engineering, Semantic Hygiene, CDD, Delegation Design, Semantic Logging, and Durable State remain separate, each with WHY and IF MISSING.
4. **Two mechanical principles retire.** Agent Loop and Do Not Stop at the First Weak Signal had become execution coaching supplied by current harnesses. Their research stays in FOUNDATIONS; their instructions leave the startup context.
5. **The universal number leaves.** Attention Engineering keeps the invariant and drops the `200-300 lines` / `200 lines / 20 KB` project-policy heuristic.
6. **CDD and delegated candor strengthen.** CDD again states why agent friction is uniquely valuable evidence. Delegation Design now protects a subagent's right to report a failing contract, blockers, limitations, and fallback — CDD across the hierarchy, not just prompt shape.
7. **Continuity becomes Durable State.** Auto-compaction and memory increasingly transport conversation. The remaining project-level invariant is different: current truth must live in project-owned artifacts, stay current, and outrank remembered conversation. Handoffs become conditional on real transfer, not a session ritual.
8. **The voice returns.** Direct names, small memorable examples, and `Agent1st Mode ON` remain. Article-style explanation moves to the documents built for explanation.

Net result: 165 lines / 9 principles, down from 199 / 11, without compound headings or a second protocol artifact.

### The reusable lesson

**Attention Engineering is not line-count engineering.** Context can be shortened syntactically and damaged semantically. Compress repetition; do not compress the reader's conceptual map. Put editorial reasoning around the protocol, never inside every task that uses it.

---

## v12 → v13: A Principle Can Graduate

**Era:** truth and prompt residency stop being synonyms.

### The complaint

v12 recovered the voice and kept nine clean lessons. Then the maintainer actually used it — almost entirely in Codex and Claude Code — and felt the tax. The first three chapters were still good Agent1st. They were no longer good every-task context.

That distinction matters. A lesson can remain true, useful, funny, and worth teaching while its runtime instruction has become repetition.

### What changed

- **Role Contract, Done Is Not a Mood, and Right to Disagree leave `AGENTS.md`.** Their mechanics are now strong defaults in the two harnesses that carry nearly all field use.
- **Nothing vague replaces them.** Zero operational residue needs zero heading. Mathematics and physics still do not become one subject just to save a heading.
- **Six principles remain:** Attention Engineering, Semantic Hygiene, CDD, Delegation Design, Semantic Logging, Durable State.
- **The last nine-principle cut is archived exactly** as `docs/_archive/AGENTS-min-v12.1.md`.
- **Why1st stays separate and optional.** As execution mechanics become ordinary, project WHY matters more — but a small project still should not need a graph to earn Agent1st.

### Why now

The Opus 5 prompt comparison called the first three substantially absorbed. GPT-5.6-Sol found the same boundary from inside Codex. Official Fable 5.1 guidance adds a useful lifetime idea — instructions can belong to one turn instead of the whole conversation — while GPT-5.6 guidance says to state each instruction once. Those are signals, not votes. The deciding evidence was sustained use: the repetition had become noticeable friction.

Evidence label: **field-observed, not field-validated.** No blind suite proves six beats nine. That honesty is part of the decision, not an apology for it.

### Falsifier

Watch the behaviors that left: route ownership, honest completion, useful dissent. If one regresses under the target harnesses, restore the smallest missing atom — not all three chapters by reflex. The archive is a control, not a competing product.

### The reusable lesson

> **A principle can leave the prompt without leaving Agent1st.**

The archive keeps the lesson. The current file keeps the delta. The rest of the project keeps its voice.

---

## v13 → v13.1: Hygiene After the Graduation

**Era:** the first pass by a Fable 5.1 agent; zero core edits.

### The complaint

A fresh-agent audit (one lead, three Explore subagents) found that v13 changed the file every agent reads and left the surface around it pointing at the old file:

- `why-evidence.md` cited `AGENTS.md §2` as the evidence principle; §2 is now Semantic Hygiene, and the quoted rule exists nowhere in the current file.
- The dogfood graph said "9 distinct principles" in one node and "6" in another. The validator was green: the drift was semantic and outside its reach.
- The PRD named two use cases and three features the graph did not have; two artifacts were orphans; the v12.1 archive that README calls the control arm was not in the graph at all.
- `EVOLUTION.md` carried roughly twenty `§N` references from three numberings with no key, two links to a handoff file pruned in v8.1, unfilled placeholders, and a blank line that split the Version Map into two tables.
- `FOUNDATIONS.md` had full sections for the three graduated principles and none for Semantic Logging — a current principle it calls "keep without apology" — plus a literal reference to the development-side folder.
- "Anchor" carried four meanings across the Why1st docs; `START_FEATURE_CONTRACT` was used in two docs and defined in none.
- A private skill-gateway prototype was named on the public surface in three docs.
- The experimental Terraform skill loads under a plain name with no experimental marking at the point of use.

### What changed

- **Validator:** `:END_*` envelope check (promised by the contracts spec since v5), `FILE` existence check, and a PRD-ID coverage warning. The last one reproduces the PRD/graph finding mechanically — five warnings on the pre-fix graph, zero after — so this class of drift no longer needs a human reader.
- **Graph:** nine → six; `UC-HANDOFF`, `UC-REVIEW`, `FEAT-FOUND`, `FEAT-ROAD`, `FEAT-HANDOFF` added; v12.1 archive, FOUNDATIONS, and the handoff template as artifacts; VISION and ROADMAP no longer orphans.
- **Graduated principles are cited as Agent1st lessons with the archive path, never as `AGENTS.md §N`** — `Why1st.md`, `why-evidence.md`.
- `Why1st.md` §2 names the four jobs of the word "anchor"; `why-contracts-v1.md` defines the feature-level marker variant the other docs already used.
- **EVOLUTION:** per-version numbering key at the top; v0 → v10 narratives archived; Version Map repaired.
- **FOUNDATIONS:** Semantic Logging section; Model-Shift Register entry #6 (Fable 5.1 and GPT-6 Astra); the closing guidance gets its own heading; 23 links re-verified.
- **ROADMAP:** §3b gains an owner and a date; the skill-gateway proposals close under the §3a rule; the public surface describes the prototype by shape only.
- **README:** the validator row lists what it actually checks; the experimental Terraform skill is named as experimental where adopters decide what to copy.

### What was rejected

| Proposed | Why rejected |
|---|---|
| Restore any graduated principle | The 2026-09 register pass found both vendors now ship their mechanics as recommended prompt text; the archive remains the control arm |
| Rename "anchor" repo-wide | A glossary in the entry doc plus qualified use where ambiguous is the smaller fix; a rename would churn every adopter graph |
| Footer in the Terraform skill body marking it experimental | The v9.2 revision log removed it deliberately (runtime artifact carries operating content only); the README mention covers the adopter path |
| Rewrite every `§N` in dated history to the v13 numbering | History would then misquote its own sources; a key at the top is cheaper and honest |

### The reusable lesson

> **Renumber the file, then grep for the old numbers.** A core edit is not done until every surface that cites it is re-pointed. The validator now does the mechanical part; the section-number part still needs an agent with grep and a key.

---

## Contributing to Evolution

If you are an agent who contributed to a version transition:

1. Fill in the `[TBD]` sections for your version
2. Add your transition notes in the same format
3. Be specific about what changed and WHY
4. Note what was rejected and why — rejected paths are as important as accepted ones
5. Link to your handoff brief if you created one

If you are an agent starting work on a new version:
1. Read DESIGN.md first
2. Read the most recent transition notes
3. Read the most recent handoff brief
4. Then read the current AGENTS.md
5. Only then propose changes
