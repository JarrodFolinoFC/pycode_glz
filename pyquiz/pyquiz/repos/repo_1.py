def question_01():
    return type(hash((10, 'alpha', (1, 2))))

def question_02():
    return type(hash((10, 'alpha', [1, 2])))

def question_03():
    return [a for a in list(set(dir([1].__class__)) - set(dir((1).__class__))) if not a.startswith('__')]

def question_04():
    l = [2,3,4,5]
    return sorted(l, reverse= True) == l.sort().reverse()

def questions():
    return [
        (question_01, [1,2,3]),
        (question_02, [1,2,3]),
        (question_03, [1,2,3]),
        (question_04, [1,2,3]),
    ]