class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root: BinaryTree):
    if root is None:
        return []
    
    result = []
    result.append(root.value)
    result.extend(pre_order_traversal(root.left))
    result.extend(pre_order_traversal(root.right))
    
    return result
    