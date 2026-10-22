from board import Board

class Game():
    """Overall game logic, including playing turns, winning + other backend features"""

    def __init__(self):

        self._board = Board()
        self.current_mark = "X"

    def initalise_game(self):
        if len(self._board.empty_cells()) == 9:
            return
        else:
            self.call_error("ERROR: During board initalisation")

    def switch_current_mark(self):
        if self.current_mark == "X":
            self.current_mark = "O"
        elif self.current_mark == "O":
            self.current_mark = "X"
        else:
            self.call_error("ERROR: During switching mark")
        return self.current_mark

    def make_move(self, row: int, col: int):
        self._board.place_mark(row, col, self.current_mark)
        self.switch_current_mark()
        return

    def check_won(self):
        if self._board.has_won(self.current_mark) == True:
            return True, self.current_mark

    def check_whos_turn(self):
        return self.current_mark

    def get_grid(self):
        return self._board.__str__()

    def call_error(self, errorMsg: str):
        raise errorMsg