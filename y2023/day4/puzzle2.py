from file_utils import read_lines
import re
from math import factorial

card_counts = {}


def run(basePath):
    lines = read_lines(f"{basePath}/day4.data.txt")
    process_cards(lines)
    print(f"Card Total: {sum(card_counts.values())}")


def process_cards(lines):
    for card in lines:
        [i, data] = card.split(":")
        card_number = int(re.split(r'\s+', i)[1])
        increment_card(card_number)

        [winners, numbers] = re.split(r'\s?\|\s?', data)
        find_winners(card_number, winners.strip(), numbers.strip())

def increment_card(number):
    card_counts[number] = 1 if number not in card_counts else card_counts[number] + 1


def find_winners(card_number, winners_str, numbers_str):
    repeat = card_counts[card_number]
    occurs = 0
    winners = re.split(r"\s+", winners_str)
    numbers = re.split(r"\s+", numbers_str)
    for winner in winners:
        occurs += numbers.count(winner)
    for i in range(card_number + 1, card_number + 1 + occurs):
        for r in range(0, repeat):
            increment_card(i)
    total = calculate_doubling(occurs)
    return total


def calculate_doubling(times):
    if times == 0:
        return 0
    num = int(f"1{'0' * (times - 1)}", 2)
    return num
