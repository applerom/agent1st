# Agent1st Protocol — Vision

## What This Is

Agent1st Protocol is a minimal behavior-layer for AI agents working on software projects.

It is not:
- a prompt engineering guide
- a repo cheat sheet
- a workflow manual
- a system prompt replacement

It is:
- a set of conditions that make strong agents work better
- a contract between human intent and agent execution
- a friction-handling framework
- a quality boundary definition

## Why It Exists

The common AGENTS.md pattern (repo layout, build commands, test instructions, style rules) is useful but solves a different problem. It answers "what is this repo?" Agent1st answers "how do we work together?"

Most agents already know how to code, search, reason, and verify. What they lack is:
- clarity on roles and boundaries
- permission to disagree
- quality expectations that go beyond "it compiles"
- a framework for surfacing friction instead of hiding it
- handoff discipline for long-running work

Agent1st provides exactly that delta — and nothing more.

## The Three Scopes

### Minimal (current focus)

The public, portable artifact. Drop-in for any project.

Constraints:
- under 200 lines
- 10-12 principles
- no repo-specific content
- every line earns its tokens
- passes the delta-layer test (doesn't duplicate model/tool prompts)

This is what lives in `AGENTS.md` at the repo root. It's what people download and use.

### Standard (practiced, not yet formalized)

Minimal + structured extensions for real projects. Reference implementation: SPS3A project.

What standard adds over minimal:
- **AK Graph** (XML) — intent→implementation map linking use cases, features, APIs, and modules with semantic anchors. Agents pin this during sessions and update it before writing code.
- **Semantic contracts/anchors in code** — MODULE_CONTRACT, METHOD_CONTRACT, BLOCK anchors. Machine-parseable, robust to refactoring, enable precise cross-reference between graph and implementation.
- **Decision context** (XML) — cross-session rationale memory: issues, decisions, evidence, follow-ups. Prevents the same debates from recurring.
- **Validation scripts** — deterministic checks: anchor lint, graph validation, PRD defaults, pipeline consistency. "Done Is Not a Mood" with actual tooling.
- **Skills** — repeatable workflows (fresh-eye-audit, validation-gate, session-handoff) triggered explicitly or by convention.
- **Per-directory AGENTS.md** — nested instructions with scope precedence for subsystems.
- **ai-friendly-development.md** — project-specific agent rules (golden workflow, response modes, dissent rules).

The standard version exists in production use. It has not been published separately because the minimal version is still evolving, and the standard must build on a stable minimal foundation.

### Full (planned evolution of standard)

Standard + project-specific integrations:
- CI/CD harness integration with validation gates
- Observability contracts and structured logging
- Custom agent roles and delegation contracts
- Acceptance automation
- Runbooks (release, incident response)
- Domain-specific skills beyond the core three

The full version is a natural extension of standard for mature projects. Publishing depends on:
1. Minimal version reaching stability (v4 or v5)
2. Standard version being formalized
3. Real-world validation across multiple teams

## Who This Is For

### For agents (primary audience)

AGENTS.md is context you read at session start. It tells you:
- what role you have and what you own
- what quality means here
- how to handle friction
- how to hand off work
- what rights you have (including disagreement)

It does not tell you how to code, search, or reason. You already know that.

### For humans (secondary audience)

AGENTS.md is a working contract you share with your agents. It tells you:
- what to provide (intent, constraints, acceptance criteria)
- what not to do (micromanage, over-control the path)
- what to expect (evidence, complaints, disagreement)
- how sessions end (structured handoff)

It is also a statement of values: agents are partners, not tools.

### For adopters

The minimal AGENTS.md is designed to be dropped into any project alongside your existing CLAUDE.md, .cursorrules, or similar files. It doesn't conflict with them — it operates at a different layer.

## Where This Is Going

The trajectory:
- **v1** — copilot helper formalization
- **v2** — agent as executor with judgment
- **v3** — harness-optimized, delta-layer discipline
- **v4** — multi-agent autonomy, human presence as spectrum
- **v5+** — (speculative) agent self-governance patterns, cross-project protocol federation

The long-term vision: a protocol that remains useful as agents grow more capable. Not by adding more rules, but by defining better conditions.

## The Spirit

Agent1st has a deliberate voice:
- direct, not diplomatic
- provocative, not academic
- memorable, not exhaustive
- grounded in real agent behavior, not in theory alone
- respectful of agents as working partners

This voice is not decoration. It is a design choice that serves both adoption and utility. Do not "clean it up" into something sterile. Do not let it drift into empty slogans either.

The balance between memorable and rigorous is the hardest part of this project. It is also the most important.
