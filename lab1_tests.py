import unittest
from lab1 import traverse_zig_zag

class TestZigZagTraversal(unittest.TestCase):

    def test_case_1(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(traverse_zig_zag(matrix), expected)

    def test_case_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(traverse_zig_zag(matrix), expected)

    def test_case_3(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(traverse_zig_zag(matrix), expected)

    def test_case_4(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(traverse_zig_zag(matrix), expected)


if __name__ == "__main__":
    unittest.main()