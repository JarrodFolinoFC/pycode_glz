from collections import namedtuple

question_1 = lambda : 1 + 2

def question_18():
    return type(hash((10, 'alpha', (1, 2))))

def question_19():
    return type(hash((10, 'alpha', [1, 2])))

def question_20():
    return [a for a in list(set(dir([1].__class__)) - set(dir((1).__class__))) if not a.startswith('__')]

def question_42():
    l = [2,3,4,5]
    return sorted(l, reverse= True) == l.sort().reverse()

def questions():
    return [
        (question_18, [1,2,3]),
        (question_19, [1,2,3]),
        (question_20, [1,2,3]),
        (question_42, [1,2,3]),
    ]