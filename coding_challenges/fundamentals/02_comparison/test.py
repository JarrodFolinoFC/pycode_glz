import unittest

from main import gt_one_hundred_and_lt_one_thousand, gt_one_hundred


class GTOneHundredTestCase(unittest.TestCase):
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


class GTOneHundredLTOneThousandTestCase(unittest.TestCase):
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
