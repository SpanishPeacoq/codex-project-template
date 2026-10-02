# Lessons Learned

Rules this project learned the hard way. Read this file at the start of a
session and before debugging.

This is not a bug log. The details of each bug or change belong in its issue
and PR; git history is the record. Add an entry only when a mistake taught a
rule that would save time or prevent harm next time. Most bug fixes do not
need an entry.

Good lessons are often about how we work, not only about code. For example:

- "Read every review thread before merging. We merged once with an open
  finding and needed a follow-up PR."
- "Read the code before building. Twice the requested feature already
  existed."
- "Four agent lanes were too many. Two worked better."

## Entry Format

Lead with the rule. Keep each entry to two or three lines. Never include
secrets, account numbers, or personal data.

```text
- [all projects] <Rule, as an instruction a future agent can follow.> <Why,
  in one sentence.> (<issue or PR link>)
```

Use the `[all projects]` tag only for lessons that pass the test below. Leave
it off for lessons that only apply here.

## Lessons For All Projects

Some lessons matter beyond this project. Record them, every time, so future
projects start with them.

The test: would this rule help a project on a completely different topic? If
yes, it applies to all projects. Most lessons about how we work (reviews,
handoffs, approvals, testing, docs, privacy, agent setup) pass this test.
Lessons about this project's domain, data, or tools usually do not.

When a lesson passes the test:

1. Add it here with the `[all projects]` tag. Write it without this project's
   names, data, or domain terms, so it reads the same in any project.
2. Propose it for the shared project standard
   (https://github.com/SpanishPeacoq/codex-project-template): open an issue or
   PR there, or tell the owner if you cannot reach that repository.
3. Delete the entry here once the standard includes it and this project has
   synced it into `AGENTS.md`.

## Promoting Lessons

When a project-only lesson becomes a standing rule, move it into `AGENTS.md`
(or the right doc) and delete it here. This file stays short: only lessons not
yet promoted, and project-specific traps.

## Lessons

None yet.
