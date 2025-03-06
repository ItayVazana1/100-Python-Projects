
# 📅 Day 6 - 100 Days of Code - Python

## 🏁 Functions and While Loops Overview

Today focused on **functions** and **while loops** — two essential building blocks for structured and efficient Python programs.

---

## 🧰 Functions - Custom Code Blocks

### What is a Function?
A **function** is a reusable block of code that can be called by name whenever needed.

### Examples
We already used built-in functions like:
- `print()`
- `len()`
- `input()`

But Python also allows us to **define our own functions** using the `def` keyword.

```python
def my_function():
    print("Hello world!")

my_function()
```

### Key Benefits
- 💻 Cleaner and more organized code.
- 🔁 Reusability — call the same logic many times without rewriting it.
- 🧩 Functions can even call other functions, forming modular building blocks.

---

## 🪜 Indentation - Essential for Structure

### What is Indentation?
Indentation refers to the spaces before each line of code inside a function or loop. It defines **which lines belong together**.

Think of it like folders in a file system:

```
C
- Desktop
    - Chrome
- Pictures
    - Camera Roll
        - image.png
```

### Best Practice
- 🟰 Use **spaces** instead of tabs to ensure consistent indentation.
- 🚨 Incorrect indentation leads to `IndentationError`.

---

## 🔄 While Loops - Dynamic Repetition

### What is a While Loop?
A `while` loop repeats a block of code **as long as a condition is true**. 

### Example
```python
num = 10

while num != 0:
    print(f"Number is {num}")
    num -= 1
```

### Key Difference from For Loops
- ✅ `for` loops iterate a fixed number of times.
- 🔄 `while` loops repeat **based on conditions**.

### ⚠️ Be Careful!
- Always make sure the condition can **become false**, or you risk an **infinite loop**.
- Use `print()` statements to debug loop progress if needed.

---

# 🌀 Day 6 Project - Lost in a Maze 🧩

## 📖 Problem Description
Reeborg, a robot, is trapped in a dark maze and must find the exit. Due to the darkness, Reeborg can only sense walls immediately around it. The robot must navigate the maze using a strategy that allows it to consistently find its way out.

### ✅ Requirements
- Use a `while` loop to keep the robot moving until it reaches the goal.
- Use `if/elif/else` conditions to check surroundings and make decisions.
- The robot can detect:
    - 🧱 Whether there is a wall directly in front (`front_is_clear()`).
    - 🧱 Whether there is a wall to its right (`right_is_clear()` or `wall_on_right()`).
    - 🎯 Whether it has reached the goal (`at_goal()`).

### 🚀 Allowed Actions
- 🐾 Move forward (`move()`).
- ↪️ Turn left (`turn_left()`).

---

## 💡 Conceptual Solution - Right-Hand Rule ✋

### What is the Right-Hand Rule?
🧭 The core concept to solving this maze is **the "Right-Hand Rule"**, a well-known maze-solving algorithm.

### Explanation
- 🤖 The robot keeps its **right side touching a wall** at all times.
- 📐 Whenever the robot detects an **opening to the right**, it turns right and moves into the open space.
- ➡️ If the path ahead is clear but there’s no opening to the right, the robot moves forward, staying close to the wall.
- ⛔ If the robot is blocked ahead and to the right, it turns left, maintaining contact with the wall.

This strategy works in mazes that are **fully connected** (no isolated sections) and guarantees that the robot will eventually find the exit if there is one. 🏁

---

## 🐍 Python Code Implementation

```python
def turn_right():
    for i in range(3):
        turn_left()

def find_first_wall_in_your_direction():
    # 🚶 Move until the robot finds the first wall
    while front_is_clear():
        move()
    turn_left()  # Start following the wall on the right

# 🔍 Initial setup: Find the first wall to start wall-following
find_first_wall_in_your_direction()

# 🔄 Main loop: Keep moving until the goal is reached
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

---

## 📊 Explanation of the Code

### 🧱 Step 1 - Finding the first wall
- The robot moves straight until it hits a wall.
- This ensures that the robot starts the maze-solving process with a wall to follow.

### 🧭 Step 2 - Wall-following logic
- ✔️ Check if the right side is open.
    - If yes, turn right and move into the space (keeping right side near a wall).
- ✔️ If the right side is blocked but the front is open, move forward.
- ✔️ If both right and front are blocked, turn left to stay in contact with the wall.

### 🎯 Step 3 - Goal Detection
- The loop ends as soon as the robot reaches the goal (`at_goal()`).

This structured approach ensures that the robot will always explore the maze efficiently using the **right-hand rule** technique. 🤖✅
