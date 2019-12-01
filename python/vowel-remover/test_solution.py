import unittest

import solution as s

tests = [
    ["hello", "hll"]
]

class TestBasic(unittest.TestCase):
    def test_calc(self):
        for test in tests:
            self.assertEquals(s.shortcut(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
