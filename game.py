from board import Board

class Game():
    """Overall game logic, including playing turns, winning + other backend features"""

    def __init__(self, ai = None):

        # Every game starts with an empty 3x3 board, X goes first
        self._board = Board()
        self._current_mark = "X"
        self._status = "Playing"
        # None means 2-player mode, otherwise the AI plays as O
        self._ai = ai

    def _switch_current_mark(self):
        """Swap the current player between X and O."""
        if self._current_mark == "X":
            self._current_mark = "O"
        elif self._current_mark == "O":
            self._current_mark = "X"

    def make_move(self, row: int, col: int):
        """Place the current mark at row, col (counting from 0). Return True if placed."""
        place_result = self._board.place_mark(row, col, self._current_mark)
        # Only switch turns if the move was valid, so the player gets another try
        if place_result:
            self._switch_current_mark()
        return place_result

    def check_status(self):
        """Return "X" or "O" if that player has won, "Draw" if the board is full, otherwise "Playing"."""
        if self._board.has_won("X"):
            self._status = "X"
            return "X"
        elif self._board.has_won("O"):
            self._status = "O"
            return "O"
        elif self._board.is_full():
            self._status = "Draw"
            return "Draw"
        else:
            self._status = "Playing"
            return "Playing"

    def check_whos_turn(self):
        """Return the mark of the player whose turn it is."""
        return self._current_mark

    def get_grid(self):
        """Return the board as printable text."""
        return self._board.__str__()

    def is_ai_turn(self):
        """Return True if an AI is playing and it is O's turn."""
        if self._ai is not None and self._current_mark == "O":
            return True
        else:
            return False

    def play_ai_turn(self):
        """Let the AI pick and play a move. Return the (row, col) it chose."""
        chosen_move = self._ai.choose_move(self._board, self._current_mark)
        self.make_move(chosen_move[0], chosen_move[1])
        return chosen_move