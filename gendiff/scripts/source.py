import json
import os


def get_data_path(filename:str) -> str:
    for root, _, files in os.walk(os.getcwd()):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, filename))



def read_file(filename: str) -> str:
    path = get_data_path(filename)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

print(read_file('file1.json'))
