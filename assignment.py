def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it meets the threshold.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage to apply (0-100)
        
    Returns:
        float: Final price after discount (if applicable), otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

def main():
    """
    Main function to handle user interaction for the discount calculator.
    """
    print("Discount Price Calculator")
    print("-------------------------")
    
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage (0-100): "))
        
        # Validate inputs
        if original_price <= 0:
            print("Error: Price must be a positive number.")
            return
        if discount_percent < 0 or discount_percent > 100:
            print("Error: Discount percentage must be between 0 and 100.")
            return
        
        # Calculate and display result
        final_price = calculate_discount(original_price, discount_percent)
        
        if discount_percent >= 20:
            print(f"\nApplied a {discount_percent}% discount.")
            print(f"Original price: ${original_price:.2f}")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (needs to be ≥20%). Price remains: ${original_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main()