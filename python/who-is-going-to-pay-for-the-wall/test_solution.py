import unittest

import solution as s

tests = [
    ["Mexico",["Mexico", "Me"]],
    ["Melania",["Melania", "Me"]],
    ["Melissa",["Melissa", "Me"]],
    ["Me",["Me"]],
    ["", [""]],
    ["I", ["I"]],
]



class TestBasic(unittest.TestCase):
    def test_solution(self):
        for test in tests:
            self.assertEquals(s.who_is_paying(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
