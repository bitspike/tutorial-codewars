import unittest
from datetime import date

import solution as s

tests = [
    [(date(2016, 6, 13), date(2016, 7, 16), 35), False],
    [(date(2016, 6, 13), date(2016, 7, 16), 28), True],
    [(date(2016, 6, 13), date(2016, 7, 16), 35), False],
    [(date(2016, 6, 13), date(2016, 6, 29), 28), False],
    [(date(2016, 7, 12), date(2016, 8, 9), 28), False],
    [(date(2016, 7, 12), date(2016, 8, 10), 28), True],
    [(date(2016, 7, 1), date(2016, 8, 1), 30), True],
    [(date(2016, 6, 1), date(2016, 6, 30), 30), False],
    [(date(2016, 1, 1), date(2016, 1, 31), 30), False],
    [(date(2016, 1, 1), date(2016, 2, 1), 30), True],
]

class TestBasic(unittest.TestCase):
    def test_calc(self):
        for test in tests:
            self.assertEqual(s.period_is_late(*test[0]), test[1])
            # period_is_late(last,today,cycle_length)

if __name__ == '__main__':
    unittest.main()
