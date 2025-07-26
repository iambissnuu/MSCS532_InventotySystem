from product_manager import ProductManager
from stock_heap import StockHeap
from price_bst import PriceBST

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("P001", "Laptop", 5, 1000)
    manager.add_product("P002", "Mouse", 2, 20)
    manager.add_product("P003", "Keyboard", 8, 50)

    print("All Products:")
    for product in manager.get_all_products():
        print(f"{product.name} - Qty: {product.quantity} - Price: ${product.price}")

    print("\nLow Stock Items:")
    stock_heap = StockHeap(manager.get_all_products())
    for item in stock_heap.get_low_stock(2):
        print(f"{item.name}: {item.quantity} units")

    print("\nProducts Sorted by Price:")
    bst = PriceBST()
    for product in manager.get_all_products():
        bst.insert(product)

    for p in bst.inorder():
        print(f"{p.name}: ${p.price}")
