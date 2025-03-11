# 🚀 Day 10 - 100 Days of Code - Python

## 🔢 Functions with Outputs

### 🔄 Remember Functions?
We’ve already explored functions, but today, we take it a step further! Now, we will use functions to **return a value**. 🎯

The **daily project** will be a **classic calculator app**! 🧮
By the end of today, you'll have a **deeper understanding** of functions in Python. 🔥

---

### 📌 Function Basics
#### This is the function format we first met:
```python
def my_fun():
    print("print something")
```

#### Then, we learned about functions with parameters:
```python
def my_fun_with_p(param):
    print(f"print this -> {param}")
```

#### Today, we add the `return` statement! 🎉
✅ **What is `return`?**
Using `return`, we can send a value **back** to the main program.
It can be something generated inside the function, or even a **constant** value.

Example:
```python
def my_fun_with_p_and_ret(param):
    base_string = "Hello, "
    return base_string + param

print(my_fun_with_p_and_ret("Mike"))
```
✅ This will print: `Hello, Mike`

Another example:
```python
def is_cap_or_low(param):
    if str(param).islower():
        return "lower"
    else:
        return "Capital"

letter = 'a'
print(f"The letter {letter} is {is_cap_or_low(letter)}")
```

✅ We are **already familiar** with functions that return a value! Remember `len()`?
```python
len("Hello")  # Returns 5
```
📝 The `len()` function **returns** the length of the input string or structure.

---

### 🎯 Returning Multiple Values
⚡ **Important:** Any code **after** a `return` statement **will not execute**!

Example:
```python
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

years = [2000, 1580, 1440, 2100, 2025, 2024, 2010]
for item in years:
    print(f"{item} is a leap year = {is_leap_year(item)}")
```

---

### 📖 Docstrings - Documenting Functions
Use **triple quotes** `"""` to document functions! 📝
```python
def is_leap_year_doc(year):
    """
    :param year: Integer representing the year
    :return: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False
```

---

### 🔄 Nested Functions - Function Inside Function 🤯
Example:
```python
def name_to_letter(name):
    def itay(this_name):
        return "I"
    def koral(this_name):
        return "K"
    def angela(this_name):
        return "A"
    
    if name == "Itay":
        return itay(name)
    elif name == "Koral":
        return koral(name)
    elif name == "Angela":
        return angela(name)
    else:
        return 'Unknown'

my_list = ['Itay', 'Koral', 'Angela', 'Patrick']
for any_name in my_list:
    print(f"The name '{any_name}' starts with the letter [{name_to_letter(any_name)}]")
```

---

## 🎯 Day 10 Project - Calculator App 🧮

### 🔍 How Does the Project Work?
This project is a simple **calculator** that supports multiple operations:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Power (`a^b`)
- Modulo (`%`)

🔹 The **core logic** is built inside the `calc()` function, which utilizes **nested functions** to define each operation separately.
🔹 A **dictionary** is used to map each operation symbol to its corresponding function.
🔹 The program runs in a loop, allowing continuous calculations until the user chooses to exit.

### 🛠️ Python Features Used in the Project
✅ **Functions & Nested Functions** - Each operation is implemented as a separate function within `calc()`.
✅ **Dictionaries** - Used to store and retrieve operations efficiently.
✅ **Loops** - The program continues running until the user chooses to exit.
✅ **User Input Handling** - Ensuring valid inputs for numbers and operations.
✅ **Math Module** - Used for power calculations (`math.pow`).

```python
from art import logo, result_box_top, result_box_bottom
import math

print("Welcome to my calculator app!")
print(logo)

def calc(a, b, op):
    def add(fn, sn):
        return fn + sn
    
    def sub(fn, sn):
        return fn - sn
    
    def mult(fn, sn):
        return fn * sn
    
    def div(fn, sn):
        return fn / sn
    
    def itp(fn, sn):
        return math.pow(fn, sn)
    
    def mod(fn, sn):
        return fn % sn
    
    dic_list = {
        '+': add(a, b),
        '-': sub(a, b),
        '*': mult(a, b),
        '/': div(a, b),
        'a^b': itp(a, b),
        '%': mod(a, b)
    }
    
    return dic_list.get(op, "Invalid operation")

continue_flag = True

while continue_flag:
    f_number = float(input("Please insert the first number --> a = "))
    print("+ = add\n- = sub\n* = multiply\n/ = divide\na^b = a in the power of b\n% = modulo (remainder only)")
    operation = input("Insert operation symbol -->  ")
    while operation not in ['+', '-', '*', '/', 'a^b', '%']:
        print("Invalid operation symbol - try again!")
        operation = input("Insert operation symbol -->  ")
    s_number = float(input("Please insert the second number --> b = "))
    result = calc(a=f_number, b=s_number, op=operation)
    print(result_box_top)
    print(f"= {float(round(result, 3))}")
    print(result_box_bottom)
    user_ans = input("For more calculations type 'yes', otherwise 'no' - ")
    if user_ans == 'no':
        print("Thank you, and goodbye! 😊")
        continue_flag = False
```

---

Next time , we continue with more **Python magic!** 🐍✨