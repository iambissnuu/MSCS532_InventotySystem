import unittest
from product import Product
from product_manager import ProductManager
from stock_heap import StockHeap
from avl_tree import AVLTree

class TestInventorySystem(unittest.TestCase):

    def test_add_product(self):
        pm = ProductManager()
        pm.add_product("P100", "TestProduct", 10, 100)
        self.assertEqual(len(pm.get_all_products()), 1)
        self.assertEqual(pm.get_product("P100").name, "TestProduct")

    def test_duplicate_product(self):
        pm = ProductManager()
        pm.add_product("P101", "Item", 5, 50)
        with self.assertRaises(ValueError):
            pm.add_product("P101", "Item", 5, 50)

    def test_low_stock_heap(self):
        pm = ProductManager()
        pm.add_product("P1", "A", 10, 10)
        pm.add_product("P2", "B", 2, 20)
        pm.add_product("P3", "C", 5, 5)
        sh = StockHeap(pm.get_all_products())
        low_stock = sh.get_low_stock(2)
        self.assertEqual(low_stock[0].name, "B")
        self.assertEqual(low_stock[1].name, "C")

    def test_price_bst(self):
        pm = ProductManager()
        pm.add_product("P1", "A", 1, 300)
        pm.add_product("P2", "B", 1, 100)
        pm.add_product("P3", "C", 1, 200)
        bst = AVLTree()
        root = None
        for p in pm.get_all_products():
            root = bst.insert(root, p)
        result = []
        bst.inorder(root, result)
        prices = [p.price for p in result]
        self.assertEqual(prices, sorted(prices))

if __name__ == '__main__':
    unittest.main()
