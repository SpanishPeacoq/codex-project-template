#!/usr/bin/env python3
"""Check whether a pull request stays within the repository scope contract."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


OUTCOME_CHECK = "- [x] This PR has one primary behavioral outcome."
REQUIRED_SECTIONS = (
    "Outcome",
    "Primary intake",
    "In scope",
    "Out of scope",
    "Verification",
    "Rollback",
    "Follow-up slices",
    "Scope declaration",
    "Scope exception",
)
NO_EXCEPTION_VALUES = {
    "none",
    "none.",
    "n/a",
    "not applicable",
    "no exception requested",
}


@dataclass(frozen=True)
class Limits:
    production_files: int
    production_churn: int
    total_files: int
    total_churn: int


@dataclass(frozen=True)
class ScopeConfig:
    soft: Limits
    hard: Limits
    non_production_prefixes: tuple[str, ...]


@dataclass(frozen=True)
class Metrics:
    production_files: int = 0
    production_churn: int = 0
    total_files: int = 0
    total_churn: int = 0


@dataclass(frozen=True)
class Result:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


def load_config(path: Path) -> ScopeConfig:
    data = json.loads(path.read_text(encoding="utf-8"))

    def limits(name: str) -> Limits:
        row = data[name]
        return Limits(
            production_files=int(row["production_files"]),
            production_churn=int(row["production_churn"]),
            total_files=int(row["total_files"]),
            total_churn=int(row["total_churn"]),
        )

    return ScopeConfig(
        soft=limits("soft_limits"),
        hard=limits("hard_limits"),
        non_production_prefixes=tuple(data["non_production_prefixes"]),
    )


def is_production(path: str, config: ScopeConfig) -> bool:
    normalized = path.replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    normalized = normalized.lstrip("/")
    if normalized.startswith(config.non_production_prefixes):
        return False
    name = normalized.rsplit("/", 1)[-1].lower()
    if name.startswith("test_") or name.endswith("_test.py"):
        return False
    return not name.endswith((".md", ".rst", ".adoc"))


def parse_numstat(text: str, config: ScopeConfig) -> Metrics:
    production_files = 0
    production_churn = 0
    total_files = 0
    total_churn = 0
    for raw in text.splitlines():
        if not raw.strip():
            continue
        parts = raw.split("\t", 2)
        if len(parts) != 3:
            raise ValueError(f"unexpected git numstat row: {raw!r}")
        added, deleted, path = parts
        churn = 0 if "-" in (added, deleted) else int(added) + int(deleted)
        total_files += 1
        total_churn += churn
        if is_production(path, config):
            production_files += 1
            production_churn += churn
    return Metrics(
        production_files=production_files,
        production_churn=production_churn,
        total_files=total_files,
        total_churn=total_churn,
    )


def collect_metrics(base: str, head: str, config: ScopeConfig) -> Metrics:
    completed = subprocess.run(
        [
            "git",
            "diff",
            "--numstat",
            "--no-renames",
            f"{base}...{head}",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return parse_numstat(completed.stdout, config)


def section(body: str, title: str) -> str | None:
    pattern = re.compile(
        rf"^##\s+{re.escape(title)}\s*$\n(.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(body)
    return match.group(1).strip() if match else None


def has_content(value: str | None) -> bool:
    if value is None:
        return False
    without_comments = re.sub(r"<!--.*?-->", "", value, flags=re.DOTALL)
    return without_comments.strip() not in {"", "-"}


def exceeded(metrics: Metrics, limits: Limits) -> list[str]:
    failures = []
    for field, label in (
        ("production_files", "production files"),
        ("production_churn", "production line churn"),
        ("total_files", "total changed files"),
        ("total_churn", "total line churn"),
    ):
        actual = getattr(metrics, field)
        limit = getattr(limits, field)
        if actual > limit:
            failures.append(f"{label}: {actual} > {limit}")
    return failures


def evaluate(
    metrics: Metrics,
    config: ScopeConfig,
    *,
    body: str | None = None,
    labels: set[str] | None = None,
) -> Result:
    labels = labels or set()
    errors: list[str] = []
    warnings: list[str] = []
    soft = exceeded(metrics, config.soft)
    hard = exceeded(metrics, config.hard)

    if body is not None:
        for title in REQUIRED_SECTIONS:
            value = section(body, title)
            if not has_content(value):
                errors.append(f"PR body section is missing or empty: {title}")
        if OUTCOME_CHECK not in body:
            errors.append("confirm the one-primary-outcome checkbox")

    exception = section(body or "", "Scope exception")
    has_exception = bool(
        exception
        and exception.strip().lower() not in NO_EXCEPTION_VALUES
        and len(exception.strip()) >= 20
    )

    if soft:
        warnings.extend(f"review budget exceeded: {item}" for item in soft)
        if body is not None and not has_exception:
            errors.append(
                "review budget exceeded; explain why the PR cannot be split "
                "in Scope exception"
            )
    if hard and "approved-large-pr" not in labels:
        errors.append(
            "hard scope budget exceeded; maintainer must apply the "
            "approved-large-pr label"
        )
    return Result(tuple(errors), tuple(warnings))


def event_context(path: Path | None) -> tuple[str | None, set[str]]:
    if path is None:
        return None, set()
    data = json.loads(path.read_text(encoding="utf-8"))
    pull_request = data.get("pull_request") or {}
    labels = {
        str(row.get("name"))
        for row in pull_request.get("labels") or []
        if row.get("name")
    }
    return pull_request.get("body") or "", labels


def render(metrics: Metrics, result: Result) -> str:
    lines = [
        "# PR scope check",
        "",
        "| Measure | Value |",
        "| --- | ---: |",
        f"| Production files | {metrics.production_files} |",
        f"| Production line churn | {metrics.production_churn} |",
        f"| Total changed files | {metrics.total_files} |",
        f"| Total line churn | {metrics.total_churn} |",
    ]
    if result.warnings:
        lines.extend(["", "## Warnings", *[f"- {x}" for x in result.warnings]])
    if result.errors:
        lines.extend(["", "## Errors", *[f"- {x}" for x in result.errors]])
    lines.extend(["", f"Result: {'PASS' if result.ok else 'FAIL'}"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--config", default=".github/pr-scope.json")
    parser.add_argument("--event", type=Path)
    args = parser.parse_args(argv)

    config = load_config(Path(args.config))
    metrics = collect_metrics(args.base, args.head, config)
    body, labels = event_context(args.event)
    result = evaluate(metrics, config, body=body, labels=labels)
    report = render(metrics, result)
    print(report, end="")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(report)
    for warning in result.warnings:
        print(f"::warning::{warning}")
    for error in result.errors:
        print(f"::error::{error}")
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
