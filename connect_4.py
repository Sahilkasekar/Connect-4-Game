```python
ROWS = 6
COLS = 7

board = [[" " for _ in range(COLS)] for _ in range(ROWS)]


def display_board():
    print("\n  1   2   3   4   5   6   7")
    print("+---+---+---+---+---+---+---+")

    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")


def drop_disc(column, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            return row
    return -1


def check_winner(row, col, player):
    directions = [
        (0, 1),   # Horizontal
        (1, 0),   # Vertical
        (1, 1),   # Diagonal
        (1, -1)   # Other diagonal
    ]

    for dr, dc in directions:
        count = 1

        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
            count += 1
            r += dr
            c += dc

        r, c = row - dr, col - dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc

        if count >= 4:
            return True

    return False


def board_full():
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True


def play_game():
    player = "X"

    print("===== CONNECT 4 GAME =====")

    while True:
        display_board()

        try:
            column = int(input(f"Player {player}, choose column (1-7): ")) - 1

            if column < 0 or column >= COLS:
                print("Please choose a column between 1 and 7.")
                continue

            row = drop_disc(column, player)

            if row == -1:
                print("This column is full. Choose another column.")
                continue

            if check_winner(row, column, player):
                display_board()
                print(f"Player {player} wins!")
                break

            if board_full():
                display_board()
                print("Game Draw!")
                break

            player = "O" if player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")


play_game()
```
