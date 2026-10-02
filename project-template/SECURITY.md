# Security

## Supported Scope

This project is early-stage unless stated otherwise. Security expectations still apply to local development, tests, documentation, and deployment scripts.

## Secret Handling

- Do not commit `.env` files containing real values.
- Use `.env.example` to document required variables.
- Never commit tokens, private keys, passwords, session cookies, or production credentials.
- Redact secrets from logs, screenshots, issues, and documentation.
- Read secrets and personal identifiers from settings outside the repo. If a required setting is missing, fail safely; never fall back to a default value.

## Private Data

- Keep personal data, account numbers, and customer details out of issues, PRs, commits, and docs. Point to evidence by its location instead.
- Plan for this before real users or accounts exist. Scrubbing history later is slow and incomplete.

## Security-Sensitive Areas

Treat these changes as requiring extra review:

- Authentication and authorization.
- Database queries and migrations.
- File upload, parsing, or path handling.
- Shell command execution.
- External webhooks or callbacks.
- Dependency additions or upgrades.
- CI/CD, deployment, and infrastructure configuration.

## Dependency Standard

Before adding a dependency, consider:

- Is it necessary?
- Is it actively maintained?
- Is the license acceptable?
- Does it meaningfully increase attack surface?

## Reporting Issues

For private projects, report security issues directly to the repository owner. For public projects, replace this section with a private contact method or GitHub Security Advisory instructions.

## Pre-Release Checklist

- No secrets are committed.
- Environment variables are documented in `.env.example`.
- Relevant tests pass.
- Authentication and authorization flows have been reviewed.
- Logs avoid sensitive data.
- Dependencies are reviewed for obvious risk.
