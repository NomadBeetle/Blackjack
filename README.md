# Blackjack Game

This is a simple **Blackjack** game written in Python. The game follows the standard Blackjack rules and allows you to play against the computer.

## How to Play

- The game starts by dealing **two cards** to you and one to the computer.
- You can choose to **draw another card** (`'y'`) or **stop** (`'n'`).
- The goal is to get as close to **21** as possible without exceeding it.
- If your total exceeds 21, you **lose**.
- The computer will continue drawing cards until its total is at least **17**.
- The player with the highest valid score **wins**.
- If both have the same score, it's a **draw**.

## Features

✅ Handles **Aces** (11 or 1) correctly to prevent busting.  
✅ Implements the **dealer rule** (dealer stops at 17 or higher).  
✅ Automatically **declares the winner**.  
✅ Allows the user to **play multiple rounds**.  
✅ Clears the console for a fresh game experience.  

## Installation & Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/NomadBeetle/Blackjack.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Blackjack
   ```
3. Run the game:
   ```sh
   python main.py
   ```

## Example Gameplay
```
Do you want to play a game of Blackjack? (y/n): y
Your current hand: [5, 10]. Total score: 15
Computer's First Card: [7]
Do you want to pick another card? (y/n): y
Your current hand: [5, 10, 6]. Total score: 21
Blackjack! You win!
```

## Contributing
Feel free to fork this project, submit PRs, or suggest improvements!

---

**Author:** [Azaan Ahmed](https://github.com/NomadBeetle) 🚀
