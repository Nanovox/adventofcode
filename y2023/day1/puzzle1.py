import re
from file_utils import read_lines


def run(basePath):
    lines = read_lines(f"{basePath}/day1.data.txt")
    total = process_lines(lines)
    print(f"Total: {total}")


def process_lines(file_lines):
    total = 0
    for line in file_lines:
        a = first_number(line)
        b = last_number(line)
        before = total
        v = a * 10 + b
        total += v
    return total


def first_number(line):
    x = re.search("^([^0-9]*)?([0-9])", line)
    return int(x.group(2))


def last_number(line):
    rline = line[::-1]
    x = re.search("^([^0-9]*)?([0-9])", rline)
    return int(x.group(2))
