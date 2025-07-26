# Dynamic Inventory Management System – Proof of Concept (Phase 2)

This project is a partial implementation of a **Dynamic Inventory Management System** developed in Python as part of an academic assignment. It focuses on demonstrating the core data structures and functionalities designed in Phase 1, including product management, stock prioritization, and price-based sorting.

## Project Structure

- `product.py` – Defines the `Product` class with attributes and comparison methods.
- `product_manager.py` – Manages the collection of products using a dictionary (hash table).
- `stock_heap.py` – Implements a min-heap to retrieve low-stock products.
- `price_bst.py` – Implements a simple unbalanced binary search tree for price sorting.
- `main.py` – Test script to demonstrate the core operations.

## 🔧 How to Run

1. Clone or download the repository.
2. Make sure you have Python 3 installed.
3. Run the `main.py` file:
   ```bash
   python main.py
