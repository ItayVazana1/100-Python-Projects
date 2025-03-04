# Day 4 - 100 Days of Code - Python
import random

# Randomization
# Computers are deterministic machines.
# to make a program pick a number randomly - we need to use specific Module.
# this module is "random" , and it's used to generate pseudo random numbers.
min = 1
max = 10
a = random.randint(min,max)
b = random.randint(min,max)
print(f"First random number --> a = {a}")
print(f"First random number --> b = {b}")
print("Now.. let's pick randomly again!")
a = random.randint(min,max)
b = random.randint(min,max)
print(f"Second random number --> a = {a}")
print(f"Second random number --> b = {b}")

# By the way ... what is a "Module"?
# A module in Python is a single file containing Python code (functions, classes, or variables)
# that can be imported and reused in other files.

# Some popular uses of random module in python:
number = random.random()
# random.random() returns a float number with value that is between 0 and 1
print(f"The number is {number}")

number = random.uniform(min,max)
# random.uniform(min,max) returns a float number with value that is between "min" and "max"
print(f"The number is {number}")

# Let's build a flipping coin game:
head = "Head"
tail = "tail"
p = random.randint(0,1)
print("Let's flip the coin!")
if p == 1:
    print(head)
else:
    print(tail)

# python Lists
# a List is a data structure.
# data structure allowed us to store items.
# List , fo example - is data structure that allowed
# us to save strings , numbers and other data - in a List
# which defined by [].
# Pay attention !
# there is importance to order of items in list!
c1 = "White"
c2 = "Black"
c3 = "Red"
c4 = "Blue"
c5 = "Yellow"
colors = [c1,c2,c3,c4,c5]
print(type(colors))
print(f"colors List --> {colors}")
colors2 = [c2,c1,c5,c4,c3]
print(f"colors2 List --> {colors2}")
print("colors != colors2 if we check order!")

# We cas access to items by using index , like that:
print(colors[1])
# remember - start from 0 !
print(colors[-2])
# also work reverse!

# add items to exist list:
# using append :
print(f"colors List --> {colors}")
new_c = "Green"
colors.append(new_c)
print(f"colors List after append new color --> {colors}")

# using extends to add mini list to list:
print(f"colors List --> {colors}")
mini_colors = ["Pink", "Orange"]
print(f"mini-colors List --> {colors}")
colors.extend(mini_colors)
print(f"colors List after append new color --> {colors}")

# random.choice() :
# the function is get as a parameter a List.
# the function returns one of the item from the list randomly:
# example :
r_color = random.choice(colors)
print("Color Picker! (version 1)")
print(f"color ----------> {r_color}")

# Another option to implement this:
# using random.randint() with min = 0 , max = highest index in the list
# use to number to access the item behind this index in the list.
# example:
r_number = random.randint(0, len(colors)-1)
print("Color Picker! (version 2)")
print(f"color ----------> {colors[r_number]}")

# Attention!!!
# we need to be careful when access by index to items in list.
# we should always remember what is the length of the list.
# the range of indexes in list is from 0 to len(lisr)-1
# (why -1 ? because we start with 0)
# access to item using an index that is out of range will give us an error.
