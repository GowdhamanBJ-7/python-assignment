import unittest

from src.iterables.utils import iterables

class TestIterables(unittest.TestCase):
    def test_iterables(self):
        fun = iterables('a a d', 1)
        self.assertEqual(fun, "0.4000")