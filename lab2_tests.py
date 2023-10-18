import unittest
from lab2 import max_hamsters

class TestMaxHamsters(unittest.TestCase):

    def test_case_1(self):
        S = 7
        C = 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        expected = 2
        self.assertEqual(max_hamsters(S, C, hamsters), expected)

    def test_case_2(self):
        S = 19
        C = 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        expected = 3
        self.assertEqual(max_hamsters(S, C, hamsters), expected)

    def test_case_3(self):
        S = 2
        C = 2
        hamsters = [[1, 50000], [1, 60000]]
        expected = 1
        self.assertEqual(max_hamsters(S, C, hamsters), expected)


if __name__ == "__main__":
    unittest.main()