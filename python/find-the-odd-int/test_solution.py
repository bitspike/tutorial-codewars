import unittest

import solution as s

tests = [
    [[20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5],
    [[1,1,2,-2,5,2,4,4,-1,-2,5], -1],
    [[20,1,1,2,2,3,3,5,5,4,20,4,5], 5],
    [[10], 10],
    [[1,1,1,1,1,1,10,1,1,1,1], 10],
    [[5,4,3,2,1,5,4,3,2,10,10], 1],
]

class TestBasic(unittest.TestCase):
    def test_calc(self):
        for test in tests:
            self.assertEqual(s.find_it(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
