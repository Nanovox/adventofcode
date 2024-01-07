import unittest

from y2023.day4.puzzle2 import process_cards, card_counts, increment_card

sample_cards = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]


class AdventOfCodeDay4Puzzle2(unittest.TestCase):
    def test_increment_card(self):
        increment_card(3)
        self.assertEqual(card_counts[3], 1)
        increment_card(4)
        self.assertEqual(card_counts[4], 1)
        increment_card(3)
        self.assertEqual(card_counts[3], 2)

    def test_process_cards(self):
        process_cards(sample_cards)
        self.assertEqual(sum(card_counts.values()), 30)


if __name__ == '__main__':
    unittest.main()
