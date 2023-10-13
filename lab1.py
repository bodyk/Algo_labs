import unittest

def traverse_zig_zag(matrix):
    result = []
    row = 0
    column = 0
    m = len(matrix)
    if m == 0:
        return result
    n = len(matrix[0])
    if n == 0:
        return result
    
    # Append first element
    result.append(matrix[row][column])
    while row + 1 < m or column + 1 < n:
        # Try move right
        if column + 1 < n:
            column += 1
            result.append(matrix[row][column])
        # We reached right side, move down
        elif row + 1 < m:
            row += 1
            result.append(matrix[row][column])

        #ZigZag downwards
        while row + 1 < m and column - 1 >= 0:
            if row + 1 < m:
                row += 1
            if column - 1 >= 0:
                column -= 1
            result.append(matrix[row][column])
        # Try move down
        if row + 1 < m:
            row += 1
            result.append(matrix[row][column])
        # We reached bottom side, move right
        elif column + 1 < n:
            column += 1
            result.append(matrix[row][column])

        #ZigZag upwards
        while column + 1 < n and row - 1 >= 0:
            if column + 1 < n:
                column += 1
            if row - 1 >= 0:
                row -= 1
            result.append(matrix[row][column])

    return result

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