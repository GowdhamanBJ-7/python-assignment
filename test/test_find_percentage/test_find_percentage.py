import unittest

from src.find_percentange.util import find_percentage

class TestFindPercentage(unittest.TestCase):
    def test_percentage(self):
        data = {
            'Krishna':[67, 68, 69],
            'Arjun': [70, 98, 63],
            'Malika':[52, 56, 60]
        }

        self.assertEqual(find_percentage(data,'Malika'), "56.00")