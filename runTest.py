# TASK 3 (Testing)

# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller
# blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.

from unittest import TestCase
import unittest
from task2 import cash

# class testATM(unittest.TestCase):
# # class TestRedOrBlueFunction(TestCase):
#     # def test_correct_pin_number(self):
#     #     expected = True
#     #     res100ult = pin(attempt=1234)
#     #     self.assertEqual(expected, result)

#     # def test_incorrect_pin_number(self):
#     #     expected = 'Red'
#     #     result = red_or_blue(5)
#     #     self.assertEqual(expected, result)

#     def test_withdraw_cash(self):
#         expected = True
#         result = cash(withdrawal=99)
#         self.assertEqual(expected, result)

    # def test_withdraw_2much_cash(self):
    #     expected = 'Red'
    #     result = red_or_blue(num=12)
    #     self.assertEqual(expected, result)




from mock import patch
from unittest import TestCase

class TestRedOrBlueFunction(TestCase):
    def test_yes(self):
        with patch('__builtin__.raw_input', withdrawal=int(99)) as _raw_input:
            self.assertEqual(answer(), 'you entered 99')
            _raw_input.assert_called_once_with('enter yes or no')








if __name__ == '__main__':
    unittest.main()