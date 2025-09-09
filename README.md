# 📦 Inventory Management System

A **simple and interactive inventory management system** written in Python 🐍.  
This project demonstrates the use of **classes, lists, dictionaries, loops, functions, and input validation** in a clean, menu-driven program.

---

## ✨ Features

- ➕ Add new products with **SKU, name, and quantity**  
- 🔑 Ensures **unique SKUs** and prevents duplicate product names  
- ✅ Input validation for **empty fields, non-numeric values, and negative numbers**  
- 🛒 Process sales with proper **stock handling**  
- 📋 Identify products with **zero stock**  
- 🖥️ **Text-based interface** with modular and reusable code  
- 🚀 Ready for extensions like GUI integration or database storage  

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:** None (pure Python)  
- **Data Storage:** In-memory list of dictionaries (via `Product` objects)  

---

## 💻 Features Explained

1. **Object-Oriented Design**
   - `Product` class represents individual items.
   - `Inventory` class handles all operations: insertion, sale, stock updates, and zero-stock detection.

2. **Input Validation**
   - Prevents empty product names, negative or non-integer quantities.
   - Checks for duplicate SKUs and product names.

3. **Sales Processing**
   - Handles normal sales, insufficient stock, and SKU not found scenarios.
   - Updates inventory dynamically and prints informative messages.

4. **Zero Stock Identification**
   - Lists SKUs of items with zero stock to help with restocking.

5. **Inventory Listing**
   - Returns inventory as a clean list of `(SKU, Quantity)` tuples for further processing.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ishan1834/DSA-Class.git
cd inventory-management
````

### 2. Run the program

```bash
python inventory.py
```

---

## 📈 Next Steps / Extensions

* Add **restock functionality**
* Delete products from inventory
* Export inventory to CSV or database
* Add GUI using Tkinter or PyQt
* Integrate with barcode scanner

```

---

If you want, I can also make a **more “GitHub-friendly” version with badges, tables, and emojis**, so it looks really polished and eye-catching on your repository page.  

Do you want me to do that?
```
