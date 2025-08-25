from typing import Union


def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount if
               discount_percent is >= 20, otherwise the original price.
    """
    # Check if the discount is at least 20%
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount amount from original price
        return price - discount_amount
    else:
        # Return original price if discount is less than 20%
        return price


def main() -> None:
    """
    Main function to prompt user input and display the final price.
    """
    try:
        # Prompt user for original price
        price_input: str = input("Enter the original price KES: ")
        price: float = float(price_input)

        # Prompt user for discount percentage
        discount_input: str = input("Enter the discount percentage: ")
        discount_percent: float = float(discount_input)

        # Calculate final price
        final_price: float = calculate_discount(price, discount_percent)

        # Display result
        if discount_percent >= 20:
            print(f"Final price after discount KES: {final_price:.2f}")
        else:
            print(f"No discount applied. Price: {final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
