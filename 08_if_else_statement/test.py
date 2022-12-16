import unittest

from main import get_actions


class GetActionsTestCase(unittest.TestCase):
    def test_get_actions_1(self):
        expected = 'sell truck to truck dealer'
        result = get_actions(100000, 'truck')
        self.assertEqual(result, expected)

    def test_get_actions_2(self):
        expected = 'sell car to car dealer'
        result = get_actions(100000, 'car')
        self.assertEqual(result, expected)

    def test_get_actions_3(self):
        expected = None
        result = get_actions(100000, 'boat')
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
