from secret_games.first_game.random_math_problem import random_math_problem

def first_secret_game():
    while True: 
        math_problem, answer = random_math_problem()
        try:
            user_answer = int(input(math_problem + " = "))
            if user_answer == int(answer):
                print("CORRECT!")
            else:
                print(f"INCORRECT! \nCorrect answer: {answer}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")