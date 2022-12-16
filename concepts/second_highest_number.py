def explain_variable(variable, desc):
    print(desc)
    print(f'Data Type: {type(variable)} \nValue: {variable}\n----------\n')

nums = [2, 5, 8, 1, 5, 'a']
explain_variable(nums, 'https://www.w3schools.com/python/python_arrays.asp')

filter_lambda = lambda num: isinstance(num, int)
explain_variable(filter_lambda, 'https://www.w3schools.com/python/python_lambda.asp')

filtered_as_tuple = filter(filter_lambda, nums)
explain_variable(filtered_as_tuple, 'https://www.w3schools.com/python/ref_func_filter.asp')

filtered_as_list = list(filtered_as_tuple)
explain_variable(filtered_as_list, 'https://www.w3schools.com/python/ref_func_list.asp')

sorted_nums = sorted(filtered_as_list)
explain_variable(sorted_nums, 'https://www.w3schools.com/python/ref_func_sorted.asp')

list_size = len(nums)
explain_variable(list_size, 'https://www.w3schools.com/python/ref_func_len.asp')

index_of_second_last_element = list_size - 2
explain_variable(index_of_second_last_element, 'https://www.w3schools.com/python/python_operators.asp')

result = nums[index_of_second_last_element]
explain_variable(result, 'https://www.w3schools.com/python/gloss_python_array_access.asp')
