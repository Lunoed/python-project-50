import json


def to_json(diff: dict):
    result = json.dumps(diff, indent=2, ensure_ascii=False)
    return result
