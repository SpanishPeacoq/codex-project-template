# 0002 Adopt Agent Operating Model

Status: Accepted

Date: YYYY-MM-DD

Extends: `0001-record-project-baseline.md`

## Context

The owner and several coding agents work on this project together. Without
written roles, handoffs, and approval rules, work gets relayed by hand, agents
approve their own risky actions, and lessons are lost between sessions.

## Decision

Add these files to the project baseline:

- `CLAUDE.md`, which only imports `AGENTS.md`, so every agent follows one rule
  file.
- `docs/operating-model.md` for roles, the work flow, handoffs, approval tiers,
  incidents, and agent identities.
- `docs/lessons-learned.md` for rules learned the hard way.
- An Operations section in `docs/architecture.md` for deploy, rollback, and
  health checks.

Accepted ADRs are append-only. A later ADR supersedes or extends an earlier
one; it does not edit it.

## Consequences

Agents hand off work through GitHub issues and labels, and the owner approves
risky actions directly. Each issue has a runnable "done when" check. The
project carries three more short documents that must stay accurate.
