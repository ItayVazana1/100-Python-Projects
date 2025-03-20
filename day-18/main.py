# Day 18 - 100 Days of Code - Python
import time
# need to complete tomorrow!
# I am back! - let's do this!

# Today we the main topics are :
# Turtle Graphics
# Tuples
# Importing of Modules

# The daily project will be an Art Generator using Turtle library.
# Fun fact - once , an art like this sold for 1 million dollars $$$

# Turtle Graphic:

# this module can help us "draw" with python.

# first import turtle  :

from turtle import Turtle, Screen

# now we will create the turtle object :

tutti_the_turtle = Turtle()

# change it to be  really turtle and not cursor :
tutti_the_turtle.shape("turtle")

# we can also change the color of the turtle :

tutti_the_turtle.color('green')

# fins all available colors here : https://cs111.wellesley.edu/labs/lab02/colors

# now we need to give this turtle a stage to live on it:

# screen = Screen()

r"""
colors = ['SpringGreen', 'RoyalBlue', 'red2', 'purple1', 'orange1', 'magenta']
while screen:
    for c in colors:
        tutti_the_turtle.color(c)
        time.sleep(0.25)
"""

# we don't actually need to remember all of those functions of each object..
# a quick search using google , ChatGPT or in the Turtle Docs online -
# will give us a lot of data!

# there is also more shapes :
# print(screen.getshapes())

# ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']

# Tkinter = also known as Tk - is one of the most popular Moduls to build GUI in python.
# Turtle is based on Tk , and it is focused more on UI , and it is more simple.

# now that we have a turtle we can do this :
# we can make him move (in specific directions and angles):


# now just delete this turtle :
tutti_the_turtle.hideturtle()


# Now just make some fun with the turtle :)
def make_square_with_turtle():

    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color("green")
    my_turtle.speed(1.5)
    my_turtle.shapesize(2, 2, 2)
    turn_counter = 0
    colors = ['blue', 'red', 'purple', 'orange', 'pink', 'green']
    color_index = 0
    while True:
        if turn_counter == 0:
            my_turtle.forward(80)
        my_turtle.right(90)
        turn_counter += 1

        if turn_counter == 4:
            my_turtle.forward(80)
            my_turtle.clear()
            if color_index == len(colors)-1:
                color_index = 0
            my_turtle.color(colors[color_index])
            turn_counter = 0
            color_index += 1
        else:
            my_turtle.forward(160)



make_square_with_turtle()

