"""读取培养项目、约束和候选评价。"""

import json
from pathlib import Path


def load_records(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("记录文件必须包含数组")
    records = []
    seen = set()
    for position, record in enumerate(payload):
        if not isinstance(record, dict) or not record.get("id") or record.get("kind") not in {"project", "criterion", "assessment"}:
            raise ValueError(f"第 {position + 1} 条项目评议记录缺少身份或类型")
        if record["id"] in seen:
            raise ValueError(f"重复记录标识：{record['id']}")
        seen.add(record["id"])
        if record["kind"] == "assessment" and record.get("score") is not None and (isinstance(record["score"], bool) or not isinstance(record["score"], (int, float))):
            raise ValueError(f"评议 {record['id']} 的 score 必须是数值")
        records.append(dict(record))
    return records
