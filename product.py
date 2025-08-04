class Product:
    def __init__(self, id, name, quantity, price):
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __lt__(self, other):
        return self.quantity < other.quantity
