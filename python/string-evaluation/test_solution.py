import unittest

import solution as s

class TestBasic(unittest.TestCase):
    def test_calc(self):
        self.assertEquals(s.string_evaluation(
            'aab#HcCcc##l#', ['a<b', '#==4', 'c>=C', 'H!=a']),
                            [ False, True,   True,   True ])
        self.assertEquals(s.string_evaluation(
            'abc#$%KDAyyaa@@@', ['#>@', 'A==2', 'a>A', '$!=2']),
                                [ False, False,  True,  True ])
        self.assertEquals(s.string_evaluation(
            'abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1']),
                [ False, False,  False,  True,  False,  True,   False])


# test.assert_equals(string_evaluation(
#     'aab#HcCcc##l#', ['a<b', '#==4', 'c>=C', 'H!=a']),
#                      [ False, True,   True,   True ])
# test.assert_equals(string_evaluation(
#     'abc#$%KDAyyaa@@@', ['#>@', 'A==2', 'a>A', '$!=2']),
#                         [ False, False,  True,  True ])
# test.assert_equals(string_evaluation(
#     'abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1']),
#            [ False, False,  False,  True,  False,  True,   False])


if __name__ == '__main__':
    unittest.main()
