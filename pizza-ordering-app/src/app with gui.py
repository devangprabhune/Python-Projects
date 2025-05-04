import tkinter as tk
from tkinter import messagebox, ttk

class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza World Ordering System")
        self.root.geometry("500x500")  # Increased height to accommodate all elements
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TLabel', font=('Arial', 11))
        
        # Price mappings
        self.SIZES = {"S": 4, "M": 6, "L": 8}
        self.FLAVOURS = {
            "1": ["Pepperoni", 3],
            "2": ["Margherita", 1],
            "3": ["Veggie", 3],
            "4": ["Chicken", 4],
            "5": ["Pineapple", 3]
        }
        
        self.TOPPINGS = {
            "1": "Pepperoni",
            "2": "Olives",
            "3": "Tomato",
            "4": "Onion",
            "5": "Corn"
        }
        
        # Initialize variables
        self.bill = 0
        self.selected_size = ""
        self.selected_flavour = ""
        self.selected_toppings = []  # Now a list to store multiple toppings
        self.has_extra_cheese = False
        
        # Start the app
        self.create_welcome_screen()

    def clear_window(self):
        """Remove all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_welcome_screen(self):
        """Initial welcome screen with buttons."""
        self.clear_window()
        self.bill = 0  # Reset bill when starting over
        
        # Create a frame for better layout
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title = tk.Label(main_frame, text="Welcome to Pizza World!", font=("Arial", 18, "bold"))
        title.pack(pady=(0, 20))
        
        # Divider
        divider = tk.Frame(main_frame, height=2, bg="gray")
        divider.pack(fill="x", pady=10)
        
        # Question
        question = tk.Label(main_frame, text="Would you like to order a pizza?", font=("Arial", 12))
        question.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Yes/No buttons
        yes_btn = ttk.Button(button_frame, text="Yes", command=self.select_size, width=10)
        yes_btn.pack(side="left", padx=10)
        
        no_btn = ttk.Button(button_frame, text="No", command=self.show_goodbye, width=10)
        no_btn.pack(side="left", padx=10)

    def select_size(self):
        """Ask user to choose pizza size using radio buttons."""
        self.clear_window()
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title = tk.Label(main_frame, text="Select Pizza Size", font=("Arial", 16, "bold"))
        title.pack(pady=(0, 15))
        
        # Size selection variable
        self.size_var = tk.StringVar()
        
        # Create frame for radio buttons
        size_frame = tk.Frame(main_frame)
        size_frame.pack(pady=10)
        
        # Radio buttons for size
        sizes = [
            ("Small ($4)", "S"),
            ("Medium ($6)", "M"),
            ("Large ($8)", "L")
        ]
        
        for text, value in sizes:
            size_btn = ttk.Radiobutton(
                size_frame, 
                text=text, 
                variable=self.size_var, 
                value=value
            )
            size_btn.pack(anchor="w", pady=5)
        
        # Set default selection
        self.size_var.set("M")
        
        # Navigation buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20, side="bottom")
        
        back_btn = ttk.Button(button_frame, text="Back", command=self.create_welcome_screen, width=10)
        back_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Next", command=self.process_size, width=10)
        next_btn.pack(side="left", padx=10)

    def process_size(self):
        """Process the selected size and move to flavor selection."""
        size = self.size_var.get()
        if size in self.SIZES:
            self.selected_size = size
            self.bill += self.SIZES[size]
            self.select_flavour()
        else:
            messagebox.showerror("Error", "Please select a size.")

    def select_flavour(self):
        """Ask user to choose pizza flavor using radio buttons."""
        self.clear_window()
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title = tk.Label(main_frame, text="Select Pizza Flavor", font=("Arial", 16, "bold"))
        title.pack(pady=(0, 15))
        
        # Flavor selection variable
        self.flavour_var = tk.StringVar()
        
        # Create frame for radio buttons
        flavour_frame = tk.Frame(main_frame)
        flavour_frame.pack(pady=5)
        
        # Radio buttons for flavors
        for key, (name, price) in self.FLAVOURS.items():
            flavour_btn = ttk.Radiobutton(
                flavour_frame, 
                text=f"{name} (${price})", 
                variable=self.flavour_var, 
                value=key
            )
            flavour_btn.pack(anchor="w", pady=3)
        
        # Set default selection
        self.flavour_var.set("1")
        
        # Navigation buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20, side="bottom")
        
        back_btn = ttk.Button(button_frame, text="Back", command=self.select_size, width=10)
        back_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Next", command=self.process_flavour, width=10)
        next_btn.pack(side="left", padx=10)

    def process_flavour(self):
        """Process the selected flavor and move to toppings selection."""
        flavour = self.flavour_var.get()
        if flavour in self.FLAVOURS:
            self.selected_flavour = flavour
            self.bill += self.FLAVOURS[flavour][1]
            self.select_extra_toppings()
        else:
            messagebox.showerror("Error", "Please select a flavor.")

    def select_extra_toppings(self):
        """Ask user to select which extra toppings they want using checkboxes."""
        self.clear_window()
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title = tk.Label(main_frame, text="Select Extra Toppings", font=("Arial", 16, "bold"))
        title.pack(pady=(0, 15))
        
        # Information label
        info_label = tk.Label(main_frame, text="Each topping adds $2 to your order", font=("Arial", 12))
        info_label.pack(pady=(0, 10))
        
        # Create frame for checkboxes
        topping_frame = tk.Frame(main_frame)
        topping_frame.pack(pady=5)
        
        # Create checkbox variables
        self.topping_vars = {}
        
        # Checkboxes for toppings
        for key, name in self.TOPPINGS.items():
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(
                topping_frame, 
                text=name, 
                variable=var
            )
            checkbox.pack(anchor="w", pady=3)
            self.topping_vars[key] = var
        
        # Navigation buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20, side="bottom")
        
        back_btn = ttk.Button(button_frame, text="Back", command=self.select_flavour, width=10)
        back_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Next", command=self.process_topping_selections, width=10)
        next_btn.pack(side="left", padx=10)

    def process_topping_selections(self):
        """Process all selected toppings and move to cheese selection."""
        # Clear previous selections
        self.selected_toppings = []
        
        # Check which toppings were selected
        for key, var in self.topping_vars.items():
            if var.get():
                self.selected_toppings.append(key)
                # Add $2 for each selected topping
                self.bill += 2
        
        self.select_extra_cheese()

    def select_extra_cheese(self):
        """Ask if user wants extra cheese using buttons."""
        self.clear_window()
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title = tk.Label(main_frame, text="Extra Cheese", font=("Arial", 16, "bold"))
        title.pack(pady=(0, 15))
        
        # Question
        question = tk.Label(main_frame, text="Would you like extra cheese for $1?", font=("Arial", 12))
        question.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        # Yes/No buttons
        yes_btn = ttk.Button(button_frame, text="Yes", command=lambda: self.process_cheese(True), width=10)
        yes_btn.pack(side="left", padx=10)
        
        no_btn = ttk.Button(button_frame, text="No", command=lambda: self.process_cheese(False), width=10)
        no_btn.pack(side="left", padx=10)
        
        # Navigation - back button
        back_frame = tk.Frame(main_frame)
        back_frame.pack(pady=20, side="bottom")
        
        back_btn = ttk.Button(back_frame, text="Back", command=self.select_extra_toppings, width=10)
        back_btn.pack()

    def process_cheese(self, wants_cheese):
        """Process cheese selection and move to order summary."""
        self.has_extra_cheese = wants_cheese
        if wants_cheese:
            self.bill += 1
        self.show_order_summary()

    def show_order_summary(self):
        """Show a summary of the order and total bill."""
        self.clear_window()
        
        # Create a canvas with scrollbar to handle all content
        canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main frame inside scrollable area
        main_frame = tk.Frame(scrollable_frame, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title = tk.Label(main_frame, text="Order Summary", font=("Arial", 16, "bold"))
        title.pack(pady=(0, 15))
        
        # Create a frame for order details
        details_frame = tk.Frame(main_frame, relief=tk.GROOVE, borderwidth=1)
        details_frame.pack(fill="x", padx=10, pady=10)
        
        # Order details
        size_label = tk.Label(details_frame, text=f"Size: {self.selected_size} (${self.SIZES[self.selected_size]})", anchor="w")
        size_label.pack(fill="x", padx=10, pady=3)
        
        flavour_label = tk.Label(details_frame, 
                               text=f"Flavour: {self.FLAVOURS[self.selected_flavour][0]} (${self.FLAVOURS[self.selected_flavour][1]})", 
                               anchor="w")
        flavour_label.pack(fill="x", padx=10, pady=3)
        
        # Display all selected toppings
        if self.selected_toppings:
            toppings_header = tk.Label(details_frame, text="Extra Toppings:", anchor="w", font=("Arial", 10, "bold"))
            toppings_header.pack(fill="x", padx=10, pady=(3, 0))
            
            for topping_key in self.selected_toppings:
                topping_label = tk.Label(details_frame, 
                                      text=f"  • {self.TOPPINGS[topping_key]} ($2)", 
                                      anchor="w")
                topping_label.pack(fill="x", padx=10, pady=1)
        
        if self.has_extra_cheese:
            cheese_label = tk.Label(details_frame, text="Extra Cheese: Yes ($1)", anchor="w")
            cheese_label.pack(fill="x", padx=10, pady=3)
        
        # Total bill
        bill_label = tk.Label(main_frame, text=f"Total Bill: ${self.bill}", font=("Arial", 14, "bold"))
        bill_label.pack(pady=20)
        
        # Payment question
        payment_frame = tk.Frame(main_frame)
        payment_frame.pack(fill="x", pady=10)
        
        question = tk.Label(payment_frame, text="Would you like to pay now?", font=("Arial", 12))
        question.pack(pady=(0, 10))
        
        # Payment buttons frame
        payment_buttons = tk.Frame(payment_frame)
        payment_buttons.pack()
        
        # Yes/No buttons for payment - ensuring they're clearly visible
        yes_btn = ttk.Button(payment_buttons, text="Yes", command=lambda: self.process_payment(True), width=10)
        yes_btn.pack(side="left", padx=10)
        
        no_btn = ttk.Button(payment_buttons, text="No", command=lambda: self.process_payment(False), width=10)
        no_btn.pack(side="left", padx=10)
        
        # Back button in separate frame
        back_frame = tk.Frame(main_frame)
        back_frame.pack(pady=20, fill="x")
        
        back_btn = ttk.Button(back_frame, text="Back", command=self.select_extra_cheese, width=10)
        back_btn.pack()

    def process_payment(self, paid_now):
        """Process payment choice and show final message."""
        if paid_now:
            messagebox.showinfo("Payment Successful", "Payment processed successfully! Thank you!")
        else:
            messagebox.showinfo("Payment Later", "You can pay later. Your order is saved.")
        self.show_goodbye()

    def show_goodbye(self):
        """Final goodbye message with restart option."""
        self.clear_window()
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Thank you message
        thank_you = tk.Label(main_frame, text="Thank you for visiting Pizza World!", font=("Arial", 18, "bold"))
        thank_you.pack(pady=(20, 10))
        
        have_nice_day = tk.Label(main_frame, text="Have a great day!", font=("Arial", 14))
        have_nice_day.pack(pady=(0, 30))
        
        # Buttons frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Option to make another order or exit
        new_order_btn = ttk.Button(button_frame, text="New Order", command=self.create_welcome_screen, width=15)
        new_order_btn.pack(side="left", padx=10)
        
        exit_btn = ttk.Button(button_frame, text="Exit", command=self.root.quit, width=15)
        exit_btn.pack(side="left", padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()