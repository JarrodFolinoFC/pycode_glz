from calories.program import find_elf_with_highest_calories

fixture1 = [
    1000, 2000, 3000, #6000
    None,
    4000, #4000
    None,
    5000, 6000, #11000
    None,
    7000, 8000, 9000, #24000
    None,
    10000 #10000
]


def test_something():
    result = find_elf_with_highest_calories(fixture1)
    assert result == 3
