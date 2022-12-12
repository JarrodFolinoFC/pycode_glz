import unittest


# Tags: [python_operators python_functions python_variables
#        python_booleans]

def described_input(input):
    return f'Is String: {isinstance(input, str)}, Is Integer: {isinstance(input, int)}'

def described_input_v2(input):
    return f'Type: {type(input)}, Length: {len(input)}'

class SimpleTestCase(unittest.TestCase):

    #### described_input ####
    def test_described_input_1(self):
        expected = 'Is String: True, Is Integer: False'
        argument_one = 'Hello'
        result = described_input(argument_one)
        self.assertEqual(result, expected)

    #### described_input_v2 ####
    def test_described_input_v2_1(self):
        expected = "Type: <class 'str'>, Length: 5"
        argument_one = 'Hello'
        result = described_input_v2(argument_one)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
