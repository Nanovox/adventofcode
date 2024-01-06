import os.path as path
import re

possible = {"red": 12, "green": 13, "blue": 14}


def run(basePath):
    filename = path.abspath(f"{basePath}/day2.data.txt")
    lines = read_lines(filename)
    total = count_possibilities(lines)
    print(f"Total: {total}")


def count_possibilities(file_lines):
    total = 0
    for line in file_lines:
        [game, picks] = line.strip().split(': ')
        game_number = int(game[5::])
        total += game_number if game_possible(picks) else 0
    return total


def game_possible(picks):
    for pick in picks.split('; '):
        for group in pick.split(', '):
            [count, color] = group.split(' ')
            if possible[color] < int(count):
                return bool(False)
    return bool(True)


def read_lines(file_name):
    lines = []
    file = open(file_name, "r")
    for line in file:
        lines.append(line)
    return lines