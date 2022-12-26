import unittest

from main import add_data_types


class AddDataTypeNumbersTestCase(unittest.TestCase):
    def test_add_data_types_1(self):
        argument_one = 1
        argument_two = 2
        result = add_data_types(argument_one, argument_two)
        expected = 3
        self.assertEqual(result, expected)

    def test_add_data_types_2(self):
        argument_one = 1.5
        argument_two = 2
        result = add_data_types(argument_one, argument_two)
        expected = 3.5
        self.assertEqual(result, expected)


class AddDataTypeArrayTestCase(unittest.TestCase):
    def test_add_data_types_1(self):
        argument_one = [1]
        argument_two = [2]
        result = add_data_types(argument_one, argument_two)
        expected = [1, 2]
        self.assertEqual(result, expected)


class AddDataTypeDictTestCase(unittest.TestCase):
    def test_add_data_types_1(self):
        argument_one = {'one': 1}
        argument_two = {'two': 2}
        result = add_data_types(argument_one, argument_two)
        expected = {'one': 1, 'two': 2}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
