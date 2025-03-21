# **Day 18 - 100 Days of Code - Python 🚀**

## **📌 Today's Topics**

### **Turtle Graphics, Tuples, Color Extraction & Modular Programming**

Today's focus was on **visual programming and modular coding** using Python's **Turtle Graphics**.  
I explored **Tuples for RGB color management**, extracting color schemes, and creating a structured approach to **automated artistic design**.  
👉 **The highlight of the day** was implementing a **Hirst-style painting generator** 🖌️ using **advanced movement logic and automated color selection**.

---

## **🎥 Demo Video Available! 🎬**  
A **demo video** showcasing the project in action is available in the file:  
📁 **`Project_Demo.mp4`**

---

## **🖥️ Theory & Practice - Turtle Graphics 🐢**

The **Turtle module** allows **interactive drawing** using Python.  
By controlling a virtual "turtle", I created **dynamic patterns, event-driven movements, and artistic grids**.

### **Key Concepts Explored Today**

- ✅ Turtle Graphics Setup
- ✅ Screen Customization
- ✅ Tuples in Python
- ✅ Randomization & Art
- ✅ Event-Driven Turtle Movement
- ✅ Structured Grid Drawing

---

## **🎨 Project of the Day - Hirst Painting Generator 🖌️**

### **Inspired by Damien Hirst's Iconic Art** 🎭

The main project was a **Hirst-style painting generator** that creates **grid-based colorful dot patterns** dynamically.

### **How It Works?** 🏗️

1️⃣ Extract Colors  
2️⃣ Filter Unwanted Colors  
3️⃣ Optimized Turtle Movement  
4️⃣ Logical Grid Navigation  
5️⃣ Automated Screenshot Capture 📸

---

## **🛠️ Libraries Used in the Project**

- 🔹 **Turtle**: For drawing
- 🔹 **Colorgram**: For palette extraction
- 🔹 **Random**: For color and movement
- 🔹 **PyAutoGUI & PyGetWindow**: For screenshotting
- 🔹 **OS & Datetime**: For file management

---

## **🔹 Code Breakdown - Hirst Painting Generator 🖌️**

### **1️⃣ Extracting & Filtering Colors 🎨**

```python
import colorgram as cg

raw_colors = []
color_palette = []

def extract_colors(image_path, number):
    global raw_colors
    ex_out = cg.extract(image_path, number)
    for sample in ex_out:
        raw_colors.append(sample)

def store_as_tuples():
    global raw_colors
    for c in raw_colors:
        r, g, b = c.rgb.r, c.rgb.g, c.rgb.b
        color_palette.append((r, g, b))
```

---

### **2️⃣ Setting Up the Turtle & Screen 🐢**

```python
from turtle import Turtle, Screen

tom = Turtle()
tom.hideturtle()
tom.penup()
tom.speed("fastest")

screen = Screen()
screen.setup(width=700, height=700)
screen.colormode(255)
screen.title("Hirst Painting - Python & Turtle Project")
```

---

### **3️⃣ Optimized Grid-Based Dot Placement 🔵**

```python
import random

grid_size = 700
gap = 50
dot_size = 20

directions = ["right", "left", "up"]
current_direction = directions[0]

positive_len_from_center = grid_size / 2
negative_len_from_center = -1 * positive_len_from_center
left_wall = negative_len_from_center + gap
right_wall = positive_len_from_center - gap
initial_xy = left_wall
destination_xy = right_wall

tom.setposition(initial_xy, initial_xy)

def draw_dot():
    tom.dot(dot_size, random.choice(color_palette))

def move_to_next_location():
    global current_direction
    x_val, y_val = tom.xcor(), tom.ycor()

    if current_direction == "right":
        x_val += gap
    elif current_direction == "left":
        x_val -= gap
    elif current_direction == "up":
        y_val += gap
        current_direction = "left" if tom.xcor() == right_wall else "right"

    tom.setposition(x_val, y_val)

while tom.ycor() < positive_len_from_center:
    draw_dot()
    move_to_next_location()
```

---

### **4️⃣ Screenshot Capture - Saving the Artwork 📸**

```python
import pyautogui
import pygetwindow as gw
import os
import datetime
import time

WIN_TITLE = "Hirst Painting - Python & Turtle Project"

def screenshot_turtle_window():
    time.sleep(1)
    try:
        windows = gw.getWindowsWithTitle(WIN_TITLE)
        if not windows:
            print("❌ Turtle window not found.")
            return

        win = windows[0]
        left, top, width, height = win.left, win.top, win.width, win.height
        screenshot = pyautogui.screenshot(region=(left, top, width, height))

        now = datetime.datetime.now().strftime("Date-[%Y-%m-%d]_Time-[%H-%M-%S]")
        os.makedirs('Gallery', exist_ok=True)
        filename = f"Gallery/Output_{now}.png"

        screenshot.save(filename)
        print(f"📸 Screenshot saved as {filename}")

    except Exception as e:
        print(f"❌ Error capturing turtle window: {e}")
```

---

## **📂 Files in This Project**

- 📌 `main.py` → Turtle Graphics, Tuples & Movement
- 📌 `daily_project.py` → Hirst Painting Generator
- 📌 `ASCII_Art.py` → ASCII logo
- 📌 `Project_Demo.mp4` → 🎥 Demo video of the project

---

## **💡 Summary & Key Takeaways**

- 🎨 Turtle Graphics for visual creativity
- 🎯 Tuples for RGB color handling
- 🔄 Structured logic for efficient grid navigation
- 📸 Screenshot capture to preserve the result

🚀 **See you on Day 19!**