import re
from file_utils import read_lines

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
alpha_numbers = "one|two|three|four|five|six|seven|eight|nine"


def run(basePath):
    lines = read_lines(f"{basePath}/day1.data.txt")
    total = process_lines(lines)
    print(f"Total: {total}")


def process_lines(file_lines):
    total = 0
    for line in file_lines:
        total += first_and_last_number(line.strip())
    return total


def first_and_last_number(line):
    x = re.findall(f'(?=(\\d|{alpha_numbers}))', line)
    n = alpha_to_number(x[0]) * 10 + alpha_to_number(x.pop())
    return n


def alpha_to_number(value):
    if type(value) is int:
        return value
    elif re.match("^[0-9]$", value):
        return int(value)
    else:
        return numbers.get(value)