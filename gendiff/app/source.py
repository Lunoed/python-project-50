import json
import os

import yaml

from .plain import format_plain
from .stylish import format_stylish


def get_data_path(filename: str) -> str:
    for root, _, files in os.walk(os.getcwd()):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, filename))


def determine_format(filename: str) -> str:
    _format = filename[-4:]
    if _format == ".yml" or _format == "yaml":
        return "yml"
    elif _format == "json":
        return "json"
    else:
        print("Unsupported format!")
        print("Program works only with json and yml formats.")
        raise ValueError(f"Unsupported file format: {filename}")


def read_file(filename: str) -> str:
    path = get_data_path(filename)
    format = determine_format(filename)
    with open(path, "r", encoding="utf-8") as f:
        if format == "json":
            data = json.load(f)
        elif format == "yml":
            data = yaml.safe_load(f)
    return data


def find_diff(filename1: str, filename2: str):
    data1 = read_file(filename1)
    data2 = read_file(filename2)

    def build(file1: dict, file2: dict) -> dict:
        result = {}
        union_keys = sorted(file1.keys() | file2.keys())
        for key in union_keys:
            in_first = key in file1
            in_second = key in file2

            if in_first and in_second:
                val1 = file1[key]
                val2 = file2[key]

                if isinstance(val1, dict) and isinstance(val2, dict):
                    if val1 == val2:
                        result[key] = {"status": "unchanged", "value": val1}
                    else:
                        result[key] = {
                            "status": "nested",
                            "children": build(val1, val2),
                        }

                elif type(val1) is not type(val2):
                    result[key] = {
                        "status": "changed",
                        "old_value": val1,
                        "new_value": val2,
                    }

                elif val1 == val2:
                    result[key] = {"status": "unchanged", "value": val1}

                else:
                    result[key] = {
                        "status": "changed",
                        "old_value": val1,
                        "new_value": val2,
                    }

            elif in_first and not in_second:
                result[key] = {"status": "removed", "value": file1[key]}
            else:
                result[key] = {"status": "added", "value": file2[key]}

        return result

    return build(data1, data2)


def generate_diff(file1: str, file2: str, format_name="stylish"):
    diff = find_diff(file1, file2)
    if format_name == "stylish":
        result = format_stylish(diff)
    elif format_name == "plain":
        result = format_plain(diff)
    return result
