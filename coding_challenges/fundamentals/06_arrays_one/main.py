def get_array():
    return [1, 2, 3, 4, 5]

def get_second_element(array):
    if len(array) < 2:
        return None
    return array[1]

def get_second_last_element(array):
    if len(array) < 2:
        return None
    return array[-2]