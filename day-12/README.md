# Day 12 - 100 Days of Code - Python 🚀

## **📌 Today's Topics**
### **Scope & Global Variables**
Understanding how Python manages variable scope and how global variables behave inside functions.

#### **Namespaces & Scope** 📍
- **Global Scope** 🌍: Variables defined at the top level of a script, accessible by all functions.
- **Local Scope** 🔒: Variables created inside functions, accessible only within that function.
- **Modifying Global Variables** ⚠️: Using the `global` keyword inside a function allows modifying a global variable.
- **Constants** 🔢: Global constants (e.g., `PI = 3.14`) remain unchanged throughout the program.

#### **Example Code from Today's Lesson** 📝
```python
limit = 3
name = "Itay"

def func1(in_name):
    limit1 = 4
    for i in range(limit1):
        print(f"{i+1}-{in_name}, this is my name!")

def func2(in_name):
    limit2 = 5
    for i in range(limit2):
        print(f"{i+1}-{in_name}, this is my name!")

def func3(in_name):
    limit = 7  # Local variable shadows global 'limit'
    for i in range(limit):
        print(f"{i+1}-{in_name}, this is my name!")

func1(name)
func2(name)
func3(name)
```

### **🏗️ Project of the Day - Number Guessing Game 🎮**
A CLI-based game where the player has to guess a secret number between 1 and 100 within a limited number of attempts.

#### **How It Works?** 🔢
1. The player selects a difficulty level:
   - **Easy**: 10 attempts
   - **Hard**: 5 attempts
2. The game generates a random secret number.
3. The player enters guesses, receiving hints if their guess is too high or too low.
4. The game tracks remaining attempts and announces the result.

#### **Concepts Used from Today's Lesson** 🎯
✅ **Global Variables**: `attempts`, `difficulty`, `secret_number`, and flags like `game_flag`  
✅ **Functions**:
   - `set_difficulty()` → Changes game difficulty.
   - `set_attempts()` → Adjusts attempts based on difficulty.
   - `new_num_to_guess()` → Generates a random number.
   - `check_if_correct(guess)` → Compares the guess with the secret number.
✅ **Conditionals & Loops**: Game runs in a loop until the player wins or loses.

#### **Example Code Snippet** 📜
```python
def check_if_correct(guess):
    global guess_is, attempts, round_flag
    
    if guess == secret_number:
        guess_is = f"Correct! The number is {secret_number} - well done!"
        round_flag = False
    elif guess < secret_number:
        guess_is = "Too low.. Try again!"
    else:
        guess_is = "Too high.. Try again!"
    
    attempts -= 1
    check_if_lose()
```

### **🎨 ASCII Art Title** (From `art.py`)
```python
print(guess_the_number)
```

## **📂 Files in This Project**
- `main.py` → Theory and practice about Scope & Global Variables.
- `daily_project.py` → The Number Guessing Game.
- `art.py` → ASCII art used in the project.

---
### **💡 Summary & Key Takeaways**
- **Understanding Scope** is essential for managing variables correctly.
- **Global Variables** should be used carefully to avoid unexpected behavior.
- **Project Integration**: The Number Guessing Game effectively applies these concepts.

🛠️ Keep coding, and see you in Day 13! 🚀
