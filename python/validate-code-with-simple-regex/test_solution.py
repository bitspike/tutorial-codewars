import unittest

import solution as s


class TestBasic(unittest.TestCase):
    def test_list_int(self):
        self.assertEquals(s.validate_code(123), True)
        self.assertEquals(s.validate_code(248), True)
        self.assertEquals(s.validate_code(8), False)
        self.assertEquals(s.validate_code(321), True)
        self.assertEquals(s.validate_code(9453), False)

if __name__ == '__main__':
    unittest.main()




# Test.assert_equals(validate_code(123), True)
# Test.assert_equals(validate_code(248), True)
# Test.assert_equals(validate_code(8), False)
# Test.assert_equals(validate_code(321), True)
# Test.assert_equals(validate_code(9453), False)