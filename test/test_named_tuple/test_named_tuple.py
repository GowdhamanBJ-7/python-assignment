import unittest

from src.named_tuple.util import named_tuple

class TestNamedTuple(unittest.TestCase):
    def testNamedTuple(self):
        n = 5
        columns = ['ID', 'MARKS', 'NAME', 'CLASS']
        fields = [
            "1          97         Raymond    7",
            "2          50         Steven     4",
            "3          91         Adrian     9",
            "4          72         Stewart    5",
            "5          80         Peter      6"
        ]
        self.assertEqual(named_tuple(n,columns, fields), "78.00")

