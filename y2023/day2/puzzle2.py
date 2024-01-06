import os.path as path
import re

possible = {"red": 12, "green": 13, "blue": 14}


def run(basePath):
    filename = path.abspath(f"{basePath}/day2.data.txt")
    lines = read_lines(filename)
    total = count_minimums(lines)
    print(f"Total: {total}")


def count_minimums(file_lines):
    total = 0
    for line in file_lines:
        [game, picks] = line.strip().split(': ')
        game_number = int(game[5::])
        total += minimum_for(picks)
    return total


def minimum_for(picks):
    mins = {"red": 0, "green": 0, "blue": 0}
    for pick in picks.split('; '):
        for group in pick.split(', '):
            [count, color] = group.split(' ')
            if int(count) > mins[color]:
                mins[color] = int(count)
    return mins["red"] * mins["green"] * mins["blue"]


def read_lines(file_name):
    lines = []
    file = open(file_name, "r")
    for line in file:
        lines.append(line)
    return lines