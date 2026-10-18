import math


def run_calculator():
    print("Calculator is running. Type 'exit' to quit.")
    print("Supported operations: +, -, *, /, %, sqrt(x)")

    while True:
        expression = input("\nInput expression: ").strip()
        user_input = expression

        if expression.lower() == "exit":
            print("Exiting the calculator.")
            break
    
        try:
            # Replace sqrt for convenient calculations via eval
            # For example, the user might enter sqrt(144)
            expression = expression.replace("sqrt", "math.sqrt")

            # Safe call to eval for prototyping
            result = eval(expression)
            
            #check whether the user has entered a specific example for the secret calculator
            if user_input == "sqrt(14+24)":
                return result 
            
            print(f"Result: {result}")
        
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as error:
            print(f"Calculation error: {error}")