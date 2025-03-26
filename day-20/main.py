# Day 20 - 100 Days of Code - Python

from turtle import Turtle, Screen


snake = []

def move_with_next(distance):
    save_pos = []
    for t in snake:
        save_pos.append([t.xcor(), t.ycor()])

    for i in range(len(save_pos)):
        save_pos[i][0] += distance

    for i in range(len(snake)):
        snake[i].setx(save_pos[i][0])



def load_turtles():
    x = 0
    for i in range(6):
        new_t = Turtle()
        new_t.pu()
        new_t.shape("circle")
        new_t.color("green")
        new_t.setx(x)
        x -= 20
        snake.append(new_t)


def move_forward():

    move_with_next(10)



load_turtles()


screen = Screen()
screen.listen()

while True:
    move_forward()



screen.exitonclick()