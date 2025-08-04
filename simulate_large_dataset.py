import random
from product_manager import ProductManager
from stock_heap import StockHeap
from avl_tree import AVLTree

pm = ProductManager()

# Generate 1000 random products
for i in range(1000):
    pid = f"P{i:04d}"
    name = f"Item{i}"
    qty = random.randint(0, 100)
    price = round(random.uniform(5, 500), 2)
    pm.add_product(pid, name, qty, price)

# Test heap (find 10 lowest stock)
stock_heap = StockHeap(pm.get_all_products())
low_stock = stock_heap.get_low_stock(10)
print(f"{len(low_stock)} Low Stock Items:")
for p in low_stock:
    print(f"{p.name} - Qty: {p.quantity}")

# Test AVL Tree (sorted by price)
bst = AVLTree()
root = None
for p in pm.get_all_products():
    root = bst.insert(root, p)

sorted_by_price = []
bst.inorder(root, sorted_by_price)

print("\nFirst 10 Products by Price:")
for p in sorted_by_price[:10]:
    print(f"{p.name} - Price: ${p.price}")
