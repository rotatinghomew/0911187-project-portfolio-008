"""组织评审证据、可行性结论与多目标候选。"""

from collections import defaultdict

from .feasibility import assess
from .frontier import pareto_candidates


def summarize(records):
    projects = {str(row["id"]): row for row in records if row["kind"] == "project"}
    criteria = [row for row in records if row["kind"] == "criterion"]
    scores = defaultdict(dict)
    for record in records:
        if record["kind"] == "assessment" and record.get("score") is not None:
            scores[str(record["project_id"])][str(record["criterion_id"])] = float(record["score"])
    feasibility = assess(projects, criteria, scores)
    objectives = [str(row["id"]) for row in criteria if not row.get("hard")]
    return {
        "projects": feasibility,
        "pareto_candidates": pareto_candidates(projects, feasibility, scores, objectives),
        "unevaluated": sorted(project_id for project_id in projects if any(key not in scores[project_id] for key in objectives)),
    }
