import unittest
from main import remove_non_integers, sort_list_of_integers, second_last_element_of_list, second_highest_number


class SimpleTestCase(unittest.TestCase):
    # 1.
    #### remove_non_integers ####
    def test_remove_non_integers_1(self):
        expected = [1, 0, 2]
        result = remove_non_integers([1, 0, 2])
        self.assertEqual(result, expected)

    def test_remove_non_integers_2(self):
        expected = [1, 0, 2]
        result = remove_non_integers([1, 'a', 0, 2])
        self.assertEqual(result, expected)

    # 2.
    #### sort_list_of_integers ####
    def test_sort_list_of_integers_1(self):
        expected = [0, 1, 2]
        argument_one = [1, 0, 2]
        result = sort_list_of_integers(argument_one)
        self.assertEqual(result, expected)

    def test_sort_list_of_integers_2(self):
        argument_one = [11, 0, -2]
        result = sort_list_of_integers(argument_one)
        expected = [-2, 0, 11]
        self.assertEqual(result, expected)

    # 3.
    #### second_last_element_of_list ####
    def test_second_last_element_of_list_1(self):
        expected = 8
        argument_one = [0, 1, 2, 3, 8, 55]
        result = second_last_element_of_list(argument_one)
        self.assertEqual(result, expected)

    def test_second_last_element_of_list_2(self):
        expected = 11
        argument_one = [11, 11, 33]
        result = second_last_element_of_list(argument_one)
        self.assertEqual(result, expected)

    # 4.
    #### second_highest_number ####
    def test_second_highest_number_1(self):
        expected = 1
        argument_one = [1, 0, 2]
        result = second_highest_number(argument_one)
        self.assertEqual(result, expected)

    def test_second_highest_number_2(self):
        expected = None
        argument_one = [5]
        result = second_highest_number(argument_one)
        self.assertEqual(result, expected)

    def test_second_highest_number_3(self):
        expected = 46597384
        argument_one = [46597384, 46597385]
        result = second_highest_number(argument_one)
        self.assertEqual(result, expected)

    def test_second_highest_number_4(self):
        expected = 3
        argument_one = [1, 2, 3, 4, '6']
        result = second_highest_number(argument_one)
        self.assertEqual(result, expected)

    def test_second_highest_number_5(self):
        expected = 3
        argument_one = [1, '2', 3, 4, '6']
        result = second_highest_number(argument_one)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
