# Day 13 - 100 Days of Code - Python
from random import randint


# Debugging
# (No daily project today - but still some important topics and concepts)

# Debugging is the process of detecting and solving problems
# in the code (not meter if it's running issues or mistake in values).

# Grace Hopper - the first documented bug found by her.
# it was actually a real bug on the plastic board which was run the program.
# the bug prevents the program to run properly

# Every one - in every level and every position - creates bugs by mistake.
# it's a part of the programing process, and it's not a shame at all!
# from each bug - we can learn more and be better !

# Tips fo right Debugging :

# 1 - First step - Describe the problem , make it more clear and less messy.
# when the problem becomes more clear - it's easier to find
# the source of it and give the right solution.

# example:

def my_func1():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")


my_func1()


# if we will run it - we will see nothing printed to screen.
# so we need to ask our self some questions:
# 1. what is the for loop doing?
# ans = running on values of 'i' in range of 1 to 20
# 2. when is the function meant to print "You got it!"?
# ans = print "You got it!" when 'i' is equal to 20
# 3. in each run of the loop - what is the value of 'i'?
# ans = the value of 'i' is starting at 1 and increment by 1 in each run.

# so now we know that the problem is somehow related to the value of 'i'.
# we can use print() to show the value of i in each running.

# here is the version of this function with this print():

def my_func1_debug_i_value():
    for i in range(1, 20):
        print(f"The value of 'i' is {i}")
        if i == 20:
            print("You got it!")


my_func1_debug_i_value()

# Output of this function:
"""
The value of 'i' is 1
The value of 'i' is 2
The value of 'i' is 3
The value of 'i' is 4
The value of 'i' is 5
The value of 'i' is 6
The value of 'i' is 7
The value of 'i' is 8
The value of 'i' is 9
The value of 'i' is 10
The value of 'i' is 11
The value of 'i' is 12
The value of 'i' is 13
The value of 'i' is 14
The value of 'i' is 15
The value of 'i' is 16
The value of 'i' is 17
The value of 'i' is 18
The value of 'i' is 19
"""


# we can see that at the last running of the loop,
# the value of 'i' is 19 , which is lower than 20.

# in order to make the function work , we can fix the MAX value
# inside the range() function , like that :


def my_func1_solution1():
    max_value = 21
    for i in range(1, max_value):
        if i == 20:
            print("You got it!")


my_func1_solution1()


# we can see now that it's works!

# another fixed version can focus on the 'if' condition:

def my_func1_solution2():
    new_i_for_condition = 19
    for i in range(1, 20):
        if i == new_i_for_condition:
            print("You got it!")


my_func1_solution2()

# that is also works!

# 2 - Reproduce the bug - somtimes , bug can be sneaky.
# they might be occurred by certain conditions , which make it
# harder to find them.
# so one of our missions in the debugging process is to find the
# specific condition such that the bug is effect the program running.

# for example :

dice_symbols = ['!', '@', '#', '$', '%', '^']
# dice_numbers = randint(a=1,b=6)
# print(dice_symbols[dice_numbers])
# (commented the problematic code lines)

# somtimes it's work , but sometimes it's give error in the output.
# This is the output when there is error:
r"""
Traceback (most recent call last):
  File <path> , line 119, in <module>
    print(dice_symbols[dice_numbers])
          ~~~~~~~~~~~~^^^^^^^^^^^^^^
IndexError: list index out of range
"""

# it's says that the list index is out of range.
# and why this is happening somtimes?
# let's remember :
# random.randint(a,b) gives random number in range [a,b] (include a and b)
# the index of list start at value 0 - so the last index is len(list)-1
# so based on that , if a = 1 , b = 6 , and list length is 6:
# the number that the randint can return is only one of those : 1,2,3,4,5,6
# the indexes of the items in the list are : 0,1,2,3,4,5
# so - we figure out 2 things:
# 1- we will never print the first symbol in the list (index 0) because we never get 0 from randint
# 2- we could get 6 from randint , but there is no item in the list with index = 6

# so now , we know that the problem related to the returned value from randint
# and also to the length of the list which gives us an indication to the range of indexes.

# to fix it , we can change the numbers in the randint parameters like that:

min_val = 0
max_val = 5
dice_numbers = randint(a=min_val, b=max_val)
print(dice_symbols[dice_numbers])

# 3 - Play Computer - scan each line of code from start to end.
# it's also recommended to create a trace chart to follow each
# variable and part of the code , and write each change in each one
# based on the flow of the program while running.
# another way to follow this flow is to write it like a story , and
# use each variable as a character in it:

# for example :

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# let's analyze the flow :
# 1) first , there is an input from user
# 2) the input casting from string type to int.
# 3) the meaning of the input - player's year of born.

# remember:  lower than 1994 == lower than or equal to 1993
# and also:  higher than 1980 == higher or equal to 1981
# 4) if the year is higher than 1980 , and also lower than or equal 1993 -
#    than the player is 32 - 44 years old (today is 2025)
# 5) if the year is higher than 1994 - then the player age is equal or lower then 32

# so now - we can see the problem - if the input is 1994 - there is no result

# to fix it - we just need to decide which classification is suitable to 1994,
# and then fix the condition to be equal or greater/lower than (based on the condition we choose to modify)

# 4 - Fix the Errors - in most (if not all) IDE's ,
# we can see that an error in syntax exists - and fix them before compile and run the code.
# but other errors - like run-time errors , we can see them only after running.
# in these situations - we need to read the error description , find the line and the specific
# part in the line that cause the problem and fix it.
# and what if we don't know what the error even mean ?
# that's the time for Dr. Google...
# (and nowadays - even ChatGPT , Gemini or some another Ai module)
# search for the specific code or title of the error , and hopefully find some useful information
# which will help us to solve it.

# 5 - using try-except in the code (catch specific errors and response it the way we want):
age = 0
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid input type (should be numerical)")

if age > 18:
    print(f"You can drive at age {age}")

# Remember - print() is your best friend in the debugging process.


# 6 - Say hello to my little friend - Debugger

# The Debugger is a powerful tool , mostly built-in the IDE ,
# and it's give us the possibility to run the program in special way:
# we can choose specific line of code (and even code blocks and functions),
# and when the program is get to it - it stop , and give us information
# about the variables and the data structure at this specific point.
# from now and on , we can run it line by line , and see the changes in real time.
# this is a game changer - we can see every little effect of each line on each defined variable
# or function , and do this in the same time , moving slowly line by line, get deeper at the code,
# until we find the problem (the value or the cause for the raising error) and fix it.
# we can also "jump over" a built-in function or part of the code that we don't want to explore
# the logic inside of them (most of the time it's because it's not relevant to the solution),
# it's also useful when our project is build from more than one file.

# Final tips :
# 7 - take a break - most of the time it's better approach then sit hours and try.
# 8 - ask friend - (a human one) , it's not a shame - maybe they had experienced same thing once and found solution.
# 9 - Run often - don't wait until the code is too long and complex , it's easier to find solution to bug when the program is still simple.
# 10 - Ask StackOverflow - basically it's like asking a programmer friend , but millions of them. ---> avengers-assemble!
