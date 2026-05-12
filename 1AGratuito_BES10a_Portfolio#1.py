# Portfolio 1: Expressions
# Course: BES10a
# Student: Ethan Seth S. Gratuito

brand_name = input("Enter brand name: ")
location = input("Enter pop-up location: ")
shirts_to_sell = int(input("Enter inventory count: "))
price_per_shirt = float(input("Enter unit price: "))
is_first_pop_up = True

projected_revenue = shirts_to_sell * price_per_shirt

print("\n--- Pop-Up Shop Details ---")
print("Brand:", brand_name)
print("Location:", location)
print("First time popping up?", is_first_pop_up)
print("Inventory count:", shirts_to_sell)
print("Price per item: P", price_per_shirt)
print("Projected Revenue: P", projected_revenue)
