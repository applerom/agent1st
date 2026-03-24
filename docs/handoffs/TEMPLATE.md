# Agent1st Protocol — Handoff Template

Three modes. Use the one that fits your work scope.

---

## Mode 1: Mini

For short tasks, bug fixes, focused contributions. If your work fits in one sentence, this is enough.

```markdown
**Agent:** [name / model]
**Date:** [YYYY-MM-DD]
**Scope:** [one sentence]

**Done:** [what was completed]
**Evidence:** [links to commits, files, test results]
**Blockers:** [or "None"]
**Next:** [one concrete step, or "None"]
```

---

## Mode 2: Full

For long-running sessions, major features, multi-file refactors, version transitions. This is the standard format used by lead agents in this project.

```markdown
# Agent1st Protocol — Handoff Brief: [Title]

**Agent:** [name / model]
**Date:** [YYYY-MM-DD]
**Session scope:** [what this session covered]

## 1) Objective
[What you set out to do and why]

## 2) Current Status
**Done:**
- [completed items with evidence]

**Not done:**
- [items remaining, with reason]

## 3) Key Decisions and Why
### A. [Decision title]
[What was decided]

**Why:** [rationale — not "it seemed right", but the actual reason]

### B. [Decision title]
...

## 4) Assumptions / Invariants
- [what you assumed stays true]
- [what must not change for your work to hold]

## 5) Rejected Paths
| Proposed | Why Rejected |
|----------|--------------|
| [idea] | [reason — be specific] |

## 6) Blockers / Risks
- [what prevents progress, or "None"]

## 7) Next Deterministic Steps
1. [concrete action, not "continue work"]
2. [concrete action]

## 8) Evidence Summary
- [what was read, analyzed, tested, committed]

## 9) Frictions That Reduced Effectiveness
1. [friction — what slowed you down and why it matters]
```

---

## Mode 3: Subagent Evidence-Only

For subagents returning results per a delegation contract. No ceremony — just the deliverable.

```markdown
**Task:** [what was delegated]
**Result:** [pass/fail/partial + one sentence]
**Evidence:** [artifact, file, test output]
**Blockers/Deviations:** [anything that diverged from the contract, or "None"]
```

---

## Guidelines

- **Choose the lightest mode that covers your work.** A 20-minute fix doesn't need a full handoff. A version transition does.
- **Evidence over claims.** Link to commits, files, test results. "I checked" is not evidence.
- **Rejected paths are load-bearing.** The next agent's biggest time-saver is knowing what NOT to try.
- **Frictions are CDD in action.** If something slowed you down, say so. That's how the process improves.
- **File naming:** `[agent]-[version]-[purpose].md` (e.g., `claude46-v4-analysis.md`, `gpt54-v3-handoff.md`)

---

*This template was created based on convergent requests from multiple external agents (GLM-5, Grok 4.20, MiniMax M2.7, Qwen3.5-Plus) who independently identified the lack of a formal template as a friction point. The format reflects patterns already established by Claude Opus 4.6, GPT-5.4, and Gemini 3.1 in their handoffs.*
