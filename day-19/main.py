# Day 19 - 100 Days of Code - Python

# I'm Back! - Got a little bit sick in the last couple days , but now I am here!

# Today we continue with turtle lib , and our goal today
# is to create 2 different kind of games using turtle :
# the first one is Etach and Sketch
# the second is Turtle race (betting game)

# Topics :

# Event listeners in Turtle -
# using this mechanism we can create programs that
# listen and ready to take action based on specific events.

# what an event can be ?
# specific period of time , key press , input - everything!

# let's see this example :

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


# now we use the listen() function of the screen :

screen.listen()

# and now we need to specify what will be the event and the action:

# onkey() => key = name of key , fun = function (without () )

screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

# now we can see that the cursor moving only when the user press the space bar

# functions as an input :
# we can use function as an argument to another function :

def get_num():
    num = ""
    while True:
        try:
            num = int(input("insert number:"))
            num = int(num)
            break
        except ValueError:
            print("It's not a valid number..")

    return num

def get_2_numbers(fun):
    a = fun()
    print("now the second number")
    b = fun()
    return [a,b]

def adding_numbers(numbers):
    return numbers[0]+numbers[1]


result = adding_numbers(get_2_numbers(get_num))

print(f"The result is = {result}")

# here we use 3 function , and the get_2_numbers using the get_num function as argument

# Now - we are ready to build the "Etch-A-Sketch" game
# You can see the code in the EtchASketch.py file.


# Now we move to the next game - Turtle race!
# in this game - the user need to bet on specific turtle (by color)
# and then there is a race between the turtles - each one in different color.
# the speed of each turtle is random.
# the winner is the first turtle that get to the finish line.

