def question_01():
    l = [10, 20, 30, 40, 50, 60]
    return l[2:]

def question_02():
    l = [10, 20, 30, 40, 50, 60]
    return l[:2]

def question_03():
    s = 'bicycle'
    return s[::3]

def question_04():
    s = 'bicycle'
    return s[::1]

def question_05():
    l = list(range(10))
    l[2:5] = [20, 30]
    return l

def question_06():
    l = list(range(10))
    del l[5:7]
    return l

def question_07():
    l = list(range(10))
    l[3::2] = [11, 22]
    return l

def slicing_questions():
    return [
        (question_01, [1,2,3]),
        (question_02, [1,2,3]),
        (question_03, [1,2,3]),
        (question_04, [1,2,3]),
        (question_05, [1,2,3]),
        (question_06, [1,2,3]),
        (question_07, [1,2,3]),
    ]