import os
from datetime import datetime

class InventoryManager:
    def __init__(self, inventory_file="Inventory.txt", sales_file="sales.txt"):
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        self.initialize_files()
        
    def initialize_files(self):
        """Initialize inventory and sales files if they don't exist"""
        # Create inventory file if it doesn't exist
        if not os.path.exists(self.inventory_file):
            initial_inventory = [
                "101,Laptop,1000,50",
                "102,Mouse,25,100",
                "103,Keyboard,45,75",
                "104,Monitor,200,30",
                "105,Headphones,50,120",
                "106,Webcam,35,22",
                "107,USB Drive,15,200",
                "108,External HDD,80,45",
                "109,Printer,150,5",
                "110,Scanner,120,20"
            ]
            with open(self.inventory_file, 'w') as f:
                f.write('\n'.join(initial_inventory))
                
        # Create sales file if it doesn't exist
        if not os.path.exists(self.sales_file):
            with open(self.sales_file, 'w') as f:
                f.write("Customer Name,Phone,Email,Product ID,Quantity,Amount,Transaction Time\n")
    
    def display_inventory(self):
        """Display current inventory"""
        with open(self.inventory_file, 'r') as fd:
            products = fd.read().splitlines()
            
        print("Current Inventory:")
        print("-" * 50)
        print("ID   | Name              | Price  | Quantity")
        print("-" * 50)
        for prod in products:
            prod_id, name, price, qty = prod.split(",")
            print(f"{prod_id:4} | {name:17} | ${price:6} | {qty:8}")
        print("-" * 50)
        return products
    
    def process_sale(self, customer_name, phone, email, product_id, quantity):
        """Process a sale transaction"""
        try:
            # Read current inventory
            with open(self.inventory_file, 'r') as fd:
                products = fd.read().splitlines()
            
            # Validate inputs
            if not str(phone).isdigit():
                raise ValueError("Phone number must contain only digits")
            if not quantity.isdigit():
                raise ValueError("Quantity must be a positive number")
            
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")
            
            # Process sale
            product_found = False
            updated_products = []
            
            for prod in products:
                prod_details = prod.split(",")
                
                if prod_details[0] == product_id:
                    product_found = True
                    available_stock = int(prod_details[3])
                    
                    if quantity > available_stock:
                        raise ValueError(f"Requested quantity ({quantity}) exceeds available stock ({available_stock})")
                    
                    # Calculate sale details
                    price = int(prod_details[2])
                    total_amount = quantity * price
                    
                    # Update inventory
                    prod_details[3] = str(available_stock - quantity)
                    
                    # Record sale
                    transaction_time = datetime.now().strftime("%d/%m/%Y %I:%M %p")
                    sale_record = f"{customer_name},{phone},{email},{product_id},{quantity},${total_amount},{transaction_time}\n"
                    
                    with open(self.sales_file, 'a') as sales_fd:
                        sales_fd.write(sale_record)
                    
                    # Print receipt
                    print("\nSale Receipt")
                    print("-" * 30)
                    print(f"Product: {prod_details[1]}")
                    print(f"Price: ${price}")
                    print(f"Quantity: {quantity}")
                    print(f"Total Amount: ${total_amount}")
                    print("-" * 30)
                
                updated_products.append(",".join(prod_details))
            
            if not product_found:
                raise ValueError(f"Product ID {product_id} not found")
            
            # Update inventory file
            with open(self.inventory_file, 'w') as fd:
                fd.write('\n'.join(updated_products))
                
            return True
            
        except Exception as e:
            print(f"Error processing sale: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize system
    inventory_system = InventoryManager()
    
    # Display current inventory
    products = inventory_system.display_inventory()
    
    # Get customer input
    print("\nEnter Customer Details")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    prod_id = input("Product ID: ")
    qty = input("Quantity: ")
    
    # Process sale
    inventory_system.process_sale(name, phone, email, prod_id, qty)
    
    # Display updated inventory
    print("\nUpdated Inventory:")
    inventory_system.display_inventory()
