
# codex-projects-standards

Personal software project standards, documentation scaffolds, and agent instructions for coding agents.

This repo is the source of truth for how I want software projects to work: the rules of the game for new and existing projects. It provides reusable templates for documentation, security, testing expectations, multi-agent coordination, and GitHub workflow setup.

## Templates

### Generic Project Template

Use `project-template/` as the default scaffold for new software projects unless a more specific template applies.

The generic template includes:

```text
README.md
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
SECURITY.md
.gitignore
docs/
  product-requirements.md
  architecture.md
  operating-model.md
  lessons-learned.md
  adr/
    0001-record-project-baseline.md
    0002-adopt-agent-operating-model.md
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

After the first push, complete the setup checklist in
`docs/operating-model.md`: branch protection with the `pr-scope` check, a
protected `production` environment, agent identities, and labels. The workflow
is present in the scaffold, but these GitHub settings are configured at the
repository level.

### Existing Projects

To bring an existing project up to the current standard, compare its
`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `docs/` with
`project-template/`. Add what is missing in one PR, keep project-specific rules,
and do not overwrite the project's own facts. Add new ADRs (such as `0002`)
rather than editing the project's accepted ones.

## A Living Standard

This repo improves over time with lessons from real projects.

1. A project records a rule it learned the hard way in its
   `docs/lessons-learned.md`.
2. If the lesson applies to every project, open a PR here that adds it as a
   short rule in the right file.
3. Cut rules that only fit one kind of project (for example, finance-only
   rules). Keep those in that project's `AGENTS.md`.
4. Existing projects pick up the change the next time they are synced.

## One Source Of Truth For Agents

`AGENTS.md` holds every rule. Most coding agents read it directly. Claude
Code reads `CLAUDE.md` instead, so `CLAUDE.md` contains only a short note and
`@AGENTS.md`, which imports the same file. Never put rules in
`CLAUDE.md`; change `AGENTS.md` instead.

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
- Repo-local coding-agent instructions in `AGENTS.md`, imported by `CLAUDE.md`.
- A clear operating model for the owner and agents in `docs/operating-model.md`.
- A short lessons-learned file of rules learned the hard way.
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
