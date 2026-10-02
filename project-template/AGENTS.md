# AGENTS.md

This file is the repo-local operating manual for coding agents. It is the
single source of truth for every agent. Most coding agents read `AGENTS.md`
directly; Claude Code reads `CLAUDE.md`, which imports this file. It extends
the user's global agent instructions.

## Writing Style Outside Coding Tasks

When answering questions outside of coding tasks, use simple, direct English. Prefer short sentences, common words, concrete explanations, active voice, and consistent terminology. Avoid jargon, unnecessary technical language, long introductions, and overly formal phrasing.

Use the principles of Simplified Technical English where useful, but do not follow ASD-STE100 so rigidly that the writing becomes robotic or unnatural.

Above all, optimize for four qualities inspired by William Zinsser:

- Simplicity
- Brevity
- Clarity
- Humanity

Preserve nuance and intellectual depth. Simple writing should make complex ideas easier to understand, not make the ideas simplistic.

## Project Mission

Describe the purpose of this repository in one or two paragraphs.

## Non-Negotiables

- Preserve user changes. Do not revert or overwrite work you did not make unless explicitly instructed.
- Keep changes scoped to the requested task.
- Prefer simple, durable designs over clever abstractions.
- Do not change architecture, business rules, data contracts, or security posture without updating or adding an ADR.
- Never commit secrets, credentials, private keys, tokens, or live `.env` values.
- Never approve your own risky action. Production deploys, data deletion or migration, spending, live external changes, and disputed decisions need the owner's direct approval. See `docs/operating-model.md`.

## First Steps

Before substantial edits:

- Check `git status` and the current branch.
- Read `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `docs/operating-model.md`, `docs/product-requirements.md`, `docs/architecture.md`, `docs/lessons-learned.md`, and relevant ADRs.
- Check before you build. Read the existing code first: the feature may already exist and only need docs or a small change.
- Identify the smallest safe change that satisfies the request.
- If multiple agents are working, state which files or modules you intend to own.

## PR Scope Contract

Before editing, state the intended review slice:

- One observable outcome.
- The primary issue, TODO, bug report, or proposal it addresses.
- The affected `PRD-*` IDs, or `N/A:` followed by a substantive explanation for non-product changes.
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
- Use a separate worktree when work is parallel, assigned to another agent, risky, long-lived, or needs `main` to remain available. A worktree is optional for a small sequential change handled by one agent in the current checkout.
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

## Roles And Handoffs

Follow the roles, flow, and approval tiers in `docs/operating-model.md`.

- Know your role. One owner per next action.
- GitHub is the only channel between agents: issues for handoffs, PR review threads for review discussion. No side chats and no copy-paste relays.
- A `next:<role>` label names whoever acts next. When you hand off, swap the label and say in a comment exactly what you need. Do not use assignees for handoffs.
- When you receive a handoff, check the evidence before acting. Do not accept the sender's diagnosis without checking.
- Every issue has a "done when" line: a check anyone can run. Work stops there, not earlier.
- Ask the owner short questions: one question, answerable with yes/no or a number, with what each answer leads to.
- Look for problems in other agents' work. Do not agree by default.

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
- A bug fix includes a test that fails on the old code. Also add a lookalike test that proves the fix does not fire when it should not.
- Run CI once per commit. Test workflows trigger on pull requests and on pushes to `main` only, not on pushes to every branch; otherwise a branch with an open PR runs the full suite twice on the same commit. See `CONTRIBUTING.md`.
- "Flaky" is not a root cause. A failure that happens again on a re-run is a real bug. Never skip or disable a test to get green.

## Review And Merge Rule

Merge only when all of these are true:

- CI is green on the latest commit.
- The reviewer's latest review has finished.
- Every review thread has been read, not just the summary, and every finding is fixed or answered.

When review findings contradict each other, ask the owner. Do not pick one quietly.

Merging is not deploying. A release goes out from an exact commit or tag, after the owner's approval, and is then verified in production.

## Security Expectations

- Treat authentication, authorization, dependency changes, command execution, database queries, file upload, and external callbacks as security-sensitive.
- Validate inputs at trust boundaries.
- Use least-privilege defaults.
- Redact secrets in logs and documentation.
- Keep private data out of issues, PRs, and commits: no personal data, account numbers, or customer details. Point to evidence by its location instead.
- Read secrets and personal identifiers from settings outside the repo. If a required setting is missing, fail safely; never fall back to a default value.

## Data Rules

- Keep one source of truth for each kind of data. Generate exports when needed; never treat a copy as the record.
- Handle time zones explicitly. Store the source time zone, set it explicitly in client libraries, and never guess it from a format.
- When a risky action (sending messages, writing core data, calling paid APIs) needs a single owner module, enforce it with a test that scans the whole repo, scripts included. Allow exceptions by name, with the reason.

## Docs And Memory

Agents start fresh each session. If it is not written in the repo or an issue, the next session will not know it.

- Update docs in the same PR as the facts they describe. Do not keep progress logs in docs; git history and PRs are the record.
- Write an ADR when a choice changes architecture, risk, or who can do what. Never edit an accepted ADR; supersede it with a new one.
- Read `docs/lessons-learned.md` before debugging. Add an entry only when a mistake taught a rule worth keeping; bug details stay in the issue and PR.
- Always record a lesson that would help a project on any topic. Tag it `[all projects]` in `docs/lessons-learned.md` and propose it for the shared project standard. See that file for the steps.

## Definition Of Done

- The issue's "done when" check passes. For anything that deploys, that means verified in production, not merged or deployed.
- The change is implemented and scoped.
- Relevant tests or checks have been run, or blockers are documented.
- Security-sensitive surfaces have been considered.
- Relevant docs and ADRs are updated.
- Changed product behavior remains traceable to an accepted requirement or an explicitly proposed requirements update.
- The PR has one primary outcome and passes the PR scope check.
- `git status` has been reviewed.
- Finished work is committed and pushed when credentials and user intent allow.
