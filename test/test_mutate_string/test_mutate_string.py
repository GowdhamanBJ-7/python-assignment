import unittest

from src.mutate_string.utils import mutate_string

class TestMutateString(unittest.TestCase):
    def test_mutate_string(self):
        string = "abracadabra"
        position = 5
        letter ='k'
        self.assertEqual(mutate_string(string,position,letter),"abrackdabra")
