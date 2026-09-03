# Project Name

Short description of what this project does and who it is for.

## Quick Start

```bash
# install dependencies

# run locally

# run tests
```

## Common Commands

| Task | Command |
| --- | --- |
| Install | `TODO` |
| Run | `TODO` |
| Test | `TODO` |
| Lint | `TODO` |
| Format | `TODO` |

## Project Structure

```text
.
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .gitignore
├── scripts/
│   └── check_pr_scope.py
├── tests/
│   └── test_check_pr_scope.py
├── docs/
│   ├── product-requirements.md
│   ├── architecture.md
│   └── adr/
└── .github/
    ├── pull_request_template.md
    ├── pr-scope.json
    └── workflows/
        └── pr-scope.yml
```

## Configuration

Document required environment variables here. If the project needs local
configuration, add a safe `.env.example`; never commit real credentials.

## Documentation

- `docs/product-requirements.md` is the authoritative statement of user needs, scope, and acceptance criteria.
- `docs/architecture.md` explains the current system shape.
- `docs/adr/` records important decisions and tradeoffs.
- `AGENTS.md` tells coding agents how to work in this repo.
- `CONTRIBUTING.md` describes how changes enter the repo safely.
- `SECURITY.md` captures security expectations.
- `scripts/check_pr_scope.py` enforces the review-size and scope contract.

## Pull Request Protection

After the first push, enable branch protection for `main` and make the
`pr-scope` GitHub Actions check required. Customize the warning and hard limits
in `.github/pr-scope.json` when the project has evidence that different limits
are more appropriate.

## Status

Current status: early project scaffold.
