import unittest

def build_description(name, age):
    return f'Name: {name}, Age: {age}'

class SimpleTestCase(unittest.TestCase):

    #### build_description ####
    def test_build_description_1(self):
        expected = 'Name: Bob, Age: 18'
        argument_one = 'Bob'
        argument_two = 18
        result = build_description(argument_one, argument_two)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
