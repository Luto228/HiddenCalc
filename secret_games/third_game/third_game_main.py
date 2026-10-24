import random

def counter_clicker():
    counter = 0
    required_number = random.randint(10, 634)
    while True:
        user_number = input(f"Obtain the number {required_number} by addition! ")
        try:
            current_user_number = int(user_number)
            if current_user_number > 9 or current_user_number <= -1:
                print("Write a number between 0 and 9!")
                continue 
            counter += current_user_number
            if counter == required_number:
                print("Win!")
                break 
            elif counter < required_number:
                print(f"Counter: {counter}")
            else:
                print(f"You have entered too large a number!")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")