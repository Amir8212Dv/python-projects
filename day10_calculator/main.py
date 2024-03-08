from logo import logo
from math_operations import operations
from util import clear_lines

print(logo)


def calculator(first_number, history_lines=0):
    if first_number == None:
        clear_lines(history_lines)
        history_lines = 0
        first_number = float(input("What's the first number? "))

    operation_symbol = input("+\n-\n*\n/\nPick an operation: ")
    while operation_symbol not in operations:
        clear_lines(5)
        operation_symbol = input("+\n-\n*\n/\nPlease enter a valid operation: ")

    second_number = float(input("What's the next number? "))

    clear_lines(7)
    result = operations[operation_symbol](first_number, second_number)
    print(f"{first_number} {operation_symbol} {second_number} = {result}")

    continue_with_result = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    )
    clear_lines(1)

    if continue_with_result == "y":
        print("\n")
        calculator(result, history_lines + 2)
    else:
        calculator(None, history_lines + 1)


calculator(None)
