import unittest

from main import get_numbers_higher_than_6


class GetNumbersHigherThan6TestCase(unittest.TestCase):
    def test_get_numbers_higher_than_6_1(self):
        expected = [7, 8, 9]
        argument_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = get_numbers_higher_than_6(argument_one)
        self.assertEqual(result, expected)

    def test_get_numbers_higher_than_6_2(self):
        expected = []
        argument_one = [1, 2, 3, 4, 5]
        result = get_numbers_higher_than_6(argument_one)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
