# Day 21 - 100 Days of Code - Python


# Make some progres , the snake object is almost ready.
# next thing - game logic and in-game event handlers.

import time
from turtle import Turtle, Screen

directions = {
    "E": 0,
    "S": 270,
    "W": 180,
    "N": 90
}


class Snake:
    def __init__(self):
        self.head = Turtle()
        self.body = []
        self.step_size = 7
        self.speed = 3
        self.speed_limit = 5
        self.apples = 0
        self.change_dir = False

    def init_snake(self):
        self.init_head()
        self.init_body()

    def init_head(self):
        self.head.pu()
        self.head.color("green")
        self.head.shape("circle")

    def init_body(self):
        x = self.head.xcor()
        x -= self.step_size
        for i in range(2):
            new_unit = Turtle()
            new_unit.pu()
            new_unit.color("green")
            new_unit.shape("circle")
            new_unit.setx(x)
            self.body.append(new_unit)
            x = new_unit.xcor()
            x -= self.step_size

    def s_movement(self):

        x_old = None
        y_old = None
        heading_old = None
        x_new = self.head.xcor()
        y_new = self.head.ycor()
        heading_new = self.head.heading()

        self.head.forward(self.step_size)

        for unit in self.body:
            x_old = unit.xcor()
            y_old = unit.ycor()
            heading_old = unit.heading()
            unit.setx(x_new)
            unit.sety(y_new)
            unit.seth(heading_new)
            x_new = x_old
            y_new = y_old
            heading_new = heading_old

    def update_speed_limit(self):
        if self.speed_limit != 10:
            self.speed_limit += 1
            self.update_speed()

    def update_speed(self, auto=False):
        if not self.speed_limit == 10:
            if not self.speed == self.speed_limit:

                new_speed = self.speed + 1

                self.head.speed(new_speed)
                for t in self.body:
                    t.speed(new_speed)

    def move_w_key(self):
        current_heading = int(self.head.heading())
        if current_heading == directions["E"] or current_heading == directions["W"]:
            self.head.seth(directions["N"])
            self.change_dir = True

    def move_d_key(self):
        current_heading = int(self.head.heading())
        if current_heading == directions["N"] or current_heading == directions["S"]:
            self.head.seth(directions["E"])
            self.change_dir = True

    def move_s_key(self):
        current_heading = int(self.head.heading())
        if current_heading == directions["E"] or current_heading == directions["W"]:
            self.head.seth(directions["S"])
            self.change_dir = True

    def move_a_key(self):
        current_heading = int(self.head.heading())
        if current_heading == directions["N"] or current_heading == directions["S"]:
            self.head.seth(directions["W"])
            self.change_dir = True


s = Snake()
s.init_snake()
screen = Screen()


while True:
    if s.change_dir:
        s.change_dir = False
        time.sleep(0.2)
    else:
        s.s_movement()
    screen.listen()
    screen.onkey(key="w", fun=s.move_w_key)
    screen.onkey(key="d", fun=s.move_d_key)
    screen.onkey(key="s", fun=s.move_s_key)
    screen.onkey(key="a", fun=s.move_a_key)


screen.exitonclick()
