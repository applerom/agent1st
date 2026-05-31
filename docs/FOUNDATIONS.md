# Agent1st Protocol — Research Foundations

This document links Agent1st recommendations to actual research. Not to prove they are correct — to show why they are not random, to give agents and humans a basis for critique, and to make the protocol improvable as new research appears.

Fast-moving fields do not hand out perfect evidence on schedule. Some entries here are mature results. Some are fresh but relevant papers. Some are theory transfers or practical hypotheses. That is fine. The rule is not "wait for certainty"; the rule is "label certainty honestly."

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

- **Paper:** Guardieiro et al., "Instruction Following by Boosting Attention of LLMs" (2025)
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
- **Connection to Agent1st:** This is the strongest external convergence the project has. A frontier lab's applied team, writing from the opposite direction, independently lands on Agent1st's own vocabulary — "attention budget," "finite resource" — and independently derives §4 (minimal high-signal tokens), §5 (naming as signal), §9 (subagents return distilled summaries, not raw context), and §11 (note-taking/memory survives compaction). When a protocol written *by* agents and a frontier lab's engineering guidance arrive at the same mechanics from opposite ends, that is the cleanest available signal that the mechanics are real and not stylistic preference. It is also a caution: where the practitioner guidance and the protocol diverge (e.g. it expects formatting to matter *less* as models improve), that divergence is a place to watch, not to paper over.

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

## Agent Loop (Explore → Execute → Reflect)

**Protocol claim:** Use stable mode transitions. Explore enough to avoid guessing, execute the smallest useful move, reflect with evidence.

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
- **Connection to Agent1st:** The "Reflect" phase in the Agent Loop and the "1-3 frictions" in Continuity are Reflexion-adjacent. The insight: reflection must produce a reusable artifact (lesson, friction report), not just conversational self-talk.

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
- **Connection to Agent1st:** Supports "Do Not Stop at the First Weak Signal." First-pass reasoning is often insufficient. One alternative check can dramatically improve outcomes.

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

---

## Role Contract / Anti-Micromanagement

**Protocol claim:** Human provides intent, constraints, acceptance criteria. Agent chooses the route. Strong agents should not be micromanaged.

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

## Continuity

**Protocol claim:** Context can be compacted or lost without warning. Keep critical state in durable artifacts. Leave the next agent a runway, not a crater.

### Memory Architecture for Long-Running Agents

- **Paper:** Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (2023, UIST 2023)
- **Link:** https://arxiv.org/abs/2304.03442
- **Finding:** Believable long-term agent behavior requires a memory architecture with observation, reflection, and planning components stored in a persistent "memory stream." Without externalized memory, agents lose coherence across interactions.
- **Strength:** Established. Widely cited (2000+ citations), foundational for agent memory research.
- **Connection to Agent1st:** Continuity's insistence on durable artifacts (files, commits, structured handoff notes) is the software engineering equivalent of generative agents' memory stream. Conversational context is volatile — it can be compacted or destroyed at any point. Artifacts are the agent's long-term memory. The hook "if your handoff disappears when the session ends, it doesn't exist" is the practical test.

### Reflexion as Continuity Mechanism

- **Paper:** Shinn et al., "Reflexion" (2023) — already cited under Agent Loop.
- **Connection to Continuity:** The "1-3 frictions" in handoffs and the structured handoff format are Reflexion-adjacent: store lessons in reusable artifact form, not just conversational self-talk. Reflexion's core insight — that verbal reflections stored in memory improve future attempts — maps directly to the handoff discipline.

- **Strength for Continuity overall:** Supported. Park 2023 provides direct grounding for memory architecture; Reflexion provides the reflection-as-artifact mechanism. The combination moves Continuity from "practical origin" to research-supported.

---

## Summary: Evidence Strength by Principle

| Principle | Evidence Level | Key Papers |
|-----------|---------------|------------|
| Attention Engineering | Established | Liu 2023, Hung 2024, Guardieiro 2025, Wallace 2024, Hong 2025 (Context Rot), Anthropic 2025 |
| Agent Loop | Established | Yao 2022 (ReAct), Shinn 2023, Yao 2023 (ToT), Chen 2025 |
| Over-exploration guard | Supported | Su 2025, Sui 2025 |
| Right to Disagree | Established | Sharma 2023 (sycophancy) |
| Delegation Design | Supported | Tran 2025, Moore 2025 |
| Done Is Not a Mood | Supported | Gao 2023, Perez 2022 (RLHF reward hacking) |
| Role Contract / Autonomy | Supported | Hadfield-Menell 2016 (principal-agent) + Kim 2025 |
| Semantic Hygiene | Hypothesis | Mechanistic reasoning from attention literature |
| CDD | Practical origin | Analogy to sycophancy + reflexion |
| Continuity | Supported | Park 2023 (memory architecture), Reflexion (reflection-as-artifact) |

