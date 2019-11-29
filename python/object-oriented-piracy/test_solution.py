import unittest

import solution as s

class TestBasic(unittest.TestCase):
    def test_ship(self):
        EmptyShip = s.Ship(0, 0)
        self.assertEquals(EmptyShip.is_worth_it(), False)

if __name__ == '__main__':
    unittest.main()
