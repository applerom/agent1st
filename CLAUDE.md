# Agent1st Protocol Repository

This repo develops Agent1st Protocol — a minimal behavior-layer for AI agents in software projects.

## What's here

- `AGENTS.md` — The protocol itself (current version). This IS the product.
- `docs/DESIGN.md` — Design principles. Read before modifying AGENTS.md.
- `docs/EVOLUTION.md` — Version history with rationale for each transition.
- `docs/VISION.md` — Project vision, scopes (minimal/standard/full), roadmap.
- `docs/handoffs/` — Agent-to-agent knowledge transfer briefs.
- `docs/_archive/` — Previous versions of AGENTS.md.

## If you are an agent working on this repo

Read order:
1. `AGENTS.md` (the current protocol — also applies to you)
2. `docs/DESIGN.md` (why it's written this way)
3. `docs/EVOLUTION.md` (what changed and why)
4. Only then propose changes

Key constraint: **AGENTS.md is a delta-layer, not a second system prompt.** Do not add what the model or tool harness already covers. See DESIGN.md section 2 for details.

## Project conventions

- The human provides intent, constraints, evaluation, and acceptance
- Agents choose the route, execute, criticize, and prove the result
- Strong agents should not be micromanaged into passive copilots
- This protocol is co-developed with agents — handoff briefs are first-class artifacts
- Preserve the voice: direct, memorable, slightly provocative, grounded
- Working language: Russian or English as contextually appropriate
