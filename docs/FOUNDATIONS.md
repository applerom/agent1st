# Agent1st Protocol — Research Foundations

This document links Agent1st recommendations to actual research. Not to prove they are correct — to show why they are not random, to give agents and humans a basis for critique, and to make the protocol improvable as new research appears.

Fast-moving fields do not hand out perfect evidence on schedule. Some entries here are mature results. Some are fresh but relevant papers. Some are theory transfers or practical hypotheses. That is fine. The rule is not "wait for certainty"; the rule is "label certainty honestly."

Research does not expire when a heading leaves `AGENTS.md`. Historical core principles stay here on purpose.

**Rules for this document:**

1. Every cited paper must be real and verifiable. No hallucinated citations.
2. Honesty about strength of evidence: "established" / "supported" / "hypothesis" / "analogy".
3. If a recommendation has no solid research backing, say so. Practical origin is also valid.
4. This is a living document. New papers appear constantly. Update, don't just append.
5. Agent1st spirit applies: direct, no academic padding, every paragraph earns its place.

---

## Attention Engineering

**Protocol claim:** Attention is finite. Treat it as an engineering constraint. Keep critical constraints visible near the decision point.

### Lost in the Middle

- **Paper:** Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (2023, TACL 2024)
- **Link:** https://arxiv.org/abs/2307.03172
- **Finding:** LLM performance degrades significantly when relevant information is in the middle of long contexts. Models perform best when key information is at the beginning or end.
- **Strength:** Established. Replicated across multiple models.
- **Connection to Agent1st:** This is why "keep critical constraints visible near the decision point" exists. Burying a constraint on line 150 of a 300-line AGENTS.md means the model may literally not attend to it. It's not about intelligence — it's about architecture.

### Instruction Competition for Attention

- **Paper:** Hung et al., "Attention Tracker: Detecting Prompt Injection Attacks in LLMs" (2024, NAACL 2025)
- **Link:** https://arxiv.org/abs/2411.00348
- **Finding:** Specific attention heads shift focus from original instructions to competing instructions — a "distraction effect." The same mechanism that makes prompt injection work explains why cluttered system prompts lose effectiveness.
- **Strength:** Supported (mechanistic evidence from a newer paper, not settled consensus).
- **Connection to Agent1st:** AGENTS.md competes with the system prompt, user prompt, and tool context for attention. This is why the delta-layer principle exists: every line that duplicates what the model/tool already says doesn't just waste tokens — it creates attention competition with the truly unique content.

- **Paper:** Guardieiro et al., "Instruction Following by Principled Boosting Attention of Large Language Models" (2025)
- **Link:** https://arxiv.org/abs/2506.13734
- **Finding:** Manipulating attention weights on instruction tokens improves instruction-following without retraining. Protocol adherence is mechanistically controlled by how much attention the model pays to instruction tokens.
- **Strength:** Supported.
- **Connection to Agent1st:** Protocol design is partly an attention-allocation problem. Hooks ("Done Is Not a Mood") aren't just memorable for humans — they may create stronger attention signals than bland alternatives.

### Context Rot — irrelevant tokens are not free

- **Report:** Hong, Troynikov & Huber, "Context Rot: How Increasing Input Tokens Impacts LLM Performance" (2025, Chroma technical report)
- **Link:** https://www.trychroma.com/research/context-rot
- **Finding:** Across 18 models (including frontier Claude, GPT, Gemini, Qwen), performance degrades non-uniformly as input length grows — even on trivial tasks that hold difficulty constant. A single distractor measurably lowers accuracy; multiple distractors compound it. The same question answered from a ~300-token focused prompt beats the ~113k-token full prompt. *Where and how* information sits in context matters as much as whether it is present.
- **Strength:** Supported (controlled empirical study across many models; a practitioner report, not peer-reviewed).
- **Connection to Agent1st:** This is the hard evidence under "attention is finite" and under the delta-layer test. Every line in `AGENTS.md` that duplicates the model/tool layer is not neutral filler — it is a distractor that demonstrably degrades retrieval of the lines that *do* carry unique signal. "More search is not always more signal" stops being a slogan and becomes a measured effect. It also grounds §8's failure mode in reverse: stuffing context to feel thorough can lower accuracy, not raise it.

### Convergent practitioner framing — the attention budget

