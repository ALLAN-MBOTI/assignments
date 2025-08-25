import pytest
from price import calculate_discount


def test_discount_above_20_percent() -> None:
    """
    Test that a discount greater than 20% is applied correctly.
    """
    price = 100.0
    discount_percent = 25.0
    expected = 75.0  # 100 - (25% of 100)
    assert calculate_discount(price, discount_percent) == expected


def test_discount_exactly_20_percent() -> None:
    """
    Test that a discount exactly equal to 20% is applied.
    """
    price = 200.0
    discount_percent = 20.0
    expected = 160.0  # 200 - (20% of 200)
    assert calculate_discount(price, discount_percent) == expected


def test_discount_below_20_percent() -> None:
    """
    Test that no discount is applied if it is below 20%.
    """
    price = 150.0
    discount_percent = 15.0
    expected = 150.0  # No discount appliedS
    assert calculate_discount(price, discount_percent) == expected


def test_zero_discount() -> None:
    """
    Test that no discount is applied if discount percentage is zero.
    """
    price = 120.0
    discount_percent = 0.0
    expected = 120.0
    assert calculate_discount(price, discount_percent) == expected


def test_zero_price() -> None:
    """
    Test that a zero price always returns zero regardless of discount.
    """
    price = 0.0
    discount_percent = 50.0
    expected = 0.0
    assert calculate_discount(price, discount_percent) == expected


def test_negative_discount() -> None:
    """
    Test that a negative discount acts like a discount below 20%
    (no discount applied).
    """
    price = 80.0
    discount_percent = -10.0
    expected = 80.0
    assert calculate_discount(price, discount_percent) == expected
