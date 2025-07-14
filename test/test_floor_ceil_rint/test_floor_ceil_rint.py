import unittest
import numpy as np
from src.Floor_Ceil_and_Rint.util import floor_Ceil_Rint  # Adjust import as needed


class TestFloorCeilRint(unittest.TestCase):
    def test_rounding(self):
        input_array = np.array([1.2, 2.5, 3.7])
        expected_floor = np.array([1., 2., 3.])
        expected_ceil = np.array([2., 3., 4.])
        expected_rint = np.array([1., 2., 4.])  # rint rounds to nearest even

        result = floor_Ceil_Rint(input_array)

        np.testing.assert_array_equal(result[0], expected_floor)
        np.testing.assert_array_equal(result[1], expected_ceil)
        np.testing.assert_array_equal(result[2], expected_rint)

