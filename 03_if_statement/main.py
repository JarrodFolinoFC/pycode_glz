import unittest


# Tags: [python_operators python_functions python_variables
#        python_booleans]

def get_actions_v1(kms):
    if kms > 300000:
        return 'sell vehicle for scrap metal'
    return None

def get_actions_v2(kms, vehicle_type):
    if kms > 300000:
        return 'sell vehicle for scrap metal'
    if vehicle_type == 'car':
        return 'sell car to car dealer'
    if vehicle_type == 'truck':
        return 'sell truck to truck dealer'
    return None

class SimpleTestCase(unittest.TestCase):

    #### get_actions_v1 ####
    def test_get_actions_v1_1(self):
        expected = 'sell vehicle for scrap metal'
        result = get_actions_v1(400000)
        self.assertEqual(result, expected)

    def test_get_actions_v1_2(self):
        expected = None
        result = get_actions_v1(100000)
        self.assertEqual(result, expected)

    #### get_actions_v2 ####
    def test_get_actions_v2_1(self):
        expected = 'sell vehicle for scrap metal'
        argument_one = 400000
        argument_two = 'truck'
        result = get_actions_v2(argument_one, argument_two)
        self.assertEqual(result, expected)

    def test_get_actions_v2_2(self):
        expected = 'sell truck to truck dealer'
        argument_one = 100000
        argument_two = 'truck'
        result = get_actions_v2(argument_one, argument_two)
        self.assertEqual(result, expected)

    def test_get_actions_v2_3(self):
        expected = 'sell car to car dealer'
        argument_one = 100000
        argument_two = 'car'
        result = get_actions_v2(argument_one, argument_two)
        self.assertEqual(result, expected)

    def test_get_actions_v2_4(self):
        expected = None
        argument_one = 100000
        argument_two = 'boat'
        result = get_actions_v2(argument_one, argument_two)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
