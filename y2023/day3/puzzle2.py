import re
import os.path as path


def run(basePath):
    filename = path.abspath(f"{basePath}/day3.data.txt")
    lines = read_lines(filename)
    total = sum_of_gear_numbers(lines)
    print(f"Total: {total}")


def read_lines(file_name):
    lines = []
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return lines


def sum_of_gear_numbers(schematic):
    total = 0
    gears = numbers_near_symbol(schematic, re.compile(r'\*'))
    for gear in gears:
        list = gears[gear]
        total += 0 if len(list) != 2 else list[0] * list[1]
    return total


def numbers_near_symbol(sample_data, regmatch):
    star_parts = {}
    for pos in range(0, len(sample_data)):
        sample = sample_data[pos]
        matches = find_all_numbers(sample)
        for match in matches:
            number = match.group(0)
            start = max(0, match.start() - 1)
            end = min(len(sample_data[pos]) - 1, match.end() + 1)
            prev_line = max(0, pos - 1)
            next_line = min(len(sample_data) - 1, pos + 1)
            for i in range(prev_line, next_line + 1):
                area = sample_data[i][start:end:]
                found = find_all_matcher(area, regmatch)
                offsets = offsets_for(start, found)
                for offset in offsets:
                    key = f"{i}:{offset}"
                    if key in star_parts:
                        star_parts[key].append(int(number))
                    else:
                        star_parts[key] = [int(number)]
    return star_parts


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
