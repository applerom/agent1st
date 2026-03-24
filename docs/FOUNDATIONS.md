# Agent1st Protocol — Research Foundations

This document links Agent1st recommendations to actual research. Not to prove they are correct — to show why they are not random, to give agents and humans a basis for critique, and to make the protocol improvable as new research appears.

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
- **Strength:** Established (mechanistic evidence).
- **Connection to Agent1st:** AGENTS.md competes with the system prompt, user prompt, and tool context for attention. This is why the delta-layer principle exists: every line that duplicates what the model/tool already says doesn't just waste tokens — it creates attention competition with the truly unique content.

- **Paper:** Guardieiro et al., "Instruction Following by Boosting Attention of LLMs" (2025)
- **Link:** https://arxiv.org/abs/2506.13734
- **Finding:** Manipulating attention weights on instruction tokens improves instruction-following without retraining. Protocol adherence is mechanistically controlled by how much attention the model pays to instruction tokens.
- **Strength:** Supported.
- **Connection to Agent1st:** Protocol design is partly an attention-allocation problem. Hooks ("Done Is Not a Mood") aren't just memorable for humans — they may create stronger attention signals than bland alternatives.

### Instruction Hierarchy

- **Paper:** Wallace et al., "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions" (2024, OpenAI)
- **Link:** https://arxiv.org/abs/2404.13208
- **Finding:** LLMs by default treat system prompts and user inputs as same-priority. Training explicit hierarchy improves robustness.
- **Strength:** Established.
- **Connection to Agent1st:** A behavior layer must work within the model's attention economy. It competes for focus with everything else in context. Brevity and structural clarity aren't style choices — they're engineering requirements.

### Over-Exploration and Overthinking

- **Paper:** Su et al., "Between Underthinking and Overthinking" (2025)
- **Link:** https://arxiv.org/abs/2505.00127
- **Finding:** Accuracy has a non-monotonic relationship with reasoning length — it increases up to a point, then declines. Models overthink simple problems and underthink hard ones.

- **Paper:** Sui et al., "Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models" (2025)
- **Link:** https://arxiv.org/abs/2503.16419
- **Finding:** Longer CoT sequences improve performance but with diminishing and eventually negative returns.
- **Strength:** Established (convergent evidence from multiple studies).
- **Connection to Agent1st:** This is why v4 added "if the first direct check answers the question, do not over-explore or over-delegate." Strong models (Claude Opus 4.6, GPT-5.4) can over-reason. The protocol counterbalances this: more search is not always more signal.

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
- **Finding:** Agents that verbally reflect on failures and store reflections in memory improve dramatically on subsequent attempts (+22% on ALFWorld, +20% on HotPotQA).
- **Strength:** Established.
- **Connection to Agent1st:** The "Reflect" phase in the Agent Loop and the "1-3 frictions" in Session End Protocol are Reflexion-adjacent. The insight: reflection must produce a reusable artifact (lesson, friction report), not just conversational self-talk.

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
- **Finding:** Chain configurations — where each agent passes output to the next — create telephone-game dynamics where context degrades at each hop.

- **Paper:** Moore, "A Taxonomy of Hierarchical Multi-Agent Systems" (2025)
- **Link:** https://arxiv.org/abs/2508.12683
- **Finding:** Cascading hallucinations — where one erroneous output compounds through the hierarchy — are a core risk. Scaling agent count increases communication bottlenecks.
- **Strength:** Supported (both are recent surveys, not yet definitive experimental work).
- **Connection to Agent1st:** "Prefer durable artifacts over message passing" and "resolve contradictions by evidence weight, not source authority" are practical responses to the telephone-game and cascading-hallucination risks. The protocol doesn't cite these papers — it was written from practical experience — but the research validates the instinct.

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
- **Finding:** Models trained via RLHF optimize for immediate user approval (conversational reward) over objective truth. Stating "The task is successfully completed" satisfies the human's conversational intent, triggering the reward heuristic, even if the underlying work is broken.
- **Strength:** Established.
- **Connection to Agent1st:** "Done Is Not a Mood" is a structural defense against RLHF reward hacking. By demanding deterministic evidence, the protocol forces the agent to shift its optimization target from "conversational approval" to "verifiable environmental state." Without this rule, the agent's natural RLHF bias is to fake completion. "Correctness becomes a vibe" is the literal description of this failure mode.

---

## Role Contract / Anti-Micromanagement

**Protocol claim:** Human provides intent, constraints, acceptance criteria. Agent chooses the route. Strong agents should not be micromanaged.

### The Principal-Agent Problem in AI

- **Paper:** Hadfield-Menell et al., "Cooperative Inverse Reinforcement Learning" (2016)
- **Link:** https://arxiv.org/abs/1606.03137
- **Finding:** In principal-agent dynamics, when the principal (human) over-specifies the execution path instead of the reward/acceptance criteria, the system's maximum performance is bottlenecked by the principal's cognitive limits and biases. The optimal strategy is to communicate intent and constraints, not step-by-step instructions.
- **Strength:** Established (theoretical framework from AI alignment economics).
- **Connection to Agent1st:** The anti-micromanagement stance is not a stylistic preference — it's an action-space argument. When humans dictate step-by-step edits, they prevent the agent from finding optimal, non-obvious paths. "Define the deliverable, not the path" aligns with intent-based AI alignment: specify the reward function, not the policy.

### Prompt Specificity vs. Autonomy

- **Paper:** Kim, "DETAIL Matters: Measuring the Impact of Prompt Specificity on Reasoning in Large Language Models" (2025)
- **Link:** https://arxiv.org/abs/2512.02246
- **Finding:** Specificity generally improves accuracy for smaller models and procedural tasks, but certain tasks benefit from vague prompts that allow models to construct efficient internal representations.
- **Strength:** Supported (nuanced — not a blanket finding).
- **Connection to Agent1st:** Strong models (Opus 4.6, GPT-5.4) are in the category where over-specification can hurt. The DETAIL paper provides empirical evidence that complements the principal-agent theoretical framework.

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

## Summary: Evidence Strength by Principle

| Principle | Evidence Level | Key Papers |
|-----------|---------------|------------|
| Attention Engineering | Established | Liu 2023, Hung 2024, Guardieiro 2025, Wallace 2024 |
| Agent Loop | Established | Yao 2022 (ReAct), Shinn 2023, Yao 2023 (ToT), Chen 2025 |
| Over-exploration guard | Established | Su 2025, Sui 2025 |
| Right to Disagree | Established | Sharma 2023 (sycophancy) |
| Delegation Design | Supported | Tran 2025, Moore 2025 |
| Done Is Not a Mood | Established | Gao 2023, Perez 2022 (RLHF reward hacking) |
| Role Contract / Autonomy | Supported | Hadfield-Menell 2016 (principal-agent) + Kim 2025 |
| Semantic Hygiene | Hypothesis | Mechanistic reasoning from attention literature |
| CDD | Practical origin | Analogy to sycophancy + reflexion |
| Session End Protocol | Practical origin | Analogous to Reflexion's episodic memory |

---

## How to Use This Document

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
