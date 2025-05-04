def validate_input(prompt, valid_options):
    response = input(prompt).strip().lower()
    while response not in valid_options:
        print("Invalid input! Please try again.")
        response = input(prompt).strip().lower()
    return response

def format_bill(bill):
    return f"${bill:.2f}"

def calculate_total(base_price, toppings_price):
    return base_price + toppings_price