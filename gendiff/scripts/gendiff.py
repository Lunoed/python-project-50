import argparse
import sys

from .source import generate_diff


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    if args is None:
        args = sys.argv[1:]
    return parser.parse_args(args)
    

def main():
    args = parse_args()
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
