
inventory = {
    "Laptop": {"price": 1200, "stock": 50},
    "Mouse": {"price": 25, "stock": 200}
}

while True:
    print("\nChoose an action: view_stock / sell_item / add_stock / quit")
    action = input("Enter action: ")

    if action == "view_stock":
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item} - Price: ${details['price']}, Stock: {details['stock']}")

    elif action == "sell_item":
        item_name = input("Enter item name to sell: ")
        if item_name in inventory:
            try:
                quantity = int(input("Enter quantity to sell: "))
                if inventory[item_name]["stock"] >= quantity:
                    inventory[item_name]["stock"] -= quantity
                    print(f"Sold {quantity} {item_name}(s).")
                else:
                    print("Insufficient stock.")
            except ValueError:
                print("Invalid quantity.")
        else:
            print("Item not found.")

    elif action == "add_stock":
        item_name = input("Enter item name to restock: ")
        if item_name in inventory:
            try:
                quantity_to_add = int(input("Enter quantity to add: "))
                inventory[item_name]["stock"] += quantity_to_add
                print(f"Added {quantity_to_add} to {item_name} stock.")
            except ValueError:
                print("Invalid quantity.")
        else:
            print("Item not found.")

    elif action == "quit":
        print("Exiting inventory manager.")
        break

    else:
        print("Invalid action. Try again.")
