import unittest

import solution as s

class TestBasic(unittest.TestCase):
    def test_calc(self):
        self.assertTrue(s.greek_comparator('alpha', 'beta') < 0, "result should be negative")
        self.assertEqual(s.greek_comparator('psi', 'psi'), 0, "result should be zero")
        self.assertTrue(s.greek_comparator('upsilon', 'rho'), "result should be positive")


if __name__ == '__main__':
    unittest.main()
