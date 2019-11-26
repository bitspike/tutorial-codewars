import unittest
import solution as s


class TestBasic(unittest.TestCase):
    def test_calc(self):
        self.assertEquals(s.string_to_array("Robin Singh"), ["Robin", "Singh"])
        self.assertEquals(s.string_to_array("CodeWars"), ["CodeWars"])
        self.assertEquals(s.string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
        self.assertEquals(s.string_to_array("1 2 3"), ["1", "2", "3"])
        self.assertEquals(s.string_to_array(""), [""])

if __name__ == '__main__':
    unittest.main()
