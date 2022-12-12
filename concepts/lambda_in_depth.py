################################
filter_lambda = lambda num: isinstance(num, int)

def filter_function(num):
    return isinstance(num, int)

def filter_function_verbose(num):
    result = isinstance(num, int)
    return result

nums = [1, 2, 3, '4', 5, 6]

# All five are the same
print(list(filter(filter_lambda, nums))) # referencing lambda variable
print(
    list( # inline lambda, newlines used in formatting
        filter(
            lambda num: isinstance(num, int), nums
        )
    )
)
print(list(filter(lambda num: isinstance(num, int), nums))) # inline lambda
print(list(filter(filter_function, nums))) # referencing function
print(list(filter(filter_function_verbose, nums))) # referencing function


################################
# These do not work
def filter_function_broken_always_true(num):
    return num

print(list(filter(filter_function_broken_always_true, nums)))
print(list(filter(lambda _: False, nums)))

def filter_function_broken_always_false(num):
    return False

print(list(filter(filter_function_broken_always_false, nums)))
print(list(filter(lambda _: True, nums)))