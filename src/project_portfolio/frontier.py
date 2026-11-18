"""提取未被其他候选支配的多目标方案。"""


def pareto_candidates(projects, feasibility, scores, objectives):
    eligible = [project_id for project_id in projects if feasibility[project_id]["feasible"] and all(key in scores[project_id] for key in objectives)]
    frontier = []
    for candidate in eligible:
        dominated = any(
            other != candidate
            and all(scores[other][key] >= scores[candidate][key] for key in objectives)
            and any(scores[other][key] > scores[candidate][key] for key in objectives)
            for other in eligible
        )
        if not dominated:
            frontier.append(candidate)
    return sorted(frontier)
