# TASK 2 (Exception Handling)

# Question 1
# Simple ATM program
# Using exception handling code blocks such as try/ except / else / finally, write a
# program that simulates an ATM machine to withdraw money.
# (NB: the more code blocks the better, but try to use at least two key words e.g.
# try/except)

# Tasks:
# 1. Prompt user for a pin code
# 2. If the pin code is correct then proceed to the next step, otherwise ask a user to
# type in a password again. You can give a user a maximum of 3 attempts and then
# exit a program.
# 3. Set account balance to 100.
# 4. Now we need to simulate cash withdrawal
# 5. Accept the withdrawal amount
# 6. Subtract the amount from the account balance and display the remaining
# balance (NOTE! The balance cannot be negative!)
# 7. However, when a user asks to ‘withdraw’ more money than they have on their
# account, then you need to raise an error an exit the program.

def request_pin():
    attempt = input('please input your pin: ')

def cash():
    balance = 100
    print(f'your balance is £{balance}')
    if balance < withdrawal:
        print('you dont have enough cash for this withdrawal!')
        return False
    else:
        balance = balance - withdrawal
        print(f'Please take your cash. Your new balance is now £{balance}')
        return True

# def pin(attempt):
#     tries = 0
#     while tries <3:
#         if attempt != 1234:
#             print('your pin was not correct')
#             tries += 1
#             return False
#         if attempt == 1234:
#             print('your pin was correct')
#             cash()
#             return True
#         if tries == 3:
#             print('your card has been blocked and you have been reported to the python police')


request_pin()

def wd():
    withdrawal = int(input('how much would would you like to withdraw? '))
wd()
# pin(attempt)