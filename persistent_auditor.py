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
