import pytest
from .program import *
solution = RunLengthEncoding()


@pytest.mark.parametrize("message,expected_output", [
    ('', ''),
    ('XYZ', 'XYZ'),
    ('AABBBCCCC', '2A3B4C'),
    ('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB', '12WB12W3B24WB'),
    ('  hsqq qww  ', '2 hs2q q2w2 '),
    ('aabbbcccc', '2a3b4c')
])
def test_encode(message, expected_output):
    assert solution.encode(message) == expected_output


@pytest.mark.parametrize("message,expected_output", [
    ('', ''),
    ('XYZ', 'XYZ'),
    ('2A3B4C', 'AABBBCCCC'),
    ('10WB12W3B24WB', 'WWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'),
    ('2 hs2q q2w2 ', '  hsqq qww  '),
    ('2a3b4c', 'aabbbcccc')
])
def test_decode(message, expected_output):
    assert solution.decode(message) == expected_output