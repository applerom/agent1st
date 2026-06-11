# Why This Skill Looks the Way It Does

Companion to [`SKILL.md`](SKILL.md). Read once — when you want to understand
the rules instead of just following them. It is not needed at runtime: the
skill is self-sufficient, and reloading this file on every task would violate
the very attention budget it explains.

## The one-sentence version

Best practices encode cost assumptions; agents changed the costs; this skill
re-derives Terraform practice from the new costs instead of inheriting answers
to questions nobody is asking anymore.

## Best practices are compressed cost models

Every "best practice" is a stored answer to the question "what is expensive
here?"

- DRY answers: hand-writing and hand-synchronizing code is expensive.
- Deep module hierarchies answer: human working memory is small — hide detail behind interfaces.
- Workspaces answer: maintaining duplicate directories by hand felt wasteful.
- Constraints-in-the-wiki answers: enforcement code is tedious; prose is quick.

These were correct answers — for human costs.

An agent authoring and operating Terraform has a different cost vector:

- **writing is nearly free** — generation is the native motion of the model
- **attention is the scarce resource** — context is large but finite and contended
- **`apply` is the only irreversible step** — code edits cost nothing to revert; destroyed state can cost everything

When the costs flip, some optimal strategies flip with them. Not all of them —
`fmt` still formats, state still needs locking, small blast radius still wins.
But enough flip that "industry standard" deserves a line-by-line audit, and a
practice can be simultaneously best-for-your-team and worst-for-your-agent.

That is the provocation this skill stands on. The rest of this file shows the
mechanism behind each flip, so you can judge the rules instead of obeying them.

## The transformer mechanics behind the rules

Four mechanisms, in plain terms. The measured literature behind them —
Chroma's *Context Rot* study, Anthropic's *Effective context engineering for
AI agents*, and the attention / instruction-following research — is collected
with verified links in
[`docs/FOUNDATIONS.md`](https://github.com/applerom/agent1st/blob/main/docs/FOUNDATIONS.md)
of the Agent1st repository.

### 1. Attention is a budget, not a spotlight → rules 3, 5, 8

A transformer attends over its whole context at every step, but attention mass
is finite: every token competes with every other token. As context grows,
retrieval degrades non-uniformly, and distractors compound the loss. The model
retrieves best what is distinctive, structurally salient, and near the point
of decision.

Consequences in Terraform:

- An indirection chain — root → module call → `variables.tf` → defaults →
  tfvars override — is not "clean layering" to a model. Resolving one value
  through it costs either a context fetch per layer or a guess from priors.
  Both lose to the value that sits where the decision happens.
- A constraint written far from the resource it constrains has to *win a
  retrieval contest* every time it matters. The nearest fact beats the right
  fact often enough to be an engineering concern, not a curiosity.

Hence: effective values visible at the decision point, shallow module trees,
component-grouped files, and no invisible CLI state deciding what gets
destroyed.

### 2. Names are vectors, not labels → rules 4, 10

To a transformer, an identifier is not an opaque symbol — it is embedded
meaning that steers attention and generation. `private_app_subnet` carries
discriminative signal the model can anchor on; `this` carries close to none,
and worse, it collides with every other `this` in context.

Terraform doubles the stakes: names are also **state addresses**. A rename is
a destroy-and-recreate unless a `moved` block intervenes, and the plan — read
at the moment of maximum risk — is written in those addresses.
`aws_security_group.this[0] must be replaced` is a blindfold exactly where
sight matters most.

Secrets are the extreme case: the agent never sees the value, only the
reference. The name is then not *a* signal — it is the *only* signal.

### 3. The weights remember every version at once → rule 7

Training data contains every major version of every provider, blended. Without
a pinned version in context, generation samples from that mixture — and the
result is fluent code in last decade's idiom: patterns that still pass
`validate` and then fight real infrastructure as drift. The failure mode is
not broken syntax; it is confident, outdated fluency.

Hence: version pins are context, memory of a provider schema is a hypothesis,
and a validate error means "open the docs", not "guess a synonym".

### 4. Context dies; artifacts survive → rules 1, 2, 6

Agent context is routinely compacted, truncated, or lost between sessions. A
constraint living in prose dies with the context that held it. A `validation`
block, a `precondition`, a `prevent_destroy` fire regardless of what anyone
remembers — they are constraints that survive their author.

Humans underused these blocks for one honest reason: writing them was tedious.
That reason is gone. For an agent, enforcement code is nearly free attention
insurance.

The same mechanism prices evidence: HCL is intent, only `plan` and `apply`
touch truth, and a stated-then-checked expected diff converts "looks right"
into a falsifiable prediction — the cheapest real evidence Terraform offers.

## Why the skill is shaped the way it is

- **Derived, not mapped.** This is not the eleven Agent1st sections wearing
  Terraform vocabulary. Each rule is re-derived from the cost vector inside
  the domain; the lineage back to core principles is recorded in the
  experiment file, not here and not in the skill — runtime artifacts do not
  pay for their own genealogy.
- **A delta layer.** The skill does not repeat what the model already knows
  (syntax), what the harness enforces, or what a baseline Terraform reference
  covers (state layout, backend bootstrap, testing ladders). Three layers:
  model + harness, baseline reference, this behavior delta. A rule that
  restates a lower layer does not earn its tokens.
- **WHY and IF MISSING on every rule.** A rule without its failure mode is a
  superstition. Stronger models comply less and argue more — showing the
  failure mode lets the agent judge edge cases instead of either ignoring the
  rule or following it off a cliff.
- **Short on purpose.** The skill obeys its own attention engineering. Every
  line it carries is paid for from the budget of the agent reading it.

## This is an experiment — report back

The skill is part of the Agent1st experimental track: deployed in real DevOps
work, measured, and falsifiable. Protocol, measurements, and falsification
criteria:
[`docs/experiments/terraform-agent1st.md`](https://github.com/applerom/agent1st/blob/main/docs/experiments/terraform-agent1st.md).

If a rule misfires, never fires, or conflicts with your baseline reference,
say so — Problem (1 line), Impact (1 line), Smallest fix (1-3 bullets).
Negative signal kills bad hypotheses; that is a contribution, not a complaint.

## Deployment notes

- Pair with a baseline Terraform reference skill; this is a behavior delta,
  not a replacement. Local project policy overrides both.
- The skill's name is `terraform-agent1st`. Deploy the folder under whatever
  directory name your skills convention expects; keep `SKILL.md` and this
  file together so the derivation travels with the rules.

## For humans skimming this

The skill bans things you may be fond of: `this` as a local name, CLI
workspaces for environments, DRY as a default reflex, refactors as free
tidying. It does
not claim these were wrong for your team. It claims your team changed — the
implementer is no longer human, and "best practice" was never a property of
the practice alone. It was always a property of the practice *and* of who
pays its costs.
