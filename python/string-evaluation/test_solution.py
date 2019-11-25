import unittest

import solution as s

tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
]

class TestBasic(unittest.TestCase):
    def test_calc(self):
        pass
        # for test in tests:
        #     self.assertEquals(s.calc(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
