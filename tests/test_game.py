from game import Game

def test_switching_mark():
    test_game = Game()
    test_game.make_move(0,0)
    assert test_game.check_whos_turn() == "O"

def test_making_move():
    test_game = Game()
    assert test_game.make_move(0,0)

def test_status():
    test_game = Game()
    assert test_game.check_status() == "Playing"

def test_whos_turn():
    test_game = Game()
    assert test_game.check_whos_turn() == "X"

def test_off_board_placement():
    test_game = Game()
    assert test_game.make_move(1,3) == False and test_game.check_whos_turn() == "X"

def test_negative_off_board_placement():
    test_game = Game()
    assert test_game.make_move(-1,0) == False and test_game.check_whos_turn() == "X"

def test_taken_cell():
    test_game = Game()
    test_game.make_move(0,0)
    assert test_game.make_move(0,0) == False and test_game.check_whos_turn() == "O"

def test_game_win_x():
    game = Game()
    game.make_move(0, 0)  # X
    game.make_move(1, 0)  # O
    game.make_move(0, 1)  # X
    game.make_move(1, 1)  # O
    game.make_move(0, 2)  # X wins
    assert game.check_status() == "X"

def test_game_win_o():
    game = Game()
    game.make_move(0, 0)  # X
    game.make_move(1, 0)  # O
    game.make_move(0, 1)  # X
    game.make_move(1, 1)  # O
    game.make_move(2, 2)  # X
    game.make_move(1, 2)  # O wins
    assert game.check_status() == "O"

def test_draw():
    game = Game()
    moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2),
    ]
    for row, col in moves:
        game.make_move(row, col)
    assert game.check_status() == "Draw"