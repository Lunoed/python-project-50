import argparse

from .source import generate_diff


def make_parser():
    parser = argparse.ArgumentParser(
        prog="gendif",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file))


def main():
    make_parser()


if __name__ == "__main__":
    main()
