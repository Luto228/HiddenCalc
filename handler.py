from secret_games.first_game.first_game_main import first_secret_game
from secret_games.second_game.second_game_main import guess_random_number
from secret_games.third_game.third_game_main import counter_clicker

def main():
    choice = input("Please choose a number from 1 to 3 to select a game ")
    try:
        choice = int(choice)
        if choice == 1:
            first_secret_game()
        elif choice == 2:
            guess_random_number()
        elif choice == 3:
            counter_clicker()
        elif choice == 123321:
            print("Bye!")
            exit()
        else:
            print("Invalid input. Please enter a number from 1 to 3.")
            exit()
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 3.")
        exit()