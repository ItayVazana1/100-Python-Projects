import random
import time
from turtle import Turtle, Screen

screen_size = 600
buffer_from_edge = 10
game_area = int((screen_size/2) - buffer_from_edge)
screen = Screen()
screen.setup(height=screen_size, width=screen_size)
screen.colormode(255)
screen.bgcolor(18, 18, 18)
screen.tracer(0)

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

    def is_eaten(self, head_pos):
        if abs(head_pos[0] - self.apple.xcor()) < 15 and abs(head_pos[1] - self.apple.ycor()) < 15:
            return True
        return False

    def remove_from_board(self):
        self.apple.hideturtle()


# ****************************************************************************************************************************
#  ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---
# ****************************************************************************************************************************
# This version of the Snake game improves performance by changing the way the snake is represented and drawn.
# In the original (alpha) version, each part of the snake was a separate Turtle object, and the body list stored those objects.
# Every movement involved updating each Turtle's position, which caused performance to drop as the snake grew longer.
# In this optimized beta version, the snake's body is stored as a list of (x, y) coordinate tuples,
# and a single Turtle (draw_turtle) is used to draw the entire snake using the stamp() method.
# Each frame clears the previous drawings and redraws the snake at the new positions.
# This drastically reduces the number of Turtle objects, improves rendering efficiency,
# and keeps the game smooth even with a long snake.
# ****************************************************************************************************************************
#  ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---- READ THIS ---
# ****************************************************************************************************************************

class Snake:
    def __init__(self):
        self.color_index = True
        self.body = [(0, 0), (-20, 0), (-40, 0)]
        self.step_size = 20
        self.base_speed = 4
        self.tail_extra = 2
        self.apples = 0
        self.change_dir = False
        self.make_harder_at = 3
        self.heading = directions["E"]

        self.draw_turtle = Turtle()
        self.draw_turtle.hideturtle()
        self.draw_turtle.penup()
        self.draw_turtle.shape("square")
        self.draw_turtle.speed(0)

    def set_color(self):
        if self.color_index:
            c = (216, 232, 200)
        else:
            c = (93, 206, 58)
        self.color_index = not self.color_index
        return c

    def draw_snake(self):
        self.draw_turtle.clearstamps()
        for segment in self.body:
            self.draw_turtle.color(self.set_color())
            self.draw_turtle.goto(segment)
            self.draw_turtle.stamp()
        screen.update()

    def update_snake(self):
        self.apples += 1
        for _ in range(self.tail_extra):
            self.body.append(self.body[-1])  
        self.draw_snake()

    def s_movement(self):
        x, y = self.body[0]
        if self.heading == directions["E"]:
            x += self.step_size
        elif self.heading == directions["W"]:
            x -= self.step_size
        elif self.heading == directions["N"]:
            y += self.step_size
        elif self.heading == directions["S"]:
            y -= self.step_size

        new_head = (x, y)
        self.body = [new_head] + self.body[:-1]
        self.draw_snake()

    def move_w_key(self):
        if self.heading in [directions["E"], directions["W"]]:
            self.heading = directions["N"]
            self.change_dir = True

    def move_d_key(self):
        if self.heading in [directions["N"], directions["S"]]:
            self.heading = directions["E"]
            self.change_dir = True

    def move_s_key(self):
        if self.heading in [directions["E"], directions["W"]]:
            self.heading = directions["S"]
            self.change_dir = True

    def move_a_key(self):
        if self.heading in [directions["N"], directions["S"]]:
            self.heading = directions["W"]
            self.change_dir = True

    def check_if_touch_the_walls(self):
        x, y = self.body[0]
        return abs(x) >= game_area or abs(y) >= game_area

    def level_up(self):
        if self.apples == self.make_harder_at:
            if self.base_speed < 10:
                self.base_speed += 2
            self.tail_extra += 1
            self.make_harder_at += 3

    def check_if_head_touch_body(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if abs(head[0] - segment[0]) < 10 and abs(head[1] - segment[1]) < 10:
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
    screen.textinput(prompt=f"{player_name} , your score is {score} ", title="Results")

def register():
    global player_name
    player_name = screen.textinput(prompt="Welcome to my Snake Game\nInsert your name:", title="Register")
    while player_name == "":
        player_name = screen.textinput(prompt="Not a valid name!\nPlease insert your name:", title="Invalid Input")


player_name = None
s = Snake()
s.draw_snake()
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

    if a.is_eaten(s.body[0]):
        print(f"apple is eaten in location ({a.x},{a.y})")
        a.remove_from_board()
        s.update_snake()
        s_board.update_score(s.apples)
        a = Apple()

    if s.check_if_touch_the_walls():
        game_over(s.apples)

    s.level_up()
    s.check_if_head_touch_body()

    screen.listen()
    screen.onkey(key="w", fun=s.move_w_key)
    screen.onkey(key="d", fun=s.move_d_key)
    screen.onkey(key="s", fun=s.move_s_key)
    screen.onkey(key="a", fun=s.move_a_key)
    screen.onkey(key="q", fun=pause_game)

    time.sleep(0.1)

screen.exitonclick()