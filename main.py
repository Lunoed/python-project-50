import yaml
import json


with open('tests/test_data/file1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(type(data))
    print(data)