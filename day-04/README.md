
# 🚀 Day 4 - 100 Days of Code - Python

## 🔎 Overview
Welcome to **Day 4** of my **100 Days of Code - Python** journey!  
Today's focus was on **randomization** using Python's `random` module and working with **lists**.  
I also created a fun **Rock, Paper, Scissors Game** project! ✊📄✂️

---

## 📚 Topics Covered

### 🎲 Randomization in Python
Computers are **deterministic**, meaning they normally follow strict instructions.  
To introduce randomness, we use Python's **`random`** module, which generates **pseudo-random numbers**.

| Function | Description | Example |
|---|---|---|
| **random.randint(min, max)** | Random integer between `min` and `max` (inclusive) | `random.randint(1, 10)` |
| **random.random()** | Random float between `0` and `1` | `random.random()` |
| **random.uniform(min, max)** | Random float between `min` and `max` | `random.uniform(1, 10)` |
| **random.choice(list)** | Randomly select an item from a list | `random.choice(colors)` |

Example:
```python
import random
number = random.randint(1, 10)
print(f"Random number: {number}")
```

---

### 📦 What is a Module?
A **module** in Python is a file containing Python code (functions, classes, variables) that can be **imported** into other files.  
The `random` module is an example of a **built-in module**.

---

### 📝 Lists in Python
A **list** is a data structure that allows storing **multiple items** (strings, numbers, etc.) in an ordered sequence.

```python
colors = ["Red", "Green", "Blue"]
```

| Action | Code Example |
|---|---|
| Access item | `colors[0]` (first item) |
| Reverse access | `colors[-1]` (last item) |
| Add item | `colors.append("Yellow")` |
| Add multiple items | `colors.extend(["Purple", "Pink"])` |

---

### 🎨 Example - Color Picker
Randomly select a color from a list:
```python
colors = ["Red", "Green", "Blue"]
selected_color = random.choice(colors)
print(f"Random color: {selected_color}")
```

---

## 🕹️ Daily Project - Rock, Paper, Scissors ✊📄✂️

### 📖 Description
I built a **Rock, Paper, Scissors** game where:
- The player chooses Rock, Paper, or Scissors.
- The computer randomly chooses one option.
- After 3 rounds, the winner is announced!

### 🚀 Gameplay Flow
1. Player chooses 1 = Rock, 2 = Paper, 3 = Scissors.
2. Computer randomly chooses from the same options.
3. Game compares choices and announces the round winner.
4. After 3 rounds, the overall **winner** is announced.

### Example Code
```python
import random

options = ["Rock", "Paper", "Scissors"]
player_choice = int(input("1. Rock\n2. Paper\n3. Scissors\nChoose: ")) - 1
computer_choice = random.choice(options)

print(f"You chose: {options[player_choice]}")
print(f"Computer chose: {computer_choice}")
```

### ⚠️ Rules Summary
| Player Choice | Computer Choice | Outcome |
|---|---|---|
| Rock | Scissors | Player Wins |
| Paper | Rock | Player Wins |
| Scissors | Paper | Player Wins |
| Same | Same | Draw |

---

## 🔑 Key Takeaways
- Learned how to use the **`random` module** to generate random numbers and selections.
- Practiced working with **lists** to store, retrieve, and manipulate data.
- Combined **randomness**, **lists**, and **conditions** to build an interactive **Rock, Paper, Scissors** game.

---

## 📅 Day 4 of 100
Each day brings new challenges and new knowledge! 💪

---

## 🏷️ Keywords
`random` `randint` `choice` `list` `append` `extend` `Rock Paper Scissors`

---
