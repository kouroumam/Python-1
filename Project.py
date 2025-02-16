
#Project


#Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
#Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
#View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
#Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
#Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.


inventory = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    # Create a dictionary to store item details
    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    # Add the item to the inventory list
    inventory.append(item)
    print(f"{name} has been added to the inventory.\n")


def update_item():
    name = input("Enter the name of the item to update: ")

    # Search for the item by name
    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"Updating {name}...")

            # Ask for new details
            item["price"] = float(input("Enter new price: "))
            item["quantity"] = int(input("Enter new quantity: "))
            item["category"] = input("Enter new category: ")

            print(f"{name} has been updated.\n")
            return

    print(f"{name} not found in the inventory.\n")


def view_inventory():
    if not inventory:
        print("The inventory is empty.\n")
        return

    print("Current Inventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
        print()


def remove_item():
    name = input("Enter the name of the item to remove: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} has been removed from the inventory.\n")
            return

    print(f"{name} not found in the inventory.\n")


def search_by_category():
    category = input("Enter the category to search: ")
    found = False

    print(f"Items in category '{category}':")
    for item in inventory:
        if item["category"].lower() == category.lower():
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            found = True

    if not found:
        print(f"No items found in the category '{category}'.\n")
    print()


def main():
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 3.\n")

main()