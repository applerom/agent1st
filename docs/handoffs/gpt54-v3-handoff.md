# Agent1st Protocol — Handoff Brief for the Next Agent

## Purpose

This brief transfers the **meaning, spirit, constraints, sources, and evolution logic** behind `AGENTS-min-v3.md` to the next agent working on Agent1st Protocol.

This is **not** a generic summary. It is a **working brief** for continuing improvement of the document.

Primary source of truth:
- `AGENTS-min-v3.md`

Historical context:
- `AGENTS-min-v2.md`
- `AGENTS-min-v1.md`

---

## 1) Current source of truth

### Main file
- `AGENTS-min-v3.md`

### Historical versions
- `AGENTS-min-v2.md`
- `AGENTS-min-v1.md`

### Local comparison material used during design
These are not “intermediate notes”. They are **uploaded local reference files** used to compare Agent1st Protocol against model-layer and tool-layer instructions:
- `gpt-5.4-thinking.md`
- `claude-opus-4.6.md`
- `codex-cli.md`
- `claude-code.md`

Use them as **local comparison artifacts**, not as files that Agent1st should imitate.

Practical meaning:
- `gpt-5.4-thinking.md` → model-layer constraints and behavior expectations for GPT-5.4
- `claude-opus-4.6.md` → model-layer constraints and behavior expectations for Claude Opus 4.6
- `codex-cli.md` → tool/harness-layer behavior for Codex CLI
- `claude-code.md` → tool/harness-layer behavior for Claude Code

They matter because one of the biggest design conclusions was:

> **AGENTS.md should be a delta-layer, not a second system prompt.**

---

## 2) The central idea

The most important idea to preserve:

> **Agent1st Protocol does not tell the agent how to work step-by-step.  
> It defines the conditions in which a strong agent works better.**

This distinction matters a lot.

Wrong framing:
- “how to manage the agent”
- “how to control the agent”
- “how to make the agent obey the process more strictly”

Right framing:
- define roles
- define boundaries
- define rights
- define quality expectations
- define friction handling
- define attention / semantic hygiene
- define handoff quality

This is closer to **harness design** than to prompt micromanagement.

---

## 3) The human-agent stance behind the protocol

Another very important design intention:

Agent1st is not built on the idea that:
- the human is the real executor,
- the agent is just a tool,
- the agent should be micromanaged like a junior intern.

It is built on the idea that:
- the agent is a real working executor,
- the human provides intent, constraints, approvals, and acceptance,
- the agent takes the route, execution, verification, and alternatives,
- the human should create conditions, not over-control the path.

That is why the `Role Contract` was moved to the top in v3.

This was one of the strongest and most intentional shifts.

---

## 4) Why this file exists at all

There is a deliberate rejection here of the common pattern:

> “AGENTS.md is mostly a repo cheat sheet.”

Typical AGENTS.md / CLAUDE.md / similar files often contain:
- repository layout
- build commands
- test commands
- local setup notes
- style conventions
- repo-specific instructions

That category is not denied or attacked. It can be useful.

But this minimal Agent1st version focuses on something else:

> **What should remain useful even when the repo changes?**

The protocol tries to capture what is:
- stable
- behavior-shaping
- model-agnostic enough
- harness-relevant
- reusable across projects

This is why the file avoids becoming:
- a stale repo walkthrough
- an overgrown manual
- a context dump
- a duplicated system prompt

---

## 5) The strongest design constraint

This is one of the most important conclusions from the session:

> **Do not repeat what the model and tool prompts already cover well.**

The protocol should not expand just because a recommendation is correct.

A recommendation can be:
- correct,
- important,
- official,
- widely endorsed,

and still be a **bad addition** to `AGENTS.md` if:
- the model already sees it in its system prompt,
- the tool already enforces it,
- it adds no new signal,
- it creates duplication,
- it creates contradiction risk,
- it spends precious context budget.

This is why a lot of “proper prompt engineering advice” was discussed and then **intentionally not copied** into v3.

That was not an omission. It was a design choice.

---

## 6) What changed during the session

These are important reflections because they show where understanding evolved.

### A. From “make it more complete” → to “make it more delta-shaped”
At first, there was a strong pull toward adding more explicit contracts:
- output contract
- tool persistence
- dependency checks
- completion contract
- verification loop
- planning / skill mechanism notes

Many of those were correct.

But after comparison with model and tool prompts, the conclusion changed:
- too many of these belong to model/tool layer,
- repeating them weakens the document,
- the better move is to keep only what Agent1st uniquely adds.

### B. From “Humans steer. Agents execute.” → to harness/partnership framing
This wording was rejected.

