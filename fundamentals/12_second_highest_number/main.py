def remove_non_integers(nums):
    return None


def sort_list_of_integers(unsorted_nums):
    return None


def second_last_element_of_list(nums):
    return None


def second_highest_number(nums):
    if len(nums) < 2:
        return None

    nums = remove_non_integers(nums)
    nums = sort_list_of_integers(nums)
    result = second_last_element_of_list(nums)
    return result
