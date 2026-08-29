from gendiff import generate_diff

with open('tests/test_data/flat_result.txt', 'r', encoding='utf-8') as f:
    result = f.read()
    print(result.strip())
