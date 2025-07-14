import unittest
from src.word_order.util import count_words

class TestWordOrder(unittest.TestCase):
    def test_positive(self):
        word = ['aa', 'bb', 'aa', 'cc', 'bb', 'aa']
        unique_count, counts = count_words(word)
        self.assertEqual(unique_count, 3)
        self.assertListEqual(counts, [3, 2, 1])

    def test_all_unique(self):
        word = ['one', 'two', 'three']
        unique_count, counts = count_words(word)
        self.assertEqual(unique_count, 3)
        self.assertEqual(counts, [1, 1, 1])