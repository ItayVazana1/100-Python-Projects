# 📅 Day 8 - 100 Days of Code - Python

## 🎯 Functions with Input

Today's focus is on **functions with parameters**, allowing us to make our code more **flexible** and **dynamic**. 

---

## 📌 Understanding Function Parameters
Functions can accept **parameters** to customize their behavior. This allows us to:
- 👤 **Personalize** output (e.g., greeting specific users).
- ⚙️ **Handle multiple inputs** dynamically.
- 🌟 **Improve code reuse** by writing general-purpose functions.

### ✨ Basic Function Example:

```python
def greet():
    for i in range(3):
        print("Hello World!")

greet()
```

### ✨ Function with Parameters:
```python
def greet_someone(specific_name):
    print(f"Hello {specific_name}, how are you?")

greet_someone("David")
```

### ✨ Using a List of Names:
```python
names = ["Mishel", "David", "Itay", "Koral", "Donald"]
for name in names:
    greet_someone(name)
```

### ✨ Function with Multiple Parameters:
```python
def greet_with_name_and_loc(specific_name, specific_location):
    print(f"Hello {specific_name}")
    print(f"What is it like in {specific_location}?")

locations = ["Finland", "Tokyo", "Tel-Aviv", "California", "Paris"]
for i in range(len(names)):
    greet_with_name_and_loc(names[i], locations[i])
```

### ✨ Using Named Parameters to Ensure Correct Order:
```python
for i in range(len(names)):
    greet_with_name_and_loc(specific_name=names[i], specific_location=locations[i])
```

---

## 💻 Day 8 Project - Caesar Cipher Generator 🌟

### 📖 What is the Caesar Cipher?
The **Caesar Cipher** is a simple encryption technique where each letter is **shifted** by a fixed number of positions in the alphabet. It helps understand:
- **String manipulation**
- **Basic encryption concepts**
- **Looping through characters**

---

## 🔑 Steps to Build the Caesar Cipher

### 🔒 Step 1 - Encoding a Message
1. Accept a **message** and a **shift number**.
2. Convert each letter using the shift.
3. Print the **encoded message**.

```python
def encode(msg, shift_num):
    encrypted_msg = ""
    low_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerical_alphabet = "0123456789"
    symbols_and_space = " ?!@#$%^&*()"
    
    for letter in msg:
        if letter in low_alphabet:
            char_bank = low_alphabet
        elif letter in cap_alphabet:
            char_bank = cap_alphabet
        elif letter in numerical_alphabet:
            char_bank = numerical_alphabet
        else:
            char_bank = symbols_and_space
        
        for i in range(len(char_bank)):
            if letter == char_bank[i]:
                c = (i + shift_num) % len(char_bank)
                encrypted_msg += char_bank[c]
                break

    print(f"The encoded result: [{encrypted_msg}]")
```

### 🔓 Step 2 - Decoding a Message
1. Accept an **encoded message** and a **shift number**.
2. Reverse the shift to get the **original message**.
3. Print the **decoded message**.

```python
def decode(msg, shift_num):
    original_msg = ""
    low_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerical_alphabet = "0123456789"
    symbols_and_space = " ?!@#$%^&*()"
    
    for letter in msg:
        if letter in low_alphabet:
            char_bank = low_alphabet
        elif letter in cap_alphabet:
            char_bank = cap_alphabet
        elif letter in numerical_alphabet:
            char_bank = numerical_alphabet
        else:
            char_bank = symbols_and_space
        
        for i in range(len(char_bank)):
            if letter == char_bank[i]:
                c = (i - shift_num) % len(char_bank)
                original_msg += char_bank[c]
                break

    print(f"The decoded result: {original_msg}")
```

### 🔧 Step 3 - Implementing User Interaction
1. Ask the user if they want to **encode** or **decode** a message.
2. Accept the **message** and **shift number**.
3. Perform the chosen operation.
4. Ask if they want to continue.

```python
p_flag = True
while p_flag:
    operation = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    while operation not in ["encode", "decode"]:
        print("Invalid input - try again!")
        operation = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    
    message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))
    
    if operation == "encode":
        encode(msg=message, shift_num=shift_number)
    else:
        decode(msg=message, shift_num=shift_number)
    
    more_op = input("To continue, type 'yes', otherwise type anything else..\n").lower()
    if more_op != 'yes':
        p_flag = False
```

---

## 🚀 Key Takeaways
- **Functions with parameters** make code **flexible** and **reusable**.
- **Caesar Cipher** demonstrates:
  - **String manipulation** 🔄
  - **Looping through characters** ⚪
  - **Basic encryption & decryption** 🔑
- **User input handling** for interactive programs ⏳

This project is a great **practice** for working with **functions, loops, and string operations**! 🎨📚
