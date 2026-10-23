# Tic-Tac-Toe

A command-line Tic-Tac-Toe game in Python. Play against another person or against an AI opponent.

## Features

- Player vs Player mode
- Player vs AI mode, with two difficulty levels:
  - Easy: picks a random empty square
  - Hard: uses Minimax, so it never loses
- Rejects invalid input and asks again, so you never lose your turn

## Requirements

- Python 3.12+
- pytest (only needed to run the tests)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

## How to Play

1. Choose a mode: `1` for another player or `2` for the AI.
2. If you picked the AI, choose `1` for Easy or `2` for Hard.
3. On your turn, enter the row and column separated by a space, using numbers 1–3. For example, `2 3` means row 2, column 3.
4. Get 3 in a row (across, down, or diagonally) to win. If the board fills up with no winner, the game is a draw.

When you play the AI, you are always **X** and the AI is always **O**.

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Menus, input, and printing the board |
| `game.py` | Game logic: turns, moves, win/draw checks |
| `board.py` | The board: placing and removing marks, win detection |
| `ai.py` | Easy and Hard AI opponents |
| `tests/` | Unit tests |
| `PLAN.md` | Requirements, components, and design decisions |

## Running Tests

```bash
pytest
```