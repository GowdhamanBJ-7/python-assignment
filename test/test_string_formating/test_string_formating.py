import unittest

from src.string_formating.util import print_formatted

class TestStringFormatting(unittest.TestCase):
    def test_string_formatting(self):
        output = ['  1   1   1   1',
                  '  2   2   2  10',
                  '  3   3   3  11',
                  '  4   4   4 100',
                  '  5   5   5 101',
                  '  6   6   6 110',
                  '  7   7   7 111']
        self.assertEqual(print_formatted(7), output)
