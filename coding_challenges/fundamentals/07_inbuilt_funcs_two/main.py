def get_numbers_higher_than_6(nums):
    filter_object = filter(lambda num: num > 6, nums)
    return list(filter_object)
