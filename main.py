from game import Game
from ai import AIPlayer, HardAI, EasyAI
import random

def take_move_input(game: Game):
    """Keep asking the player for a move until they enter a valid one."""
    print("\nIt's " + game.check_whos_turn() + "'s turn\n")
    clean_input = None

    while clean_input == None:
        move_input = input("Enter position (space separated): ")
        print("\n")
        clean_input = check_valid_input(move_input,game)

    return clean_input

def check_valid_input(move_input: str, game: Game):
    """Return [row, col] if the input is 2 numbers from 1 to 3, otherwise print an error and return None."""
    clean_input = move_input.strip().split(" ")

    if len(clean_input) != 2:
        print("\nPlease enter 2 values only!")
        return None

    if not all(value.isdigit() for value in clean_input):
        print("\nPlease enter digits only!")
        return None

    # Convert the text to numbers
    clean_numbers = [int(value) for value in clean_input]

    if not all(1 <= num <= 3 for num in clean_numbers):
        print("\nPlease ensure entered values are between 1 and 3!")
        return None

    return clean_numbers

def game_loop(game: Game):
    """Play turns until someone wins or the board is full, then print the result."""
    while game.check_status() == "Playing":
        print(game.get_grid())
        if game.is_ai_turn() == True:
                move = game.play_ai_turn()
                # Show the AI's move counting from 1, like the player's input
                print("\nThe AI has played: " + str(move[0]+1) + " " + str(move[1]+1) + "\n")
        else: 
            clean_input = take_move_input(game)
            # Player enters 1-3, the board counts from 0
            game.make_move(clean_input[0]-1,clean_input[1]-1)
            game.check_status()

    print(game.get_grid())

    if game.check_status() != "Draw":
        print("\n"+game.check_status()+" has won!!!\n")
    else:
        print("\nThe game was a draw...\n")

def menu_input(prompt, choices: list):
    """Keep asking until the player enters one of the allowed choices."""
    output = input(prompt).strip()
    while output not in choices:
        output = input("Invalid input, please choose a valid input: \n").strip()
    return output
            

def main():
    """Show the menus, set up the chosen game mode and start the game."""
    print("Welcome to Tic-Tac-Toe!\n")
    selection = menu_input("Would you like to play against: Another player [1] or AI [2]\n",["1","2"])
    # Selection 2 = play against the AI, otherwise 2-player
    if selection == "2":
        ai_selection = menu_input("Would you like to play against: Easy AI [1] or Hard AI [2]\n",["1","2"])
        if ai_selection == "1":
            game = Game(EasyAI(random.Random()))
        else:
            game = Game(HardAI(random.Random()))
    else:
        game = Game()
    
    game_loop(game)

if __name__ == "__main__":
    main()