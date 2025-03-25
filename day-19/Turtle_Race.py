import random
from turtle import Turtle, Screen

init_turtle = Turtle()
screen = Screen()
screen.colormode(255)
colors = [(0, 0, 0), (255, 0, 0), (1, 156, 1), (69, 49, 246), (228, 37, 164), (21, 95, 206), (255, 128, 0)]
turtles = []
screen.setup(800, 600)

y = -250
gap = 75

for i in range(1, 7):
    new_t = Turtle()
    new_t.pu()
    new_t.color(colors[i-1])
    new_t.shape("turtle")
    new_t.shapesize(2)
    new_t.speed(random.randint(4, 10))
    new_t.setx(-350)
    new_t.sety(y + (gap*i))
    turtles.append(new_t)

game = True

while game:

    for t in turtles:
        t.forward(random.randint(5, 15))
        if t.xcor() >= 350:
            game = False
            break

screen.exitonclick()
