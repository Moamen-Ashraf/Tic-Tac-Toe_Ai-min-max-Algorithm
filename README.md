# Tic-Tac-Toe — Minimax AI

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Algorithm](https://img.shields.io/badge/Algorithm-Minimax-orange)
![AI](https://img.shields.io/badge/AI-Game%20Tree%20Search-green)
![Platform](https://img.shields.io/badge/Platform-Jupyter%20%7C%20Colab-lightgrey?logo=jupyter)

A Python implementation of Tic-Tac-Toe where the computer plays optimally using the **Minimax algorithm** — it never loses.

---

## Demo

```
-------------
| X | X | O |
-------------
| O | O | X |
-------------
| O |   | X |
-------------
Computer Wins!
```

---

## How It Works

The human plays as **X**, the computer plays as **O**.

The AI uses the **Minimax algorithm** to explore every possible future game state and always pick the optimal move.

```
Current Board
     │
     ├── AI places O at cell 1 → score = minimax(depth+1, minimizing)
     ├── AI places O at cell 3 → score = minimax(depth+1, minimizing)
     ├── AI places O at cell 7 → score = minimax(depth+1, minimizing)  ← best
     └── ...

AI picks the move with the highest score and applies it.
```

**Scoring:**

| Result | Score |
|--------|-------|
| AI (O) wins | +1 |
| Human (X) wins | -1 |
| Draw | 0 |

The AI maximizes its score; the human (simulated) minimizes it — hence **Minimax**.

---

## Algorithm

### `minimax(board, depth, isMaximizing)`

Recursively scores every possible game state from the current board position.

```
minimax()
├── Base cases:
│   ├── O wins  → return +1
│   ├── X wins  → return -1
│   └── Draw    → return  0
│
├── Maximizing (AI/O turn):
│   ├── Try each empty cell with 'O'
│   ├── Recurse as minimizer
│   └── Return the highest score found
│
└── Minimizing (Human/X turn):
    ├── Try each empty cell with 'X'
    ├── Recurse as maximizer
    └── Return the lowest score found
```

### `min_max(board)`
Wrapper that calls `minimax` for each available move and applies the one with the highest score to the actual board.

### `is_Win(player)`
Checks all 8 winning combinations — 3 rows, 3 columns, 2 diagonals.

### `Play_XO()`
Main game loop — alternates between human input and AI moves, checks win/draw after each turn.

---

## Project Structure

```
Tic-Tac-Toe-Minimax/
├── Tic_Tac_Toe_Minimax.ipynb   ← Jupyter notebook (original, runnable)
├── Tic_Tac_Toe_Minimax.py      ← Clean Python script with full comments
└── README.md
```

---

## Run It

**Google Colab** (easiest):
Upload the `.ipynb` file to [colab.research.google.com](https://colab.research.google.com) and run the cell.

**Locally:**
```bash
pip install jupyter
jupyter notebook Tic_Tac_Toe_Minimax.ipynb
```

**As a script:**
```bash
python Tic_Tac_Toe_Minimax.py
```

---

## Board Layout

Positions the human enters (1–9):

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

---

## Why the AI Never Loses

Minimax explores the **complete game tree** — every possible sequence of moves to the end. With only 9 cells, the tree has at most 9! = 362,880 leaf nodes, which is trivially small. The AI evaluates all of them and guarantees the best possible outcome (win or draw) every time.

---

## Author

**Momen Ashraf**  
[linkedin.com/in/momen-ashraf-](https://linkedin.com/in/momen-ashraf-)
