class AVLNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, product):
        if not node:
            return AVLNode(product)
        if product.price < node.product.price:
            node.left = self.insert(node.left, product)
        else:
            node.right = self.insert(node.right, product)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Rotate if unbalanced
        if balance > 1 and product.price < node.left.product.price:
            return self.right_rotate(node)
        if balance < -1 and product.price >= node.right.product.price:
            return self.left_rotate(node)
        if balance > 1 and product.price >= node.left.product.price:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and product.price < node.right.product.price:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.product)
            self.inorder(node.right, result)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x
