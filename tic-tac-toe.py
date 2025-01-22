# Simple Tic Tac Toe Game in Python

def display_board(board):
    """
    Displays the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks for a winner in the board.
    Returns 'X', 'O', or None if there is no winner yet.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    """
    Checks if the board is full.
    """
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    """
    Main function to play the Tic Tac Toe game.
    """
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get player's move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for a draw
        if is_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
