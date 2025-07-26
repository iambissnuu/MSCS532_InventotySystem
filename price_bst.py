class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class PriceBST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = BSTNode(product)
        else:
            self._insert(self.root, product)

    def _insert(self, node, product):
        if product.price < node.product.price:
            if node.left is None:
                node.left = BSTNode(product)
            else:
                self._insert(node.left, product)
        else:
            if node.right is None:
                node.right = BSTNode(product)
            else:
                self._insert(node.right, product)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.product)
            self._inorder(node.right, result)
