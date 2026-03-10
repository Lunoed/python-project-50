import argparse


def run_gendif():
    parser = argparse.ArgumentParser(
        prog="gendif",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(args)
