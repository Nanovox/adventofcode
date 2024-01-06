import unittest

from y2023.day1.puzzle2 import first_and_last_number, alpha_to_number, process_lines

sample_lines = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]


class AdventOfCodeDay1(unittest.TestCase):
    def test_process_lines(self):
        n = process_lines(sample_lines)
        self.assertEqual(n, 142)

    def test_first_and_last_number(self):
        n = first_and_last_number("testone2")
        self.assertEqual(n, 12)
        n = first_and_last_number("test2numbers")
        self.assertEqual(n, 22)
        n = first_and_last_number("testfourasnumber")
        self.assertEqual(n, 44)

    def test_alpha_to_number(self):
        one = alpha_to_number("one")
        intone = alpha_to_number(1)
        self.assertEqual(one, 1)
        self.assertEqual(intone, 1)


if __name__ == '__main__':
    unittest.main()
