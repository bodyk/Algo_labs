import unittest
from src.lab2 import min_price

class TestMinPrice(unittest.TestCase):

    def test_case_1(self):
        product_prices = [50, 20, 30, 17, 100]
        discount = 10
        expected = 207.0
        self.assertEqual(min_price(product_prices, discount), expected)

    def test_case_2(self):
        product_prices = [1, 2, 3, 4, 5, 6, 7]
        discount = 100
        expected = 15.0
        self.assertEqual(min_price(product_prices, discount), expected)

    def test_case_3(self):
        product_prices = [1, 1, 1]
        discount = 33
        expected = 2.67
        self.assertEqual(min_price(product_prices, discount), expected)


if __name__ == "__main__":
    unittest.main()