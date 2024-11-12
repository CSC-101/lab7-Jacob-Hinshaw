import unittest
from lib2to3.pytree import convert

from convert import str_to_float


class TestCases(unittest.TestCase):

    def test1_str_to_float(self):
        input1 = "123"
        result = str_to_float(input1)
        expected = 123.0
        self.assertEqual(expected, result)
    def test2_str_to_float(self):
        input1 = "Hey"
        result = str_to_float(input1)
        expected = None
        self.assertEqual(expected, result)


