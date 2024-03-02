import demo
from demo import swap_strings
import unittest


class TestSwapStrings(unittest.TestCase):
    def test_swap_strings(self):
        string1 = 'abc'
        string2 = 'xyz'
        expected = 'xyc abz'
        actual = swap_strings(string1, string2)
        self.assertEqual('xyc abz', demo.swap_strings('abc', 'xyz'))




