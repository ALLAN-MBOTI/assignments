# Procedural version (no separate function)

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    print(f"Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Price remains: {price:.2f}")
