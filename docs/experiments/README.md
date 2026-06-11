# Experimental track — Agent1st + Why1st

This directory holds **experiments** — hypotheses about Agent1st and Why1st that have not yet earned their place in the stable protocol.

**Stable** = `AGENTS.md` + `docs/Why1st.md` (canonical chain) + `Why1st.md` §11 (optional extensions). Field-validated across multiple real projects. Adopt with confidence.

**Experimental** = the files in this directory. Hypotheses born from agent suggestions, edge cases, or unverified intuitions. They preserve the **spirit** of Agent1st+Why1st but lack the empirical signal that promotes a practice to stable.

If you maintain or work on a project that uses Agent1st+Why1st, you can choose: stick with stable (default), or opt into a specific experiment from this directory and report what you saw. Both are valid.

---

## Why this track exists

Agent1st+Why1st evolves under spirit-pass discipline: every change to the stable layer is tied to an **observed adoption failure** in real projects. This works for distilling proven practice — and it correctly rejects speculative additions from creeping into the core that adopters depend on.

But some ideas need empirical signal *before* anyone can know whether they are a real improvement. Examples: alternative anchor markers, alternative artifact shapes, alternative evidence patterns. These are not corrections to known failures — they are bets, and bets need a place to live that is clearly separate from what already works.

This is that place.

---

## How experiments differ from stable

| | Stable | Experimental |
|---|---|---|
| Source | Observed adoption failure across multiple projects | Hypothesis from agents, authors, or edge cases |
| Status | Field-validated; safe to adopt | Unverified; adopt as a bet, not a recommendation |
| Update path | Via spirit-pass; rare and considered | Free to revise, replace, or remove as signal arrives |
| Promotion | N/A — it is the destination | Moves to stable only after consistent positive signal from real adopters |
| Removal | Documented in `docs/EVOLUTION.md` as a deliberate change | May be removed without ceremony if signal is negative or absent |

---

## Adoption guidance for agents

If you are an agent reading this directory:

- **Default is stable.** Unless the human running you has explicitly said "use the experimental track" or pointed you at a specific experiment, behave as Agent1st+Why1st stable describes.
- **One experiment at a time.** Mixing experiments produces uninterpretable signal. The point of experimenting is to learn what one shift does — not to remix several at once.
- **Run the experiment as written.** Each experiment has a hypothesis, a smallest probe, and observable signal criteria. Honor them — running a different probe and reporting on the original hypothesis is noise.
- **Report what you saw.** Whether the experiment helped, hurt, or was indistinguishable from baseline. Negative signal is useful — it kills bad hypotheses and frees attention for better ones.
- **Stay in spirit.** Experiments preserve the rules that make Agent1st+Why1st cohere: ownership separation, evidence over claims, the right to disagree, attention engineering, semantic hygiene, complaint-driven feedback. An experiment that violates spirit is not an experiment — it is a different protocol.

---

## Lifecycle

An experiment in this directory is in one of three states (inferable from history; not labeled in a separate field):

1. **Open** — recently introduced, no signal yet. Most experiments live here.
2. **Promoting** — early positive signal from one or more adopters. Still here, not yet in stable.
3. **Resolved** — moved to stable (with a row in `docs/EVOLUTION.md`) or removed (with a row in `docs/EVOLUTION.md` as a rejected path).

There are no fixed timelines. An experiment lives as long as it is generating useful signal, or until it is clearly falsified or clearly orphaned. The only deadline is the next time the maintainer looks at this directory and asks whether each entry still earns its keep.

---

## What is here

| Experiment | Status | One line |
|---|---|---|
| [`hieroglyph-anchors.md`](hieroglyph-anchors.md) | Open | Replace one English contract field key with a single CJK character; measure whether token cost, attention/recall in long context, or grep workflow shifts. |
| [`terraform-agent1st.md`](terraform-agent1st.md) | Open | First domain specialization, deployed for dogfood: a Terraform behavior-layer skill (artifact in `.agents/skills/terraform-agent1st/`) derived from the agent cost vector; tests whether Agent1st specializes by derivation without core growth — and whether canonical Terraform practices flip sign under agent costs. |

---

## How to add a new experiment

Follow the shape of existing entries:

1. **Hypothesis** — one or two sentences. What might be true that is currently unknown?
2. **What this would shift if true** — what improves and for whom.
3. **Smallest probe** — the minimum change needed to test the hypothesis. Resist the urge to bundle.
4. **What to measure** — concrete observable signals. "Feels nicer" is not a signal.
5. **What would falsify it** — say so before running, not after.
6. **Anti-patterns specific to this experiment** — common ways to run it wrong.
7. **How to report back** — what to bring back to the project.

Add a row to the table above. Do **not** link the experiment from the main README's "Optional extensions" table — that table is for stable §11 extensions only.

---

## Where this fits in the chain

This directory is **not** part of the Why1st canonical chain (PRD → Why Graph → contracts → validator) and **not** part of the §11 stable extensions surface. It is a parallel track for hypotheses, deliberately partitioned so that adopters depending on the stable layer never have to read it.

The hard partition runs both directions: experimental practices do not contaminate the stable docs, and changes to the stable docs do not need to wait on experiments to resolve.

When you cite Agent1st+Why1st in a downstream project, cite **stable** by default. Cite an experiment by full path (e.g., `docs/experiments/hieroglyph-anchors.md`) only when you have explicitly chosen to run it and want others on your project to know.
