# import sys
# sys.path.append('/Users/bogdanbalanik/University/labs/Algo-Labs/Algo_labs/src')

import unittest
# from lab6 import rabin_karp_search
from lab6 import rabin_karp_search

class TestRabinKarpSearch(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rabin_karp_search("ABABDABACDABABCABAB", "ABABCABAB"), [10])

    def test_no_match(self):
        self.assertEqual(rabin_karp_search("hello", "world"), [])

    def test_empty_needle(self):
        self.assertEqual(rabin_karp_search("hello", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(rabin_karp_search("", "world"), [])

if __name__ == '__main__':
    unittest.main()
