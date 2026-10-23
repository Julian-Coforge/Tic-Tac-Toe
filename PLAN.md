# Goal

The game is Tic-Tac-Toe, a game with a 3x3 grid and 2 players, where the objective is to get line of 3 - either X's or O's - in either a vertical, horizontal, or diagonal line. The player can play against another player, or an AI opponent.

# Requirements

| ID | Requirement | Type | Priority | How Verified? |
|---|---|---|---|---|
| 1 | The game recognises when there is 3 in a row/column/diagonal and gives the win to the appropriate player | Functional | Must | Test all win cases |
| 2 | The game allows only 2 players, with only 1 with permission to update the board per turn | Functional | Must | Manually play in attempt to interfere with board updates |
| 3 | Attempting to place a mark out of the board's bounds rejects the input | Functional | Must | Use out of range values during a game to see result |
| 4 | The AI has an Easy and Hard mode, with Easy picking random and Hard picking using minmax | Functional | Must | AI tests per level |
| 5 | When playing the AI, the human always plays as X and AI as O | Non-Functional | Must | Play against AI to view which mark is provided |
| 6 | Only X's and O's are allowed as valid marks | Functional | Must | Attempt to play using multiple different characters |

# Components

| File | Responsibility |
|---|---|
| board.py | Creates the board, contains functions for placing/removing marks and wins. |
| ai.py | Holds the logic for the Easy and Hard AI opponenets. |
| game.py | Main game logic, such as providing turns for each player, detecting wins. |
| main.py | Provides the 'UI' for the player(s), providing inputs and printing outputs. |
| PLAN.md | Holds the Game details, Requirements, Components and Decisions |
| README.md | Contains information about the game, how to run and play. |
| .github/workflows/ci.yml | CI Pipeline |
| tests/ | Contains multiple files for testing logic throughout development |

# Decisions

1. How are invalid mark placements handle
    - Option 1: End game if player puts mark out of bounds
    - Option 2: Reject input and ask player again
    - Choice: Option 2
    - Why: Greatly improves UX and ensures player doesn't lose turn

2. How to check for a win
    - Option 1: Check every possible winning combination separately 
    - Option 2: Use a list of winning positions and check them in a loop
    - Option 3: Loop over rows and columns, then check both diagonals
    - Choice: Option 3
    - Why: Less repetition of code

# What Changed

1. Test size increased from initial plan
    - Plan: a few tests to check core logic during development
    - Actual: 25 tests across 3 files
        - `test_board.py` (4 tests): empty board, placing and removing marks, finding empty cells
        - `test_game.py` (15 tests): switching turns, out-of-bounds and taken cells, X win, O win, draw, AI turns
        - `test_ai.py` (6 tests): Easy AI picks an empty cell, both AIs leave the board unchanged, Hard AI takes wins, blocks the opponent and never loses
    - Why: Adding the AI opponents meant more behaviour to verify. The tests also run in CI on every push to main and on every pull request

2. How valid marks are enforced (Requirement 6)
    - Players never type a mark. `Game` switches between X and O after each valid move, so only X and O can be placed