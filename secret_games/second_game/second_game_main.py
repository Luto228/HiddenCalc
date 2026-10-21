import random

def guess_random_number():
    random_num = random.randint(1, 1000)
    while True:
        user_input = input("Guess the number between 1 and 1000: ")
        try:
            user_guess = int(user_input)
            if user_guess == random_num:
                print("CORRECT!")
                break
            elif user_guess < random_num:
                print("▲")
            else:
                print("▼")
        except ValueError:
            print("Invalid input. Please enter a number.")