# Day 21 - 100 Days of Code - Python
import random
# Make some progres , the snake object is almost ready.
# next thing - game logic and in-game event handlers.

import time
from turtle import Turtle, Screen

screen_size = 600
buffer_from_edge = 10
game_area = int((screen_size/2) - buffer_from_edge)
screen = Screen()
screen.setup(height=screen_size, width=screen_size)
screen.colormode(255)

directions = {
    "E": 0,
    "S": 270,
    "W": 180,
    "N": 90
}

class ScoreBoard:
    def __init__(self):
        self.sb = Turtle()
        self.sb.pu()
        self.sb.hideturtle()
        self.sb.setpos((-game_area + 70, game_area - 20))

    def update_score(self, score):

        self.sb.clear()
        self.sb.write(f"Score : {score}", move=False, align="right", font=("Arial", 12, "bold"))

class Apple:
    def __init__(self):
        self.apple = Turtle()
        self.apple.hideturtle()
        self.apple.pu()
        self.x = random.randint(-game_area, game_area)
        self.y = random.randint(-game_area, game_area)
        self.apple.setpos((self.x, self.y))
        self.apple.shape("circle")
        self.apple.color("red")
        self.apple.showturtle()

    def is_eaten(self, s_head):
        df = 10
        x_apple = self.apple.xcor()
        y_apple = self.apple.ycor()
        x_head = s_head.xcor()
        y_head = s_head.ycor()
        if (x_apple - df) <= x_head <= (x_apple + df) and (y_apple - df) <= y_head <= (y_apple + df):
            return True
        else:
            return False

    def remove_from_board(self):
        self.apple.hideturtle()


class Snake:
    def __init__(self):
        self.color_index = True
        self.head = Turtle()
        self.body = []
        self.tail = None
        self.step_size = 10
        self.speed = 3
        self.speed_limit = 5
        self.apples = 0
        self.change_dir = False

    def set_color(self):
        if self.color_index:
            c = (29, 95, 9)
        else:
            c = (93, 206, 58)

        self.color_index = not self.color_index
        return c

    def init_snake(self):
        self.init_head()
        self.init_body()

    def init_head(self):
        self.head.pu()
        self.head.color(self.set_color())
        self.head.shape("circle")

    def init_body(self):
        x = self.head.xcor()
        x -= self.step_size
        for i in range(2):
            new_cell = self.create_cell()
            new_cell.setx(x)
            self.body.append(new_cell)
            self.tail = new_cell
            x = new_cell.xcor()
            x -= self.step_size
            new_cell.showturtle()

    def create_cell(self):
        new_unit = Turtle()
        new_unit.hideturtle()
        new_unit.shape("circle")
        new_unit.pu()
        new_unit.color(self.set_color())
        return new_unit

    def update_snake(self):
        self.apples += 1
        new_cell = self.create_cell()
        x = self.tail.xcor()
        y = self.tail.ycor()
        new_cell.setpos((x, y))
        self.body.append(new_cell)
        self.tail = new_cell
        new_cell.showturtle()

    def s_movement(self):

        x_new = self.head.xcor()
        y_new = self.head.ycor()

        self.head.forward(self.step_size)

        for unit in self.body:
            x_old = unit.xcor()
            y_old = unit.ycor()
            unit.setx(x_new)
            unit.sety(y_new)
            x_new = x_old
            y_new = y_old

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
a = Apple()
s_board = ScoreBoard()
s_board.update_score(s.apples)

while True:
    if s.change_dir:
        s.change_dir = False
        time.sleep(0.2)
    else:
        s.s_movement()
    if a.is_eaten(s.head):
        print(f"apple is eaten in location ({a.x},{a.y})")
        a.remove_from_board()
        s.update_snake()
        s_board.update_score(s.apples)
        a = Apple()
    screen.listen()
    screen.onkey(key="w", fun=s.move_w_key)
    screen.onkey(key="d", fun=s.move_d_key)
    screen.onkey(key="s", fun=s.move_s_key)
    screen.onkey(key="a", fun=s.move_a_key)


screen.exitonclick()
