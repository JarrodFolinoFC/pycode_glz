from itertools import groupby

def find_elf_with_highest_calories(calories_list):
    seperator = None
    calorie_groupings = [list(group) for k, group in groupby(calories_list, lambda x: x == seperator) if not k]
    calorie_aggregate = [sum(cals) for cals in calorie_groupings]
    return calorie_aggregate.index(max(calorie_aggregate))
