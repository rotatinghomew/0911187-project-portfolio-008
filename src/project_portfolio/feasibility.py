"""应用项目评审的硬性条件并标明未核实项。"""


def assess(projects, criteria, scores):
    result = {}
    for project_id in projects:
        failed = [str(row["id"]) for row in criteria if row.get("hard") and scores[project_id].get(str(row["id"])) is not None and scores[project_id][str(row["id"])] < row.get("minimum", 0)]
        unknown = [str(row["id"]) for row in criteria if row.get("hard") and scores[project_id].get(str(row["id"])) is None]
        result[project_id] = {"feasible": not failed and not unknown, "failed_constraints": failed, "unknown_constraints": unknown, "scores": scores[project_id]}
    return result
