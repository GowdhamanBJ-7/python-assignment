import unittest
from src.time_delta.utils import time_delta

class TestTimeDelta(unittest.TestCase):
    def test_time_delta(self):
        t1="Sun 10 May 2015 13:54:36 -0700"
        t2="Sun 10 May 2015 13:54:36 -0000"

        self.assertEqual(time_delta(t1,t2), "25200")

