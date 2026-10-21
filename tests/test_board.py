from board import Board

def test_new_board_is_empty():
    board = Board()
    assert board.empty_cells(board)
    

def test_place_mark_out_of_bounds():
    board = Board()
    assert board.place_mark(4,5,"X") == "Out"