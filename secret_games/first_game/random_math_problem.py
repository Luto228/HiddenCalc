import random

def random_math_problem():
    ops = ['+', '-', '*', '/']
    op = random.choice(ops)
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    math_problem = f"{a} {op} {b}"
    answer = eval(math_problem)
    return math_problem, answer