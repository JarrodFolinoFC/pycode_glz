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
