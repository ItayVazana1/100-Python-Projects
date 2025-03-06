
# 🌀 Lost in a Maze - Problem and Solution Explanation 🧩

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
