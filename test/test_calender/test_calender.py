import unittest

from src.calender.util import day_finder

class TestCalender(unittest.TestCase):
    def test_positive_day(self):
        date = ['08', '09', '2025']
        self.assertEqual(day_finder(date),'SATURDAY')

    def test_negative_day(self):
        date = ['09','09','2024']
        self.assertNotEqual(day_finder(date),'SUNDAY')