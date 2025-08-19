inventory = []

def insert_product():
    sku = input("enter the sku: ").strip()
    if not sku:
        print(" it cannot be empty.")
        return
    if any(item['sku'].lower() == sku.lower() for item in inventory):
        print("This SKU already exists.")
        return

    name = input("enter product name: ").strip()
    if not name:
        print("product name cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        if quantity < 0:
            print("quantity cannot be negative.")
            return
    except ValueError:
        print("quantity must be a number.")
        return

    inventory.append({'sku': sku, 'name': name, 'quantity': quantity})
    print("Product added.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nSKU\t\tProduct Name\t\tQuantity")
    print("-" * 40)
    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")

def main():
    while True:
        print("\n1. insert New Product\n2. Display Inventory\n3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == '1':
            insert_product()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            print("cya!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
