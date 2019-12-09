import unittest

import solution as s

result = None

def dump(r):
    global result
    result = r


class TestBasic(unittest.TestCase):
    def test_f(self):
        s.f(10, dump)
        self.assertEqual(result, 20)
        s.f(0, dump)
        self.assertEqual(result, 0)
        s.f(-1, dump)
        self.assertEqual(result, -2)

    def test_g(self):
        s.g(10, dump)
        self.assertEqual(result, 101)
        s.g(0, dump)
        self.assertEqual(result, 1)
        s.g(-1, dump)
        self.assertEqual(result, -9)

    def test_main(self):
        s.main(dump)
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()
