# Day 18 - 100 Days of Code - Python
import time
import turtle
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

        print(my_turtle.heading())


# make_square_with_turtle()


def controlled_turtle():
    my_c_turtle = Turtle()
    my_c_turtle.shape("turtle")
    my_c_turtle.color("green")
    my_c_turtle.speed(1.5)
    my_c_turtle.shapesize(2, 2, 2)
    screen = Screen()

    def turn_up():
        turtle_angle = my_c_turtle.heading()
        if turtle_angle == 0.0:
            r"""facing right"""
            my_c_turtle.left(90)
        elif turtle_angle == 270.0:
            r"""facing down"""
            my_c_turtle.left(180)
        elif turtle_angle == 180.0:
            r"""facing left"""
            my_c_turtle.right(90)

        my_c_turtle.forward(100)
        return

    def turn_down():
        turtle_angle = my_c_turtle.heading()
        if turtle_angle == 0.0:
            r"""facing right"""
            my_c_turtle.right(90)
        elif turtle_angle == 90.0:
            r"""facing up"""
            my_c_turtle.right(180)
        elif turtle_angle == 180.0:
            r"""facing left"""
            my_c_turtle.left(90)

        my_c_turtle.forward(100)
        return

    def turn_right():
        turtle_angle = my_c_turtle.heading()
        if turtle_angle == 90.0:
            r"""facing up"""
            my_c_turtle.right(90)
        elif turtle_angle == 270.0:
            r"""facing down"""
            my_c_turtle.left(90)
        elif turtle_angle == 180.0:
            r"""facing left"""
            my_c_turtle.right(180)

        my_c_turtle.forward(100)
        return

    def turn_left():
        turtle_angle = my_c_turtle.heading()
        if turtle_angle == 0.0:
            r"""facing right"""
            my_c_turtle.left(180)
        elif turtle_angle == 270.0:
            r"""facing down"""
            my_c_turtle.right(90)
        elif turtle_angle == 90.0:
            r"""facing up"""
            my_c_turtle.left(90)

        my_c_turtle.forward(100)
        return


    screen.listen()
    screen.onkeypress(turn_up, "Up")
    screen.onkeypress(turn_down, "Down")
    screen.onkeypress(turn_right, "Right")
    screen.onkeypress(turn_left, "Left")
    turtle.mainloop()


# controlled_turtle()

turn_counter = 0
def dashed_line_turtle():

    global turn_counter
    my_turtle = Turtle()
    my_turtle.pensize(2)
    my_turtle.shape("turtle")
    my_turtle.speed(1.5)
    my_turtle.shapesize(2, 2, 2)
    screen = Screen()


    def dash_handle():
        if my_turtle.isdown():
            my_turtle.pu()
        else:
            my_turtle.pd()

    def make_tiny_steps(distance):
        for i in range(distance):
            my_turtle.forward(5)
            dash_handle()

    def turtle_move_in_square():

        global turn_counter
        if turn_counter == 0:
            make_tiny_steps(25)
        my_turtle.right(90)
        if turn_counter == 4:
            make_tiny_steps(25)
            turn_counter = 0
            my_turtle.clear()
        else:
            make_tiny_steps(40)


    while True:
        turtle_move_in_square()



dashed_line_turtle()
