from functions import calculate, is_valid_operator
from appSettings import decimal_places
from logs.logger import log_operation, log_history, show_history

memory = None

def set_decimal_places():
    global decimal_places 
    try:
        new_places = int(input("Enter the number of decimal places (0-10): "))
        if 0 <= new_places <= 10:
            decimal_places = new_places
            print(f"Decimal places set to {decimal_places}.")
        else:
            print("Please enter a valid number between 0 and 10.")
    except ValueError:
        print("Invalid input. Please try again.")

def get_input():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, ^, %, √): ")
        num2 = None
        if operator != '√':
            num2 = float(input("Enter the second number: "))
        return num1, operator, num2
    except ValueError:
        print("Invalid input. Please try again.")
        return get_input()

def store_in_memory(result):
    global memory
    memory = result
    print(f"Result {result} stored in memory.")

def recall_memory():
    if memory is not None:
        print(f"Stored value: {memory}")
        return memory
    else:
        print("Memory is empty.")
        return None

def ask_to_continue():
    return input("Do you want to perform another calculation? (yes/no): ").lower() == 'yes'

def calculator():
    print(f"Results will be displayed with {decimal_places} decimal places.")
    while True:
        num1, operator, num2 = get_input()

        if not is_valid_operator(operator):
            print("Invalid operator. Please try again. You can use only +, -, *, /, ^, % or √ ")
            continue

        try:
            result = calculate(num1, operator, num2)
            result = round(result, decimal_places)
            print(f"Result: {result}")
            store_in_memory(result)

            expression = f"{num1} {operator} {num2 if num2 is not None else ''}"
            log_operation(f"{expression} = {result}")
            log_history(expression, result) 

        except (ZeroDivisionError, ValueError) as e:
            print(e)

        if input("Do you want to view the calculation history? (yes/no): ").lower() == 'yes':
            show_history()

        if not ask_to_continue():
            break

if __name__ == "__main__":
    calculator()
