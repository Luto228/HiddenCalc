from base_calculator_func import run_calculator
from handler import main

if __name__ == "__main__":
    result = run_calculator()
    if result is not None:
        main()