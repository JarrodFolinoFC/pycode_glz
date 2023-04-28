import unittest

from main import described_input, described_input_v2


class DescribeInputTestCase(unittest.TestCase):
    def test_described_input_1(self):
        expected = 'Is String: True, Is Integer: False'
        argument_one = 'Hello'
        result = described_input(argument_one)
        self.assertEqual(result, expected)

    def test_described_input_v2_1(self):
        expected = "Type: <class 'str'>, Length: 5"
        argument_one = 'Hello'
        result = described_input_v2(argument_one)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
