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