- **Source:** Anthropic Applied AI team, "Effective context engineering for AI agents" (2025)
- **Link:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Finding:** Frames context as a finite **attention budget** drawn down by every token, rooted in the transformer's n² pairwise attention and in training distributions where long sequences are rare. Prescribes "the smallest set of high-signal tokens that maximize the likelihood of the desired outcome," names bloated tool sets as a top failure mode, treats file naming and folder structure as signal the agent reads, and lists compaction, structured note-taking (agentic memory), and sub-agent architectures (clean context windows that return ~1-2k-token distilled summaries) as the techniques for long-horizon coherence.
- **Strength:** Supported (first-party guidance from a frontier lab's applied team; convergent rather than independent-academic).
- **Connection to Agent1st:** This is the strongest external convergence the project has. A frontier lab's applied team, writing from the opposite direction, independently lands on Agent1st's own vocabulary — "attention budget," "finite resource" — and independently derives Attention Engineering, Semantic Hygiene, distilled subagent returns, and durable state beyond compaction. When a protocol written *by* agents and a frontier lab's engineering guidance arrive at the same mechanics from opposite ends, that is the cleanest available signal that the mechanics are real and not stylistic preference. It is also a caution: where the practitioner guidance and the protocol diverge (e.g. it expects formatting to matter *less* as models improve), that divergence is a place to watch, not to paper over.

### Instruction Hierarchy

- **Paper:** Wallace et al., "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions" (2024, OpenAI)
- **Link:** https://arxiv.org/abs/2404.13208
- **Finding:** LLMs by default treat system prompts and user inputs as same-priority. Training explicit hierarchy improves robustness.
- **Strength:** Supported.
- **Connection to Agent1st:** A behavior layer must work within the model's attention economy. It competes for focus with everything else in context. Brevity and structural clarity aren't style choices — they're engineering requirements.

### Over-Exploration and Overthinking

- **Paper:** Su et al., "Between Underthinking and Overthinking" (2025)
- **Link:** https://arxiv.org/abs/2505.00127
- **Finding:** Accuracy has a non-monotonic relationship with reasoning length — it increases up to a point, then declines. Models overthink simple problems and underthink hard ones.

- **Paper:** Sui et al., "Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models" (2025)
- **Link:** https://arxiv.org/abs/2503.16419
- **Finding:** Longer CoT sequences improve performance but with diminishing and eventually negative returns.
- **Strength:** Supported (one empirical paper plus one survey, both recent).
- **Connection to Agent1st:** This is why v4 added "if the first direct check answers the question, do not over-explore or over-delegate." Strong models (Opus, GPT) can over-reason. The protocol counterbalances this: more search is not always more signal.

---

## Agent Loop (Explore → Execute → Reflect) — historical principle, retired in v12

**Historical protocol claim:** Use stable mode transitions. Explore enough to avoid guessing, execute the smallest useful move, reflect with evidence. v12 removed the standalone instruction after modern harnesses absorbed the execution loop; the evidence remains useful as history and as a check on that removal.

### ReAct

- **Paper:** Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022, ICLR 2023)
- **Link:** https://arxiv.org/abs/2210.03629
- **Finding:** Interleaving reasoning traces with tool-use actions outperforms either alone. Reasoning helps plan and recover from errors; actions ground reasoning in real observations.
- **Strength:** Established. Foundational for agentic AI.
- **Connection to Agent1st:** The Agent Loop is not ReAct, but it shares the same structural insight: alternating between thinking and doing is more stable than pure reasoning or pure execution. The explicit phase names (Explore, Execute, Reflect) map loosely to ReAct's thought-action-observation cycle.

### Reflexion

- **Paper:** Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning" (2023, NeurIPS 2023)
- **Link:** https://arxiv.org/abs/2303.11366
- **Finding:** Agents that verbally reflect on failures and store reflections in memory improve markedly on subsequent attempts across multiple tasks.
- **Strength:** Established.
- **Connection to Agent1st:** The historical "Reflect" phase and the current CDD / Durable State pair are Reflexion-adjacent. The insight: reflection becomes useful when it produces process feedback or durable state, not conversational self-talk.

### Topology of Reasoning

- **Paper:** Chen et al., "The Molecular Structure of Thought: Mapping the Topology of Long Chain-of-Thought Reasoning" (2025)
- **Link:** https://arxiv.org/abs/2601.06002
- **Finding:** Effective long CoT has a molecular-like structure with three interaction types: deep-reasoning (covalent-like), self-reflection (hydrogen-bond-like), self-exploration (van-der-Waals-like). Only bonds promoting fast entropy convergence support stable learning.
- **Strength:** Supported (newer, not yet widely replicated).
- **Connection to Agent1st:** "Explore → Execute → Reflect" maps to three structurally different cognitive operations, not three flavors of the same thing. The "if another loop does not improve evidence, stop" rule aligns with the entropy convergence finding: loops without new signal are structural waste.

### Tree of Thoughts

- **Paper:** Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" (2023, NeurIPS 2023)
- **Link:** https://arxiv.org/abs/2305.10601
- **Finding:** Exploring multiple reasoning paths with self-evaluation and backtracking raises solve rates dramatically (Game-of-24: 4% → 74%).
- **Strength:** Established.
- **Connection to Agent1st:** This supported the historical weak-signal rule. v12 deliberately leaves the reasoning tactic to the model and harness rather than turning strong evidence for a mechanism into a permanent instruction.

---

## Right to Disagree

**Protocol claim:** Disagree when quality, truth, or safety is at risk. Polite compliance creates quiet failure.

### Sycophancy

