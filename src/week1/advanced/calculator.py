"""
A simple calculator program that:
1. Asks the user for two numbers.
2. Asks for a mathematical operation (+, -, *, /).
3. Performs the operation and displays the result.
"""

from typing import Union


def calculate(num1: float, num2: float, operation: str) -> Union[float, str]:
    """
    Perform a calculation based on the provided operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The mathematical operation (+, -, *, /).

    Returns:
        Union[float, str]: The result of the calculation, or an error message.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."


def main() -> None:
    """
    Main program loop.
    Prompts the user for inputs and displays the calculation result.
    """
    # Prompt user for the first number
    num1: float = float(input("Enter the first number: "))

    # Prompt user for the second number
    num2: float = float(input("Enter the second number: "))

    # Prompt user for the mathematical operation
    operation: str = input("Enter operation (+, -, *, /): ").strip()

    # Perform calculation
    result: Union[float, str] = calculate(num1, num2, operation)

    # Display result
    if isinstance(result, float):
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()
