def gt_one_hundred(num):
    return num > 100


def gt_one_hundred_and_lt_one_thousand(num):
    gt_one_hundred = num > 100
    lt_one_thousand = num < 1000
    return gt_one_hundred and lt_one_thousand
