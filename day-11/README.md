# Day 11 - 100 Days of Code

# BlackJack - Python Capstone Project 🃏💰

## 🎮 Overview
This is a **single-player BlackJack game**, implemented as part of the *100 Days of Code* challenge (Day 11). The project consolidates all the concepts learned so far, integrating functions, loops, user input validation, and object handling into a fully functional game.

## 📜 Game Rules
- **Players:** One player (You) vs. the Computer.
- **Starting Bank:** Both the player and computer start with 1000 coins.
- **Betting:** The player must place a bet at the beginning of each round.
- **Card Usage:** Used cards are removed from play. A new deck is introduced when all cards are used.
- **Game End Conditions:**
  1. The player chooses to quit after any round. The final bank amounts are compared, and the player with more coins wins.
  2. The player runs out of coins, resulting in an automatic loss.

## 🔄 Round Structure
1. Both the player and the computer receive **one public (visible) card**.
2. Each side is dealt **one private (hidden) card**.
3. The player can **draw additional cards (hit)** or **stop drawing (stand)**.
4. The goal is to get as close as possible to **21** without exceeding it (**bust** if above 21).
5. The **"17 Rule"** applies to the computer:
   - If the computer’s total is below **17**, it *must* draw another card.
   - If the computer exceeds **21**, the player wins.

## 🎴 Card Values
- **Numbered Cards (2-10):** Face value.
- **J, Q, K:** Worth **10** points.
- **Ace (A):** Can be **1** or **11** (player’s choice).

## 🏆 Possible Outcomes
1. **Player Wins** – Player's hand is **higher** than the computer's and ≤ 21.
2. **Computer Wins** – Computer’s hand is **higher** than the player’s and ≤ 21.
3. **Draw** – Both hands are equal and ≤ 21.
4. **Computer Wins** – Player **busts** (hand value > 21).
5. **Player Wins** – Computer **busts** (hand value > 21).

---

## 🛠 Technologies & Concepts Used
### ✅ Python Programming Features
- **Functions**: Modular approach with `game_functions.py` handling game logic.
- **Loops & Conditions**: Used for game flow, user input validation, and AI decisions.
- **Randomization**: `random.choice()` used for drawing cards.
- **Time Delays**: `time.sleep()` for user experience enhancement.
- **String Formatting**: `f-strings` for clear output messages.

### ✅ Object-Oriented Approach
- The deck is structured using **dictionaries & lists**.
- Cards are dynamically **updated & removed** after each round.

### ✅ User Interaction & Input Validation
- **Ensuring valid inputs** (e.g., restricting bet values and valid responses for Ace choice).
- **Looping mechanics** allow repeated gameplay until the user quits.

---

## 🚀 How to Run
1. Ensure you have Python installed (3.x recommended).
2. Run the main game script:
   ```sh
   python BlackJack.py
   ```
3. Follow the on-screen instructions to play.

---

## 📂 Project Structure
```
📂 BlackJack Game
├── 🃏 BlackJack.py      # Main game script
├── 🔄 game_functions.py # Contains game logic and helper functions
├── 🎨 art.py            # ASCII art & game rules text
├── 🏁 main.py           # Project description and structure
```

---

## 🏅 Summary
This **capstone project** integrates key programming concepts while implementing a fun and interactive game. The modular approach ensures scalability, making it possible to add multiplayer, GUI, or betting strategies in future iterations.

🎲 *Enjoy your game of BlackJack!*