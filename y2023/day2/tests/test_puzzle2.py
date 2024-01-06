import unittest

from y2023.day2.puzzle2 import minimum_for


class AdventOfCodeDay2Puzzle2(unittest.TestCase):
    def test_minimum_for_with_all_colors(self):
        n = minimum_for("1 red, 3 green, 2 blue")
        self.assertEqual(n, 6)

    def test_minimum_for_with_no_red(self):
        n = minimum_for("3 green, 2 blue")
        self.assertEqual(n, 0)


if __name__ == '__main__':
    unittest.main()
