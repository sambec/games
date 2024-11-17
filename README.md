# Tic Tac Toe Game 🕹️

A simple, interactive implementation of the classic **Tic Tac Toe** game in Python. This project is designed to be beginner-friendly, with clear and concise code that showcases fundamental programming concepts like loops, conditionals, and functions.

---

## Features ✨

- **Two-player gameplay**: Players alternate turns to place their marks (X or O).
- **Winner detection**: The game automatically checks for wins across rows, columns, and diagonals.
- **Draw detection**: If the board is full without a winner, the game declares a draw.
- **Input validation**: Ensures players provide valid moves (e.g., not overwriting existing marks or entering out-of-bounds positions).
- **Simple UI**: The game runs in the terminal, making it lightweight and easy to use.

---

## How to Play 🎮

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/sambec/tic-tac-toe.git
   cd tic-tac-toe
   ```
2. Run the game using Python:
   ```bash
   python tic_tac_toe.py
   ```
3. Follow the prompts to take turns entering the row and column numbers (0-2) where you'd like to place your mark.
4. The game ends when:
   - One player gets three marks in a row (horizontally, vertically, or diagonally).
   - The board is full (resulting in a draw).

---

## Example Gameplay 🎲

```
  |   |  
---------
  |   |  
---------
  |   |  
Player X's turn.
Enter row (0-2): 0
Enter column (0-2): 1

  | X |  
---------
  |   |  
---------
  |   |  
Player O's turn.
Enter row (0-2): 1
Enter column (0-2): 1
```

---

## File Structure 📂

- **`tic_tac_toe.py`**: Contains the full implementation of the game.
- *(Optional)* Additional files for future extensions or documentation.

---

## Roadmap 🛤️

Future enhancements to this project might include:
- A **single-player mode** with an AI opponent (e.g., using the Minimax algorithm).
- A graphical user interface (GUI) using libraries like Tkinter or Pygame.
- A web-based version using Flask/Django.

---

## Requirements 🛠️

- Python 3.x
- No external dependencies required.

---

## Contributing 🤝

Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-newFeature`).
3. Commit your changes (`git commit -am 'Add some newFeature'`).
4. Push to the branch (`git push origin feature-newFeature`).
5. Open a Pull Request.

---

## License 📄

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments 🙌

Thanks for checking out this project! Feel free to reach out with any feedback or suggestions. 😊

---

Let me know if you'd like to modify or add sections to suit your project further!