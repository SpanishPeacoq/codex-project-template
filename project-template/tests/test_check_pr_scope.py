from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_pr_scope.py"
SPEC = importlib.util.spec_from_file_location("check_pr_scope", SCRIPT)
assert SPEC and SPEC.loader
scope = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scope
SPEC.loader.exec_module(scope)


CONFIG = scope.ScopeConfig(
    soft=scope.Limits(5, 400, 15, 1000),
    hard=scope.Limits(8, 800, 25, 2000),
    non_production_prefixes=(".github/", "docs/", "tests/", "test/"),
)


def body(exception: str = "None.", checked: bool = True) -> str:
    checkbox = "x" if checked else " "
    return f"""## Outcome
One result.
## Primary intake
Issue 1.
## In scope
- implementation
## Out of scope
- adjacent work
## Verification
- tests
## Rollback
Revert this PR.
## Follow-up slices
None.
## Scope declaration
- [{checkbox}] This PR has one primary behavioral outcome.
## Scope exception
{exception}
"""


class ScopeCheckTests(unittest.TestCase):
    def test_numstat_separates_production_from_tests_and_docs(self):
        metrics = scope.parse_numstat(
            "100\t20\tsrc/app.py\n"
            "300\t0\ttests/test_app.py\n"
            "40\t10\tdocs/design.md\n"
            "15\t5\t.github/workflows/ci.yml\n",
            CONFIG,
        )
        self.assertEqual(metrics.production_files, 1)
        self.assertEqual(metrics.production_churn, 120)
        self.assertEqual(metrics.total_files, 4)
        self.assertEqual(metrics.total_churn, 490)

    def test_small_complete_pr_passes(self):
        result = scope.evaluate(
            scope.Metrics(2, 200, 6, 600), CONFIG, body=body(), labels=set()
        )
        self.assertTrue(result.ok)
        self.assertEqual(result.warnings, ())

    def test_review_budget_requires_explanation(self):
        result = scope.evaluate(
            scope.Metrics(6, 500, 16, 1100), CONFIG, body=body(), labels=set()
        )
        self.assertFalse(result.ok)
        self.assertTrue(result.warnings)
        self.assertIn("explain why", " ".join(result.errors))

    def test_review_budget_accepts_documented_exception(self):
        result = scope.evaluate(
            scope.Metrics(6, 500, 16, 1100),
            CONFIG,
            body=body("The schema and its only consumer must land atomically."),
            labels=set(),
        )
        self.assertTrue(result.ok)

    def test_hard_budget_requires_maintainer_label(self):
        explanation = "Generated migration and reader must land atomically."
        without_label = scope.evaluate(
            scope.Metrics(9, 900, 26, 2100),
            CONFIG,
            body=body(explanation),
            labels=set(),
        )
        with_label = scope.evaluate(
            scope.Metrics(9, 900, 26, 2100),
            CONFIG,
            body=body(explanation),
            labels={"approved-large-pr"},
        )
        self.assertFalse(without_label.ok)
        self.assertTrue(with_label.ok)

    def test_unchecked_outcome_fails(self):
        result = scope.evaluate(
            scope.Metrics(1, 20, 2, 40),
            CONFIG,
            body=body(checked=False),
            labels=set(),
        )
        self.assertFalse(result.ok)
        self.assertIn("one-primary-outcome", " ".join(result.errors))

    def test_template_placeholders_do_not_count_as_content(self):
        incomplete = body().replace(
            "One result.",
            "<!-- One sentence describing the observable result. -->",
        )
        result = scope.evaluate(
            scope.Metrics(1, 20, 2, 40),
            CONFIG,
            body=incomplete,
            labels=set(),
        )
        self.assertFalse(result.ok)
        self.assertIn("Outcome", " ".join(result.errors))


if __name__ == "__main__":
    unittest.main()
