"""生成培养项目的比较报告。"""

from .analysis import summarize


def build_report(records, source_revision=""):
    if not source_revision:
        raise ValueError("必须提供数据修订标识")
    return {"source_revision": source_revision, "comparison": summarize(records)}
