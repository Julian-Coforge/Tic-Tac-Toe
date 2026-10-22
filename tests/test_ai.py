from ai import AIPlayer, EasyAI, HardAI
from board import Board
import random

def test_easy_returns_empty_cell():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")

    for seed in range(5):
        ai = EasyAI(random.Random(seed))
        move = ai.choose_move(board, "O")
        assert move in board.empty_cells()


def test_easy_does_not_change_board():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")

    empty_before = board.empty_cells()

    ai = EasyAI(random.Random(42))
    ai.choose_move(board, "O")

    assert board.empty_cells() == empty_before


def test_hard_does_not_change_board():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")

    empty_before = board.empty_cells()

    ai = HardAI()
    ai.choose_move(board, "O")

    assert board.empty_cells() == empty_before


def test_hard_takes_winning_move():
    board = Board()
    board.place_mark(0, 0, "O")
    board.place_mark(0, 1, "O")
    board.place_mark(1, 0, "X")
    board.place_mark(1, 1, "X")

    ai = HardAI()
    move = ai.choose_move(board, "O")

    assert move == (0, 2)


def test_hard_blocks_opponent():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 0, "O")
    board.place_mark(2, 1, "O")

    ai = HardAI()
    move = ai.choose_move(board, "O")

    assert move == (0, 2)


def test_hard_never_loses():
    ai = HardAI()

    def play_game(board):
        for row, col in board.empty_cells():
            board.place_mark(row, col, "X")

            assert not board.has_won("X")

            if not board.is_full():
                move = ai.choose_move(board, "O")
                board.place_mark(move[0], move[1], "O")

                if not board.has_won("O") and not board.is_full():
                    play_game(board)

                board.remove_mark(move[0], move[1])

            board.remove_mark(row, col)

    board = Board()
    play_game(board)