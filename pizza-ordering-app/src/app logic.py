print("Welcome to Pizza World")
print("=" * 50)

# Price mappings
SIZES = {"S": 4, "M": 6, "L": 8}
FLAVOURS = {
    "1": 3,  # Pepperoni
    "2": 1,  # Margherita
    "3": 3,  # Veggie
    "4": 4,  # Chicken
    "5": 3   # Pineapple
}

def get_valid_input(prompt, valid_options):
    """Prompt user until valid input is received."""
    while True:
        user_input = input(prompt).strip().upper()  # Changed to upper() for case insensitivity
        if user_input.lower() in [opt.lower() for opt in valid_options]:  # Case-insensitive comparison
            return user_input.upper() if user_input.upper() in SIZES else user_input.lower()  # Return uppercase for sizes
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def get_order():
    return get_valid_input("Would you like to order a Pizza (yes/no)? ", ["yes", "no"])

def get_size():
    print("S $4\nM $6\nL $8")
    return get_valid_input("What size would you like (S/M/L)? ", ["S", "M", "L"])  # Explicitly use uppercase

def get_flavour():
    print("Select Flavour: ")
    print("1. Pepperoni $3\n2. Margherita $1\n3. Veggie $3\n4. Chicken $4\n5. Pineapple $3")
    return get_valid_input("What flavour would you like? ", FLAVOURS.keys())

def get_extra_toppings():
    """Get multiple extra topping selections (1–5)"""
    print("Select extra toppings ($2 each):")
    print("1. Pepperoni\n2. Olives\n3. Tomato\n4. Onion\n5. Corn")
    print("Enter topping numbers separated by commas (e.g., 1,3,5) or 'done' when finished:")
    
    selected_toppings = []
    valid_options = [str(i) for i in range(1, 6)]
    
    while True:
        selection = input("> ").strip()
        
        if selection.lower() == 'done':
            break
            
        # Split by commas and process each number
        for item in selection.split(','):
            item = item.strip()
            if item in valid_options and item not in selected_toppings:
                selected_toppings.append(item)
            elif item not in valid_options:
                print(f"Invalid option: {item}. Please enter numbers 1-5.")
        
        print(f"Current selections: {', '.join(selected_toppings)}")
        print("Enter more toppings or type 'done' to finish")
    
    return selected_toppings

def calculate_bill(size, flavour, extra_toppings_list, extra_cheese):
    bill = SIZES[size] + FLAVOURS[flavour]
    # Add $2 for each selected topping
    bill += len(extra_toppings_list) * 2
    if extra_cheese == "yes":
        bill += 1
    return bill

def main():
    print("Welcome to Pizza World!")
    order = get_order()
    
    if order == "yes":
        size = get_size()
        flavour = get_flavour()
        
        extra_toppings_list = []
        extra_toppings = get_valid_input("Would you like extra toppings ($2 each) (yes/no)? ", ["yes", "no"])
        if extra_toppings == "yes":
            print("You can select multiple toppings. Each topping costs $2.")
            extra_toppings_list = get_extra_toppings()
            
            if not extra_toppings_list:
                print("No extra toppings selected.")
            else:
                print("Selected toppings:")
                for topping in extra_toppings_list:
                    if topping == "1":
                        print("- Pepperoni")
                    elif topping == "2":
                        print("- Olives")
                    elif topping == "3":
                        print("- Tomato")
                    elif topping == "4":
                        print("- Onion")
                    elif topping == "5":
                        print("- Corn")
        else:
            print("No extra toppings selected.")
        
        extra_cheese = get_valid_input("Extra Cheese for $1 (yes/no)? ", ["yes", "no"])

        bill = calculate_bill(size, flavour, extra_toppings_list, extra_cheese)
        print(f"\nYour total bill is ${bill}")
        
        payment = get_valid_input("Would you like to pay now (yes/no)? ", ["yes", "no"])
        if payment == "yes":
            print("Please pay at the counter. Payment processed successfully!")
        else:
            print("You can pay later. Your order is saved.")
    
    print("\nThank you for visiting Pizza World! Have a great day!")

if __name__ == "__main__":
    main()