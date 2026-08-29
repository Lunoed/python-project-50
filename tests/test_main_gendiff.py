from gendiff import generate_diff


PATH_TO_RESULT = 'tests/test_data/flat_result.txt'

def test_main_gendiff():
    with open(PATH_TO_RESULT, 'r', encoding='utf-8') as file:
        result = file.read()
    assert generate_diff('file1.json', 'file2.json') == result.strip()
