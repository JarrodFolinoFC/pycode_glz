def question_26():
    l = [10, 20, 30, 40, 50, 60]
    return l[2:]

def question_27():
    l = [10, 20, 30, 40, 50, 60]
    return l[:2]

def question_28():
    s = 'bicycle'
    return s[::3]

def question_29():
    s = 'bicycle'
    return s[::1]

def question_30():
    l = list(range(10))
    l[2:5] = [20, 30]
    return l

def question_31():
    l = list(range(10))
    del l[5:7]
    return l

def question_32():
    l = list(range(10))
    l[3::2] = [11, 22]
    return l

def slicing_questions():
    return [
        (question_26, [1,2,3]),
        (question_27, [1,2,3]),
        (question_28, [1,2,3]),
        (question_29, [1,2,3]),
        (question_30, [1,2,3]),
        (question_31, [1,2,3]),
        (question_32, [1,2,3]),
    ]