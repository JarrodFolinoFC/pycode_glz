import unittest


# Tags: [python_operators python_functions python_variables
#        python_booleans]

def gt_one_hundred(num):
    return num > 100

def gt_one_hundred_and_lt_one_thousand(num):
    gt_one_hundred = num > 100
    lt_one_thousand = num < 1000
    return gt_one_hundred and lt_one_thousand

class SimpleTestCase(unittest.TestCase):

    #### gt_one_hundred ####
    def test_gt_one_hundred_1(self):
        expected = False
        argument_one = 10
        result = gt_one_hundred(argument_one)
        self.assertEqual(result, expected)

    def test_gt_one_hundred_2(self):
        expected = False
        argument_one = 100
        result = gt_one_hundred(argument_one)
        self.assertEqual(result, expected)

    def test_gt_one_hundred_3(self):
        expected = True
        argument_one = 101
        result = gt_one_hundred(argument_one)
        self.assertEqual(result, expected)

    #### gt_one_hundred ####
    def test_gt_one_hundred_and_lt_one_thousand_1(self):
        expected = False
        argument_one = 10
        result = gt_one_hundred_and_lt_one_thousand(argument_one)
        self.assertEqual(result, expected)

    def test_gt_one_hundred_and_lt_one_thousand_2(self):
        expected = True
        argument_one = 101
        result = gt_one_hundred_and_lt_one_thousand(argument_one)
        self.assertEqual(result, expected)

    def test_gt_one_hundred_and_lt_one_thousand_3(self):
        expected = False
        argument_one = 1001
        result = gt_one_hundred_and_lt_one_thousand(argument_one)
        self.assertEqual(result, expected)

    def test_gt_one_hundred_and_lt_one_thousand_3(self):
        expected = True
        argument_one = 999
        result = gt_one_hundred_and_lt_one_thousand(argument_one)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
