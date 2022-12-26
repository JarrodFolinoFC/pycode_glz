def remove_values_lt_50(nums):
    filter_object = filter(lambda num: num >= 50, nums)
    return list(filter_object)


def remove_values_lt(nums, threshold):
    filter_object = filter(lambda num: num >= threshold, nums)
    return list(filter_object)
