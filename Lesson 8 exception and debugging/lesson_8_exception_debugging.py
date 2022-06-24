
# EXAMPLE 1

# denominator = int(input("Please enter a number to divide by: "))
# try:            # run this code
#     division_result = 100 / denominator
#     print(division_result)

# except ZeroDivisionError:
#                 # execute this code when there is an exception
#     print("You cannot divide by 0, please try gain")
# else:           # no exceptions? run this code
#     print("I ran successfully")
# finally:        # always run this code regardless
#     print("I always run regardless of error situation")


# EXAMPLE 2

# number = int(input('Enter a number in the range 5-10: '))

# try:
#     if number < 5 or number > 10:
#         raise Exception     # if condition is met then raise an exception thus jumping to the 'except:' code
#         # raise ValueError    # this can be an alternative

#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")

# except:
#     print("Your number is NOT in the requested range")




# EXAMPLE 3 - user defined errors

# class ValueIsBelowHundredError(ValueError):
#     """Raised when value is below 100"""
#     pass

# number = int(input('enetr a number above 100: '))

# try:
#     if number < 100:
#         raise ValueIsBelowHundredError
#     print(f"You sent {number}")

# except ValueIsBelowHundredError:
#     print("Your number is below 100")

# # EXAMPLE 4 - debugging


# def debugging_n_breakpoints():
#     my_list = []
#     for i in range(10):
#         new_i = 10 + i      # creates a number

#         print('new value is: ', i)
#         my_list.append((new_i))
#     return my_list

# debugging_n_breakpoints()


#########################################################
###                     PRACTICE                      ###
#########################################################

is_success = False

def validate_username(name):
    if ',' not in name:
        raise ValueError("Incorrect input: missing ',' to separate first anme from last name")

    # name_array = name.split(',')
    # first_name = name_array[0]
    # second_name = name_array[1]
    # shortened version:
    first_name, last_name = name.split(',')

    if not len(first_name) or not len(last_name):
        raise ValueError("Incorrect input: missing name or surname values")

def validate_age(age):
    if age < 0:    
        raise ValueError("Only teenagers are allowed")
    assert 12 < age <= 18

try:
    username = input('please input your full name (Firstname, Lastname): ')
    validate_username(username)
    age = int(input('what is your age?'))
    validate_age(age)

except ValueError as exc:
    print("Invalid input: %s" %exc)
except AssertionError as exc:
    print("the age is not within the teenage category")

else: 
    with open("register.txt", 'a') as text_file:
        text_file.write(f'new member name: {username} and age {age} \n')
    is_success = True
finally: 
    if is_success:
        print("Registratuion process completed successfully")
    else:
        print("could not complete regsitration, please try again")
    
print(".......proceeding")


# assert is used to evaluate stuff