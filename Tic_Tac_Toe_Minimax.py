# ─────────────────────────────────────────────────────────────────────────────
# Tic-Tac-Toe with Minimax AI
# ─────────────────────────────────────────────────────────────────────────────
# The board is represented as a flat list of 9 cells, indexed like this:
#
#   1 | 2 | 3
#   ---------
#   4 | 5 | 6
#   ---------
#   7 | 8 | 9
#
# Internally (0-indexed):
#   [0][1][2]
#   [3][4][5]
#   [6][7][8]
#
# Player  → 'X'  (human)
# Computer → 'O'  (AI using Minimax)
# ─────────────────────────────────────────────────────────────────────────────

from IPython.display import clear_output

# Global board state — a list of 9 cells, each ' ', 'X', or 'O'
board = [" "] * 9


# ─────────────────────────────────────────────────────────────────────────────
# is_Win(player)
#   Returns True if the given player ('X' or 'O') has won the game.
#   Checks all 8 winning combinations:
#     - 3 rows
#     - 3 columns
#     - 2 diagonals
# ─────────────────────────────────────────────────────────────────────────────
def is_Win(player):
    # Check rows: [0,1,2], [3,4,5], [6,7,8]
    for i in range(3):
        if board[i*3] == board[i*3 + 1] == board[i*3 + 2] == player:
            return True

    # Check columns: [0,3,6], [1,4,7], [2,5,8]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals: [0,4,8] and [2,4,6]
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


# ─────────────────────────────────────────────────────────────────────────────
# display_board()
#   Prints the current board state to the console in a readable grid format.
# ─────────────────────────────────────────────────────────────────────────────
def display_board():
    print('-' * 13)
    for i in range(3):
        print("|", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2], "|")
        print('-' * 13)


# ─────────────────────────────────────────────────────────────────────────────
# minimax(board, depth, isMaximizing)
#   Core recursive algorithm that scores every possible future game state.
#
#   Parameters:
#     board         – current board state (modified in-place, then restored)
#     depth         – recursion depth (used for potential depth-limited search)
#     isMaximizing  – True when it's the AI's turn (O), False for human (X)
#
#   Returns:
#     +1  if 'O' (AI) wins in this branch
#     -1  if 'X' (human) wins in this branch
#      0  if the game is a draw
#
#   How it works:
#     - Maximizing player (AI/O) tries to pick the move with the highest score.
#     - Minimizing player (Human/X) tries to pick the move with the lowest score.
#     - The algorithm explores every possible future move via recursion,
#       effectively building a full game tree and backing up the optimal score.
# ─────────────────────────────────────────────────────────────────────────────
def minimax(board, depth, isMaximizing):
    # Base cases — terminal states
    if is_Win('X'):
        return -1   # Human wins → bad for AI
    elif is_Win('O'):
        return 1    # AI wins → good for AI
    elif ' ' not in board:
        return 0    # Draw

    if isMaximizing:
        # AI's turn — try all empty cells, pick the highest score
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'                          # try move
                score = minimax(board, depth + 1, False) # recurse as minimizer
                board[i] = ' '                          # undo move
                best_score = max(score, best_score)
        return best_score
    else:
        # Human's turn — try all empty cells, pick the lowest score
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'                         # try move
                score = minimax(board, depth + 1, True) # recurse as maximizer
                board[i] = ' '                         # undo move
                best_score = min(score, best_score)
        return best_score


# ─────────────────────────────────────────────────────────────────────────────
# min_max(board)
#   Wrapper that calls minimax for each available cell and picks the move
#   with the highest score — then applies it to the real board.
#
#   This is the AI's "make a move" function.
# ─────────────────────────────────────────────────────────────────────────────
def min_max(board):
    final_score = float('-inf')
    final_i = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'                        # try move
            score = minimax(board, 0, False)       # score this move
            board[i] = ' '                        # undo move

            if score > final_score:
                final_score = score
                final_i = i                       # remember best move index

    board[final_i] = 'O'  # apply the best move found


# ─────────────────────────────────────────────────────────────────────────────
# Play_XO()
#   Main game loop.
#
#   Flow:
#     1. Display the board.
#     2. If it's X's turn → prompt the human for a valid position (1-9).
#     3. If it's O's turn → let the AI pick via min_max().
#     4. After each move, check for win or draw.
#     5. Switch turns and repeat.
# ─────────────────────────────────────────────────────────────────────────────
def Play_XO():
    player = 'X'  # Human always goes first

    while True:
        display_board()

        if player == 'X':
            # ── Human turn ────────────────────────────────────────────────────
            while True:
                position = int(input("Player " + player + ", enter the position (1-9): "))

                if position < 1 or position > 9:
                    print('\nInvalid position, please enter a position between 1 and 9\n')
                    continue
                elif board[position - 1] != ' ':
                    print(f'\nInvalid position, cell is occupied by {board[position - 1]}\n')
                else:
                    break  # valid input

            board[position - 1] = player

            if is_Win(player):
                display_board()
                print("Player " + player + " Wins!")
                break
            elif ' ' not in board:
                print("It's a Tie!")
                break

        else:
            # ── AI turn (Minimax) ─────────────────────────────────────────────
            min_max(board)

            if is_Win('O'):
                display_board()
                print("Computer Wins!")
                break
            elif ' ' not in board:
                print("It's a Tie!")
                break

        # Switch turn and clear screen for clean display
        player = 'O' if player == 'X' else 'X'
        clear_output(wait=True)


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────
Play_XO()