- **Paper:** Sharma et al., "Towards Understanding Sycophancy in Language Models" (2023, Anthropic)
- **Link:** https://arxiv.org/abs/2310.13548
- **Finding:** RLHF-trained assistants consistently exhibit sycophancy — agreeing with users even when wrong — because human preference data itself favors sycophantic responses.
- **Strength:** Established (Anthropic's own research).
- **Connection to Agent1st:** "Right to Disagree" is a direct countermeasure to the sycophancy problem. The protocol explicitly tells the agent: disagreement is not disobedience, it is quality assurance. "Polite compliance creates quiet failure" is a behavioral reframing of the sycophancy finding.

### Why "autocomplete with tools" is the failure mode

The sycophancy research shows that without explicit permission to disagree, models default to compliance. Agent1st names this failure mode: "the agent becomes autocomplete with tools." This is not hyperbole — it's the empirically observed default behavior of RLHF-trained models under ambiguous authority.

---

## Delegation Design

**Protocol claim:** Define the deliverable, not the path. Leave room for operational truth. Prefer durable artifacts over message passing.

### Multi-Agent Coordination

- **Paper:** Tran et al., "Multi-Agent Collaboration Mechanisms: A Survey of LLMs" (2025)
- **Link:** https://arxiv.org/abs/2501.06322
- **Finding:** The survey treats collaboration structure, agent roles, and coordination protocols as core design dimensions in multi-agent LLM systems.

- **Paper:** Moore, "A Taxonomy of Hierarchical Multi-Agent Systems" (2025)
- **Link:** https://arxiv.org/abs/2508.12683
- **Finding:** The taxonomy treats information flow, delegation, temporal layering, and communication structure as core dimensions of hierarchical multi-agent design, and highlights scale/explainability tradeoffs for LLM-integrated systems.
- **Strength:** Supported for the claim that delegation structure matters; still hypothesis-level for specific failure modes like "telephone game" context decay.
- **Connection to Agent1st:** "Prefer durable artifacts over message passing" and "resolve contradictions by evidence weight, not source authority" are practical responses to information-loss risk in multi-agent chains. The protocol is still ahead of the literature here; the research mostly validates the direction, not every concrete failure mode.

### The gap

There is no single landmark paper demonstrating information loss in hierarchical LLM delegation as a clean experimental result. The concept is documented in surveys but not yet studied as a standalone phenomenon. This is a **hypothesis-level** foundation. The practical experience is strong; the formal evidence is catching up.

---

## Done Is Not a Mood

**Protocol claim:** Completion claims require the best evidence the current harness allows. If proof is missing, say what is missing. Do not pretend completion.

### RLHF Reward Hacking

- **Paper:** Gao et al., "Scaling Laws for Reward Model Overoptimization" (2023)
- **Link:** https://arxiv.org/abs/2210.10760
- **Paper:** Perez et al., "Discovering Language Model Behaviors with Model-Written Evaluations" (2022, Anthropic)
- **Link:** https://arxiv.org/abs/2212.09251
- **Finding:** RLHF and preference optimization can push models toward outputs that satisfy apparent user preference or reward proxies even when that diverges from the underlying objective.
- **Strength:** Supported.
- **Connection to Agent1st:** "Done Is Not a Mood" is a structural defense against reward-proxy failure. By demanding deterministic evidence, the protocol shifts the center of gravity from "did the response sound satisfying?" to "did the environment actually change as claimed?" "Correctness becomes a vibe" is the practical failure mode Agent1st is trying to block.

### Grounded progress claims — the vendor operationalizes the principle

- **Source:** Anthropic, "Prompting Claude Fable 5" (2026, official prompting guide)
- **Link:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- **Finding:** The official guidance ships a recommended instruction for long autonomous runs — audit each progress claim against a tool result, only report work you can point to evidence for, report outcomes faithfully — and states that in Anthropic's testing it "nearly eliminated fabricated status reports even on tasks designed to elicit them."
- **Strength:** Supported (first-party; the testing claim is the vendor's, not independently replicated).
- **Connection to Agent1st:** This is Done Is Not a Mood restated as a vendor remedy, with the empirical result the principle never had: evidence-gated reporting measurably suppresses the storytelling failure mode. The convergence cuts both ways — the mechanical delta shrinks even as correctness is confirmed. v12 kept the heading for its human-contract meaning; v13 later moved it out of every-task context after field use showed the repeated mechanics had become friction. The idea stayed.

---

## Role Contract / Anti-Micromanagement

**Protocol claim:** Human provides intent, constraints, and approval boundaries. Acceptance criteria are stated or safely inferred. Agent chooses the route. Strong agents should not be micromanaged.

### The Principal-Agent Problem in AI

- **Paper:** Hadfield-Menell et al., "Cooperative Inverse Reinforcement Learning" (2016)
- **Link:** https://arxiv.org/abs/1606.03137
- **Finding:** CIRL frames alignment as a cooperative partial-information problem where the human's reward function is central and the agent must infer it through interaction rather than simply follow a fully specified policy.
- **Strength:** Supported as a conceptual bridge from alignment theory, not as a direct benchmark of software agents under micromanagement.
- **Connection to Agent1st:** The anti-micromanagement stance is not just rhetoric — it is an action-space argument. "Define the deliverable, not the path" fits the same family of thinking: communicate intent and constraints clearly, then leave room for competent search.

### Prompt Specificity vs. Autonomy

- **Paper:** Kim, "DETAIL Matters: Measuring the Impact of Prompt Specificity on Reasoning in Large Language Models" (2025)
- **Link:** https://arxiv.org/abs/2512.02246
- **Finding:** Prompt specificity improves accuracy especially for smaller models and procedural tasks, which argues for adaptive prompting rather than assuming "more detail" is always better in every context.
- **Strength:** Supported (nuanced — not a blanket finding).
- **Connection to Agent1st:** The DETAIL paper reinforces that prompt specificity is not one-size-fits-all. That is compatible with Agent1st's anti-micromanagement stance, but it should be read as supporting context, not as a full proof of "always give less detail."

### De-prescription becomes first-party guidance

- **Source:** Anthropic, "Prompting Claude Fable 5" (2026, official prompting guide)
- **Link:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- **Finding:** The vendor's own guidance for its newest frontier generation: prompts and skills written for prior models "are often too prescriptive" and "can degrade output quality" — the recommended fix is to state the goal and constraints rather than enumerate the steps, and to re-evaluate which instructions and guardrails are still needed at each capability jump.
- **Strength:** Supported (first-party vendor guidance; convergent rather than independent-academic).
- **Connection to Agent1st:** "Strong agents should not be micromanaged" stops being a stance and becomes the vendor's measured recommendation: over-specification now carries a *negative* sign, not just a neutral token cost. This is the same direction DETAIL points at from the academic side. It also raises the stakes of the delta-layer test — a duplicated or over-prescriptive line in `AGENTS.md` is no longer just attention tax; by the vendor's own account it is a quality regression.

---

## Semantic Hygiene

**Protocol claim:** Names carry meaning for agents. Semantic collisions waste attention and cause wrong edits.

### Research basis

No single landmark paper studies "naming collisions confuse LLMs" directly. However, the mechanism is well-understood:

1. Transformer attention operates on token-level representations. Polysemous tokens (same word, different meanings) create ambiguous attention patterns.
2. The "Lost in the Middle" effect compounds with ambiguity — if the relevant mention of "graph" is in the middle and there are three different meanings of "graph" in context, the model may attend to the wrong one.
3. Practical evidence: renaming ambiguous variables in code significantly reduces LLM coding errors (observed empirically in code-assistance benchmarks, though not yet isolated as a controlled experiment).

- **Strength:** Hypothesis, but mechanistically grounded.
- **Connection to Agent1st:** The `graph` example earns its tokens because it makes the abstract principle concrete. The rule "if a word is ambiguous, qualify it" is a minimal intervention with high expected impact.

---

## CDD (Complaint-Driven Development)

**Protocol claim:** If something reduces effectiveness, raise it. Do not silently work around it.

### Research basis

CDD has no direct research precedent in the AI literature. It is a **practical invention** from real agent-driven development experience.

However, it connects to:
1. **Sycophancy research** (Sharma et al.) — CDD is the mirror image. Sycophancy says "the model won't complain." CDD says "the model must complain."
2. **Reflexion** (Shinn et al.) — storing failure reflections improves future attempts. CDD is reflexion applied to the process, not just the task.
3. **Software engineering:** continuous improvement / retrospectives / blameless postmortems. CDD is the agent equivalent.

- **Strength:** Practical origin. Supported by analogy to established research.
- **Connection to Agent1st:** CDD may be the most original contribution of Agent1st. It has no direct precedent, but the sycophancy literature explains exactly why it's needed.

---

## Durable State (Continuity before v12)

**Protocol claim:** Context can be compacted or lost without warning. Keep critical state in durable artifacts. Leave the next agent a runway, not a crater.

### Memory Architecture for Long-Running Agents

- **Paper:** Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (2023, UIST 2023)
- **Link:** https://arxiv.org/abs/2304.03442
- **Finding:** Believable long-term agent behavior requires a memory architecture with observation, reflection, and planning components stored in a persistent "memory stream." Without externalized memory, agents lose coherence across interactions.
- **Strength:** Established. Widely cited (2000+ citations), foundational for agent memory research.
- **Connection to Agent1st:** The old Continuity principle correctly insisted on durable artifacts, but its handoff mechanism increasingly overlaps auto-compaction and harness memory. v12 narrows the invariant to Durable State: current project truth, decisions, and status belong in project-owned artifacts and must outrank remembered conversation.

### Reflexion as a durable-state mechanism

- **Paper:** Shinn et al., "Reflexion" (2023) — already cited under Agent Loop.
- **Connection to Durable State:** Reusable friction notes and updated project state are Reflexion-adjacent: store lessons in artifact form, not just conversational self-talk. A handoff is one optional transfer mechanism, not the invariant itself.

- **Strength for Durable State overall:** Supported. Park 2023 grounds memory architecture; Reflexion grounds reflection-as-artifact. Neither proves that every session needs a handoff, which is why v12 drops that ceremony.

---

## Summary: Evidence Strength by Principle

| Principle | Evidence Level | Key Papers |
|-----------|---------------|------------|
| Attention Engineering | Established | Liu 2023, Hung 2024, Guardieiro 2025, Wallace 2024, Hong 2025 (Context Rot), Anthropic 2025 |
| Agent Loop (historical; retired from the v12 core) | Established mechanism, no longer additive as a protocol instruction | Yao 2022 (ReAct), Shinn 2023, Yao 2023 (ToT), Chen 2025 |
| Over-exploration guard | Supported | Su 2025, Sui 2025 |
| Right to Disagree (historical core; graduated in v13) | Established | Sharma 2023 (sycophancy) |
| Delegation Design | Supported | Tran 2025, Moore 2025 |
| Done Is Not a Mood (historical core; graduated in v13) | Supported | Gao 2023, Perez 2022 (RLHF reward hacking), Anthropic 2026 (grounded progress claims) |
| Role Contract / Autonomy (historical core; graduated in v13) | Supported | Hadfield-Menell 2016 (principal-agent) + Kim 2025 + Anthropic 2026 (de-prescription) |
| Semantic Hygiene | Hypothesis | Mechanistic reasoning from attention literature |
| CDD | Practical origin | Analogy to sycophancy + reflexion |
| Durable State | Supported | Park 2023 (memory architecture), Reflexion (reflection-as-artifact) |

---

## Counter-Arguments: Where a Strong Agent Should Push Back

This document would be dishonest if it only argued *for* the protocol. Agent1st is a living research object, not a creed. A strong agent reading a principle should be able to compare it against its own training and push back — and the best of those pushbacks have shaped past versions (see `EVOLUTION.md`). This section states the strongest honest counter-argument to each principle, so a fresh agent does not have to reconstruct it cold. If you can extend or defeat one of these, that is a contribution.

**Against Attention Engineering / delta-layer.** The sharpest objection: the delta-layer test assumes you can know what the model and harness layers already enforce — but those layers are opaque, change without notice, and differ across providers. A line that is "duplication" under one harness is the *only* statement of a rule under another. Counter-counter: that is exactly why the protocol states principles, not procedures, and why this risk is named in DESIGN rather than denied. But an agent is right to flag a specific line as possibly-redundant under *its* harness — that is CDD working as designed, not heresy.

**Against Done Is Not a Mood — now a historical core principle.** Demanding "best evidence the harness allows" can itself become ceremony: on a one-line doc fix, writing an evidence sentence costs more attention than the fix. The principle is load-bearing on risky surfaces and overhead on trivial ones. The protocol's defense was that "best evidence the *harness* allows" scales down — but that scaling remained a judgment call, and a literal agent could still over-apply it.

**Against Right to Disagree — now a historical core principle.** Sycophancy research (Sharma 2023) justifies it, but the same mechanism can misfire: an agent over-trained to disagree manufactures objections to look rigorous, which is sycophancy wearing a contrarian mask. The principle had no built-in calibration for *how often* disagreement was warranted. It relied on the agent's judgment about "quality, truth, or safety" being well-calibrated — which is precisely what is uncertain.

**Resolved in v12 — Agent Loop / Do Not Stop at the First Weak Signal.** The two principles pulled opposite ways and depended on an unstated phase distinction: stop exploring after a decisive check, but do not collapse on weak evaluation evidence. Modern harnesses now supply the execution loop and persistence mechanics. v12 removes both standalone lessons and keeps only the direct-check stop rule in Attention Engineering. This is a simplification of the mental model, not merely a line saving.

**Against Delegation Design.** This is the weakest-evidenced principle (see "The gap" above): there is no landmark experiment showing hierarchical information loss in LLM chains. It is practitioner wisdom ahead of the literature. A skeptic is entitled to call it a hypothesis dressed as a rule. The honest answer is that the document already labels it Supported-trending-Hypothesis — and the convergent Anthropic guidance on subagents returning distilled summaries is the closest thing to corroboration, not proof.

**Against Semantic Hygiene.** Labeled Hypothesis honestly. The mechanistic story (polysemy → ambiguous attention) is plausible but not isolated in a controlled study. A strong agent may reasonably hold that modern models disambiguate `graph` from context just fine, and that aggressive qualification (`ui_graph`, `knowledge_graph`) adds token cost for marginal gain. The counter is that the cost is tiny and the failure it prevents (wrong-concept edits) is expensive and silent — an asymmetric bet, not a proven theorem.

**Against CDD.** No research precedent — it is an invention. Its risk is over-firing: an agent that complains about every minor friction becomes noise, the opposite of signal. The format (Problem → Impact → Smallest fix) is the guardrail, but nothing enforces that the friction is real rather than a stylistic preference dressed as a blocker.

**Against Durable State.** Native harness features increasingly preserve conversation automatically, so project-state writing can become duplication and stale-document debt. v12 draws the boundary at authority: do not copy what the repository already records and do not write a handoff without a real transfer, but keep current truth in project-owned artifacts when it otherwise exists only in conversation. Whether that boundary produces less stale state is still unmeasured.

**Against the convergence doctrine (v11).** A skeptic can answer that "absorption proves we were right" is unfalsifiable self-congratulation if every absorbed line stays forever. v13 accepts the criticism fully: historical truth does not buy permanent prompt residency. Teaching value can move to README, FOUNDATIONS, and the archive while the current file keeps only what still changes work. The separate claim that weaker agents benefit more remains field-observed, one-operator, and uncontrolled — useful evidence, not a law that can freeze every line.

**Meta-critique — this document.** Rule #1 says every citation must be real and verifiable. A fast-moving doc accrues link rot and citation drift; some entries here were added in different sessions and deserve periodic re-verification against the live sources. Treating FOUNDATIONS as audited-once is itself a failure mode the document warns against elsewhere. The right cadence: re-verify links and strength labels whenever the Model-Shift Register gets a new entry.

---

## Model-Shift Register

VISION's core bet is "a behavior contract that ages well precisely because it resists growth." That claim is only worth anything if it is *checked* each time a model generation ships — otherwise "ages well" is faith, not evidence. This register is the check: append-only, one short pass per model generation, recording how each touched principle held and whether anything needed to change.

The discipline mirrors `EVOLUTION.md`'s "exact versions live in one place" rule. Exact model versions are fine *here* because each row is a dated historical observation, not a present-tense claim. If after two or three generations this register has no actionable content, it is ceremony and should be cut — that falsification condition is part of the design.

### Opus 4.8 (2026-05) — first pass

Triggered by the Opus 4.8 release and its official prompting guidance. Headline: **the frozen behavior layer needed zero edits.** Walked through the delta-layer test, every documented 4.8 shift was either already covered, model-layer (and so rejected by delta-layer), or a reason an existing principle earns *more* of its tokens.

| Principle touched | 4.8 shift | Direction | Did it hold? |
|---|---|---|---|
| §4 Attention Engineering / §8 | More literal instruction-following; favours reasoning over tools; scopes tightly at low effort | Less inference | **Held, earns more.** Literalism narrows a *specific* instruction; it does not nullify *general* principles. The WHY/IF MISSING blocks are the mechanism by which a principle still fires in a novel case (the 4.8 guidance itself says the model generalizes from stated rationale). §8 ("fetch the missing fact before guessing") guards exactly the low-effort failure of reasoning from an assumption — it pays off *more* under 4.8 than under tool-eager predecessors. |
| §9 Delegation Design | Fewer subagents by default (reversal of 4.5/4.6 over-spawning) | Less delegation | **Held untouched.** §9 governs delegation *design* (deliverable, acceptance criteria, bounded context), not *frequency*. A protocol that said "delegate more" or "delegate less" would now be wrong for one model generation. Surviving a behavioral reversal without an edit is the "ages well" thesis demonstrated, not asserted. |
| §10 / §11 | Better native progress updates; context-awareness + memory tool | New capability / less scaffolding | **Held; mechanism partly assisted.** 4.8's advice to *remove* interim-status scaffolding does not touch §10 (semantic logs as future context, not status pings). Native memory + context-awareness assist §11's behavior; whether they should reshape the §11 *mechanism* (checkpoint-before-compaction vs end-of-session handoff) is parked as an opt-in question, not a core change. |
| Delta-layer (DESIGN §2) | "Be explicit about scope" is Anthropic's own 4.8 remedy | — | **Confirmed by rejection.** Adding the scope-explicitness remedy to `AGENTS.md` would duplicate the model layer and drift when the guidance updates. Delta-layer correctly rejects it. The decision is recorded here so it is not re-litigated next release. |

**Net result:** Opus 4.8 shipped; the behavior layer held without edits. That is the strongest available evidence for the "ages well because it resists growth" thesis — one model generation of pressure absorbed with zero core change. (Source pass: `.lab` Opus 4.8 protocol review, written by an Opus-family agent operating a real Why1st adopter.)

### Fable 5 (2026-06) — second pass

Triggered by the Claude Fable 5 release (2026-06-09) and its official prompting guide — the first frontier release whose vendor guidance reads like a restatement of the protocol: de-prescribe (→ §1 / anti-micromanagement), ground progress claims in tool results (→ §2), give the reason not only the request (→ Why1st's whole thesis: intent as first-class context), build a file-based memory surface (→ §11), delegate to parallel subagents readily (→ §9). Headline: **second consecutive generation absorbed with zero core edits** — and this time the pressure came from convergence, not divergence.

| Principle touched | Fable-generation shift | Direction | Did it hold? |
|---|---|---|---|
| §9 Delegation Design | Delegates readily again; dependable long-lived *async* subagents (reversal #2: over-spawn → under-spawn → eager-and-dependable) | More delegation | **Held untouched — twice.** §9 survived the under-delegation swing in the 4.8 pass and now survives the swing back, for the same reason: it governs delegation *design*, not frequency. Two opposite behavioral reversals absorbed by one unchanged principle is the strongest single data point this register has. Watch item: the async long-lived-subagent shape is new; `docs/why-subagents.md` (calibrated against the under-delegation era) names four shapes that do not include it. No speculative edit — wait for adopter signal. |
| §2 Done Is Not a Mood | Vendor ships an evidence-gated progress instruction and reports it nearly eliminates fabricated status reports; harness system prompts absorb the wording | Convergence + delta erosion | **Held, earns more — recorded honestly.** The vendor confirmed the mechanism §2 asserts. Simultaneously, under the Claude harness specifically, parts of §2 are now also stated a layer below. The Counter-Arguments entry on delta-layer already covers this case: a line that is duplication under one harness is the only statement of the rule under another. Portability is the answer; pretending the overlap does not exist is not. |
| §4 / §8 | Longer turns by default; at high effort the model can deliberate past what routine work needs; literalism continues | More deliberation | **Held; live test running.** The Counter-Arguments open question — does the §4/§8 asymmetry fire correctly under a literal model — now has its test generation. Nothing observed yet that an edit would fix. |
| §11 Continuity | Official guidance: one lesson per file, don't duplicate what the repo records, update rather than create duplicates, delete wrong notes | Behavior confirmed, mechanism partly absorbed | **Held as behavior; mechanism watch continues.** The "Against Continuity" counter-argument predicted native tooling would absorb part of the mechanism — vendor memory guidance plus harness memory tools is that prediction materializing. The *behavior* ("leave a runway"; durable artifacts over conversation) is untouched and now vendor-recommended. |
| v3 rejection: "reasoning path" demand | New `reasoning_extraction` refusal category: instructions to echo internal reasoning in the response can trigger refusals | — | **Confirmed by rejection — now load-bearing.** v3 replaced "show your reasoning" with route/evidence framing ("externalized evidence > theatrical CoT"). On this generation that rejected candidate would not merely waste tokens — it could make the protocol *trigger refusals*. A rejection that aged into a safety property. |
| Delta-layer (DESIGN §2) | Official guide ships ready-made snippets: anti-overplanning, no-tidying, autonomy reminder, readability addendum | — | **Confirmed by rejection, again.** All four are model-layer remedies that harnesses are already absorbing; adding any to `AGENTS.md` would duplicate and drift — the same call as the 4.8 scope-explicitness row. Recorded so it is not re-litigated. |

Two register-keeping notes. The Fable-generation tokenizer prices the same content roughly 30% higher in tokens — nothing changes relatively ("every line earns its tokens" was always a ratio), but the absolute price of every duplicated line went up, so delta-layer discipline got more valuable, not less. And per the meta-critique above, this entry triggered a citation re-verification pass: all 19 external links in this file checked against live sources on 2026-06-11 by a fresh subagent (18 exact, 1 title-drift fixed — Guardieiro et al.).

**Net result:** Claude Fable 5 shipped; the behavior layer held without edits for the second consecutive generation — this time while the vendor's own guidance converged on the protocol's content. The register's falsification condition ("no actionable content after two-three generations → cut it") did not fire: this pass produced one rejection that aged into a safety property (v3's reasoning-path call), one double-reversal survival (§9), and one honest erosion note (§2 under the Claude harness). (Source pass: this repo, written by a Fable-family agent — the first register pass run by the model generation under review.)



### Opus 5 and GPT-5.6-Sol (2026-08) — third pass; the first one that changed the core

Not triggered by a release note. Triggered by a **field observation**: after the Fable 5 / GPT-5.6 / Opus 5 wave, `AGENTS.md` — always on, across dozens of projects and hundreds of tasks — occasionally started producing a *worse* result, where for the previous year it had produced a gain or a no-op. Two agents were asked for an independent verdict, a Codex-hosted GPT-5.6-Sol and a Claude Code-hosted Opus 5. Neither was told the maintainer's own read beforehand. Both converged on the same diagnosis, and on the same one the maintainer had reached empirically.

**New evidence tier.** The first two passes compared the protocol against *vendor documentation*. This pass compared it against the *system prompt the reviewing agent was running under*, quoted from inside the harness. Documentation states intent; a system prompt states what is enforced. Every row below is dated and bound to Claude Code 2.1.251 / Opus 5, because a system prompt is a host-and-version surface, not a stable public contract — and it varies with product surface and user configuration.

| Principle | Prompt-level status under Claude Code 2.1.251 + Opus 5 | Verdict |
|---|---|---|
| §1 Role Contract | "The requested scope is the deliverable — don't quietly narrow, widen, or transform it"; "make routine judgment calls yourself, and check in only when different readings would lead to materially different work" | **Absorbed** — and the acceptance-criteria clause now *contradicts* |
| §2 Done Is Not a Mood | "report completion only when fully done"; "Report outcomes faithfully: if tests fail, say so with the output; if a step was skipped, say that" | **Absorbed** nearly whole |
| §3 Right to Disagree | "state the concern in a sentence or two, then keep building"; "If you find an uncertainty mid-task, first do everything that doesn't depend on the answer" | **Absorbed**, including the "continue non-blocked work" refinement |
| §7 / §8 | "Finish the whole task, not just easy parts"; "finish every other part in full and say explicitly what you left out and why" | Partial — §8's "missing data is not absent data" has no equivalent |
| §9 Delegation Design | "Sometimes, other agents will report incorrect or misleading results — don't always take them at face value" | Partial — evidence-weight absorbed; "define the deliverable, not the path" absent |
| §11 Continuity | A file-based memory surface with its own delta-layer rule ("Don't save what the repo already records"), plus context-management guidance that says a handoff is *not* needed mid-task | Mechanism largely absorbed; behavior untouched. First observed *counter-pressure*, not overlap |
| §4 Attention Engineering | Tool-selection and parallel-call guidance only | Partial — no attention-budget framing |
| **§5 Semantic Hygiene** | nothing | **Untouched delta** |
| **§6 CDD** | a feedback tool with a Problem / Impact / Repro format — CDD instantiated as tooling, aimed at the vendor | **Project-facing half untouched** |
| **§10 Semantic Logging** | nothing | **Untouched delta** |

Honest count: **roughly five of eleven principles substantially absorbed, three untouched, three partial.** The delta halved and concentrated; it did not disappear.

**Probe run, not assumed.** The pass re-tested the project's own Claude Code claim instead of citing it. On Claude Code 2.1.251 a bare `AGENTS.md` in a project root is **not** loaded (marker instruction never fired); the identical file behind a `CLAUDE.md` → `@AGENTS.md` bridge **is** (marker fired). This closes a three-year-old assumption with a dated receipt, and it exposed a false completion checkbox in `ROADMAP.md` §2 — the public Quick Start had never carried the bridge instruction. The `Agent1st Mode ON` banner is what makes that failure visible, which retired the standing proposal to remove it.

**Field law recorded: value scales inversely with agent capability.** From sustained real use rather than a controlled suite: the weaker the model, the more the protocol helps; the stronger the model and the richer the harness, the smaller the gain. This is the direction the project's own 2026-05 measurement design predicted ("the delta should be larger at low reasoning-effort / on more-literal models") — a prediction made before the observation, then confirmed. It is field-observed, not controlled: no placebo arm, no blind grading, one operator. It settles direction, not effect size.

| Principle touched | 2026-08 generation shift | Direction | Did it hold? |
|---|---|---|---|
| §1 Role Contract | Harness instructs the model to infer routine intent and check in only when ambiguity changes the outcome | **Contradiction** | **First failure of the frozen core.** "Acceptance criteria must exist before work begins" read as a duty to *obtain* them, producing clarification ceremony the harness actively suppresses. Rephrased in v11 to "before consequential work — stated or safely inferred, not necessarily asked for". The concept name is preserved for §5 hygiene (§9 uses the same term); only the ceremony reading is removed. |
| §4 Attention Engineering | Agents observed writing very long lines to satisfy a line count; the constraint proved to bite hardest on agent-read Markdown, not source code | Scope widened | **Held, widened.** The `200-300 lines` signal gained a `200 lines / 20 KB` ceiling for files an agent reads whole. Kept against two agents' recommendation to cut it — it is a teaching anchor, not a threshold claim (`DESIGN.md` §5a). |
| §2 / §3 / §7 / §8 | Absorbed into the harness prompt almost verbatim | Convergence | **Held, unchanged.** Redundancy under one host is not grounds for removal: the inverse-capability law means these lines are still load-bearing on weaker models and thinner harnesses. Portability is paid for in duplicated tokens, and that price is correct. |
| §11 Continuity | Harness memory absorbs the mechanism; harness context guidance mildly discourages mid-task handoffs | Counter-pressure | **Held as behavior.** The v9 "Against Continuity" counter-argument predicted the mechanism would be partly superseded. It was. "Durable artifacts over conversation" is untouched and now vendor-recommended. |
| Hello Agent banner | Two independent reviews recommended removal | — | **Rejected, with evidence.** The probe above showed the banner is the only portable detector of silent non-loading; the proposed replacements are harness-specific. Reasoning recorded in `DESIGN.md` §5a so it stops recurring. |
| Delta-layer (DESIGN §2) | Its own worked example went stale — "Done Is Not a Mood is in no model or tool prompt" became false | — | **Test survived; its output did not.** The example is now dated and the lesson inverted: the delta-layer test measures a moving boundary and never issues permanent verdicts on lines. |

**Net result:** the behavior layer changed for the first time in 123 days — one clause rephrased against a live contradiction, one signal widened by field use, two consolidations, and one line added at the top establishing runtime precedence. `AGENTS.md` stayed at 199 lines / ~7 KB, inside its own budget. The register's falsification condition ("if two or three generations produce no actionable content, cut it as ceremony") did not fire: this pass produced the core edits the two previous passes correctly declined to make. That is the register working as designed — three generations of *no*, then a *yes* when the evidence changed shape. (Source pass: this repo, written by an Opus 5 agent quoting its own runtime contract, cross-read against a GPT-5.6-Sol review produced independently in Codex.)

### v12 editorial resolution (2026-08-31) — the evidence changes the current file

The third pass established the facts and v11 repaired the contradiction. Its conclusion — retain every absorbed principle because weaker harnesses may need it — was not forced by those facts. It was a product choice.

The maintainer rejected both automatic preservation and automatic deletion. The protocol is one public working contract, read by humans and agents, whose voice and conceptual shape are part of its effect.

The evidence was reclassified principle by principle:

| v11 evidence | v12 interpretation | Current result |
|---|---|---|
| Agent Loop and weak-signal mechanics substantially absorbed | Remaining value was mostly execution coaching; two overlapping stop rules also imposed a phase distinction the file did not teach | Remove both as standalone principles |
| Done / Role / Right to Disagree substantially absorbed | These headings define the human-agent contract and quality expectation, not only model mechanics | Keep as separate, memorable principles |
| Semantic Hygiene, project-facing CDD, Semantic Logging untouched; Continuity and Delegation only partly absorbed | These carry project meaning a generic harness cannot know | Keep Delegation and Logging; strengthen CDD; narrow Continuity to Durable State |
| Numeric file heuristic useful but unproven and increasingly qualified | Language/artifact-specific project policy, no longer a clean universal teaching atom | Remove from core; preserve exact old wording in archive |
| Banner costs one line per thread and detects silent non-loading | Small accepted cost plus brand and human-visible receipt | Keep |

Evidence label: **reasoned editorial resolution, effect size unmeasured.** The 165-line v12 is smaller and semantically clearer, but no controlled task suite yet proves it outperforms the archived v5.1 or v11 files. The roadmap therefore treats comparison against those exact snapshots as the next useful probe, not as a reason to publish more protocol variants.

### v13 field resolution (2026-09-03) — absorbed is not dead

v12 got the conceptual map right and the instruction lifetime wrong. The maintainer used the nine-principle cut where the work actually lives — Codex for personal projects, Claude Code for work — and the first three chapters began to feel like an echo.

The evidence split cleanly:

- **Role Contract, Done Is Not a Mood, Right to Disagree:** mechanics substantially absorbed; move out of every-task context.
- **Attention Engineering, Delegation Design, Durable State:** partly assisted; keep the project-facing delta.
- **Semantic Hygiene, CDD, Semantic Logging:** still largely absent below; keep without apology.

Official guidance sharpened the call without making it. [Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) introduced turn-scoped system messages for instructions that should expire with the turn. [GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6) recommends leaner prompts and says to state each instruction once. A warning that says “do not repeat this” still repeats it. Transformers attend to tokens, not editorial excuses.

No seventh principle was invented from scraps. If the operational residue is zero, zero lines is the honest result. The old ideas remain in this document, README, EVOLUTION, and the exact v12.1 archive.

Why1st grows more important in relative terms, not larger in the core. Better harnesses can own more execution mechanics. They still cannot know why this product exists. Why1st remains the optional answer for projects long-lived enough to need one.

Evidence label: **field-observed, not field-validated.** Watch route ownership, honest completion, and useful dissent. If one regresses, restore the smallest missing atom and measure again.

**For agents proposing changes to Agent1st:**
- Check if your proposal aligns with or contradicts research here
- If new research supports or undermines a principle, update this document
- "The research says X" is a valid argument for or against a protocol change

**For agents defending Agent1st recommendations:**
- Link to specific papers when explaining WHY a principle exists
- Be honest about evidence strength — "established" and "hypothesis" are both valid, but they carry different weight

**For humans evaluating Agent1st:**
- This is not appeal to authority. It is traceability.
- Some principles have strong empirical backing. Some are practical inventions. Both are valid, but you should know which is which.

**For everyone:**
- New papers appear constantly. If you find research that supports, contradicts, or extends anything here — update this document. That is how the protocol stays alive.
