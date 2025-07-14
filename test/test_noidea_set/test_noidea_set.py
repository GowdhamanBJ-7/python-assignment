import unittest

from src.noidea_set.util import noIdea

class TestNoIdea(unittest.TestCase):
    def test_happiness(self):
        self.assertEqual(noIdea([1,5,3], [3,1], [5,7]),1)