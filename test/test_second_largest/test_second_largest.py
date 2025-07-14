import unittest

from src.second_largest.util import second_largest

class TestSecondLargest(unittest.TestCase):
    def testSecondLargest(self):
        score_arr = [1,2,3,4,5]
        self.assertNotEqual(second_largest(score_arr),2)
        self.assertEqual(second_largest(score_arr),4)