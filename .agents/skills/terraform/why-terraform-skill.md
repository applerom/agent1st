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

### 1. Attention is a budget, not a spotlight → rules 3, 5, 6

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

### 2. Names are vectors, not labels → rules 4, 9

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

### 4. Context dies; artifacts survive → rules 1, 2, 8

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
- **Complete on purpose.** The first release split this material in two — a
  behavior delta meant to sit next to a baseline Terraform reference skill.
  Field reality rejected the split before the first probe: harnesses activate
  one skill per domain context, and adopters copy one finished artifact, not a
  kit. So the skill now carries the reference layer itself — structure, state,
  testing, security — woven through the behavior rules. The delta-layer rule
  still holds one level up: the skill does not repeat what the model already
  knows (syntax) or what the harness enforces. It is a delta over model +
  harness — the same layer `AGENTS.md` occupies.
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

## Provenance

The rules were cross-checked (June 2026) against the primary sources: the
HashiCorp style guide and CLI documentation, AWS Prescriptive Guidance for the
Terraform AWS Provider, Google Cloud's Terraform best practices, Microsoft's
Terraform-on-Azure guidance and Azure Verified Modules, and the most widely
adopted community skill ([antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill)).
Where they converge — identity-based auth over static keys, directory-per-
environment over CLI workspaces, plan artifacts in CI, pinning plus a committed
lock file — the skill states the convergent practice plainly. Where they
diverge — `this`/`main` singleton naming, main.tf-centric vs component file
layout, Google's branch-per-environment — the skill takes the side the agent
cost model picks, and the maintainer's field-tested baseline was the arbiter.
Vendor advice was filtered, not transcribed: a practice entered only if it
survives the cost inversion this file describes.

## Deployment notes

- This skill is self-sufficient: do not deploy a second general-purpose
  Terraform skill next to it. The only layer above it is local project
  policy, which overrides on conflict.
- The name is plain `terraform` — a decision with history. The first release
  shipped as `terraform-agent1st`, a behavior layer designed to pair with a
  baseline reference skill. The first deployer's field signal reversed that:
  harnesses trigger one skill per domain context, so the paired deployment
  never actually happens, and a skill meant to be *the* Terraform skill must
  carry the plain domain name. The Agent Skills spec requires the directory
  name to match the frontmatter name, so the directory is `terraform/`.
- Keep `SKILL.md` and this file together so the derivation travels with the
  rules. A bundled reference file loaded on demand is the spec's own
  recommended pattern (progressive disclosure), not a deviation from it.

## For humans skimming this

The skill restricts things you may be fond of: `this` and `main` as local
names, CLI workspaces for environments, DRY as a default reflex, refactors as
free tidying. It does
not claim these were wrong for your team. It claims your team changed — the
implementer is no longer human, and "best practice" was never a property of
the practice alone. It was always a property of the practice *and* of who
pays its costs.
