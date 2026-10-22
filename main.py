from game import Game
import time

def take_move_input(game: Game):
    print("\nIt's " + game.check_whos_turn() + "'s turn\n")
    clean_input = None

    while clean_input == None:
        move_input = input("Enter position (comma separated): ")
        print("\n")
        clean_input = check_valid_input(move_input,game)

    return clean_input

def check_valid_input(move_input: str, game: Game):
    clean_input = move_input.split(" ")

    # Check that exactly 2 values were entered
    if len(clean_input) != 2:
        print("\nPlease enter 2 values only!")
        return None

    # Check that both values are digits
    if not all(value.isdigit() for value in clean_input):
        print("\nPlease enter digits only!")
        return None

    clean_numbers = [int(value) for value in clean_input]

    # Check that both values are between 0 and 2
    if not all(1 <= num <= 3 for num in clean_numbers):
        print("\nPlease ensure entered values are between 1 and 3!")
        return None

    return clean_numbers

def game_loop(game: Game):

    while game.check_status() == "Playing":
        print(game.get_grid())
        clean_input = take_move_input(game)
        game.make_move(clean_input[0]-1,clean_input[1]-1)

    print(game.get_grid())

    if game.check_status() != "Draw":
        
        print("\n"+game._current_mark + " has won!!!\n")


def main():
    game = Game()
    print("Welcome to Tic-Tac-Toe!\n")
    game_loop(game)

if __name__ == "__main__":
    main()