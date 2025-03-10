# Day 9 - 100 Days of Code - Python 🚀

## 📚 Dictionaries and Nesting in Python

### What is a Dictionary in Python? 📖
A dictionary in Python works similarly to a real dictionary:
- It consists of **key-value pairs**.
- The **key** serves as a label for a specific value.
- The **value** is the actual data associated with the key.

#### Example:
```python
# Creating a dictionary
my_dict = {
    "A": "Angela",
    "I": "Itay",
    "R": "Ronald"
}
```
- Accessing a value:
  ```python
  print(my_dict['A'])  # Output: Angela
  ```
- Adding a new key-value pair:
  ```python
  my_dict['Z'] = 'Zebra'
  ```
- Looping through a dictionary:
  ```python
  for key in my_dict:
      print(f"[{key}] is the key for the value [{my_dict[key]}]")
  ```

### 🏗️ Nesting in Python
Nesting means storing a **data structure inside another one**.
Examples:
- A **list inside a dictionary**
- A **dictionary inside a list**
- A **dictionary inside another dictionary**

#### Example:
```python
nested_dict = {
    'A': ['Algorithm', 'Animal', 'Automata'],
    'B': ['Basketball', 'Binary', 'Brave'],
    'C': ['Cave', 'Clock', 'Cooking']
}
```
- Accessing nested values:
  ```python
  print(nested_dict['A'][0])  # Output: Algorithm
  ```
- A more complex nesting:
  ```python
  complex_dict = {
      'A': ['Algorithm', 'Animal', ['Automata']],
      'B': ['Basketball', 'Binary', 'Brave']
  }
  print(complex_dict['A'][2][0])  # Output: Automata
  ```

---

## 🎯 Daily Project: Secret Auction Program 🎩💰

### 🎬 The Secret Auction is Starting!

#### 🖼️ Logo:
```
                         ___________
                         |         /
                          )_______(
                          |"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"(
                         /_________|
                       .-------------.
                      /_______________||
```

### 🔧 How the Program Works:
1. The program starts by displaying a **logo** and an **introduction**.
2. It **collects bids** from multiple users.
3. Each bid is stored in a **dictionary**.
4. The program **hides previous bids** (simulating a secret auction).
5. At the end, it finds the **highest bidder** and announces the winner.
6. A **countdown animation** is added using the `time` module.

### 📝 Code Implementation:
```python
import time

print("The Secret Auction is Starting now!")
print("Each one, in turn - insert your name and then your bid!")

dic_bids = {}
more_players = True

while more_players:
    name = input("Insert your name: ")
    bid = int(input("Insert your bid in $ (make sure no one is watching): $"))
    dic_bids[name] = bid
    last_bid = input("Are there more bids? (yes/no): ")
    
    while last_bid not in ['yes', 'no']:
        print("Invalid input!")
        last_bid = input("Are there more bids? (yes/no): ")
    
    if last_bid == 'no':
        more_players = False
    
    print("\n" * 100)  # Clearing the screen

max_bid_name = max(dic_bids, key=dic_bids.get)
max_bid = dic_bids[max_bid_name]

print("Auction closes in:")
time.sleep(0.2)
print("3...")
time.sleep(0.7)
print("2...")
time.sleep(0.7)
print("1...")
time.sleep(0.2)
print(f"Sold to {max_bid_name} - The Highest bid was ${max_bid}")
```

### 🔥 Key Features of the Program:
✅ Uses **dictionaries** to store bids securely.

✅ Ensures **bid confidentiality** by clearing the screen.

✅ Uses **loops** to collect multiple bids.

✅ Includes **error handling** for user input.

✅ Displays a **countdown effect** before revealing the winner.


---

🎯 **Summary**:

- Today we learned about **dictionaries** and **nesting** in Python.

- We applied this knowledge to create a **Secret Auction Program**.

- This project demonstrates how **dictionaries** can be used for storing and retrieving data efficiently.


🚀 **On to the next challenge!** 🔥
