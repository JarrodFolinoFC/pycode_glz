from decorators.quiz_item import quiz_item

@quiz_item(choices=[], tags=['built in functions'])
def question_01():
    return type(hash((10, 'alpha', (1, 2))))

def question_02():
    return type(hash((10, 'alpha', [1, 2])))

def question_03():
    return [a for a in list(set(dir([1].__class__)) - set(dir((1).__class__))) if not a.startswith('__')]

def question_04():
    l = [2,3,4,5]
    return sorted(l, reverse= True) == l.sort().reverse()

