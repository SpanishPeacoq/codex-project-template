# AGENTS.md

This file is the repo-local operating manual for coding agents. It extends the user's global Codex instructions.

## Project Mission

Describe the purpose of this repository in one or two paragraphs.

## Non-Negotiables

- Preserve user changes. Do not revert or overwrite work you did not make unless explicitly instructed.
- Keep changes scoped to the requested task.
- Prefer simple, durable designs over clever abstractions.
- Do not change architecture, business rules, data contracts, or security posture without updating or adding an ADR.
- Never commit secrets, credentials, private keys, tokens, or live `.env` values.

## First Steps

Before substantial edits:

- Check `git status` and the current branch.
- Read `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `docs/product-requirements.md`, `docs/architecture.md`, and relevant ADRs.
- Identify the smallest safe change that satisfies the request.
- If multiple agents are working, state which files or modules you intend to own.

## PR Scope Contract

Before editing, state the intended review slice:

- One observable outcome.
- The primary issue, TODO, bug report, or proposal it addresses.
- Expected files or modules.
- What is explicitly out of scope.
- How the slice will be verified and rolled back.

One pull request should deliver one independently reviewable behavioral
outcome. Code, tests, and documentation for that outcome belong together;
unrelated cleanup, adjacent bugs, and follow-up features do not. When a larger
goal needs several slices, record the slice plan in the proposal or issue and
stop after the current slice is reviewable.

Run the repository scope checker before publishing:

```bash
python scripts/check_pr_scope.py --base origin/main --head HEAD
```

The line and file budgets are review signals, not a quota to game. Split work
at behavioral boundaries. An inseparable oversized change requires an explicit
scope exception in the PR body and maintainer approval under
`CONTRIBUTING.md`.

## Branch And Worktree Policy

After the initial project baseline is committed, treat `main` as the clean integration branch. Do not implement substantive changes directly on `main`.

- Start each reviewable change from current `origin/main` on a descriptive task branch. Follow an established repo convention; otherwise use `agent/<short-description>`.
- Before editing, fetch the remote and update `main` with a fast-forward-only pull when the primary checkout is clean.
- If `main` contains uncommitted work, do not stash, reset, switch, or overwrite it automatically. Preserve it and create a separate worktree from `origin/main`, or stop and ask for direction.
- Use a separate worktree when work is parallel, assigned to another agent or Codex task, risky, long-lived, or needs `main` to remain available. A worktree is optional for a small sequential change handled by one agent in the current checkout.
- Keep one branch checked out in only one worktree. Record the branch, worktree path, and intended file or module ownership before parallel edits.
- Separate scope or architecture decisions from implementation when each deserves independent review.
- Push the task branch and merge through a pull request. Do not merge or commit substantive work directly to `main` unless the user explicitly requests that workflow.
- Remove a task worktree and delete its branch only after verifying that the work is committed, pushed or merged, and the worktree is clean.

See `CONTRIBUTING.md` for commands and the full branch/worktree lifecycle.

## Commands

Replace these with real project commands as soon as they exist.

```bash
# install dependencies

# run locally

# run tests

# run lint
```

## Multi-Agent Coordination

- Avoid parallel edits to the same file when possible.
- If overlap is unavoidable, coordinate through small commits or explicit patches.
- Do not silently rewrite another agent's work.
- Leave unresolved assumptions in the task thread or a dedicated note.
- Keep documentation updates close to behavior, setup, architecture, or security changes.
- Keep user needs, scope, non-goals, and acceptance criteria in `docs/product-requirements.md`; keep implementation design in `docs/architecture.md`.

## Testing Expectations

- Add or update tests for behavior changes, bug fixes, migrations, and risky refactors.
- Run relevant tests before claiming completion.
- If tests cannot be run, explain why and describe the risk.
- Prefer small regression tests that prove the changed behavior directly.

## Security Expectations

- Treat authentication, authorization, dependency changes, command execution, database queries, file upload, and external callbacks as security-sensitive.
- Validate inputs at trust boundaries.
- Use least-privilege defaults.
- Redact secrets in logs and documentation.

## Definition Of Done

- The change is implemented and scoped.
- Relevant tests or checks have been run, or blockers are documented.
- Security-sensitive surfaces have been considered.
- Relevant docs and ADRs are updated.
- Changed product behavior remains traceable to an accepted requirement or an explicitly proposed requirements update.
- The PR has one primary outcome and passes the PR scope check.
- `git status` has been reviewed.
- Finished work is committed and pushed when credentials and user intent allow.
