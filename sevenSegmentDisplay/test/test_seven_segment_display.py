import unittest
from unittest import TestCase

from seven_segment_display import *


class MyTestCase(unittest.TestCase):
    def test_input_value(self):
        self.assertRaises(ValueError, lambda: input_value("10112112"))

    def test_input_value(self):
        self.assertRaises(ValueError, lambda: test_input_value )