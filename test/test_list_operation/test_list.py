import unittest

from src.list.util import process_commands

class TestListOperation(unittest.TestCase):
    def test_list_operation(self):
        N = 12
        commands = [
                'insert 0 5',
                'insert 1 10',
                'insert 0 6',
                'print',
                'remove 10',
                'append 9',
                'append 1',
                'sort',
                'print',
                'pop',
                'reverse',
                'print'
        ]
        expected_output = [
                [6, 5, 10],
                [1, 5, 6, 9],
                [6, 5, 1]
        ]
        self.assertEqual(process_commands(N,commands),expected_output)


