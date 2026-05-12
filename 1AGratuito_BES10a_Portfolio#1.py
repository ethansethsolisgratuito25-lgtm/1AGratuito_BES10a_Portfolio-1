# Portfolio 1: Expressions
# Course: BES10a
# Student: Ethan Seth S. Gratuito

# --- Variables and Data Types ---
brand_name = input("Enter brand name: ")               # String
location = input("Enter pop-up location: ")            # String
shirts_to_sell = int(input("Enter inventory count: ")) # Integer conversion
price_per_shirt = float(input("Enter unit price: "))   # Float conversion
is_first_pop_up = True                                 # Boolean

# Simple calculation
projected_revenue = shirts_to_sell * price_per_shirt

# Output
print("\n--- Pop-Up Shop Details ---")
print("Brand:", brand_name)
print("Location:", location)
print("First time popping up?", is_first_pop_up)
print("Inventory count:", shirts_to_sell)
print("Price per item: P", price_per_shirt)
print("Projected Revenue: P", projected_revenue)
