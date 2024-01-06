import unittest

from y2023.day3.puzzle1 import numbers_near_symbol, sum_of_part_numbers

sampleData = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

class AdventOfCodeDay3Puzzle1(unittest.TestCase):
    def test_numbers_near_symbol(self):
        n = numbers_near_symbol(sampleData)
        self.assertEqual(n, [467, 35, 633, 617, 592, 755, 664, 598])

    def test_sum_of_part_numbers(self):
        n = sum_of_part_numbers(sampleData)
        self.assertEqual(n, 4361)


if __name__ == '__main__':
    unittest.main()
