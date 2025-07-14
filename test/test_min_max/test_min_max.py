import unittest
from src.min_max.util import min_max
import numpy as np

class TestMinMax(unittest.TestCase):
    def test_min_max(self):
        arr = np.array([
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ])
        result = min_max(arr)
        self.assertEqual(result,3)