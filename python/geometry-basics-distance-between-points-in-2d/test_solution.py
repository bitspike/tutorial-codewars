import unittest
from collections import namedtuple

import solution as s

class TestBasic(unittest.TestCase):
    def test_calc(self):
        Point = namedtuple('Point', ['x', 'y'])
        self.assertEqual(s.distance_between_points(Point(3, 3), Point(3, 3)), 0)
        self.assertEqual(s.distance_between_points(Point(1, 6), Point(4, 2)), 5)
        self.assertEqual(round(s.distance_between_points(Point(-10.2, 12.5), Point(0.3, 14.7)), 6), 10.728001)


if __name__ == '__main__':
    unittest.main()
