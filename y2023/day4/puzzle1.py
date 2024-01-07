from file_utils import read_lines
import re
from math import factorial


def run(basePath):
    lines = read_lines(f"{basePath}/day4.data.txt")
    total = process_cards(lines)
    print(f"Total: {total}")


def process_cards(lines):
    total = 0
    for card in lines:
        [_id, data] = card.split(":")
        [winners, numbers] = re.split(r'\s?\|\s?', data)
        total += find_winners(winners.strip(), numbers.strip())
    return total


def find_winners(winners_str, numbers_str):
    occurs = 0
    winners = re.split(r"\s+", winners_str)
    numbers = re.split(r"\s+", numbers_str)
    for winner in winners:
        occurs += numbers.count(winner)
    total = calculate_doubling(occurs)
    return total


def calculate_doubling(times):
    if times == 0:
        return 0
    num = int(f"1{'0' * (times - 1)}", 2)
    return num
