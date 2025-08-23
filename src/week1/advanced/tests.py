"""
Unit tests for the calculator module.
Covers all valid operations, error handling, and edge cases.
"""

import pytest
from calculator import calculate


@pytest.mark.parametrize(
    "num1, num2, operation, expected",
    [
        # --- Basic operations ---
        (10, 5, "+", 15),
        (10, 5, "-", 5),
        (10, 5, "*", 50),
        (10, 5, "/", 2),

        # --- Division by zero ---
        (10, 0, "/", "Error: Division by zero is not allowed."),

        # --- Invalid operations ---
        (10, 5, "%", "Error: Invalid operation."),
        (10, 5, "x", "Error: Invalid operation."),  # lowercase x
        (10, 5, "X", "Error: Invalid operation."),  # uppercase X

        # --- Negative numbers ---
        (-5, -3, "+", -8),
        (5, -3, "*", -15),
        (-10, 5, "/", -2),

        # --- Floating point numbers ---
        (2.5, 0.5, "+", 3.0),
        (7.5, 2.5, "/", 3.0),
        (1e-10, 1e-10, "+", 2e-10),  # very small numbers

        # --- Whitespace in operation ---
        (5, 5, " + ", 10),
        (5, 5, "   *", 25),

        # --- Very large numbers ---
        (1e10, 1e10, "+", 2e10),
        (1e10, 1e5, "/", 1e5),

        # --- Zero as first number ---
        (0, 5, "+", 5),
        (0, 5, "*", 0),
        (0, 5, "-", -5),

        # --- Zero as second number (non-division) ---
        (5, 0, "+", 5),
        (5, 0, "-", 5),
        (5, 0, "*", 0),

        # --- Integer division result should be float ---
        (5, 2, "/", 2.5),
    ]
)
def test_calculate(num1, num2, operation, expected) -> None:
    """
    Test the calculate function with:
    - Standard arithmetic operations
    - Error handling for invalid operations and division by zero
    - Negative numbers
    - Floating point and very small numbers
    - Whitespace in operation
    - Very large numbers
    - Zero handling in different positions
    - Decimal correctness for division
    """
    # Perform calculation with stripped operation for consistency
    result = calculate(num1, num2, operation.strip())

    # Assert result matches expectation
    assert result == expected
