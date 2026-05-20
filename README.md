
# codex-projects-standards

Personal software project standards, documentation scaffolds, and agent instructions.

This repo is the source of truth for how I want new software projects to begin. It provides reusable templates for documentation, security, testing expectations, multi-agent coordination, and GitHub workflow setup.

## Templates

### Generic Project Template

Use `templates/generic/` as the default scaffold for new software projects unless a more specific template applies.

The generic template includes:

```text
README.md
AGENTS.md
CONTRIBUTING.md
SECURITY.md
.env.example
.gitignore
docs/
  architecture.md
  adr/
    0001-record-project-baseline.md
.github/
  pull_request_template.md
  workflows/
    ci.yml
```

## How To Use

Copy the contents of `templates/generic/` into the root of a new project, then customize the TODOs, commands, architecture notes, and ADR date.

```bash
cp -R templates/generic/. /path/to/new-project/
```

## Philosophy

The goal is useful structure, not clutter.

Every new project should have:

- A clear front door in `README.md`.
- Repo-local coding-agent instructions in `AGENTS.md`.
- A safe collaboration protocol in `CONTRIBUTING.md`.
- Security expectations in `SECURITY.md`.
- A current system map in `docs/architecture.md`.
- Durable decisions captured as ADRs in `docs/adr/`.
- GitHub workflow defaults when the project is hosted on GitHub.

Do not add empty bureaucracy. Every file should answer recurring questions, preserve important decisions, or make future work safer.

## Agent Expectations

Coding agents working from this standard should:

- Check git status before editing.
- Preserve user changes.
- Keep work scoped.
- Add or update tests for behavior changes.
- Check security-sensitive surfaces.
- Update docs and ADRs when decisions or architecture change.
- Commit and push finished work when credentials and user intent allow.

## Notes

This repo is meant to evolve. Add more templates only when a project type has genuinely different needs.

