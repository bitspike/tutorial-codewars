import unittest

import solution as s

tests = [
    ((0,3), 0),
    ((2,0), 0),
    ((2,3), 6),
    ((1,3), 3),
    ((3,3), 9),
    ((-2,3), -6),
    ((-1,0), 0),
]

class TestBasic(unittest.TestCase):
    def test_calc(self):
        for test in tests:
            self.assertEquals(s.multiply(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
