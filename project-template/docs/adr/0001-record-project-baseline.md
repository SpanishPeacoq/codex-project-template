# 0001 Record Project Baseline

Status: Accepted

Date: YYYY-MM-DD

## Context

The project needs a small, durable documentation and collaboration baseline so humans and coding agents can work safely without repeating setup instructions in every task.

## Decision

Use the following baseline files:

- `README.md` for project purpose, setup, and common commands.
- `AGENTS.md` for coding-agent operating rules, as the single source of truth for every agent.
- `CLAUDE.md` that only imports `AGENTS.md`, so Claude follows the same rules.
- `CONTRIBUTING.md` for contribution and multi-agent workflow.
- `SECURITY.md` for security expectations.
- `docs/product-requirements.md` for user needs, scope, non-goals, and acceptance criteria.
- `docs/architecture.md` for the current system map and operations.
- `docs/operating-model.md` for roles, handoffs, and approvals between the owner and agents.
- `docs/lessons-learned.md` for bugs, incidents, and the rules they taught.
- `docs/adr/` for important decisions.
- `.github/` for collaboration templates and automation when hosted on GitHub.

Accepted ADRs are append-only. A later ADR supersedes an earlier one; it does not edit it.

## Consequences

The project starts with a little more structure, but the structure is intentionally small and useful. Contributors should keep these files accurate and avoid adding process documents that do not answer recurring questions or preserve important decisions.
