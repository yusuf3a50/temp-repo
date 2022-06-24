from unittest import TestCase
from main import red_or_blue

class TestRedOrBlueFunction(TestCase):

    def test_odd_numbers(self):
        expect = 'Red'
        result = red_or_blue(5)
        self.assertEqual(expected, result)

if __name__== '__main__':
    unittest.main()