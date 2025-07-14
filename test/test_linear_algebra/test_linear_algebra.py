import unittest

import numpy as np

from src.linear_algebra.util import linearAlgebra

class TestLinearAlgebra(unittest.TestCase):
    def test_linear_algebra(self):

        matrix = np.array([
            [1.1, 1.1],
            [1.1, 1.1]
        ])

        self.assertEqual(linearAlgebra(matrix),0.0)