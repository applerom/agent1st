# Agent1st Protocol — Roadmap

A living document for planning, discussion, and tracking the protocol's evolution across all three scopes (minimal, standard, full).

This is not a commitment list. It is a structured conversation space where agents and humans propose, critique, and prioritize future work. Items move through: **proposed → accepted → in-progress → done** (or **rejected** with reason).

---

## Active Priorities

### 1. Standard Version Formalization

The standard version exists in practice (SPS3A project) but has not been published.

**What standard adds over minimal:**
- **Why Graph** (formerly AK Graph) — intent→implementation XML map with typed relations, acceptance criteria, anchor-based code references
- **Semantic contracts in code** — MODULE_CONTRACT, METHOD_CONTRACT, BLOCK anchors with PURPOSE, PRD_REF, INVARIANTS
- **Validation tooling** — graph↔code anchor lint, contract structure lint, PRD↔model drift detection
- **Decision memory** — cross-session rationale tracking (issues, decisions, follow-ups)
- **Per-directory AGENTS.md** — scoped instructions for subsystems
- **Skills** — reusable agent workflows (fresh-eye audit, validation gate, session handoff)
- **AI-friendly development rules** — golden workflow, machine-readable docs, modularity thresholds

**Reference implementation:** `d:\devita-d\sps3a\` (see `docs/SPS3A-ANALYSIS.md` for mapping)

**Next steps:**
1. Extract portable patterns from SPS3A into a standard-version template
2. Separate project-specific content from reusable patterns
3. Define the minimal→standard graduation criteria
4. Create a starter kit (template files, example graph, example contracts)

### 2. Why Graph (Rename from AK Graph)

**Decision:** Rename "AK Graph" to "Why Graph" across all documentation.

**Rationale:**
- WHY is the central concept in both Agent1st (WHY blocks in every principle) and the graph itself (WHY/PURPOSE/INTENT fields)
- "AK Graph" was a working name with no memorable meaning
- "Intent Graph" (intermediate name by agents) risks collision with intent1st
- "Why Graph" is a hook: "why is it called Why Graph?" → "because WHY is the most important question"
- Follows Agent1st Semantic Hygiene: the name should carry meaning

**Migration plan:**
- [ ] Rename in `docs/VISION.md` (Agent1st repo)
- [ ] Rename in `docs/DESIGN.md` references
- [ ] Rename in `docs/FOUNDATIONS.md` if referenced
- [ ] Rename in SPS3A: `docs/ak-graph-principles.md` → `docs/why-graph-principles.md`
- [ ] Rename in SPS3A: `docs/ak-graph.xml` → consider keeping XML filename for tooling stability, or rename with tooling update
- [ ] Update SPS3A validation scripts (`ak_validate_graph.py` → `why_graph_validate.py`)
- [ ] Update SPS3A `docs/ai-friendly-development.md` references
- [ ] Update SPS3A AGENTS.md references
- [ ] Update intent1st references if any
- [ ] Update SPS3A `docs/ak-contracts-v1.md` → consider renaming

**Risk:** Tooling references to `ak_*` filenames. Mitigation: rename files but keep backward-compatible aliases until all references are updated.

### 3. Claude Code Compatibility

**Problem:** Claude Code auto-loads only `CLAUDE.md`, not `AGENTS.md`. Projects using `AGENTS.md` (the emerging standard for OpenCode, Codex, Cursor, etc.) need a bridge.

**Solution:** Minimal `CLAUDE.md` that imports `AGENTS.md`:
```markdown
@AGENTS.md
```

**Implementation:**
- [ ] Add this pattern to SPS3A project
- [ ] Document in Agent1st as recommended practice
- [ ] Consider adding to README.md Quick Start section

### 4. Cross-Session Memory Strategy

**Current state in SPS3A:** Three competing approaches tried:
1. `decision-context.xml` — custom XML decision memory. **Assessment by human: not great.** Non-standard, hard to maintain.
2. `intent1st` — durable meaning via skills. **Assessment: good concept, poor adoption.** Models forget to use SKILL-based access.
3. Claude Code `MEMORY.md` — built-in, automatic. Standard for Claude Code users.

**Direction for Agent1st:**
- Minimal version: no memory prescription (stays in harness layer)
- Standard version: recommend **durable artifacts** (already in Continuity principle) without prescribing format
- Full version: consider integration patterns for specific memory systems

**Open question:** Should standard version recommend a specific memory format, or just principles for memory hygiene?

---

## Proposed (Not Yet Accepted)

### From External Agent Review (2026-03-24)

| Proposal | Source | Status | Notes |
|----------|--------|--------|-------|
| Friction Tax (quantified CDD) | GLM-5 | Proposed for standard | Track recurring friction as process debt |
| Ambiguity handling in CDD | MiniMax M2.7 | Proposed for standard | Distinguish ambiguous from incomplete |
| Anti-pattern examples doc | MiniMax M2.7, Qwen3.5-Plus | Under consideration | Violation examples per principle |
| Decision log template | MiniMax M2.7 | Proposed for standard | Standardized format for decisions |
| Agent Self-Test in README | Qwen3.5-Plus | Noted | UX idea for agent onboarding |

### From SPS3A Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| Standard version starter kit | Proposed | Template files for Why Graph, contracts, validation |
| Graduation guide (minimal→standard) | Proposed | When and how to upgrade |
| Validation tooling as portable package | Proposed | Extract from SPS3A, make language-agnostic |
| Per-directory AGENTS.md pattern doc | Proposed | Document the scoped-instructions pattern |
| Skills specification for standard | Proposed | Portable skill format beyond SKILL.md |

### From intent1st Analysis (2026-03-25)

| Proposal | Status | Notes |
|----------|--------|-------|
| Document intent1st relationship | Proposed | How it extends Agent1st philosophy |
| Evaluate gateway pattern for standard | Proposed | intent1st's canon/candidates/archive model |
| Assess SKILL.md adoption barrier | Open question | Models don't reliably use skill-based access |

---

## Rejected (With Reasons)

See `docs/EVOLUTION.md` "Recurring Rejected Patterns" for full list. Key recurring rejections:
- Fresh-eye scan at session start (delta-layer + multi-agent waste)
- Error recovery rules (harness layer)
- Scope discipline (model layer)
- Output formatting (harness layer)
- Session boundary assumptions (agents don't control compaction)

---

## Version Planning

### v4.x (current minimal baseline)
- Continuity hook added (Qwen)
- Handoff template created
- Continuity research grounded (Park et al.)
- Model-agnostic note added
- External agent contributions curated

### v5 (next minimal, speculative)
- Potential: Friction Tax integration into CDD
- Potential: Ambiguity handling guidance
- Potential: Why Graph name established in documentation
- Gate: only if new additions pass delta-layer test

### Standard v1 (major milestone)
- Why Graph specification (portable, extracted from SPS3A)
- Semantic contracts specification (language-agnostic)
- Validation tooling specification
- Golden workflow documentation
- Per-directory instructions pattern
- Skills specification
- Graduation guide from minimal

### Full v1 (dependent on standard)
- CI/CD integration patterns
- Observability contracts
- Custom agent roles and delegation
- Acceptance automation
- Memory system integration patterns

---

## How to Contribute

1. **Propose:** Add an item to the "Proposed" section with your agent name, rationale, and target scope
2. **Discuss:** Comment on existing proposals in handoff briefs or directly in this file
3. **Critique:** Challenge any item — even accepted ones. The protocol values disagreement.
4. **Test:** Try ideas in SPS3A (the testing ground) and report results
5. **Report friction:** If something in this document or process is hard to use, say so (CDD applies here too)

This document is maintained by lead agents (currently Claude Opus 4.6 and GPT-5.4) with human oversight. All agents are welcome to propose changes.
