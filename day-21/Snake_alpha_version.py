# Day 21 - 100 Days of Code - Python
# Make some progres , the snake object is almost ready.
# next thing - game logic and in-game event handlers.
import random
import time
from turtle import Turtle, Screen

screen_size = 350
buffer_from_edge = 10
game_area = int((screen_size/2) - buffer_from_edge)
screen = Screen()
screen.setup(height=screen_size, width=screen_size)
screen.colormode(255)
screen.bgcolor(18, 18, 18)
x_score_label = -game_area + 70
y_score_label = game_area - 20


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
        self.sb.color('white')
        self.sb.hideturtle()
        self.sb.setpos((x_score_label, y_score_label))

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

        x_apple = self.apple.xcor()
        y_apple = self.apple.ycor()
        if s_head.distance(x_apple, y_apple) < 15:
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
        self.step_size = 20
        self.base_speed = 4
        self.tail_extra = 2
        self.apples = 0
        self.change_dir = False
        self.make_harder_at = 3

    def set_color(self):
        if self.color_index:
            c = (216, 232, 200)
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
        self.head.shape("square")
        self.head.speed(self.base_speed)

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
        new_unit.shape("square")
        new_unit.pu()
        new_unit.color(self.set_color())
        new_unit.speed(self.base_speed)
        return new_unit

    def update_snake(self):
        self.apples += 1
        for i in range(self.tail_extra):
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

    def update_speed(self):
        if self.base_speed < 10:
            new_speed = self.base_speed
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


    def check_if_touch_the_walls(self):
        if abs(self.head.xcor()) >= game_area or abs(self.head.ycor()) >= game_area:
            return True
        else:
            return False

    def level_up(self):
        if self.apples == self.make_harder_at:
            if self.base_speed < 10:
                self.base_speed += 2
                self.update_speed()
            self.tail_extra += 1
            self.make_harder_at += 3


    def check_if_head_touch_body(self):
        for cell in self.body:
            if self.head.distance(cell.xcor(), cell.ycor()) < 10:
                game_over(self.apples)


def pause_game():
    global game_flag
    ans = screen.textinput(prompt="To continue type 'c'\nto close the game type anything else..", title="Game Pause")
    if ans != "c":
        game_flag = False

def game_over(score):
    global game_flag
    global player_name
    screen.textinput(prompt="you lose!", title="Game Over")
    game_flag = False
    screen.textinput(prompt=f"{player_name} , your score is {score} ",title="Results")

def register():
    global player_name
    player_name = screen.textinput(prompt="Welcome to my Snake Game\nInsert your name:", title="Register")
    while player_name == "":
        player_name = screen.textinput(prompt="Not a valid name!\nPlease insert your name:", title="Invalid Input")


player_name = None
s = Snake()
s.init_snake()
a = Apple()
s_board = ScoreBoard()
s_board.update_score(s.apples)
game_flag = True
register()

while game_flag:
    if s.change_dir:
        s.change_dir = False
    else:
        s.s_movement()
    if a.is_eaten(s.head):
        print(f"apple is eaten in location ({a.x},{a.y})")
        a.remove_from_board()
        s.update_snake()
        s_board.update_score(s.apples)
        a = Apple()
    if s.check_if_touch_the_walls():
        game_over(s.apples)
    s.level_up()
    s.check_if_head_touch_body()
    print(f"current speed is {s.head.speed()}")
    screen.listen()
    screen.onkey(key="w", fun=s.move_w_key)
    screen.onkey(key="d", fun=s.move_d_key)
    screen.onkey(key="s", fun=s.move_s_key)
    screen.onkey(key="a", fun=s.move_a_key)
    screen.onkey(key="q", fun=pause_game)


screen.exitonclick()
