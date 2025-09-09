class Product:
    def __init__(self, sku, name, quantity):
        self.sku = sku
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"SKU: {self.sku}, Name: {self.name}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self, capacity=100):
        self.products = {}
        self.capacity = capacity

    def insert_product(self, sku, name, quantity):
        if not name.strip():
            return "Error: Product name cannot be empty."
        if not isinstance(quantity, int):
            return "Error: Invalid quantity."
        if quantity <= 0:
            return "Error: Quantity must be positive."
        if len(self.products) >= self.capacity:
            return "Error: Inventory capacity exceeded."
        if sku in self.products:
            return "Error: Duplicate SKU. Product already exists."
        for p in self.products.values():
            if p.name.lower() == name.lower():
                return f"Error: Product with name '{name}' already exists."
        self.products[sku] = Product(sku, name, quantity)
        return f"Product {name} inserted successfully."

    def update_quantity(self, sku, new_quantity):
        if sku not in self.products:
            return "Error: Product not found."
        if not isinstance(new_quantity, int) or new_quantity < 0:
            return "Error: Invalid quantity."
        self.products[sku].quantity = new_quantity
        return f"Quantity for {sku} updated successfully."

    def process_sale(self, sku, qty_sold):
        if sku not in self.products:
            msg = f"SKU {sku} not found in inventory."
            print(msg)
            return self.get_inventory_list(), msg
        product = self.products[sku]
        if product.quantity >= qty_sold:
            product.quantity -= qty_sold
            msg = f"Sale processed: {qty_sold} units of SKU {sku}."
        else:
            msg = f"Insufficient stock for SKU {sku}. Available: {product.quantity}"
        print(msg)
        return self.get_inventory_list(), msg

    def identify_zero_stock(self):
        zero_stock = [p.sku for p in self.products.values() if p.quantity == 0]
        if zero_stock:
            msg = f"Zero stock SKUs: {zero_stock}"
        else:
            msg = "No zero stock items found."
        print(msg)
        return zero_stock, msg

    def get_inventory_list(self):
        return [(p.sku, p.quantity) for p in self.products.values()]


if __name__ == "__main__":
    inv = Inventory()

    # Example test case execution

    # TC1 – Normal Sale
    inv.insert_product(101, "Pencil", 50)
    inventory, msg = inv.process_sale(101, 30)
    print("Inventory:", inventory)

    # TC2 – Insufficient Stock
    inv.insert_product(102, "Pen", 20)
    inventory, msg = inv.process_sale(102, 25)
    print("Inventory:", inventory)

    # TC3 – SKU Not Found
    inventory, msg = inv.process_sale(104, 10)
    print("Inventory:", inventory)

    # TC4 – Zero Stock Detection
    inv.insert_product(103, "Eraser", 0)
    zero_stock, msg = inv.identify_zero_stock()

    # TC5 – No Zero Stock
    inv2 = Inventory()
    inv2.insert_product(101, "Pencil", 10)
    inv2.insert_product(102, "Pen", 5)
    zero_stock, msg = inv2.identify_zero_stock()

    # TC6 – Sale Reducing to Zero
    inv3 = Inventory()
    inv3.insert_product(101, "Pencil", 10)
    inventory, msg = inv3.process_sale(101, 10)
    print("Inventory:", inventory)

