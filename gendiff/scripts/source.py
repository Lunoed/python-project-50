import json
import os


def get_data_path(filename: str) -> str:
    for root, _, files in os.walk(os.getcwd()):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, filename))


def read_file(filename: str) -> str:
    path = get_data_path(filename)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def generate_diff(filename1: str, filename2: str) -> str:
    data1: dict = read_file(filename1)
    data2: dict = read_file(filename2)
    data_with_all_keys = data1 | data2
    keys = list(data_with_all_keys.keys())
    keys.sort()
    result = []
    for key in keys:
        if key in data1.keys() and key in data2.keys():
            if data1[key] == data2[key]:
                result.append(f'   {key}: {data1[key]}\n')
            else:
                result.append(f' - {key}: {data1[key]}\n')
                result.append(f' + {key}: {data2[key]}\n')
        elif (key in data1.keys()) and not (key in data2.keys()):
            result.append(f' - {key}: {data1[key]}\n')
        else:
            result.append(f' + {key}: {data2[key]}\n')
    string = ''.join(result)
    answer = '{\n' + string + '}'
    return answer.strip()


#print(generate_diff('file1.json', 'file2.json'))
