import unittest

from y2023.day1.puzzle1 import first_number, last_number

class AdventOfCodeDay1(unittest.TestCase):
    def test_first_name(self):
        n = first_number("test1")
        self.assertEqual(n, 1)  # add assertion here

    def test_last_name(self):
        n = last_number("test12three")
        self.assertEqual(n, 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
