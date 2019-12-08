import unittest

import solution as s

tests = [
    (([[2, 1, 4, 1], [0, 4, 8, 1], [1, 0, 10, 0]]), 320),
    (([[2, 0, 1], [1, 4, 0], [4, 8, 10], [1, 1, 0]]), 320),
    (([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0),
    (([[0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0]]), 1),
    (([]), 0),
    (([[2, 0, 4, 0], [0, 0, 0, 0], [1, 0, 10, 0]]), 0),
]


class TestBasic(unittest.TestCase):
    def test_calc(self):
        for test in tests:
            self.assertEquals(s.highest_prod(test[0]), test[1], test[0])

if __name__ == '__main__':
    unittest.main()
