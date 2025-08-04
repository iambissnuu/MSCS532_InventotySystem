from product import Product

class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, id, name, quantity, price):
        if id in self.products:
            raise ValueError(f"Product with ID {id} already exists.")
        self.products[id] = Product(id, name, quantity, price)

    def get_product(self, id):
        return self.products.get(id)

    def update_quantity(self, id, new_quantity):
        if id in self.products:
            self.products[id].quantity = new_quantity

    def get_all_products(self):
        return list(self.products.values())
