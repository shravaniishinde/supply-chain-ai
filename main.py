from dotenv import load_dotenv
import os

load_dotenv()

# Simulated tools
def check_inventory(product):
    return f"{product} stock is low"

def find_supplier(product):
    return f"Best supplier for {product} is ABC Corp"

# Simple workflow
product = "laptop"

inventory_status = check_inventory(product)
print("Inventory:", inventory_status)

if "low" in inventory_status:
    supplier = find_supplier(product)
    print("Supplier:", supplier)