
# 🚀 Day 3 - 100 Days of Code - Python

## 🔎 Overview
Welcome to **Day 3** of my **100 Days of Code - Python** journey!  
Today's focus was all about **conditions, logical operators, and nested decision-making**.  
I also built a fun **Treasure Hunt Game** project! 🏝️💰

---

## 📚 Topics Covered

### ✅ Conditions in Python
Python allows us to control program flow using **conditions**.
| Statement | Description |
|---|---|
| **if** | Run code block if condition is `True`. |
| **else** | Run code block if condition is `False`. |
| **elif** | Additional condition check if previous conditions were `False`. |

Example:
```python
if name == "Itay":
    print("Welcome Itay!")
elif name == "Max":
    print("Hello Max!")
else:
    print("I don't know you.")
```

---

### 🔗 Logical Operators
| Operator | Description | Example |
|---|---|---|
| **and** | All conditions must be `True` | `if a > 5 and b < 10:` |
| **or** | At least one condition must be `True` | `if a > 5 or b < 2:` |
| **not** | Reverse the condition | `if not is_logged_in:` |

---

### ➗ The Modulo Operator
The modulo operator (`%`) gives the **remainder** after division.

```python
print(5 % 3)  # 2 (since 5 divided by 3 leaves remainder 2)
```

Real-life example:
If you have 5 apples and want to distribute them equally into 3 baskets, 2 apples will be left out.

---

### 🧩 Nested Conditions
Conditions can be **nested** inside each other to handle more complex logic.

Example:
```python
if name == "Itay":
    if age < 18:
        print("You're a teenager!")
    else:
        print("You're an adult!")
```

---

### 🍕 Mini Project - Pizza Ordering System
I created a small **Pizza Ordering System** where users:
1. Choose a pizza size (S/M/L).
2. Add optional toppings (regular or special).
3. Receive a **final bill** based on their choices.

| Size | Price |
|---|---|
| **S** | $7.5 |
| **M** | $10 |
| **L** | $12 |

| Topping Type | Price |
|---|---|
| **Regular** | +$0.5 |
| **Special** | +$1.5 |

Example Flow:
```
Choose size (S/M/L): M
Add regular topping? (Y/N): Y
Total: $10.5
```

---

## 🎮 Daily Project - Treasure Hunt Game 🏝️

### 📖 Storyline
In this interactive **text-based adventure**, the player goes on a treasure hunt, facing challenges and making choices along the way.  
Only the right sequence of decisions leads to the hidden treasure! 💰

### 🚀 Gameplay Flow
1. Choose how to get to the beach (✈️ Plane, 🚗 Car, 🚶 Walking).
2. Pick a direction at the beach (➡️ Right, ⬅️ Left).
3. Select a door (🚪 Red, 🟨 Yellow, 🔵 Blue).

### Example Code
```python
print("Welcome to the Treasure Hunt!")
name = input("What's your name? ")
print(f"Good luck, {name}!")
```

### ⚠️ What Can Go Wrong?
| Choice | Outcome |
|---|---|
| Wrong Transport | Flat tire = Game Over 🚗💥 |
| Wrong Path | Injury = Game Over 🦵💢 |
| Wrong Door | Lions or mystery hospital = Game Over 🏥🦁 |
| Correct Door | 🎉 You Win! |

---

## 🔑 Key Takeaways
- Mastered **if / elif / else**.
- Combined multiple conditions with **and**, **or**, **not**.
- Practiced **nested conditions**.
- Applied logic in **real-life inspired projects**.

---

## 📅 Day 3 of 100
Each day brings new challenges and new knowledge! 💪

---

## 🏷️ Keywords
`if` `else` `elif` `nested conditions` `modulo` `%` `logical operators` `and` `or` `not`

---