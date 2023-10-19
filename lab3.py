class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def pre_order_traversal(node):
    if node:
        current_value = [node.value]
        left_values = pre_order_traversal(node.left)
        right_values = pre_order_traversal(node.right)
        return current_value + left_values + right_values
    else:
        return []

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.right = BinaryTree(5)

print(pre_order_traversal(root))