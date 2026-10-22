import random
from abc import ABC, abstractmethod

class AIPlayer(ABC):
    """Base class for every computer opponent."""

    @abstractmethod
    def choose_move(self, board, mark):
        """Return a (row, col) tuple for an empty cell on the board."""

class EasyAI(AIPlayer):
    """Picks any empty cell at random."""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())

class FirstEmptyAI(AIPlayer):
    """Always picks the first empty cell. Predictable, so it is handy for testing."""

    def choose_move(self, board, mark):
        return board.empty_cells()[0]