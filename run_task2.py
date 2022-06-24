# This method of running the script allows automated unit testing without any user prompts

from task2 import cash, correct_pin, attempts

pin = int(input('please input your pin: '))
attempts(pin, 0)