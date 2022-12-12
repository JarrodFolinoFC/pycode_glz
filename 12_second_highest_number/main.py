import unittest


# Tags: [ref_func_filter ref_func_list ref_func_sorted
#        python_operators gloss_python_array_access
#        python_functions python_variables]
#
#

def remove_non_integers(nums):
    # In-built `filter` function
    # https://www.w3schools.com/python/ref_func_filter.asp
    filter_object = filter(
        # Keyword lambda (annoymous function)
        # https://www.w3schools.com/python/python_lambda.asp
        lambda num: isinstance(num, int), nums
    )

    # In-built `list` function
    # https://www.w3schools.com/python/ref_func_list.asp
    filtered_as_list = list(filter_object)

    return filtered_as_list

def sort_list_of_integers(unsorted_nums):
    # In-built `sorted` function
    # https://www.w3schools.com/python/ref_func_sorted.asp
    sorted_nums = sorted(unsorted_nums)

    return sorted_nums

def second_last_element_of_list(nums):
    # In-built `len` function
    # https://www.w3schools.com/python/ref_func_len.asp
    list_size = len(nums)

    # Arithmetic operator
    # https://www.w3schools.com/python/python_operators.asp
    index_of_second_last_element = list_size - 2

    # Access element from list
    # https://www.w3schools.com/python/gloss_python_array_access.asp
    result = nums[index_of_second_last_element]

    return result

def second_highest_number(nums):
    if len(nums) < 2:
        return None

    nums = remove_non_integers(nums)
    nums = sort_list_of_integers(nums)
    result = second_last_element_of_list(nums)
    return result

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
