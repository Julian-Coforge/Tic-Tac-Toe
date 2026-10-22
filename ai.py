import random
from abc import ABC, abstractmethod
from board import Board

class AIPlayer(ABC):
    """Base class for every computer opponent."""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    @abstractmethod
    def choose_move(self, board: Board, mark):
        """Return a (row, col) tuple for an empty cell on the board."""


class EasyAI(AIPlayer):
    """Picks any empty cell at random."""

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())

class HardAI(AIPlayer):
    """Uses Minmax to make a choice"""

    def choose_move(self, board, mark):
        return

    def change_mark(self, mark):
        if mark == "X":
            return "O"
        else:
            return "X"

    def _minimax(self, board: Board, ai_mark, current_turn_mark):

        opponents_mark = self.change_mark(ai_mark)

        if board.has_won(ai_mark):
            return 1
        elif board.has_won(opponents_mark):
            return -1
        elif board.is_full():
            return 0

        