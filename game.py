from board import Board

class Game():
    """Overall game logic, including playing turns, winning + other backend features"""

    def __init__(self):

        self._board = Board()
        self._current_mark = "X"
        self._status = "Playing"

    def _switch_current_mark(self):
        if self._current_mark == "X":
            self._current_mark = "O"
        elif self._current_mark == "O":
            self._current_mark = "X"

    def make_move(self, row: int, col: int):
        place_result = self._board.place_mark(row, col, self._current_mark)
        if place_result:
            self._switch_current_mark()
        return place_result

    def check_status(self):
        if self._board.has_won("X"):
            self._status = "X"
        elif self._board.has_won("O"):
            self._status = "O"
        elif self._board.is_full():
            self._status = "Draw"
            return "The game is a draw..."
        else:
            self._status = "Playing"
        return "\n" + self._status + " has won!!!\n"

    def check_whos_turn(self):