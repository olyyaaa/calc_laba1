from const_GlobalVariables.operators import OPERATORS
import math

def handle_zero_division():
    raise ZeroDivisionError("Error: Division by zero!")

def handle_invalid_operator():
    raise ValueError("Error: Invalid operator")

def handle_negative_sqrt():
    raise ValueError("Error: Cannot take square root of a negative number!")

def calculate(num1, operator, num2=None):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            handle_zero_division()  
        return num1 / num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    elif operator == '√':
        if num1 < 0:
            handle_negative_sqrt()  
        return math.sqrt(num1)
    else:
        handle_invalid_operator() 

def is_valid_operator(operator):
    return operator in OPERATORS