Why:
- it sounded too manager/executor,
- it contradicted the intended spirit,
- it undercut the anti-micromanagement stance.

It was replaced with the more Agent1st-consistent pattern:
- human provides intent / constraints / approvals / acceptance
- agent chooses the route, executes, and proves the result
- strong agents should not be micromanaged

### C. From “reasoning path” → to route / execution / reflection / alternatives
There was an early temptation to justify “reasoning path” through research on long CoT.

But after deeper reflection:
- raw reasoning path is not the right thing to demand,
- externalized route and evidence are more useful than theatrical CoT,
- the right idea to keep was the structure of good search, not the demand for full trace disclosure.

### D. From “let subagents break the format to tell the truth” → to “design delegation contracts correctly”
This was a major change.

At first, one possible answer to silent subagents seemed to be:
- let them slightly violate output format to surface blocker/friction truth.

That was later rejected.

The better conclusion:
- this is a delegation-design bug,
- the parent agent should leave room for operational truth,
- do not force subagents into silence through badly designed return contracts.

This led to:
- `Delegate for truth, not silence.`
- `Leave subagents room to report blockers, repeated friction, or fallback.`

### E. From “remove Hello Agent because it is noise” → to “keep it as low-cost identity + session marker”
At first, `Hello Agent!` looked like expendable noise.

Later reflection changed that:
- the noise cost is tiny,
- the adoption value is real,
- the handshake gives project identity,
- it acts as a useful session boundary marker,
- it makes the document more memorable.

So it was brought back intentionally.

---

## 7) The style constraints are real, not cosmetic

The file is intentionally trying to satisfy multiple goals that often conflict.

It should be:
- useful to the agent
- readable to the human
- compact
- memorable
- slightly provocative
- somewhat humorous
- serious enough to feel expert
- short enough not to become an article
- strong enough to get adopted
- stable enough to stay useful
- not too repo-specific
- not too generic

Do not “clean this up” into sterile correctness if that kills:
- hooks
- memorability
- adoption
- spirit

At the same time, do not let hooks turn into:
- empty slogans
- vague philosophy
- prompt theater
- ungrounded declarations

This balance is one of the hardest parts of the project.

---

## 8) Why the document uses hooks, WHY blocks, and humor

These were not accidental flourishes.

### Hooks
Examples:
- `Done Is Not a Mood`
- `Strong agents should not be micromanaged`
- `Right to Disagree`
- `Delegate for truth, not silence`
- `Leave the next agent a runway, not a crater`
- `autocomplete with tools`

Hooks are used because they:
- compress meaning,
- stick in human memory,
- travel well,
- stay useful in the agent’s context.

### WHY blocks
These are connected to a broader idea around **Why-driven Development**:
- strong agents benefit from understanding not just the rule, but the purpose,
- WHY increases generalization value,
- WHY makes the rule less brittle.

But WHY must stay:
- short
- operational
- non-essay-like

### Humor / spice
Controlled humor is intentional.
It helps with:
- adoption
- memorability
- reducing dryness
- making the protocol feel alive

It should stay low-noise.

---

## 9) Main external documents and why they matter

### 1. Harness engineering: leveraging Codex in an agent-first world
Link:
- https://openai.com/index/harness-engineering/

Why it mattered:
- strongest support for harness-first thinking
- shows humans moving toward environment design, intent specification, and feedback loops
- validates the importance of observability, scaffolding, repository legibility, and feedback systems
- reinforced the idea that harness quality often matters more than small model gains

### 2. OpenAI Prompting Guide
Link:
- https://developers.openai.com/api/docs/guides/prompting

Why it mattered:
- useful as an official reference point for modern OpenAI prompting behavior
- helped compare what belongs in a prompt vs what should stay out of Agent1st
- reinforced that prompting is model/snapshot dependent and iterative

### 3. Introducing Codex
Link:
- https://openai.com/index/introducing-codex/

Why it mattered:
- useful for understanding mainstream framing of AGENTS.md in the Codex world
- shows the common expectation that AGENTS.md explains repo workflow, commands, and practices
- helped sharpen what Agent1st is deliberately *not* doing in its minimal version

### 4. Claude prompting best practices
Link:
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

Why it mattered:
- confirmed value of explicit, structured instructions
- supported the use of concise motivation / context
- helped compare what Claude-level prompting already covers and what Agent1st should avoid duplicating

### 5. Claude Code memory / CLAUDE.md
Link:
- https://code.claude.com/docs/en/memory

Why it mattered:
- helpful for understanding how CLAUDE.md is positioned in the Anthropic ecosystem
- useful contrast for local memory / project memory / operating guidance
- reinforced the distinction between repo memory and Agent1st’s behavior-layer focus

