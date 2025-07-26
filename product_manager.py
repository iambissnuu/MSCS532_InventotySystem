from product import Product

class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, id, name, quantity, price):
        if id not in self.products:
            self.products[id] = Product(id, name, quantity, price)

    def update_quantity(self, id, quantity):
        if id in self.products:
            self.products[id].quantity = quantity

    def get_product(self, id):
        return self.products.get(id)

    def get_all_products(self):
        return list(self.products.values())
