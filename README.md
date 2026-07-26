# 🤖 AI Grid Cleaner

## 📌 Project Overview

AI Grid Cleaner is a Python-based simulation that demonstrates how an intelligent robot automatically cleans a grid containing randomly placed dirt while avoiding obstacles using the **A\* (A-Star) Pathfinding Algorithm**.

The robot identifies the nearest dirty cell, calculates the shortest available path, moves through the grid, and cleans all dirt automatically.

---

## 🎯 Objectives

- Simulate an autonomous cleaning robot.
- Implement the A* pathfinding algorithm.
- Demonstrate obstacle avoidance.
- Visualize robot movement using Pygame.
- Track cleaning progress and robot steps.

---

## ✨ Features

- Random grid generation
- Random dirt placement
- Random obstacle placement
- AI-controlled cleaning robot
- A* shortest path algorithm
- Automatic obstacle avoidance
- Automatic dirt cleaning
- Step counter
- Cleaned dirt counter
- Graphical interface using Pygame

---

## 🛠️ Technologies Used

- Python 3.x
- Pygame
- A* Pathfinding Algorithm

---

## 📂 Project Structure

```
AI-Grid-Cleaner/
│── main.py              # Main game loop
│── grid.py              # Grid generation and dirt placement
│── robot.py             # Robot class
│── astar.py             # A* pathfinding algorithm
│── utils.py             # Helper functions
│── constants.py         # Colors and game settings
│── requirements.txt
│── README.md
│── assets/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Grid-Cleaner.git
```

### 2. Open the project

```bash
cd AI-Grid-Cleaner
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

---

## 🧠 Algorithm Used

The project uses the **A\* (A-Star) Pathfinding Algorithm** to determine the shortest path from the robot's current position to the nearest dirty cell.

The algorithm:

1. Finds the nearest dirty cell.
2. Calculates the shortest obstacle-free path.
3. Moves the robot one step at a time.
4. Cleans the dirt.
5. Repeats until all dirt is cleaned.

---

## 🖥️ Output

The simulation displays:

- Cleaning robot
- Dirt locations
- Obstacles
- Grid layout
- Number of cleaned cells
- Number of steps taken

---

## 🚀 Future Enhancements

- Multiple cleaning robots
- Battery management
- Charging station
- Different grid sizes
- Manual obstacle placement
- Animated robot movement
- Real robot integration using IoT

---

## 📚 Learning Outcomes

This project demonstrates knowledge of:

- Python Programming
- Object-Oriented Programming (OOP)
- A* Pathfinding Algorithm
- Graph Algorithms
- Pygame
- Artificial Intelligence Basics
- Problem Solving

---

## 👩‍💻 Author

**Kavya Khandapu**

B.Tech – Computer Science and Engineering (IoT)

Raghu Engineering College

---

## 📄 License

This project is developed for educational and learning purposes.