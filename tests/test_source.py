from gendiff import read_file, determine_format


def test_format_yaml():
    assert determine_format('filename.yml') == 'yml'
    assert determine_format('filename.yaml') == 'yml'


def test_format_json():
    assert determine_format('filename.json') == 'json'


def test_read_file():
    assert read_file('file1.json') == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert read_file('file1.yml') == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}