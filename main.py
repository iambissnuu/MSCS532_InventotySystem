from product_manager import ProductManager
from stock_heap import StockHeap
from avl_tree import AVLTree

manager = ProductManager()
manager.add_product("P001", "Laptop", 5, 1000)
manager.add_product("P002", "Mouse", 2, 20)
manager.add_product("P003", "Keyboard", 8, 50)

print("Low-stock items:")
stock_heap = StockHeap(manager.get_all_products())
for item in stock_heap.get_low_stock(2):
    print(f"{item.name} - {item.quantity} left")

print("\nPrice-sorted products:")
avl = AVLTree()
root = None
for product in manager.get_all_products():
    root = avl.insert(root, product)
sorted_by_price = []
avl.inorder(root, sorted_by_price)
for p in sorted_by_price:
    print(f"{p.name} - ${p.price}")