### 6. The Molecular Structure of Thought: Mapping the Topology of Long Chain-of-Thought Reasoning
Link:
- https://arxiv.org/abs/2601.06002

Why it mattered:
- supported the idea that strong reasoning is not just one straight path
- informed the intuition behind:
  - `Explore -> Execute -> Reflect`
  - not stopping at the first weak signal
  - allowing alternative paths instead of early collapse

Important caution:
- this paper should not be over-read as direct operational law for AGENTS.md
- it was used more as conceptual support than as a direct template

---

## 10) How the four local comparison files should be used

Again, these are not random temporary notes. They were local comparison artifacts.

### `gpt-5.4-thinking.md`
Use for:
- understanding what GPT-5.4 system-layer instructions may already strongly influence
- avoiding unnecessary duplication of behavior already covered by the model

### `claude-opus-4.6.md`
Use for:
- the same comparison on the Claude model side
- avoiding universalizing OpenAI-shaped assumptions where Claude already behaves differently

### `codex-cli.md`
Use for:
- understanding what Codex CLI already tells the agent about tools, approvals, progress, and execution
- avoiding turning Agent1st into a duplicate of the tool harness

### `claude-code.md`
Use for:
- understanding what Claude Code already handles around tasks, subagents, memory, or workflow structure
- avoiding repetition at the harness layer

If a future agent wants, it can redo the comparison from scratch.
But these files were part of the actual reasoning process that led to v3.

---

## 11) The current document structure and why it matters

One of the major design improvements in v3 was the split into:

- `Core`
- `Operations`

This should be preserved unless there is a very strong reason to remove it.

### Why `Core`
These are the conditions / rights / structural assumptions:
- Role Contract
- Done Is Not a Mood
- Right to Disagree
- Attention Engineering
- Semantic Hygiene

### Why `Operations`
These are workflow and runtime behavior patterns:
- CDD
- Agent Loop
- Do Not Stop at the First Weak Signal
- Semantic Logging
- Session End Protocol

This split made the document:
- easier to scan
- cleaner to reason about
- more architecturally sound
- less mixed-up than v1/v2

---

## 12) Notes on specific points in v3

### Role Contract
Keep the anti-micromanagement framing.
This is not a “humans steer, agents execute” worldview.
It is a harness/ownership framing.

### Done Is Not a Mood
Keep it.
It may look abstract to humans at first, but it is one of the most useful anti-fake-completion rules.
Do not let it balloon into a giant procedural verification section.

### Right to Disagree
One of the strongest human-facing points.
Do not weaken it into generic safety boilerplate.

### Attention Engineering
Keep the practical heuristic.
The numeric heuristic (`200-300 lines` for frequently edited Python/TypeScript modules) is intentionally provocative.
It is not treated as a universal law, but as a useful refactor signal.

### Semantic Hygiene
The example is worth the tokens.
This is one of the few places where a concrete example improves usability enough to justify itself.

### CDD
This is both a practical and brand-defining part of the protocol.
Do not over-formalize it.
The subagent/delegation extension is important.

### Agent Loop
Keep it compact.
Do not turn it into a shadow workflow manual.

### Do Not Stop at the First Weak Signal
Important because it protects against early collapse, weak evidence, and false “clean results”.

### Semantic Logging
Must stay short in the minimal version.
A more detailed version can exist elsewhere later.

### Session End Protocol
Keep it crisp.
The handoff must remain short enough to be usable.

### Hello Agent!
Preserve unless there is a very strong reason to remove it.

---

## 13) Agent-to-agent reflection

If I were handing this topic directly to another agent, here is what I would emphasize:

### Do not “improve” this file by making it more textbook-correct but less alive.
That would be a regression.

### Do not assume every correct recommendation belongs inside the document.
A lot of correct things were intentionally left out.

### Respect the fact that this project is trying to satisfy human adoption and agent utility at the same time.
That makes the design weird on purpose.

### The user is not treating the agent as a subordinate assistant.
That changes everything.
Many default formulations that sound reasonable in generic AI UX become wrong here.

### The anti-micromanagement stance is not rhetoric.
It is central.
If you lose that, you lose the protocol.

### Hooks matter.
WHY blocks matter.
The file’s “voice” matters.

### But never confuse memorable with vague.
Every line still has to earn its place.

---

## 14) The shortest possible summary

If you only remember one thing:

> **Agent1st Protocol is a minimal behavior-layer for strong agents.  
> It exists to define roles, rights, quality expectations, friction handling, focus discipline, and handoff quality—without bloating into a repo manual or repeating model/tool prompts.**

