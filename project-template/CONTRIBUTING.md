# Contributing

This project treats human and AI-agent contributions the same way: changes should be understandable, scoped, tested, and easy to review.

## Before Starting

- Check the current branch.
- Check `git status`.
- Pull the latest remote state when working on a shared branch.
- Read `README.md`, `AGENTS.md`, `SECURITY.md`, `docs/architecture.md`, and relevant ADRs.

## Branch And Worktree Workflow

After the initial baseline commit, substantive work should not begin directly on `main`.

1. Inspect the current checkout:

   ```bash
   git status --short --branch
   git worktree list
   ```

2. When the primary checkout is clean, update the baseline:

   ```bash
   git fetch origin
   git switch main
   git pull --ff-only
   ```

   If the checkout is dirty, preserve it. Do not automatically stash, reset, or move user changes.

3. Create a descriptive task branch. Follow an existing naming convention; otherwise use `agent/<short-description>`.

   For a small sequential change in the current checkout:

   ```bash
   git switch -c agent/<short-description>
   ```

   For parallel, risky, long-lived, or separate-agent work, create an isolated sibling worktree directly from current `origin/main`:

   ```bash
   git fetch origin
   git worktree add ../<project>-<short-description> \
     -b agent/<short-description> origin/main
   ```

4. Make scoped changes, add focused tests, and commit on the task branch. Multiple agents should declare file or module ownership and avoid sharing a branch or worktree.
5. Push the branch and open a pull request into `main`. Keep scope/design work separate from implementation when they are independently reviewable.
6. After merge, verify the worktree is clean before cleanup:

   ```bash
   git worktree remove ../<project>-<short-description>
   git branch -d agent/<short-description>
   git fetch --prune
   ```

Never force-remove a worktree or force-delete a branch merely to make cleanup succeed. Inspect unmerged commits and uncommitted files first.

## Change Style

- Keep behavior changes separate from unrelated refactors.
- Prefer small, reviewable commits.
- Update tests when behavior changes.
- Update docs when setup, commands, architecture, security posture, or workflows change.
- Add an ADR for project-shaping decisions.

## Pull Request Scope Harness

Every pull request declares one primary behavioral outcome. Code, tests, and
documentation needed to prove that outcome are one slice. Adjacent fixes,
cleanup, and features become follow-up slices.

The repository runs `scripts/check_pr_scope.py` in GitHub Actions. Its default
budgets are:

| Measure | Review threshold | Hard threshold |
| --- | ---: | ---: |
| Production files | 5 | 8 |
| Production line churn | 400 | 800 |
| Total changed files | 15 | 25 |
| Total line churn | 1,000 | 2,000 |

Tests, documentation, and `.github/` files count toward total size but not
production size. Thresholds are signals, not instructions to divide work at an
arbitrary line. A small PR can still be too broad, and a cohesive change can
occasionally exceed a threshold.

When a review threshold is exceeded, the PR body must explain why the change
cannot be divided safely. When a hard threshold is exceeded, the PR also needs
the `approved-large-pr` label from a maintainer. Generated files, mechanical
migrations, and genuinely atomic cross-cutting changes use the same documented
exception path.

Before opening a PR, run:

```bash
python scripts/check_pr_scope.py --base origin/main --head HEAD
```

Repositories created from this template should make the `pr-scope` GitHub
Actions check required in branch protection. The workflow is the shared
enforcement layer across humans, computers, and coding agents; local hooks are
optional convenience only.

## Multi-Agent Work

- State intended file or module ownership before editing.
- Avoid overlapping edits to the same files.
- If another agent's changes are present, work with them instead of reverting them.
- Use clear commit messages so parallel work is easier to reconcile.

## Testing

Before submitting or committing finished work:

- Run the relevant unit, integration, lint, typecheck, or build commands.
- Add regression coverage for bug fixes.
- Document any skipped checks and why they were skipped.

## Security Review

For security-sensitive changes, check:

- Secrets are not committed.
- Inputs are validated at trust boundaries.
- Authentication and authorization behavior is explicit.
- Dependencies are necessary and reasonably maintained.
- Logs do not expose private data.

## Definition Of Done

- Code is implemented.
- Tests/checks pass or documented blockers remain.
- Relevant docs are updated.
- ADRs capture important decisions.
- The PR template is complete and the `pr-scope` check passes.
- Changes are committed and pushed when appropriate.
