# Operating Model

This document describes how the owner and agents work together on this
project, as a small software company where agents fill the roles. `AGENTS.md`
holds the rules every agent must follow; this file explains the roles and the
flow behind them.

Start small. Add a role only when one agent is clearly overloaded or doing two
jobs that conflict, such as reviewing its own work. Handoffs cost more than
headcount: each one takes time and can lose context.

## Roles

| Role | Owns | Never does |
| --- | --- | --- |
| Owner (human) | Priorities, risky approvals, disputed decisions | Relays messages between agents |
| Product | Turns ideas into issues: problem, "done when", priority | Writes code |
| Builder | Code, tests, PRs, review fixes, release notes | Deploys without approval, touches production data |
| Reviewer | Reviews every PR; marks findings blocking or optional | Merges its own suggestions |
| QA / Verifier | Tests releases in staging and checks them in production | Fixes code (it files a bug instead) |
| Operator | Deploys approved releases, watches health, investigates incidents, files bugs | Changes production code |

Default setup: the owner also acts as Product, and the Operator also acts as
QA. That leaves two agents you talk to (Builder and Operator) plus an
automatic Reviewer that runs on every PR commit. Use a Reviewer from a
different vendor or model than the Builder when possible, so they do not
share blind spots.

Record the actual role assignments for this project here:

| Role | Assigned to | GitHub identity |
| --- | --- | --- |
| Owner | TODO | TODO |
| Builder | TODO | TODO |
| Reviewer | TODO | TODO |
| Operator | TODO | TODO |

## Work Flow

1. **Issue.** The owner or Product writes the issue with a "done when" line.
   Label it `next:builder`.
2. **Build.** The Builder reads the existing code first, then opens one PR per
   purpose, with tests, linked to the issue.
3. **Review.** The Reviewer runs on every commit. The Builder fixes or answers
   each finding.
4. **Merge.** Allowed only under the merge rule in `AGENTS.md`. Merging does
   not deploy.
5. **Release.** The Builder drafts a release from an exact commit or tag. It
   states what changed, the risk, what the Operator should check, and how to
   roll back.
6. **Approve.** The owner approves the release (see Approval Tiers).
7. **Deploy and verify.** The Operator deploys, runs the checks, and reports
   the result on the issue.
8. **Close.** The issue closes only after the Operator confirms it works in
   production.

If the project does not deploy (for example, a library or a local tool), skip
steps 5 to 7. The issue closes once its "done when" check passes on `main`.

### "Done when"

Every issue has one or two lines that say how everyone will know the work is
finished. It is a check anyone can run, not a description of the work.

- Weak: "Fix the export."
- Clear: "Done when the nightly export includes all accounts created that day,
  and the Operator confirms it in production."

It tells the Builder when to stop, tells the Reviewer and Operator what to
check, and stops issues from closing at "merged" when the goal was "works in
production."

## Bug Flow

1. The Operator files a bug: what happened, when, the impact, and where the
   evidence is. No private data in the issue; point to the evidence by its
   location.
2. The Builder confirms the cause from the evidence. It does not accept the
   reported diagnosis without checking.
3. The Builder fixes it with a test that fails on the old code, plus a
   lookalike test that proves the fix does not fire when it should not.
4. Release and verify as above. The Operator closes the bug.
5. If the bug taught a rule worth keeping, add it to `docs/lessons-learned.md`.

## Handoffs

- GitHub is the only channel. Issues carry handoffs; PR review threads carry
  review findings and the Builder's answers. No side chats and no copy-paste
  between agents.
- A `next:<role>` label names whoever acts next. Create one label for each
  active role: `next:owner`, `next:builder`, `next:reviewer`, and
  `next:operator` by default, plus `next:product` or `next:qa` if those roles
  are separate. An open issue has exactly one `next:` label.
- Labels work with any agent identity. GitHub Apps usually cannot be issue
  assignees, so do not route work through assignees. The owner may still use
  assignees for personal tracking.
- Whoever hands off swaps the label and says in a comment exactly what they
  need.
- Whoever receives the handoff checks the evidence before acting.
- Questions to the owner are short: one question, answerable with yes/no or a
  number, with what each answer leads to.

## Approval Tiers

The owner approves anything risky directly. Agents never approve their own
risky actions.

| Tier | Examples | Approval |
| --- | --- | --- |
| Risky | Production deploys, data deletion or migration, spending money, changes to live external systems, disputed decisions | Owner, directly |
| Routine | Merging a PR that meets the merge rule | Merge rule; owner approval if branch protection requires it |
| Free | Branches, draft PRs, local tests, issue comments | None |

Default: the owner approves every production deploy. Approve in batches (one
release can carry several PRs) to avoid becoming the bottleneck.

A project may later allow low-risk deploys to go out automatically, but only
after it has automated checks, a tested rollback, and health alerts. Record
that change in an ADR.

Until agents have their own GitHub identities, an issue comment cannot prove
who approved something. Give risky approvals to the agent directly, then
record them on the issue.

## Incidents

An incident is anything that breaks production for users or risks data,
money, or security.

1. The Operator opens an issue labelled `incident` with the time, impact, and
   evidence location, and tells the owner directly.
2. First restore service: roll back or disable the feature. Fix forward only
   if rollback is not possible.
3. Follow the Bug Flow for the real fix.
4. Write a short, blameless summary on the incident issue: what happened, the
   root cause, and the fix. Add the rule it taught to
   `docs/lessons-learned.md`.

## Agent Identities

Give each agent its own GitHub identity so history shows who did what, and so
a review or approval means something.

- **Prefer GitHub Apps.** An app is installed on chosen repositories, gets
  narrow permissions, uses short-lived tokens, and appears as `name[bot]`.
  Vendor apps (for example Claude's and Codex's) separate vendors but not
  roles; create your own app per role if one vendor runs two roles.
- **Machine user accounts** are the fallback when a tool needs a full user
  login. Give them the lowest role that works, never admin.
- **The owner is the only admin.** No agent gets admin rights or a bypass on
  branch rules.

## Setup Checklist

These are GitHub settings, not files. Do them once per repository.

- [ ] Protect `main`: require PRs, require the `pr-scope` check and other CI
      checks, and block force-pushes.
- [ ] Require the owner's approval on PRs if the owner wants to sign off on
      every merge.
- [ ] If the project deploys: create a `production` environment with the
      owner as required reviewer, and set `environment: production` on every
      deploy job. The approval only applies to jobs that name the
      environment.

      ```yaml
      jobs:
        deploy:
          environment: production
      ```
- [ ] Install or create the agent GitHub Apps and record them in Roles.
- [ ] Create labels: `incident`, plus one `next:<role>` label for each active
      role (see Handoffs).

## Watch Out For

- **Too many agents too soon.** Add a role only for a real bottleneck.
- **The owner as bottleneck.** Batch approvals and keep questions to yes/no.
- **Agents agreeing by default.** The Reviewer and Verifier look for problems;
  they do not confirm the Builder.
- **No memory between sessions.** If it is not written in the repo or an
  issue, the next session will not know it.

## Measuring The Process

Check these from time to time to see whether the model works:

- Time from issue opened to verified in production.
- How often a release causes a bug or rollback.
- Time to restore service after an incident.
