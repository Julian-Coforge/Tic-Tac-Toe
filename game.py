from board import Board

class Game():
    """Overall game logic, including playing turns, winning + other backend features"""

    def __init__(self):

        self._board = Board()
        self._current_mark = "X"

    def _switch_current_mark(self):
        if self._current_mark == "X":
            self._current_mark = "O"
        elif self._current_mark == "O":
            self._current_mark = "X"
        return self._current_mark

    def make_move(self, row: int, col: int):
        placeResult = self._board.place_mark(row, col, self._current_mark)
        if placeResult:
            self._switch_current_mark()
        return placeResult

    def check_status(self):
        status = None
        if self._board.has_won("X"):
            status = "X"
        elif self._


    def check_stalemate(self):
        return

    def check_whos_turn(self):
        return self._current_mark

    def get_grid(self):
        return self._board.__str__()
