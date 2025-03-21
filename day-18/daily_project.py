# Day 18 - Hirst Painting Project

# Modules and tools importing

import os
import random
import time
import datetime
import pyautogui
import pygetwindow as gw
from turtle import Turtle, Screen
from colorgram import colorgram as cg
from ASCII_Art import logo

# Global variables

raw_colors = []
color_palette = []
number_of_colors = [6, 5, 5, 6, 6]
color_format = 255
screen_dim = 700
dot_size = 20
drawing_flag = True
gap = 50
directions = ["right", "left", "up"]
positive_len_from_center = screen_dim / 2
negative_len_from_center = -1 * positive_len_from_center
left_wall = negative_len_from_center + gap
right_wall = positive_len_from_center - gap
initial_xy = left_wall
destination_xy = right_wall
current_direction = directions[0]
move_right = gap
move_left = -1 * gap
WIN_TITLE = "Hirst Painting - Python & Turtle Project"

# Color management functions
def extract_colors(image_path, number):

    global raw_colors
    ex_out = cg.extract(image_path,number)
    for sample in ex_out:
        raw_colors.append(sample)


def store_as_tuples():
    global raw_colors
    for c in raw_colors:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        color_tuple = (r, g, b)
        color_palette.append(color_tuple)


def remove_edges_colors():

    print(f"Color count before filter : {len(color_palette)}")
    white_threshold = 225
    black_threshold = 20
    for rgb_comb in color_palette:
        rgb_values = [rgb_comb[0], rgb_comb[1], rgb_comb[2]]
        if rgb_values[0] < black_threshold and rgb_values[1] < black_threshold and rgb_values[2] < black_threshold:
            color_palette.remove(rgb_comb)
            print(f"Dropped color -> {rgb_comb} - almost black")
        elif rgb_values[0] > white_threshold and rgb_values[1] > white_threshold and rgb_values[2] > white_threshold:
            color_palette.remove(rgb_comb)
            print(f"Dropped color -> {rgb_comb} - almost white")
    print(f"Color count after filter : {len(color_palette)}")


# Setup functions

def set_color_palette():

    for i in range(1, 5):
        img_path = f"Color_Schemes/scheme_{i}.png"
        color_count = number_of_colors[i-1]
        extract_colors(image_path=img_path, number=color_count)

    store_as_tuples()
    remove_edges_colors()

def setup_turtle():
    tom.hideturtle()
    tom.pu()
    tom.clear()
    tom.speed("fastest")
    tom.teleport(initial_xy,initial_xy)

def setup_screen():
    screen.setup(width=screen_dim,height=screen_dim)
    screen.colormode(color_format)
    screen.title(WIN_TITLE)


# Drawing and program flow functions

def draw_dot():
    dot_color = random.choice(color_palette)
    tom.dot(dot_size, dot_color)


def is_blocked():
    global current_direction
    x_val = tom.xcor()
    if (x_val == right_wall and current_direction == "right") or (x_val == left_wall and current_direction == "left"):
        current_direction = directions[2]


def move_up():
    global current_direction
    x_val = tom.xcor()
    if x_val == right_wall:
        current_direction = directions[1]
    elif x_val == left_wall:
        current_direction = directions[0]


def move_to_next_location():
    x_val = tom.xcor()
    y_val = tom.ycor()
    if current_direction == "right":
        x_val += move_right
    elif current_direction == "left":
        x_val += move_left
    elif current_direction == "up":
        move_up()
        y_val += gap
    tom.setposition(x_val, y_val)


def is_in_destination():
    global drawing_flag
    x_val = tom.xcor()
    y_val = tom.ycor()
    if x_val == y_val == destination_xy:
        drawing_flag = False


# Bonus function - saving the draw in specific folder (using screenshot)

def screenshot_turtle_window(window_title_part=WIN_TITLE, canvas_offset_top=30, border_offset=8):

    time.sleep(1)

    try:
        windows = gw.getWindowsWithTitle(window_title_part)
        if not windows:
            print("❌ Turtle window not found.")
            return

        win = windows[0]
        if win.isMinimized:
            win.restore()

        left, top, width, height = win.left, win.top, win.width, win.height

        canvas_left = left + border_offset
        canvas_top = top + canvas_offset_top
        canvas_width = width - 2 * border_offset
        canvas_height = height - canvas_offset_top - border_offset

        screenshot = pyautogui.screenshot(region=(canvas_left, canvas_top, canvas_width, canvas_height))

        now = datetime.datetime.now().strftime("Date-[%Y-%m-%d]_Time-[%H-%M-%S]")
        os.makedirs('Gallery', exist_ok=True)
        filename = f"Gallery/Output_{now}.png"

        screenshot.save(filename)
        print(f"📸 Screenshot saved as {filename}")

    except Exception as e:
        print(f"❌ Error capturing turtle window: {e}")


# Main program

print(logo)
print("--------------------------------")
print("Setup the color palette...")
print("--------------------------------")
time.sleep(0.5)
set_color_palette()
print("--------------------------------")
print("Setup Turtle tools and window...")
print("--------------------------------")
tom = Turtle()
screen = Screen()
setup_turtle()
setup_screen()
time.sleep(0.5)
print("--------------------------------")
print("------ D r a w i n g . . . ----- ")
print("--------------------------------")
while drawing_flag:

    is_in_destination()
    draw_dot()
    move_to_next_location()
    is_blocked()

print("--------------------------------")
print("------ S a v i n g  . . . ----- ")
print("--------------------------------")
screenshot_turtle_window()
print("--------------------------------")
print("------ Click to Close ... ----- ")
print("--------------------------------")
screen.exitonclick()
