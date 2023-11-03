import sys
sys.path.append('/Users/bogdanbalanik/University/labs/Algo-Labs/Algo_labs/src')

import unittest
from lab3 import pre_order_traversal, BinaryTree

class TestMinPrice(unittest.TestCase):

    def test_case_1(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        expected = [3, 9, 20]
        actual = pre_order_traversal(root)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        expected = [1, 2, 5, 3, 6, 7]
        actual = pre_order_traversal(root)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()