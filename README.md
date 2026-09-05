
# codex-projects-standards

Personal software project standards, documentation scaffolds, and agent instructions for openAI codex.

This repo is the source of truth for how I want new software projects to begin. It provides reusable templates for documentation, security, testing expectations, multi-agent coordination, and GitHub workflow setup.

## Templates

### Generic Project Template

Use `project-template/` as the default scaffold for new software projects unless a more specific template applies.

The generic template includes:

```text
README.md
AGENTS.md
CONTRIBUTING.md
SECURITY.md
.gitignore
docs/
  product-requirements.md
  architecture.md
  adr/
    0001-record-project-baseline.md
.github/
  pull_request_template.md
  pr-scope.json
  workflows/
    pr-scope.yml
scripts/
  check_pr_scope.py
tests/
  test_check_pr_scope.py
```

## How To Use

Copy the contents of `project-template/` into the root of a new project, then customize the TODOs, commands, architecture notes, and ADR date.

```bash
cp -R project-template/. /path/to/new-project/
```

After the first push, enable branch protection for `main` and require the
`pr-scope` check. The workflow is present in the scaffold, but GitHub branch
protection is configured at the repository level.

## How Codex Loads Instructions

Codex reads `~/.codex/AGENTS.md` for personal defaults on each computer, then
loads the project's `AGENTS.md`. A global `AGENTS.override.md`, when present,
takes precedence over the global `AGENTS.md`. Project instructions can override
global defaults. Instructions load when a Codex run or session starts.

The scaffold's `project-template/AGENTS.md` includes the writing rule for
questions outside coding tasks: simple, brief, clear, human English that
preserves nuance and depth. New projects receive it when you copy the scaffold.

This GitHub repository does not automatically sync instructions to other
computers or existing projects. For personal defaults across projects, add the
same writing section to `~/.codex/AGENTS.md` on each computer while preserving
its existing rules. For an existing project, add the section to that project's
`AGENTS.md`. Start a new Codex session to load updated file instructions.

See [OpenAI's instruction-loading guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Philosophy

The goal is useful structure, not clutter.

Every new project should have:

- A clear front door in `README.md`.
- Repo-local coding-agent instructions in `AGENTS.md`.
- A safe collaboration protocol in `CONTRIBUTING.md`.
- Security expectations in `SECURITY.md`.
- An authoritative user and product contract in `docs/product-requirements.md`.
- A current system map in `docs/architecture.md`.
- Durable decisions captured as ADRs in `docs/adr/`.
- GitHub workflow defaults when the project is hosted on GitHub.

Do not add empty bureaucracy. Every file should answer recurring questions, preserve important decisions, or make future work safer.

## Agent Expectations

Coding agents working from this standard should:

- Check git status before editing.
- Keep `main` clean, use a task branch for substantive changes, and use an isolated worktree for parallel, risky, long-lived, or separate-agent work.
- Preserve user changes.
- Keep work scoped.
- Add or update tests for behavior changes.
- Check security-sensitive surfaces.
- Update docs and ADRs when decisions or architecture change.
- Commit and push finished work when credentials and user intent allow.

## Notes

This repo is meant to evolve. Add more templates only when a project type has genuinely different needs.
