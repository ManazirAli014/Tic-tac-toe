# Tic Tac Toe Game in Python

def print_board(board):
    """Function to print the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Function to check if the current player has won."""
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal
        [board[0][2], board[1][1], board[2][0]]   # Diagonal
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    """Function to check if the game is a draw (no empty spaces)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"\nPlayer {players[current_player]}'s turn")
        try:
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Try again.")
            continue
        if board[row][col] != " ":
            print("Position already taken. Try again.")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player

tic_tac_toe()
