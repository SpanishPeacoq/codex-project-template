# Architecture

This document describes the current system shape. Keep it factual and short enough that future contributors will actually read it.

## Purpose

Describe the problem this project solves.

## Current System

Describe the major pieces of the system and how they fit together.

## Components

| Component | Responsibility | Notes |
| --- | --- | --- |
| TODO | TODO | TODO |

## Data Flow

Describe the main flow of data or control through the system.

```text
input -> processing -> output
```

## Boundaries

Document important boundaries:

- External services:
- Databases:
- File system:
- Network calls:
- User input:

## Runtime And Deployment

Describe how the project runs locally and how it is deployed.

## Operations

Fill this in before the first production release. The Operator uses it to deploy and verify.

- Environments: local, staging, production. Note any that do not exist yet.
- Deploy: how a release goes out, from which commit or tag.
- Rollback: how to undo a release, and how long it takes.
- Health signals: what "working" means (for example, a health endpoint, error rate, a job that must run daily).
- Alerts: what triggers an alert and who receives it.
- Logs and evidence: where logs live. Point to them by location; do not copy private data into issues.

## Important Decisions

Record durable decisions in `docs/adr/`. Link the most relevant ADRs here.

- `docs/adr/0001-record-project-baseline.md`

## Known Risks

List sharp edges, fragile assumptions, or areas needing extra care.

## Update Rule

Update this file when the system shape, major boundaries, or deployment model changes.
