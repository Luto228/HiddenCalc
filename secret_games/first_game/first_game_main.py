from secret_games.first_game.random_math_problem import random_math_problem

def first_secret_game():
    print("Welcome! P.S: If it is a floating-point number, enter only the first 3 digits after the decimal point.")
    while True: 
        math_problem, answer = random_math_problem()
        try:
            user_answer = float(input(math_problem + " = "))
            if user_answer == float(answer):
                print("CORRECT!")
            else:
                print(f"INCORRECT! \nCorrect answer: {answer}")
                break
        except ValueError:
            print(f"Invalid input. Please enter a number. Correct: {answer}")