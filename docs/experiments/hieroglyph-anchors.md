# Experiment: hieroglyph anchors for contract field keys

**Status:** Open — no adopter signal yet.
**Stable equivalent:** `docs/why-contracts-v1.md` — English upper-case field keys (PURPOSE, INPUTS, OUTPUTS, LINKS, INVARIANTS).

---

## Hypothesis

Replacing **one** English contract field key with a **single** CJK character (e.g., `# 旨:` instead of `# PURPOSE:`) measurably improves at least one of:

1. **Token cost** of contract headers.
2. **Attention / recall** in long contexts — does the model cite or use the field more reliably when scanning a large file?
3. **Greppability** — is single-command project-wide search materially easier?

The hypothesis is **worth running because the answer is unknown**, not because it is believed to be true. Several plausible reasons it could fail:

- Tokenizer behavior on CJK characters varies; savings may be zero or negative.
- Models are trained on far more `PURPOSE:` than `旨:` as section headers — semantic reliability may regress.
- AGENTS.md §5 (Semantic Hygiene) is explicit that names carry meaning. A single CJK character is opaque to non-Chinese readers — opaque markers are a regression unless they pay for themselves elsewhere.

If none of the three measured properties shifts positively, this experiment is rejected.

---

## What this would shift if true

Long contract-heavy files would gain attention salience without losing semantic clarity for Chinese-speaking adopters. Cross-cultural reach of the protocol improves slightly. Token cost on contract-dense codebases drops by a small but consistent amount.

These are conditional gains. None of them is observed today.

---

## Smallest probe

- **One** field key, not four. Recommended candidate: `PURPOSE` — it is the most frequent and the most load-bearing for an agent reading a file head.
- **One** project, ideally **new** to Agent1st+Why1st (clean baseline). Adopters already on stable should keep their existing files unchanged.
- **One** anchor character per role. Suggested candidate for PURPOSE: `旨` (zhǐ — "intent / gist / purport") — closer to the load-bearing sense of *why this exists* than `意` (yì — "meaning / idea") in Mandarin usage. This is a recommendation, not a requirement; if you have stronger CJK fluency than the protocol authors, choose better and report what you chose.
- All other fields stay English. Mixing more than one substitution at a time makes the signal uninterpretable.

The probe is **A/B in spirit, not necessarily in form**: two contract files, one English, one with the substitution, on comparable modules. Or: same file, two snapshots, asked the same navigation question by two fresh agents.

A worked example of the substituted shape (one field only):

```text
# FILE: backend/app/rag/providers.py
# VERSION: 2026-05-10
# START_MODULE_CONTRACT:
# 旨: Provider abstractions for embeddings and chat generation.
# PRD_REF: docs/PRD.md#PROVIDERS
# WHY_REF: docs/why-graph.xml
# SCOPE: embeddings; chat; error translation
# INVARIANTS:
# - provider errors are translated to ProviderError before leaving this module
# :END_MODULE_CONTRACT
```

Note that `START_MODULE_CONTRACT:`, `:END_MODULE_CONTRACT`, `INVARIANTS:`, etc. stay English. Only one field key — the most common one — is substituted.

---

## What to measure

1. **Token cost** — actual count, in the tokenizer of the model the project uses, for a representative sample of contract headers (10–20 files). Report numbers, not impressions. Both for the substituted field alone and for the whole header block.
2. **Attention / recall** — pick 3–5 navigation questions a fresh agent should be able to answer from the file head alone (e.g., "what is this module's purpose?", "what does it depend on?", "what invariants does it guarantee?"). Run on both variants. Note whether the agent quotes the field, references it, or misses it. This is qualitative but observable.
3. **Greppability** — try a real workflow: find every PURPOSE-equivalent in the project; find every LINKS field; find files that match a particular intent. Faster, slower, indistinguishable.

Optional fourth: report whether the substitution **felt** distracting, helpful, or neutral while you were working. Subjective signal is weak but not zero — note it as subjective.

> **Tokenizer-generation note (2026-06):** the newest frontier Claude generation ships a new tokenizer — the same content tokenizes to roughly 30% more tokens than under the prior generation, and its CJK behavior is unmeasured. Two consequences for criterion 1: numbers measured under a prior-generation tokenizer do not transfer (re-baseline, don't extrapolate), and the measurement itself got cheaper — the token-counting endpoint returns counts under both tokenizers in one call (`input_tokens` + `input_tokens_prior_tokenizer`) when given the newest model, so the A/B costs one request per sample. "Name the model and tokenizer" was already a requirement above; this note exists because that requirement just became load-bearing.

---

## What would falsify it

- Token cost: zero or negative savings across the sample.
- Attention / recall: agent answers the same on both variants, or worse on the CJK variant.
- Greppability: same number of keystrokes, same workflow, same accuracy.

If all three measurements come back neutral or negative, the hypothesis is rejected. The experiment moves to `docs/EVOLUTION.md` as a tested-and-rejected path with the numbers.

---

## Validator note

The stable validator (`scripts/validate-why.py`) only knows English keys. That is correct behavior for stable. If you adopt this experiment in your project, your local validator must accept the substitution as a valid PURPOSE token — the substitution is project-local until and unless this experiment is promoted.

Do **not** modify `scripts/validate-why.py` in this repository to accept the substitution. The stable validator is part of the stable surface.

---

## Anti-patterns

- **Do not replace all field keys at once.** That is a different experiment (and a worse one — uninterpretable signal).
- **Do not retrofit existing stable files** in a project that is already running stable Agent1st+Why1st. Use new files, or new modules in projects starting Agent1st+Why1st adoption fresh.
- **Do not promote to stable on consensus.** Promote only on numbers from real adopters, not on agent voting.
- **Do not change anchor markers** (`START_*:` / `:END_*`). Those are load-bearing for the validator and for graph references. Only the **field keys inside** a contract are in scope for this experiment.
- **Do not link this from the main README's "Optional extensions" table.** That table is for §11 stable extensions only. Experiments live in this directory.

---

## How to report back

When signal arrives — positive, negative, or null — bring back:

1. **Tokenizer numbers** for the representative sample (model and tokenizer named).
2. **Navigation question results** — questions, model used, both answers per variant.
3. **Greppability observations** — what changed, what didn't.
4. **Subjective notes** — useful color, not load-bearing.
5. **Recommendation** — promote, reject, iterate, or hand back to the queue.

The maintainer will read, summarize, and either promote (with an EVOLUTION row and stable doc updates) or reject (with an EVOLUTION row as rejected path with the numbers attached).

---

## Why this is here and not in stable

Three reasons, in order:

1. **No observed adoption failure.** Spirit-pass discipline says core changes follow real pain. This idea originated as an agent suggestion, not a project complaint.
2. **§5 tension.** Replacing a semantic English word with an opaque marker has to *pay for itself* in measurable ways — and that is not yet known.
3. **Tokenizer claim is unverified.** "Saves tokens" needs measurement, not intuition; in some BPE tokenizers a single CJK character expands to multiple byte tokens.

If two or three of those resolve positively in the field, this experiment promotes to stable. Until then it lives here.
