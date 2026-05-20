# Contributing

This project treats human and AI-agent contributions the same way: changes should be understandable, scoped, tested, and easy to review.

## Before Starting

- Check the current branch.
- Check `git status`.
- Pull the latest remote state when working on a shared branch.
- Read `README.md`, `AGENTS.md`, `SECURITY.md`, `docs/architecture.md`, and relevant ADRs.

## Change Style

- Keep behavior changes separate from unrelated refactors.
- Prefer small, reviewable commits.
- Update tests when behavior changes.
- Update docs when setup, commands, architecture, security posture, or workflows change.
- Add an ADR for project-shaping decisions.

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
- Changes are committed and pushed when appropriate.
