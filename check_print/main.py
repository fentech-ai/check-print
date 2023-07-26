# print_arguments/main.py
import argparse
import logging
import re

logger = logging.getLogger()


def check_print_file(file: str) -> bool:
    success = True
    with open(file, "r") as file_one:
        for idx, line in enumerate(file_one):
            if re.search("print", line):
                logger.error(f"Print Stmt : {file} : L{idx}: {line}")
                success = False
    return success


def check_print(filenames: list[str]):
    valid = []
    for filename in filenames:
        valid.append(check_print_file(filename))
    if all(valid):
        return 0
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    if not args.filenames:
        raise ValueError("Empty file list")

    check_print(args.filenames)


if __name__ == "__main__":
    main()
