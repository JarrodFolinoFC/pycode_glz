import unittest

from main import get_array, get_second_element, get_second_last_element


class GetArrayTestCase(unittest.TestCase):
    def test_get_array_1(self):
        expected = [1, 2, 3, 4, 5]
        result = get_array()
        self.assertEqual(result, expected)


class GetSecondElementTestCase(unittest.TestCase):
    def test_get_second_element_1(self):
        expected = 2
        argument_one = get_array()
        result = get_second_element(argument_one)
        self.assertEqual(result, expected)

    def test_get_second_element_2(self):
        expected = None
        argument_one = []
        result = get_second_element(argument_one)
        self.assertEqual(result, expected)


class GetSecondLastElementTestCase(unittest.TestCase):
    def test_get_second_last_element_1(self):
        expected = 4
        argument_one = get_array()
        result = get_second_last_element(argument_one)
        self.assertEqual(result, expected)

    def test_get_second_last_element_2(self):
        expected = None
        argument_one = []
        result = get_second_last_element(argument_one)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
