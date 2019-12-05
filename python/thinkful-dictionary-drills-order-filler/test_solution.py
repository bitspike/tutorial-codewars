import unittest

import solution as s

stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}

class TestBasic(unittest.TestCase):
    def test_calc(self):
        self.assertEquals(s.fillable(stock, 'football', 3), True)
        self.assertEquals(s.fillable(stock, 'leggos', 2), False)
        self.assertEquals(s.fillable(stock, 'action figure', 1), False)


if __name__ == '__main__':
    unittest.main()
