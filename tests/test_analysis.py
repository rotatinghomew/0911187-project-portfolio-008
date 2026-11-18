import unittest

from project_portfolio.analysis import summarize
from project_portfolio.reports import build_report


class ProjectPortfolioTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"id": "p1", "kind": "project", "name": "储能诊断"},
            {"id": "p2", "kind": "project", "name": "调度优化"},
            {"id": "p3", "kind": "project", "name": "材料检测"},
            {"id": "budget", "kind": "criterion", "hard": True, "minimum": 5},
            {"id": "impact", "kind": "criterion", "hard": False},
            {"id": "risk", "kind": "criterion", "hard": False},
            {"id": "a1", "kind": "assessment", "project_id": "p1", "criterion_id": "budget", "score": 4},
            {"id": "a2", "kind": "assessment", "project_id": "p1", "criterion_id": "impact", "score": 9},
            {"id": "a3", "kind": "assessment", "project_id": "p1", "criterion_id": "risk", "score": 7},
            {"id": "a4", "kind": "assessment", "project_id": "p2", "criterion_id": "budget", "score": 8},
            {"id": "a5", "kind": "assessment", "project_id": "p2", "criterion_id": "impact", "score": 8},
            {"id": "a6", "kind": "assessment", "project_id": "p2", "criterion_id": "risk", "score": 9},
            {"id": "a7", "kind": "assessment", "project_id": "p3", "criterion_id": "budget", "score": 7},
            {"id": "a8", "kind": "assessment", "project_id": "p3", "criterion_id": "impact", "score": 6},
            {"id": "a9", "kind": "assessment", "project_id": "p3", "criterion_id": "risk", "score": 10},
        ]

    def test_hard_constraint_precedes_objective_comparison(self):
        result = summarize(self.records)
        self.assertFalse(result["projects"]["p1"]["feasible"])
        self.assertNotIn("p1", result["pareto_candidates"])

    def test_tradeoff_candidates_are_not_forced_into_one_winner(self):
        result = summarize(self.records)
        self.assertEqual(result["pareto_candidates"], ["p2", "p3"])

    def test_report_keeps_source_revision(self):
        self.assertEqual(build_report(self.records, "review-4")["source_revision"], "review-4")


if __name__ == "__main__":
    unittest.main()
