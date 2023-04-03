print("Welcome to the Snakes Cafe!\n")
print("Please check our menu below.")


menu_items = {

    "Appetizers":["Wings", "Cookies", "Spring Rolls"],
   "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
    
}

orders = {}


for category, items in menu_items.items():
    print(f"\n{category}\n{'-' * len(category)}")
    for item in items:
        print(item)

print("\nWhat would you like to order? (Type 'quit' to exit.)")




while True:
    order = input("> ")
    if order.lower() == "quit":
        break
    elif order.capitalize() in [item for sublist in menu_items.values() for item in sublist]:
        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1
        print(f"** {orders[order]} order of {order} has been added to your meal **")
    else:
        print("Sorry, we don't have that item on our menu. Please try again.")

if orders:
    print("\nHere is your order summary:")
    for item, count in orders.items():
        print(f"{count} {item}")
else:
    print("No orders received. Goodbye!")