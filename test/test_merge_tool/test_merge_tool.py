import unittest

from src.merge_the_tools.utils import merge_the_tools

class TestMergeTool(unittest.TestCase):
    def test_merge_tool(self):
        self.assertEqual(merge_the_tools('AABCAAADA',3), ['AB', 'CA', 'AD'])