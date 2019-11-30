import unittest

import solution as s

tests = [
    ["hello", "Error"],
    [1, 56],
]

class TestBasic(unittest.TestCase):
    def test_calc(self):
        for test in tests:
            self.assertEquals(s.problem(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
