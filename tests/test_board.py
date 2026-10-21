from board import Board

def test_new_board_is_empty():
    board = Board()
    positions = board.empty_cells()
    assert len(positions) == 9

def test_empty_cells_detects_marks():
    board = Board()
    board.place_mark(0,0,"X")
    positions = board.empty_cells()
    assert len(positions) == 8

def test_placing_mark():
    board = Board()
    assert board.place_mark(0,0,"X")

def test_removing_mark():
    board = Board()
    board.place_mark(0,0,"X")
    board.remove_mark(0,0)
    assert board.empty_cells()