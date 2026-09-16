import json


from gendiff import read_file
from gendiff.app.type_mapper import JsonDict


def gen_diff(filename1: str, filename2: str):
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
                        result[key] = {
                            "value": val1,
                            "status": "unchanged",
                        }
                    else:
                        result[key]= {
                            "status": "nested",
                            "children": build(val1, val2),
                        }
                elif val1 == val2:
                    result[key] = {
                        "status": "unchanged",
                        "value": val1
                    }
                else:
                    result[key] = {
                        "status": "changed",
                        "old_value": val1,
                        "new_value": val2
                    }
            elif in_first and not in_second:
                result[key] = {
                    "status": "removed",
                    "value": file1[key]
                }
            else:
                result[key] = {
                    "status": "added",
                    "value": file2[key]
                }
        return result
    return build(data1, data2)


if __name__ == "__main__":
    diff = gen_diff('file3.json', "file4.json")
    print(json.dumps(diff, indent = 2, ensure_ascii = False))
                    