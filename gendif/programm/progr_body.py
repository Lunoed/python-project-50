import argparse
import json
import os
#import orjson 

def show_info(data:dict):
    info = json.dumps(data, indent=4)
    print(info)

def find_file(file_name:str):
    for path, dir_names, files in os.walk("/home"):
        for file in files:
            if file == file_name:
                path = os.path.join(path, file)
                print(path)
                print(f'type(path) = {type(path)=}')

def find_path(file_name:str) ->str:
    for root, _, files in os.walk("/home"):
        for file in files:
            if file == file_name:
                path_to_file = os.path.join(root, file_name)
    return path_to_file

def read_file(file_name:str):
    path_to_file = find_path(file_name)
    with open(path_to_file, "r", encoding='utf-8') as f:
        data = json.load(f)
        show_info(data)
    return data

def work_with_file():
    ...

def run_gendif():
    parser = argparse.ArgumentParser(
        prog="gendif",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format',
                        help='set format of output')
    args = parser.parse_args()
    print(args)

file_name = 'file2.json'
#read_file(file_name)
read_file(file_name)
