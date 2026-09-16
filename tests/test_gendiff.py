from gendiff import generate_diff

PATH_TO_RESULT = "tests/test_data/flat_result.txt"
PATH_TO_NESTED_RESULT_STYLISH = "tests/test_data/nested_stylish_result.txt"
PATH_TO_NESTED_RESULT_PLAIN = "tests/test_data/nested_plain_result.txt"


def test_gendiff_json():
    with open(PATH_TO_RESULT, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff("file1.json", "file2.json") == result.strip()


def test_gendiff_yaml():
    with open(PATH_TO_RESULT, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff("file1.yml", "file2.yml") == result.strip()


def test_nested_stylish():
    with open(PATH_TO_NESTED_RESULT_STYLISH, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff("file3.json", "file4.json") == result.strip()
    assert generate_diff("file3.yml", "file4.yml") == result.strip()


def test_nested_result_plain():
    with open(PATH_TO_NESTED_RESULT_PLAIN, "r", encoding="utf-8") as file:
        result = file.read()
    assert generate_diff("file3.json", "file4.json", "plain") == result.strip()
    assert generate_diff("file3.yml", "file4.yml", "plain") == result.strip()
