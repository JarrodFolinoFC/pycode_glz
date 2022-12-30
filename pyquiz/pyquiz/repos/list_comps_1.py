from collections import namedtuple

def question_11():
    letters = 'abcde'
    codes = [(f'{letter.upper()}') for letter in letters]
    return codes

def question_12():
    codes = [last := c for c in [1,2,3,4,5]]
    return last

def question_13():
    codes = [last := c for c in [1,'2',3,4,'5'] if isinstance(c, int)]
    return last

def question_14():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    return tshirts[4]

def question_15():
    accumulated_gexp = sum((x for x in [1,2,3,4,5]))
    return accumulated_gexp

def question_16():
    return type(hash((10, 'alpha', [1, 2])))

def question_17():
    return [a for a in list(set(dir([1].__class__)) - set(dir((1).__class__))) if not a.startswith('__')]

def questions():
    return [
        (question_11, [1,2,3]),
        (question_12, [1,2,3]),
        (question_13, [1,2,3]),
        (question_14, [1,2,3]),
        (question_15, [1,2,3]),
        (question_16, [1,2,3]),
        (question_17, [1,2,3]),
    ]