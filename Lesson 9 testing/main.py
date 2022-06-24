import unittest

def is_within_range(num, min, max):
    return num >= min and num <= max

def is_even(num):
    return num % 2 != 0

def red_or_blue(num):
    if (is_even(num) and num > 20) or (is_even(num) and is_within_range(num, 2, 5)):
        return 'Blue'
    if (not is_even(num)) or ((is_even(num)) and is_within_range(num, 6, 20)):
        return 'Red'
        
    