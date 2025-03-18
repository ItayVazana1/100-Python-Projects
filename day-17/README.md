# Day 17 - Object-Oriented Programming (OOP) in Python 🚀

## 📌 Overview  
Today, we continued our journey into **Object-Oriented Programming (OOP)** by applying it to a fun and interactive **QUIZ Game**! We explored how to create and use **classes**, manage **attributes and methods**, and implement **game logic** using OOP principles.

In this lesson, we built a **True/False quiz game** where players answer randomized questions while tracking their score and lives. 🎮

---

## 🏗️ What is OOP?  
**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into objects. Each object:  
- **Has attributes** (data/properties describing it)  
- **Has methods** (functions that define its behavior)  
- **Belongs to a class**, which acts as a blueprint  

For example, a `Car` object might have:  
- **Attributes:** `brand`, `model`, `color`  
- **Methods:** `drive()`, `brake()`, `honk()`  

OOP allows us to **reuse code**, making projects **scalable and maintainable**.

---

## 📜 Key OOP Concepts  
✅ **Classes & Objects**  
A **class** is a template for creating objects.  
An **object** is an instance of a class.  

### **Syntax Example:**  
```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def show(self):
        print(self.text)
```
`q1 = Question("Is the Earth round?", True)  # Creating an object`

✅ **Encapsulation**  
Bundling data and methods inside a class to **protect** it from unintended modifications.

✅ **Game Logic in OOP**  
We used **OOP principles** to design the quiz game, making it structured and reusable.

---

## 🎮 **Project: OOP-Based QUIZ Game**
We built a **True/False quiz game** using **Python classes and objects**.  

### 🏗️ Project Structure  
The game consists of the following classes:

- **`Question` 📜** - Represents each quiz question.
- **`Player` 🏆** - Tracks the player’s **score** and **lives**.
- **Main Game Logic 🎲** - Runs the game, handles user input, and updates the player's stats.

### 📝 **Implementation**
📂 **Files in the project:**
- `daily_project.py` - Contains game logic, `Question` and `Player` classes.
- `data_base.py` - Stores a **bank of True/False questions**.
- `main.py` - Introduction to **OOP concepts**.

### 🎯 **Game Flow**
1️⃣ The game starts by **asking for the player's name**.  
2️⃣ **Random True/False questions** appear one by one.  
3️⃣ The player **chooses an answer** (`True` or `False`).  
4️⃣ If the answer is **correct**, the score **increases**.  
5️⃣ If the answer is **wrong**, the player **loses a life**.  
6️⃣ The game **ends when the player runs out of lives** or **chooses to quit**.

### 📌 **Example Output**
```
Welcome to the QUIZ Game! 🎮
Insert your name:
>> Alex
And the game begins!
----------------------------------------------------
#1# - The sky is blue.
True or False?
>> true
Correct! ✅
Score: 1
You have 5 lives remaining.

Type 'Q' to quit or any key for the next question...
```

---

## 🔥 **What We Learned**
✅ **How to create and use classes and objects.**  
✅ **How to manage object attributes and methods.**  
✅ **How to apply Encapsulation in game logic.**  
✅ **How to structure a game using OOP.**  
✅ **The benefits of OOP over procedural programming.**  

Next, we will continue exploring **OOP principles** by extending our knowledge with **Inheritance and Polymorphism**! 🚀
