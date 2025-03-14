# Day 13 - 100 Days of Code - Python 🐍

## **🔍 Debugging - Finding & Fixing Bugs!**
Today, we focused on **debugging** – a crucial skill for every programmer. Debugging helps us find and fix errors, making our code more reliable and efficient.

😢 **No project today, but important concepts were covered!**

---

## **🐛 What is Debugging?**
- Debugging is the process of identifying and resolving bugs in the code.
- Bugs can be syntax errors, logical mistakes, or unexpected behavior.
- Fun Fact: Grace Hopper discovered the first documented "bug" – an actual moth stuck in a computer! 🦋

---

## **🛠️ Debugging Tips & Techniques**

### **1️⃣ Describe the Problem Clearly**
- Understand what the code is supposed to do.
- Identify where the issue might be occurring.
- Example:
  ```python
  def my_func1():
      for i in range(1, 20):
          if i == 20:
              print("You got it!")

  my_func1()
  ```
  **Bug:** The condition `i == 20` is never met because `range(1, 20)` stops at 19. 
  **Fix:** Adjust the range to include 20:
  ```python
  def my_func1_fixed():
      for i in range(1, 21):  # Now includes 20
          if i == 20:
              print("You got it!")

  my_func1_fixed()
  ```

---

## **🎯 10 Essential Debugging Tips**

### **1️⃣ Describe the Problem Clearly**
Break the issue into small parts and describe exactly what is wrong.

### **2️⃣ Reproduce the Bug**
Some bugs only appear under certain conditions. Try different inputs to see when the bug occurs.

### **3️⃣ Print Statements are Your Best Friend 🖨️**
Use `print()` to track variable values and execution flow.
```python
print(f"Current value of x: {x}")
```

### **4️⃣ Play Computer 🤓**
Go through the code line by line, as if you were the Python interpreter.

### **5️⃣ Read Error Messages Carefully**
The error message often tells you exactly what went wrong and where.

### **6️⃣ Google & Stack Overflow Are Lifesavers 🔎**
Look up error messages and similar issues online.

### **7️⃣ Use a Debugger 🛠️**
A built-in debugger lets you step through code, inspect variables, and find issues faster.

### **8️⃣ Take a Break ☕**
Sometimes, stepping away from the screen for a while helps you see the problem clearly.

### **9️⃣ Ask a Friend 👥**
A fresh set of eyes can quickly spot mistakes you might have missed.

### **🔟 Test Often, Test Early**
Run your code frequently, rather than waiting until you write large chunks.

---

## **💡 Key Takeaways**
- Debugging is a normal part of coding – everyone makes mistakes!
- Learning to debug efficiently will save you **hours** of frustration.
- The more you practice, the better you'll get at **finding and fixing bugs**.

🚀 See you in **Day 14!** 🏆
