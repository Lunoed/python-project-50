import os

from gendiff import generate_diff

DATA_DIR = os.path.join("tests", "test_data")


def get_file_path(filename):
    return os.path.join(DATA_DIR, filename)


PATH_TO_RESULT = get_file_path("flat_result.txt")
PATH_TO_NESTED_RESULT_STYLISH = get_file_path("nested_stylish_result.txt")
PATH_TO_NESTED_RESULT_PLAIN = get_file_path("nested_plain_result.txt")
PATH_TO_NESTED_RESULT_JSON = get_file_path("nested_result.json")

FILE1_JSON_PATH = get_file_path("file1.json")
FILE2_JSON_PATH = get_file_path("file2.json")
FILE3_JSON_PATH = get_file_path("file3.json")
FILE4_JSON_PATH = get_file_path("file4.json")

FILE1_YAML_PATH = get_file_path("file1.yml")
FILE2_YAML_PATH = get_file_path("file2.yml")
FILE3_YAML_PATH = get_file_path("file3.yml")
FILE4_YAML_PATH = get_file_path("file4.yml")


def test_gendiff_json():
    with open(PATH_TO_RESULT, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH) == result.strip()


def test_gendiff_yaml():
    with open(PATH_TO_RESULT, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH) == result.strip()


def test_nested_stylish():
    with open(PATH_TO_NESTED_RESULT_STYLISH, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff(FILE3_JSON_PATH, FILE4_JSON_PATH) == result.strip()
    assert generate_diff(FILE3_YAML_PATH, FILE4_YAML_PATH) == result.strip()


def test_nested_result_plain():
    with open(PATH_TO_NESTED_RESULT_PLAIN, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff(FILE3_JSON_PATH, FILE4_JSON_PATH, "plain") == result.strip()
    assert generate_diff(FILE3_YAML_PATH, FILE4_YAML_PATH, "plain") == result.strip()


def test_type_json():
    with open(PATH_TO_NESTED_RESULT_JSON, "r", encoding="utf-8") as file:
        data = file.read()
    assert generate_diff(FILE3_JSON_PATH, FILE4_JSON_PATH, "json") == data
