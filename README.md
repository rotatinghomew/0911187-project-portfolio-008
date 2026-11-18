# 培养项目组合比较

比较能源工程培养项目的预算可行性和多项研究目标。本地合成 JSON 记录包含项目、评审条件和项目—条件评价；`hard` 条件可设最低值，普通目标按当前评分比较。

只有硬约束齐全且通过的项目会进入候选前沿。未评估的硬约束不会被当作通过，目标缺项的项目会单独列出。多个互不支配的候选都保留，不自动选出唯一赢家。当前报告仅使用最新条件与评价，尚未保存会议讨论时的规则版本和候选解释。

需要 Python 3.11 或更新版本，无外部服务。执行 `PYTHONPATH=src python -m unittest discover -s tests -v` 运行测试。`project_portfolio.facts` 读取评审记录，`project_portfolio.feasibility.assess` 判断硬约束，`project_portfolio.frontier.pareto_candidates` 保留多目标候选，`project_portfolio.analysis.summarize` 协调当前比较，`project_portfolio.reports.build_report` 绑定数据修订号。样例见 `examples/sample.json`。
