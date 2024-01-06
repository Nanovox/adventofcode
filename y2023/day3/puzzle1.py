import re
import os.path as path

star_parts = {}


def run(basePath):
    filename = path.abspath(f"{basePath}/day3.data.txt")
    lines = read_lines(filename)
    total = sum_of_part_numbers(lines)
    print(f"Total: {total}")


def read_lines(file_name):
    lines = []
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return lines


def sum_of_part_numbers(schematic):
    return sum(numbers_near_symbol(schematic))


def numbers_near_symbol(sample_data):
    near_list = []
    for pos in range(0, len(sample_data)):
        sample = sample_data[pos]
        matches = find_all_numbers(sample)
        near_line = []
        for match in matches:
            number = match.group(0)
            start = max(0, match.start() - 1)
            end = min(len(sample_data[pos]) - 1, match.end() + 1)
            prev_line = max(0, pos - 1)
            next_line = min(len(sample_data) - 1, pos + 1)
            near_symbol = False
            for i in range(prev_line, next_line + 1):
                area = sample_data[i][start:end:]
                found = find_all_matcher(area, re.compile(r'[^\d.]'))
                if len(found) > 0:
                    near_symbol = True
            if near_symbol:
                near_line.append(int(number))
        near_list += near_line
    return near_list


def offsets_for(start, matches):
    offsets = []
    for match in matches:
        offsets.append(start + match.start())
    return offsets


def find_all_matcher(line, matcher):
    start = 0
    matches = []
    while match := matcher.search(line, start):
        start = match.end()
        matches.append(match)
    return matches


def find_all_numbers(line):
    return find_all_matcher(line, re.compile(r'[0-9]+'))


    # print(f'number: {number} at {start} to {end}: {sample} : {area} => {found}')
