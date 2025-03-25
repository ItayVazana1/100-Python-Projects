# Day 19 - Etch-A-Sketch (using Turtle)

import os
import random
import time
import datetime
from turtle import Turtle, Screen
import pyautogui
import pygetwindow as gw


WIN_TITLE = "Etch-A-Sketch"
brush = Turtle()
screen = Screen()
screen.title(WIN_TITLE)

# key mapping :
# 'W' = Forwards
# 'S' = Backwards
# 'A' = Rotate brush left (Counter-Clockwise)
# 'D' = Rotate brush right (Clockwise)
# 'C' = Change color randomly
# 'N' = start new draw (restart screen and turtle position)
# 'P' = Save the draw to picture in .png format


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
        os.makedirs('EAS_Gallery', exist_ok=True)
        filename = f"EAS_Gallery/Output_{now}.png"

        screenshot.save(filename)
        print(f"📸 Screenshot saved as {filename}")

    except Exception as e:
        print(f"❌ Error capturing turtle window: {e}")



def move_forwards():
    brush.forward(10)

def move_backwards():
    brush.backward(10)

def rotate_left():
    current = brush.heading()
    brush.seth(current + 10)

def rotate_right():
    current = brush.heading()
    brush.seth(current - 10)

def change_color():
    colors = [(0, 0, 0), (255, 0, 0), (1, 156, 1), (69, 49, 246), (228, 37, 164), (21, 95, 206), (255, 128, 0)]
    new_c = random.choice(colors)
    brush.color(new_c)

def start_new_draw():
    brush.clear()
    brush.pu()
    brush.home()
    brush.pd()


brush.pensize(3)
brush.shapesize(3)
screen.colormode(255)
screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=rotate_left)
screen.onkeypress(key='d', fun=rotate_right)
screen.onkey(key='c', fun=change_color)
screen.onkey(key='n', fun=start_new_draw)
screen.onkey(key='p', fun=screenshot_turtle_window)


screen.exitonclick()
