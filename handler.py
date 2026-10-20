from secret_games.first_game.first_game_main import first_secret_game

def main():
    choice = input("Please choose a number from 1 to 3 to select a game ")
    try:
        choice = int(choice)
        if choice == 1:
            first_secret_game()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            print("Invalid input. Please enter a number from 1 to 3.")
            exit()
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 3.")
        exit()