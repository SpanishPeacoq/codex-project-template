# Product Requirements

This document is the authoritative statement of what the product should achieve for its users. Keep implementation design in `docs/architecture.md`, durable technical or product-shaping decisions in `docs/adr/`, and execution tasks in the issue tracker or project backlog.

## Document Control

- Status: Draft
- Product owner: TODO
- Last reviewed: YYYY-MM-DD
- Applies to: TODO release, milestone, or product stage

## Product Summary

Describe the product, its intended users, and the outcome it should create in one or two paragraphs.

## Problem And Evidence

Describe the user problem and the evidence that it is worth solving. Distinguish observed facts from assumptions that still need validation.

## Users

Identify the primary users and any materially different roles. Capture their goals, constraints, and access boundaries without inventing unsupported personas.

## Desired Outcomes

- TODO: State a measurable or observable user outcome.
- TODO: State the operational or business outcome, if applicable.

## Scope

### In Scope

- TODO

### Non-Goals

- TODO

## User Journeys

Describe the small number of end-to-end workflows that define a useful first release.

## Functional Requirements

Use stable identifiers so requirements can be referenced from issues, tests, pull requests, and release notes.

| ID | Requirement | Acceptance criteria | Priority |
| --- | --- | --- | --- |
| `PRD-001` | TODO: Describe observable product behavior. | TODO: State how a reviewer can determine that it works. | Must |

## Non-Functional Requirements

Document only requirements that materially constrain the product or implementation.

- Privacy and data ownership: TODO
- Security and access control: TODO
- Reliability and recovery: TODO
- Performance: TODO
- Accessibility and supported devices: TODO
- Portability or interoperability: TODO

## Data And Integrations

List required data sources, outputs, external systems, ownership rules, retention expectations, and consent boundaries.

## Constraints And Assumptions

- Constraint: TODO
- Assumption requiring validation: TODO

## Decisions And Open Questions

Record confirmed product decisions briefly and link project-shaping decisions to an ADR. Keep unresolved questions explicit rather than silently turning assumptions into requirements.

## Traceability

Link each implementation slice to the requirement it satisfies:

| Requirement | Issue or proposal | Pull request | Verification |
| --- | --- | --- | --- |
| `PRD-001` | TODO | TODO | TODO |

## Change Control

Change accepted requirements through a reviewed pull request. Explain the user-facing reason, update affected acceptance criteria and non-goals, link any required ADR, and record delivered behavior in `CHANGELOG.md` when the project uses one.
