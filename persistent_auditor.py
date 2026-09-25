def get_valid_input():
    # Handles prompt and input validation.
    # Returns an integer delivery amount, or the string 'quit'.
    # Returns None for invalid inputs.
    user_input = input("Enter stock quantity or 'quit': ").strip()
    
    if user_input.lower() == "quit":
        return "quit"
    
    try:
        val = int(user_input)
        if val < 0:
            print("ERROR! Please enter a positive integer.")
            return None
        return val
    except ValueError:
        print("ERROR! Please enter a valid integer or 'quit' to exit.")
        return None


def process_delivery(current_total, new_value):
    # Calculates and returns the new inventory total.
    return current_total + new_value


def calculate_tax(amount):
    # Calculates 10% tax for a specific delivery amount.
    return amount * 0.10