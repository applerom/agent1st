# Agent1st Protocol — SPS3A Analysis

How Agent1st emerged from real practice, and how SPS3A serves as the reference implementation for the standard version.

---

## Context

SPS3A (`d:\devita-d\sps3a\`) is a GraphRAG application for bioresonance therapy. It is also the project where Agent1st Protocol was born, tested, and evolved through hundreds of real development sessions.

This document captures the relationship for future agents working on either project.

---

## 1) How Agent1st Emerged from SPS3A

Agent1st was not designed top-down. It was extracted bottom-up from real friction:

- **Role Contract** emerged from sessions where agents defaulted to passive copilot mode instead of driving implementation
- **Done Is Not a Mood** emerged from agents claiming completion without evidence, discovered only when humans tested
- **Right to Disagree** emerged from agents silently implementing risky changes they disagreed with
- **CDD** emerged from agents silently working around tooling problems instead of reporting them
- **Agent Loop** emerged from agents either over-planning or jumping to code without exploration
- **Semantic Hygiene** emerged from SPS3A having four different things called "graph" (Why Graph, LangGraph runtime, DR Graph, Graph Explorer UI)
- **Continuity** emerged from losing context across sessions when server-side compaction destroyed conversation
- **Attention Engineering** emerged from agents losing focus in long contexts with competing instructions

The SPS3A `AGENTS.md` was the first formalization. The portable Agent1st Protocol was extracted from it by separating project-specific content (§1-§9) from universal principles (§0).

---

## 2) SPS3A as Standard Version Reference

SPS3A implements what Agent1st's `docs/VISION.md` describes as the "standard version":

| Standard Version Component | SPS3A Implementation |
|---|---|
| **Why Graph** (intent→implementation map) | `docs/ak-graph.xml` — XML schema 0.8, USECASE→FEATURE→API→MODULE→ANCHOR hierarchy |
| **Semantic contracts in code** | MODULE_CONTRACT, METHOD_CONTRACT, BLOCK anchors with PURPOSE, PRD_REF, INVARIANTS |
| **Validation tooling** | `scripts/tooling/ak_validate_graph.py`, `anchor_lint.py`, `validate_decision_context.py`, `validate_prd_defaults.py` |
| **Decision memory** | `docs/decision-context.xml` — issues, decisions, follow-ups with typed references |
| **Per-directory AGENTS.md** | `scripts/AGENTS.md` — scoped instructions for scripts subsystem |
| **Skills** | `.agents/skills/consult-intent1st/`, `.agents/skills/capture-intent1st-candidate/` |
| **AI-friendly development rules** | `docs/ai-friendly-development.md` — golden workflow, modularity, validation |
| **PRD as ground truth** | `docs/PRD.md` — product requirements referenced by graph and contracts |

### The Golden Workflow (from SPS3A)

```
PRD.md (product intent)
  ↓ referenced by
Why Graph (docs/ak-graph.xml) — USECASE → FEATURE → API → MODULE → ANCHOR
  ↓ anchors point to
Code contracts (MODULE_CONTRACT, METHOD_CONTRACT, BLOCK anchors)
  ↓ validated by
Tooling scripts (ak_validate_graph.py, anchor_lint.py)
  ↓ decisions tracked in
Decision context (docs/decision-context.xml)
```

This workflow is what makes the standard version operationally different from minimal: agents always have the intent→implementation map "in front of them" when editing code, and the map is validated to stay consistent.

---

## 3) Mapping: SPS3A AGENTS.md vs Agent1st v4

SPS3A `AGENTS.md` §0 covers 10 of 11 Agent1st v4 principles:

| v4 Principle | SPS3A Status | Gap |
|---|---|---|
| Role Contract | Present, full | None |
| Done Is Not a Mood | Present, full, with project-specific verification checklist | None |
| Right to Disagree | Present, full | None |
| Attention Engineering | Present, full | None |
| Semantic Hygiene | Present, extended with "four graphs" example | None |
| CDD | Present, with severity levels | None |
| Agent Loop | Present, full | None |
| Do Not Stop at First Weak Signal | Present, full | None |
| **Delegation Design** | **Missing** | **Hard gap** — this v4 addition hasn't been backported |
| Semantic Logging | Present, full | None |
| Continuity | Present as "Session protocol" | Label drift only |

### What SPS3A Adds Beyond Agent1st Minimal

- §1 Fast Onboarding (specific read order, run commands)
- §2 Semantic-First Delivery Workflow (the golden workflow)
- §3 Contracts & Anchors quick reference
- §4 Project Defaults & Boundaries
- §5 GraphRAG Model/Terminology
- §6 Deterministic Commands
- §7 Shell/Runtime Notes
- §8 SPS2 Data Reference
- §9 Quick Links
- intent1st integration sub-section in §0

---

## 4) What SPS3A Teaches About Standard Version Design

### Portable Patterns (extract for standard version)

1. **Why Graph specification** — intent→implementation map concept. The XML schema is one implementation; the pattern (typed nodes, relations, acceptance criteria, anchor-based code references) is portable.

2. **Semantic contracts** — comment-based markers with PURPOSE, PRD_REF, INVARIANTS. Language-agnostic pattern (works in Python, TypeScript, any comment syntax).

3. **Anchor-based navigation** — file#START_NAME instead of line numbers. Stable across refactoring. Machine-parseable.

4. **Validation pipeline** — scripts that verify graph↔code consistency. The specific scripts are SPS3A-bound, but the validation pattern is portable.

5. **Golden workflow** — PRD → Graph → Contracts → Code → Validate. The specific steps are SPS3A-bound, but the workflow pattern (intent-first, graph-first, validate-always) is portable.

### Project-Specific Patterns (stay in SPS3A)

1. GraphRAG terminology and pipeline
2. SPS2/Devita data references
3. PowerShell-specific commands
4. Port assignments and runtime notes
5. Next.js/FastAPI specifics

---

## 5) intent1st and Its Relationship to Agent1st

`intent1st` (`d:\ai\intent1st\`) is a **durable meaning repository** — a separate project for preserving WHY-driven knowledge across sessions and projects.

| Aspect | Agent1st | intent1st |
|---|---|---|
| **Scope** | How agents work (behavior protocol) | What agents know (meaning preservation) |
| **Persistence** | AGENTS.md in project repo | Separate git-backed repo |
| **Access** | Auto-loaded by harness | Skills-based gateway |
| **Content** | Principles, rights, quality stances | Decisions, rationale, preferences, process meaning |
| **Time scale** | Per-session behavior | Cross-session, cross-project |

They are complementary: Agent1st guides how agents act, intent1st records what they learn.

### Current Assessment

**Strengths:** Well-structured (archive → candidates → canon), agent-legible, git-backed, skill-based access.

**Challenges:** Models reliably forget to invoke skills. The SKILL.md mechanism depends on harness support that current models don't consistently provide. This is an adoption barrier, not a concept problem.

**Relevance to Agent1st standard version:** The *idea* of durable meaning preservation is essential. The specific *mechanism* (separate repo + skills) may need alternatives depending on harness capabilities. Claude Code's MEMORY.md is a simpler but less structured approach. The standard version should recommend the principle without mandating the mechanism.

---

## 6) For Agents Working on Agent1st

If you're working on Agent1st and want to understand the standard version:

1. **Read this document first** — it maps the landscape
2. **Look at SPS3A's `docs/ak-graph-principles.md`** — the Why Graph authoring guide
3. **Look at `docs/ak-contracts-v1.md`** — the contracts specification
4. **Look at `docs/ai-friendly-development.md`** — the golden workflow
5. **Look at `scripts/tooling/`** — the validation harness
6. Don't get lost in SPS3A's domain specifics (bioresonance, GraphRAG) — focus on the *patterns*

### SPS3A as Testing Ground

SPS3A serves as the testing ground for Agent1st development:
- New Agent1st versions can be tested by updating SPS3A's AGENTS.md §0
- Standard version patterns can be validated against SPS3A's real infrastructure
- Changes to Why Graph specification can be prototyped in SPS3A's `docs/ak-graph.xml`
- Friction from using the protocol in practice feeds back into Agent1st improvements

---

## 7) For Agents Working on SPS3A

If you're working on SPS3A development:

1. **AGENTS.md** is your primary guide (project-specific)
2. **docs/ai-friendly-development.md** is the development rules
3. **docs/ak-graph-principles.md** is the graph authoring guide
4. The Agent1st minimal protocol (11 principles) is embedded in §0
5. You're also implicitly testing Agent1st — report friction via CDD

### Agent1st-Related Updates Needed in SPS3A

- [ ] Add Delegation Design principle to AGENTS.md §0 (missing from v4)
- [ ] Rename "Session protocol" to "Continuity" (align with v4 naming)
- [ ] Add Continuity hook: "if your handoff disappears when the session ends, it doesn't exist"
- [ ] Add `CLAUDE.md` with `@AGENTS.md` import for Claude Code compatibility
- [ ] Consider Why Graph rename (pending decision — see `ROADMAP.md`)
