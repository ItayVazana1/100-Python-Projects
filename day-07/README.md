# 📅 Day 7 - 100 Days of Code - Python

## 🎯 Flowcharts - Visualizing Logic Before Coding

Today’s focus is on **Flowcharts**—a powerful tool that helps us **plan** our code visually before writing a single line. 

---

## 📌 Why Use Flowcharts?
A **Flowchart** is a diagram that represents the **logic** of a program using symbols. This approach helps:
- 🏗 **Structure complex logic** before writing code.
- 🔎 **Spot errors early** in the planning phase.
- 📖 **Explain logic** to others in a clear way.

### 🛠 Basic Flowchart Symbols:
- 🔲 **Start/End** → Represented by ovals.
- 🔹 **Decisions** (Yes/No) → Represented by diamonds.
- 📏 **Processes** (Actions) → Represented by rectangles.
- ➡ **Arrows** → Indicate the flow of logic.

---

## 🎮 Day 7 Project - Hangman Game 🏆

### 📖 Game Overview
**Hangman** is a word-guessing game where:
1. One player thinks of a **secret word**.
2. The other player **guesses letters** one by one.
3. If the guessed letter is **correct**, it is revealed in the word.
4. If the guess is **wrong**, the player loses a life.
5. The game ends when:
   - 🎉 The full word is guessed → **You win!**
   - 💀 The player runs out of lives → **Game over!**

---

## 🔑 Steps to Build the Hangman Game

### 📝 Step 1 - Choose a Word 🎲
- Use a **list of words**.
- Pick a **random word** from the list.

```python
import random

words = ["apple", "mouse", "bedroom", "fire", "lamp", "software", "elephant"]
rand_word = random.choice(words)
```

### 📝 Step 2 - Create a Placeholder for the Word 🖋
- Replace each letter with `_` (underscore).
- Example: `apple` → `_ _ _ _ _`

```python
placeholder = ["_" for _ in rand_word]
```

### 📝 Step 3 - Take User Input 🎤
- Ask the user to **guess a letter**.
- Check if the letter is in the word.

```python
letter = input("Guess a letter: ").lower()

if letter in rand_word:
    print("✅ Correct guess!")
else:
    print("❌ Wrong guess!")
```

### 📝 Step 4 - Update the Placeholder ✏
- If the guessed letter is in the word, **replace the `_`** with the letter.
- Example: If the word is `apple` and the guess is `p` → `_ p p _ _`

```python
for i in range(len(rand_word)):
    if rand_word[i] == letter:
        placeholder[i] = letter
```

### 📝 Step 5 - Track Lives ❤️
- The player starts with **6 lives**.
- Each wrong guess **reduces** the number of lives.
- The game ends when **lives reach 0**.

```python
lives = 6
if letter not in rand_word:
    lives -= 1
    print(f"❌ Wrong guess! Lives left: {lives}")
```

### 📝 Step 6 - Check Win Condition 🏆
- The player wins if **all letters are guessed**.

```python
if "_" not in placeholder:
    print("🎉 You win!")
```

---

## 🖥 Full Hangman Code 🕹

```python
import random

words = ["apple", "mouse", "bedroom", "fire", "lamp", "software", "elephant"]
lives = 6
rand_word = random.choice(words)

placeholder = ["_" for _ in rand_word]
win_flag = False

print("🎭 Welcome to Hangman! Try to guess the word.")

while not win_flag and lives > 0:
    print(f"
Word: {' '.join(placeholder)}")
    letter = input("Guess a letter: ").lower()

    if letter in placeholder:
        print("⚠️ You've already guessed this letter!")
        continue

    if letter in rand_word:
        print("✅ Good guess!")
        for i in range(len(rand_word)):
            if rand_word[i] == letter:
                placeholder[i] = letter
    else:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")

    if "_" not in placeholder:
        win_flag = True

if win_flag:
    print(f"🎉 Congratulations! You guessed the word: {rand_word}")
else:
    print(f"💀 Game over! The word was: {rand_word}")
```

---

## 🚀 Key Takeaways
- **Flowcharts** help plan and visualize logic **before coding**.
- **Hangman** is a great project to practice:
  - `input()` and user interaction. 🎤
  - `random.choice()` for selecting words. 🎲
  - `if/else` statements for game logic. 🕹
  - `while` loops for repeated guessing. 🔄

