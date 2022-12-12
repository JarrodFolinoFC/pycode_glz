import unittest


# Tags: [python_operators python_functions python_variables
#        python_booleans]
def get_array():
    return [1, 2, 3, 4, 5]

def get_second_element(array):
    return array[1]

class SimpleTestCase(unittest.TestCase):

    #### get_array ####
    def test_get_array_1(self):
        expected = [1, 2, 3, 4, 5]
        result = get_array()
        self.assertEqual(result, expected)

    #### get_second_element ####
    def test_get_second_element_1(self):
        expected = 2
        argument_one = get_array()
        result = get_second_element(argument_one)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
