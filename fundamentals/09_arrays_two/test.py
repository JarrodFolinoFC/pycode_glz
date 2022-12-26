import unittest

from main import remove_values_lt_50, remove_values_lt


class ArrayRemoveElementsTestCase(unittest.TestCase):
    def test_remove_values_lt_50_1(self):
        expected = [51, 88]
        argument_one = [12, 51, 88]
        result = remove_values_lt_50(argument_one)
        self.assertEqual(result, expected)

    def test_remove_values_lt_1(self):
        expected = [40, 51, 88]
        argument_one = [12, 40, 51, 88]
        argument_two = 40
        result = remove_values_lt(argument_one, argument_two)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
