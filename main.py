from gendiff.app.source import find_diff
import json


result = find_diff('file3.json', "file4.json")

with open('tests/test_data/nested_result.json', 'w', encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=2)