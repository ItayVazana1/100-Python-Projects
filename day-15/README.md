# **Day 15 - 100 Days of Code - Python ☕**

## **📌 Today's Focus**
Today, we transitioned from the **Beginner level** to the **Intermediate level**! 🚀  
The main project of the day: **Coffee Machine Simulation**.

## **☕ Coffee Machine Project**
This project simulates a **real-life coffee vending machine** that can process orders, handle payments, and manage ingredients dynamically.

### **👨‍💻 How Does It Work?**
1. The machine **displays a menu** with available coffee options (Espresso, Latte, Cappuccino).  
2. The user **selects a drink**, and the machine checks if there are enough ingredients to make it. 🥛 + ☕ + 💧  
3. The machine **requests payment** 💰. If the user inserts **insufficient coins**, the transaction is canceled.  
4. If the payment is **successful**, the machine prepares the coffee and calculates any necessary **change**.  
5. After each order, **the ingredient levels are updated**. If an ingredient is too low, the machine notifies that a refill is needed.  

### **💡 Features & Functionalities**
✅ **1. Machine Report System** 📊  
   - Displays the **remaining amounts of ingredients**.  
   - Shows the **total money collected** in the machine.  
   - Identifies which ingredients are **running low**.  

✅ **2. Resource Management System** 🔄  
   - Keeps track of **water, milk, and coffee** levels.  
   - Ensures that orders cannot be processed if an ingredient is missing.  
   - Marks ingredients as **"Need to Refill"** if they drop below a minimum threshold.  

✅ **3. Payment Handling System** 💵  
   - Supports **four types of coins** (Penny, Nickel, Dime, Quarter).  
   - Calculates **if the payment is sufficient** for the selected drink.  
   - Returns **the correct amount of change** when necessary.  
   - If the payment is **too low**, the money is refunded.  

✅ **4. Interactive Menu & Admin Options** ⚙️  
   - Users can type **'sys'** to enter the **technical menu**, where they can:  
     - **View a Machine Report** 📋  
     - **Refill Ingredients** 🚰  
     - **Collect Money** from the machine 💰  
     - **Reboot the Machine** 🔄  
     - **Turn Off the Machine** 🔌  
   - Any invalid input is handled gracefully with error messages.  

✅ **5. Fun Visuals with ASCII Art** 🎨  
   - The machine has cool **ASCII animations** for:  
     - Starting the machine 🚀  
     - Processing an order ☕  
     - Rebooting or shutting down 🔄  

---

## **📂 Project Files**
- **`main.py`** → The main entry point for running the program.  
- **`coffe_machine.py`** → Contains the core logic that processes user input.  
- **`machine_functions.py`** → Handles machine operations, transactions, and order processing.  
- **`menu_and_resources.py`** → Defines the menu items, their ingredients, and available coin denominations.  
- **`art.py`** → ASCII art for a better user experience. 🎭  

---

## **🎨 ASCII Art Example**
```python
print(start_machine)
```
✨ Cool animations for starting, rebooting, and shutting down the machine!  

---

## **🛠️ Code Snippet: Checking if Payment is Sufficient**
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
This ensures that the **player's guess is validated**, and **attempts are tracked** correctly.  

---

## **💡 Key Takeaways**
- **Intermediate-Level Python**: Implementing modular programming for real-world applications.  
- **Resource & Inventory Management**: Tracking and updating dynamic resources.  
- **Coin Transactions & Change Calculation**: Handling financial logic programmatically.  
- **Interactive UI via CLI**: Making the console-based program feel engaging and responsive.  

---

## **🚀 Final Thoughts**
This project was **super fun to build** and taught many **real-world software engineering skills**! 💪  
The structured approach, combining **functions, data management, and user interactions**, makes this **a great stepping stone** for more complex projects.  

🔜 See you in **Day 16**! 🚀  
