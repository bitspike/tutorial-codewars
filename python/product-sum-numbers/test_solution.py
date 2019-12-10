import unittest

import solution as s

productsum_tests = [
    [(3,), 10],
    [(6,), 30],
    [(12,), 61],
    [(13,), 79],
    [(14,), 99],
    [(15,), 123],
    [(16,), 123],
    [(17,), 123],
    [(18,), 123],
    [(19,), 123],
    [(20,), 151],
    [(100,), 2061],
    [(200,), 6623],
    [(300,), 12686],
    [(2,), 4],
]

class TestBasic(unittest.TestCase):
    def test_productsum(self):
        for test in productsum_tests:
            self.assertEqual(s.productsum(*test[0]), test[1], '%s' % test)

if __name__ == '__main__':
    unittest.main()
