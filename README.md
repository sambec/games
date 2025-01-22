# Games Repository 🎮

A collection of Python scripts showcasing various games, built as exercises to explore and enhance programming skills with Python. This repository currently includes:

- **Tic Tac Toe**: The classic grid-based strategy game for two players.
- **La Bataille**: A traditional French card game for two players.
- Stay tuned for more games in the future!

---

## Table of Contents 📚

1. [Tic Tac Toe](#tic-tac-toe-game-🕹️)
   - Features
   - How to Play
   - Example Gameplay
2. [La Bataille](#la-bataille-game-♠️)
   - Rules
   - How to Play
   - Example Gameplay
3. [File Structure](#file-structure-📂)
4. [Roadmap](#roadmap-🛤️)
5. [Requirements](#requirements-🛠️)
6. [Contributing](#contributing-🤝)
7. [License](#license-📄)
8. [Acknowledgments](#acknowledgments-🙌)

---

## Tic Tac Toe Game 🕹️

A simple, interactive implementation of the classic **Tic Tac Toe** game in Python. This project is designed to be beginner-friendly, with clear and concise code that showcases fundamental programming concepts.

### Features ✨

- Two-player gameplay.
- Automatic winner and draw detection.
- Input validation to ensure fair play.
- Lightweight and terminal-based.

### How to Play 🎮

1. Clone the repository and navigate to the directory:
   ```bash
   git clone https://github.com/your-username/games.git
   cd games
   ```
2. Run the Tic Tac Toe game:
   ```bash
   python tic_tac_toe.py
   ```
3. Follow the prompts to take turns entering the row and column numbers (0-2) to place your mark.

---

## La Bataille Game ♠️

An implementation of the traditional French card game **La Bataille** in Python. This project demonstrates concepts like shuffling, list manipulation, and loops.

### Rules 📜

- The game is played with a standard 52-card deck, divided equally between two players.
- Players reveal the top card of their deck simultaneously:
  - The player with the higher card value wins the round and takes both cards.
  - If the cards are of equal value, a **Bataille** (battle) occurs:
    - Each player places three cards face down, then reveals a fourth card.
    - The higher fourth card wins all the cards from the round.
    - If there's another tie, the battle continues in the same way.
- The game continues until one player has all the cards or a predefined number of rounds is reached.

### How to Play 🃏

1. Run the La Bataille game:
   ```bash
   python la_bataille.py
   ```
2. The program shuffles and distributes the cards automatically.
3. Players take turns revealing cards, and the game announces the winner of each round.
4. The game ends when one player has all the cards, or the maximum number of rounds is reached.

### Example Gameplay 🎲

```
Joueur 1 a joué ('2', 'COEUR')
Joueur 2 a joué ('7', 'CARREAU')
Joueur 2 gagne ce tour
-----
Joueur 1 a joué ('10', 'CARREAU')
Joueur 2 a joué ('Dame', 'TREFLE')
Joueur 2 gagne ce tour
```

---

## File Structure 📂

```
games/
│
├── tic_tac_toe.py       # Tic Tac Toe implementation
├── la_bataille.py       # La Bataille implementation
├── requirements.txt     # Dependencies (if any)
└── README.md            # Documentation
```

---

## Roadmap 🛤️

Upcoming features and games:

- A **single-player Tic Tac Toe** mode with an AI opponent.
- Additional card games like Le Président
- A **leaderboard** feature to track scores across games.
- A web-based interface to play games online.

---

## Requirements 🛠️

- Python 3.x
- No external dependencies are currently required.

---

## Contributing 🤝

Contributions are welcome! Here's how you can help:

1. Fork the repository.
2. Add your new feature or game in a separate branch.
3. Open a Pull Request for review.

---

## License 📄

This repository is licensed under the [MIT License](LICENSE).

---

## Acknowledgments 🙌

Special thanks to all the creators of Python tools and resources that made this possible. Feel free to reach out with feedback or ideas for new games. 😊

---

