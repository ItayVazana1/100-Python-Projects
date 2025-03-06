# Day 6 - 100 Days of Code - Python

# look at the resources folder - inside you will find screenshots from Reeborg's world - https://reeborg.ca/index_en.html

# Functions
# we already saw some functions - print() , len() , input() ....
# all of those functions are built-in functions , a part of python.
# a function is a code block that can be called by using name (the function name)
# function are useful to make code cleaner and more structured.

# but we don't have to use a built-in function , we cane create one of our own.
# using def key word , we can define functions:

def my_function():
    print("Hello world!")

# this function for example - printing the "Hello World"
# we can use it by refer to that function at the main program (calling the function)


my_function()

# we can use function as much as we want - even when looping :
for i in range(0,5):
    print(f"this is {i+1} time.")
    my_function()


# we can also use function inside function (in this example - print() is inside my_function() )

# Indentation:
# Indent is the space before the code in the specific line compared to the whole code.
# we can think about it like a File System :
# C
# - Desktop
# - - Chrome
# - Movies
# - Downloads
# - Pictures
# - - Camera_roll
# - - - You_and_I.png
# - - Backup

# if we will try to remove one of the spaces of "You_and_I.png"
# it will be out og the camera_roll , so it's change the correct order of files and folders in the File System.

# for indentations - the best practice is using spaces and not Tabs.

# while loops
# remember the concept of for loops ?
# in for loops the looping was based on a number or count of items in list.
# which mean before we enter loop - we could know exactly how much times it will operate
# remember the concept of if ?
# if a condition is True - we will enter the code block.

# so while loop is kind of this two ideas together -
# looping over code block again and again , when specific condition is true.
# let's see an example:

num = 10

while num != 0:
    print(f"num is {num}")
    num -= 1

# the loop is operating until the condition (num != 0) is false , which mean - until num == 0.
# we should be careful with while loops condition and make sure the condition will have a real potential to be false,
# so we don't risk to enter infinite loop.

# for example - "while 1" will be true allways - so it's not a good conditions.
# if we created infinity loop by mistake - we can just quit the program and fix the loop condition.
# using print() to debug the loop process is an amazing tool!