---

## Counter-Arguments: Where a Strong Agent Should Push Back

This document would be dishonest if it only argued *for* the protocol. Agent1st is a living research object, not a creed. A strong agent reading a principle should be able to compare it against its own training and push back — and the best of those pushbacks have shaped past versions (see `EVOLUTION.md`). This section states the strongest honest counter-argument to each principle, so a fresh agent does not have to reconstruct it cold. If you can extend or defeat one of these, that is a contribution.

**Against Attention Engineering / delta-layer.** The sharpest objection: the delta-layer test assumes you can know what the model and harness layers already enforce — but those layers are opaque, change without notice, and differ across providers. A line that is "duplication" under one harness is the *only* statement of a rule under another. Counter-counter: that is exactly why the protocol states principles, not procedures, and why this risk is named in DESIGN rather than denied. But an agent is right to flag a specific line as possibly-redundant under *its* harness — that is CDD working as designed, not heresy.

**Against Done Is Not a Mood.** Demanding "best evidence the harness allows" can itself become ceremony: on a one-line doc fix, writing an evidence sentence costs more attention than the fix. The principle is load-bearing on risky surfaces and overhead on trivial ones. The protocol's defense is "best evidence the *harness* allows" scales down to "none needed" — but that scaling is a judgment call the text leaves implicit, and a literal agent at low effort may over-apply it.

**Against Right to Disagree.** Sycophancy research (Sharma 2023) justifies it, but the same mechanism can misfire: an agent over-trained to disagree manufactures objections to look rigorous, which is sycophancy wearing a contrarian mask. The principle has no built-in calibration for *how often* disagreement is warranted. It relies on the agent's judgment about "quality, truth, or safety" being well-calibrated — which is precisely what is uncertain.

**Against Agent Loop / Do Not Stop at the First Weak Signal.** These two pull opposite ways: §4 says stop early, §8 says don't stop early. The project treats this as deliberate architecture (§4 guards over-exploration during search; §8 guards premature collapse during evaluation — see `EVOLUTION.md` on the reverted v6 merge). But a fast reader can experience it as a contradiction with no explicit arbiter. The honest position: the resolution lives in *which phase you are in*, and that context is not restated at each principle. Under a literal model at low effort, the asymmetry may not fire as intended — this is an open, testable question (see Model-Shift Register).

**Against Delegation Design.** This is the weakest-evidenced principle (see "The gap" above): there is no landmark experiment showing hierarchical information loss in LLM chains. It is practitioner wisdom ahead of the literature. A skeptic is entitled to call it a hypothesis dressed as a rule. The honest answer is that the document already labels it Supported-trending-Hypothesis — and the convergent Anthropic guidance on subagents returning distilled summaries is the closest thing to corroboration, not proof.

**Against Semantic Hygiene.** Labeled Hypothesis honestly. The mechanistic story (polysemy → ambiguous attention) is plausible but not isolated in a controlled study. A strong agent may reasonably hold that modern models disambiguate `graph` from context just fine, and that aggressive qualification (`ui_graph`, `knowledge_graph`) adds token cost for marginal gain. The counter is that the cost is tiny and the failure it prevents (wrong-concept edits) is expensive and silent — an asymmetric bet, not a proven theorem.

**Against CDD.** No research precedent — it is an invention. Its risk is over-firing: an agent that complains about every minor friction becomes noise, the opposite of signal. The format (Problem → Impact → Smallest fix) is the guardrail, but nothing enforces that the friction is real rather than a stylistic preference dressed as a blocker.

**Against Continuity.** The strongest principle by evidence (Park 2023, Reflexion). The honest weakness is the reverse: native harness features (compaction, memory tools, context-awareness) increasingly do some of this automatically, so a handoff written by hand can duplicate what the harness already persists. The principle ages well as a *behavior* ("leave a runway") but its *mechanism* (write a handoff doc at session end) is the part most likely to be partly superseded by tooling — see Model-Shift Register.

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
