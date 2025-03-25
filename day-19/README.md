# **Day 19 - 100 Days of Code - Python 🚀**

## **📌 Today's Focus**
### 🎮 Interactive Games with Turtle Graphics  
Today was all about **event-driven programming** using the `turtle` module to create **interactive games**.  
After a short break due to illness 🤒, I’m back and building again!

## **🧠 Topics Covered**
- ✅ **Event Listeners in Turtle**
- ✅ **Key Bindings and Real-Time Input Handling**
- ✅ **OOP with Turtle (Classes and Game Logic)**
- ✅ **User Interaction & Input Validation**
- ✅ **Screen Management and Turtle Positioning**
- ✅ **Saving Drawings as Images**

---

## **🎨 Project 1: Etch-A-Sketch 🖌️**

A modern take on the classic drawing toy, controlled with keyboard keys:

### **Controls**
| Key | Action |
|-----|--------|
| W   | Move forward |
| S   | Move backward |
| A   | Rotate left |
| D   | Rotate right |
| C   | Change color randomly |
| N   | Clear and restart drawing |
| P   | Save drawing as PNG |

### **Features**
- Uses `onkeypress()` for live input
- Random RGB color changes using `colormode(255)`
- Saves the turtle canvas as `.png` using `pyautogui` and `pygetwindow`

---

## **🏁 Project 2: Turtle Race - Betting Game 🐢**

A fun turtle race game where the player **bets** on which turtle will win!

### **How It Works**
- User chooses one of 6 turtles, each with a unique name and color
- Turtles move forward with **random speed and distance**
- The first turtle to cross the finish line is declared the winner
- User is notified if their turtle won 🏆 or lost 💔

### **Turtle Lineup**
| Name   | Color  |
|--------|--------|
| Tim    | Red    |
| Tranx  | Green  |
| Tomi   | Blue   |
| Tate   | Orange |
| Truman | Purple |
| Tramp  | Pink   |

### **Design Features**
- Object-Oriented Programming: Each turtle is an instance of `CompTurtle`
- Position labels dynamically update above each turtle
- Start and finish lines are drawn using an extra "drawing turtle"
- Winner announcement and real-time leader updates in the console

---

## **📂 Files Included**
- `main.py` → Theory + high-level overview of both projects  
- `EtchASketch.py` → Full logic for the Etch-A-Sketch drawing game  
- `Turtle_Race.py` → Full logic for the Turtle Race betting game  
- Screenshots from both games included for reference

---

## **💡 Key Takeaways**
- Event-driven programming with `turtle` unlocks real interactivity
- OOP design in games makes the logic cleaner and easier to manage
- Handling real-time input, saving canvas outputs, and managing user flow make these projects feel like real games
- Most importantly — it was **fun and creative**! 🎉

🚀 **See you on Day 20!**
