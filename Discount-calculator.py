def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Display the result
if final_price != original_price:
    print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
else:
    print("No discount applied. The original price is: ${:.2f}".format(original_price))
