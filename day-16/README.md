# Day 16 - Object-Oriented Programming (OOP) in Python 🚀

## 📌 Overview
Today, we dive into the world of **Object-Oriented Programming (OOP)** in Python! Until now, all projects in this course were written using **Procedural Programming**, but as programs become more complex, **OOP provides better structure, reusability, and maintainability**.

In this lesson, we implemented an **OOP-based Coffee Machine** using classes and objects. ☕

## 🏗️ What is OOP?
OOP is a programming paradigm based on the concept of **objects**. Each object:
- Has **attributes** (data/properties that describe it)
- Has **methods** (functions that define its behavior)
- Belongs to a **class**, which acts as a blueprint

For example, a **human** object might have:
- **Attributes**: name, age, height, eye color
- **Methods**: sleep(), eat(), work()

OOP allows **code reuse** by creating multiple objects from a single class, improving **scalability and readability**.

## 📜 Key OOP Concepts
### ✅ Classes & Objects
- A **class** is a blueprint for creating objects.
- An **object** is an instance of a class.
- Syntax:
  ```python
  class Animal:
      def __init__(self, name, species):
          self.name = name
          self.species = species

      def make_sound(self):
          print("Animal sound!")
  
  dog = Animal("Buddy", "Dog")  # Creating an object
  ```

### ✅ Encapsulation
- Bundling **data and methods** inside a class to protect it from unintended modification.

### ✅ Inheritance
- Allows a class to **inherit** attributes and methods from another class, promoting **code reuse**.

### ✅ Polymorphism
- Enables different classes to share the **same method name** but behave differently.

---

## ☕ Project: OOP-Based Coffee Machine
We refactored our **Coffee Machine** project to use OOP principles, making it **modular and structured**.

### 🏗️ Project Structure
The project consists of the following classes:
1. **`MenuItem`** 📋 - Represents each drink option.
2. **`Menu`** 🍹 - Manages the menu and finds drinks.
3. **`CoffeeMaker`** ☕ - Handles coffee-making and resource tracking.
4. **`MoneyMachine`** 💰 - Manages transactions.

### 📝 Implementation
#### `main_CM.py` (Main Program)
- Uses **objects** from the classes to create a functioning coffee machine.
- Displays a **report** of resources and earnings.
- Handles **user input** for ordering drinks.
- Ensures **sufficient resources and payment** before making a coffee.

#### Example Flow:
```
****** Report ******
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
******  END  ******

Hey, Welcome to the Coffee Machine!
I can make for you one of these: latte/espresso/cappuccino
Please type your order:
>> espresso
Processing payment...
Here is your espresso ☕️. Enjoy!
```

---

## 🔥 What We Learned
✅ The benefits of **OOP** over procedural programming.  
✅ How to create and use **classes and objects**.  
✅ How to apply **Encapsulation, Inheritance, and Polymorphism**.  
✅ How **OOP improves code organization** in large projects.  

Next, we will **deepen our understanding of OOP**, including how to build and extend our own classes! 🚀
