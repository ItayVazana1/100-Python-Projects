import random
from turtle import Turtle, Screen


gap = 75
screen_height = 600
screen_width = 800
start_line_x = -1 * ((screen_width/2) - gap)
first_route_cor = -275
finish_line = 340
comp_turtles = []
screen = Screen()
screen.colormode(255)
screen.setup(width=screen_width, height=screen_height)


t_names = ["Tim", "Tranx", "Tomi", "Tate", "Truman", "Tramp"]
t_color_names = ["Red", "Green", "Blue", "Orange", "Purple", "Pink"]
t_color_rgb = [
    (255, 0, 0),      # Red
    (0, 128, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 192, 203)   # Pink
]


class CompTurtle:
    def __init__(self, name, color_name, color, loc):
        self.name = name
        self.color_name = color_name
        self.t = Turtle()
        self.t.pu()
        self.t.color(color)
        self.t.shape("turtle")
        self.t.shapesize(2)
        self.t.setx(start_line_x)
        self.t.sety(first_route_cor + (gap * loc))
        self.t.speed(random.randint(5, 8))
        self.t_name = Turtle()
        self.t_name.pu()
        self.t_name.hideturtle()
        self.t_name.color("black")
        self.set_label_position()

    def set_label_position(self):
        self.t_name.clear()
        x = self.t.xcor()
        y = self.t.ycor() + 25
        self.t_name.setposition(x,y)
        self.t_name.write(f"{self.name}", move=False, font=("Calibri", 10, "bold"))


    def create_name_label(self):
        name_label = Turtle()
        name_label.pu()
        name_label.hideturtle()
        name_label.color("black")
        self.set_label_position()
        return name_label


    def move_forwards(self):
        if random.randint(0, 10) in [3, 6, 9]:
            self.t.speed(random.randint(5, 8))
        self.t.clear()
        step_distance = random.randint(5, 20)
        current_position = self.t.xcor()
        self.t.setx(current_position + step_distance)
        self.set_label_position()

    def check_if_win(self):
        current_x = self.t.xcor()
        if current_x >= finish_line-40:
            return True
        else:
            return False

    def winner(self):
        print("*************************************")
        print(f"The Winner is ...\n{self.name} ({self.color_name}) !!")
        print("*************************************")
        return self.name


def set_comp_turtles():
    global comp_turtles
    for i in range(6):
        new_turtle = CompTurtle(name=t_names[i], color_name=t_color_names[i], color=t_color_rgb[i], loc=i+1)
        comp_turtles.append(new_turtle)


def create_drawer_turtle():
    new_dt = Turtle()
    new_dt.hideturtle()
    new_dt.pu()
    new_dt.speed("fastest")
    new_dt.pensize(3)
    return new_dt

def draw_start_and_finish_lines():
    dt = create_drawer_turtle()
    x = -340
    y = -275
    dt.setposition(x,y)
    dt.pd()
    y = y * (-1)
    dt.goto(x, y)
    dt.pencolor("green")
    dt.write("Start line",False, align="left", font=("Calibri", 14, "bold"))
    dt.pencolor("black")
    dt.pu()
    x = x * (-1)
    y = y * (-1)
    dt.setposition(x, y)
    dt.pd()
    y = y * (-1)
    dt.goto(x, y)
    dt.pencolor("red")
    dt.write("Finish line",False, align="right", font=("Calibri", 14, "bold"))

def bet_on_winner():
    i = 1
    print("Choose your winner Turtle:")
    for comp_t in comp_turtles:
        print(f"{i} - {comp_t.name} - ({comp_t.color_name})")
    bet_name = input("\n(Insert the name of the turtle):\n")
    while bet_name not in t_names:
        print("You must choose a valid name!")
        bet_name = input("\n(Insert the name of the turtle):\n")
    return bet_name

def the_leader_is():

    leader = None
    leader_position = start_line_x
    for com_t in comp_turtles:
        if leader_position < com_t.t.xcor():
            leader_position = com_t.t.xcor()
            leader = com_t.name

    print(f"current leader - {leader}")


draw_start_and_finish_lines()
set_comp_turtles()
bet = bet_on_winner()
winner = ""
finish_flag = True

while finish_flag:

    for ct in comp_turtles:
        ct.move_forwards()
        if ct.check_if_win():
            finish_flag = False
            winner = ct.winner()
            break

    the_leader_is()

if bet == winner:
    print("\nYour Turtle is the winner - well done!")
else:
    print("\nYou lose.. maybe next time :) ")

screen.exitonclick()
