# Day 10 - 100 Days of Code - Python

# Functions with outputs

# Remember functions ?
# so now - we use functions to return a value.
# the daily project will be a classic calculator app.
# today we will also finally understand deeply the consept of functions in python.

# this is the function format we first mat :
def my_fun():
    print("print somthing")

# after that , we also learn function with parameters:

def my_fun_with_p(param):
    print(f"print this -> {param}")


# and today , we will add to this format the return statement.
# what is "return"?
# using 'return' , we can return a value to the main program.
# it can be somthing that created inside the function or even just
# a constant value.

# example :
def my_fun_with_p_and_ret(param):
    base_string = "Hello, "
    return base_string + param


print(my_fun_with_p_and_ret("Mike"))

# this will print hello greeting to the name in param.

# another example :
def is_cap_or_low(param):
    if str(param).islower():
        return "lower"
    else:
        return "Capital"


letter = 'a'
print(f"The letter {letter} is {is_cap_or_low(letter)}")


# we are already familiar with function that return a value:
# remember len() ?
# the parameter of len is a string or a data structure with countable items.
# the output is an integer , which describe the length of the input!

# function can return each data type or data structure that the python support.
# so we can return numbers,Strings,Boolean,Lists and even dictionaries


# Multiple return values.
# first , we need to know that each line of code in the function
# after the executed return - will not execute.
# return statement is the last executable line of code in the code.

# example of using multiple returns in function:
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False


years = [2000, 1580, 1440, 2100, 2025, 2024, 2010]
for item in years:
    print(f"{item} is a leap year = {is_leap_year(item)}")


# Docstring - using strings to document a function we built.
# to use that - we need to use 3x" to start and close :
"""
This is a DocString , just a Docstring without meaning !
"""

def is_leap_year_doc(year):
    """
    :param year: Integer represent the year
    :return: True if year is a leap year and False otherwise.
    """

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

for item in years:
    print(f"{item} is a leap year = {is_leap_year_doc(item)}")


# By the way - we can create function inside function...
# example :

def name_to_letter(name):
    def itay(this_name):
        return "I"
    def koral(this_name):
        return "K"
    def angela(this_name):
        return "A"

    if name == "Itay":
        return itay(name)
    elif name == "Koral":
        return koral(name)
    elif name == "Angela":
        return angela(name)
    else:
        return 'Unknown'


my_list = ['Itay', 'Koral', 'Angela', 'Patrick']
for any_name in my_list:
    print(f"The name "
          f"The name '{any_name}' start with the letter [{name_to_letter(any_name)}]")



# TIP - using 'r' before string allow using '\' as a valid char!
