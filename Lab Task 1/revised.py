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

        self.products[sku] = Product(sku, name, quantity)
        return f"Product {name} inserted successfully."

    def update_quantity(self, sku, new_quantity):
        if sku not in self.products:
            return "Error: Product not found."
        if not isinstance(new_quantity, int) or new_quantity <= 0:
            return "Error: Invalid quantity."
        self.products[sku].quantity = new_quantity
        return f"Quantity for {sku} updated successfully."

    def search_by_sku(self, sku):
        return str(self.products.get(sku, "Error: Product not found."))

    def search_by_name(self, name):
        results = [str(p) for p in self.products.values() if p.name.lower() == name.lower()]
        return "\n".join(results) if results else "Error: Product not found."

    def delete_product(self, sku):
        if sku in self.products:
            removed = self.products.pop(sku)
            return f"Product {removed.name} removed from inventory."
        return "Error: Product not found."

    def display_inventory(self):
        if not self.products:
            return "Inventory is empty."
        return "\n".join(str(p) for p in self.products.values())


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    inv = Inventory(capacity=5)

    print(inv.insert_product("P101", "Pencil", 50))        # TC01
    print(inv.insert_product("P101", "Pen", 20))           # TC02
    print(inv.insert_product("P102", "Pen", 20))           # TC03
    print(inv.insert_product("P103", "Eraser", 10))        # TC03
    print(inv.insert_product("P104", "Marker", "ten"))     # TC04
    print(inv.search_by_sku("P101"))                       # TC05
    print(inv.search_by_name("Eraser"))                    # TC06
    print(inv.insert_product("P105", "", 5))               # TC07
    print(inv.insert_product("P106", "Notebook", -10))     # TC08
    print(inv.delete_product("P102"))                      # TC09
    print(inv.display_inventory())                         # TC10
    print(inv.insert_product("P107", "Pen", 12))           # TC12
    print(inv.update_quantity("P101", 100))                # TC13
    print(inv.delete_product("P103"))                      # TC14
    print(inv.display_inventory())                         # Final State
