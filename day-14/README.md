# Day 13 - 100 Days of Code - Python 🐍

## 🎮 Higher or Lower Game

Welcome to the **Higher or Lower Game**! This is a simple Python game where players guess whether one quantity is higher or lower than another.

---

## 🚀 How to Play
1. Run the script.
2. Enter your name to start the game.
3. The game will randomly select two quantities and display them as **A** and **B**.
4. You must guess whether **A** is **higher** or **lower** than **B**.
5. Type **'higher'** or **'lower'** to submit your answer.
6. If you guess correctly, your score increases, and the game continues.
7. If you guess incorrectly, the game ends, and your final score is displayed.

---

## 📜 Requirements
- Python 3.x
- `random` module (built-in)
- `art` module (for displaying game logo)
- `Database.py` file containing `quantities_dict`

---

## 🛠 Setup
1. Install dependencies (if needed):
   ```bash
   pip install art
   ```
2. Ensure the `Database.py` file exists and includes the dictionary `quantities_dict`.
3. Run the script:
   ```bash
   python game.py
   ```

---

## 📌 Features
✅ Randomized questions 🎲  
✅ Input validation ✅  
✅ Score tracking 🏆  
✅ Fun and engaging gameplay 🤩  

---

## 🎯 Example Output
```shell
🎮 Welcome to the Higher or Lower Game!
Type any key to start the game..
Type your name: Alex
Hey Alex, let's start the game!

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Question #1:
A : Speed of Light
B : Speed of Sound

Is A higher or lower than B?
Type 'higher' or 'lower' ---> higher
You are right!
```

---

## 📌 Notes
- The game continues until the player makes a wrong guess.
- The `quantities_dict` dictionary should contain numerical values for proper comparisons.

Enjoy playing! 🎉
