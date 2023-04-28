import unittest

from main import add_nums


class AddNumsTestCase(unittest.TestCase):
    def test_add_nums_1(self):
        expected = 15
        argument_one = 10
        argument_two = 5
        result = add_nums(argument_one, argument_two)
        self.assertEqual(result, expected)

    def test_add_nums_2(self):
        expected = -7
        argument_one = -10
        argument_two = 3
        result = add_nums(argument_one, argument_two)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
