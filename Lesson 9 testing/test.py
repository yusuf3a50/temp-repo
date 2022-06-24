# from unittest import TestCase
import unittest
from main import red_or_blue

class TestRedOrBlueFunction(unittest.TestCase):

    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(5)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=54)
        self.assertEqual(expected, result)

    def test_range_6_to_20(self):
        expected = 'Red'
        result = red_or_blue(num=12)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()