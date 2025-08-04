# Dynamic Inventory Management System

This project demonstrates a dynamic inventory management system using core data structures implemented in Python. The primary focus is on using a Min-Heap to track low-stock items and an AVL Tree to sort products by price efficiently.

## Files and Descriptions

- `product.py`: Defines the `Product` class with attributes like ID, name, quantity, and price.
- `product_manager.py`: Handles the creation and management of product records.
- `stock_heap.py`: Implements a Min-Heap to find the lowest stock items.
- `avl_tree.py`: Implements an AVL Tree to maintain products sorted by price.
- `main.py`: Small demonstration using predefined products.
- `simulate_large_dataset.py`: Runs a simulation with 1000 randomly generated products.
- `test.py`: Optional file used for testing methods and outputs.
- `Inventory_System_Phase3.pdf`: Final project report.
- `README.md`: This documentation file.

## How to Run

To run the small demo with a few predefined products and the simulation with 1000 randomly generated products:
```bash
python main.py

python simulate_large_dataset.py
