import argparse

from gendiff import parse_args


def test_parse_args_two_files():
    args = parse_args(['file1.json', 'file2.json'])
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format is None


def test_args_with_format():
    args = parse_args(['file1.json', 'file2.json', '-f', 'plain'])
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'
