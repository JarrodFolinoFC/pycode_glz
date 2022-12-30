def question_01():
    letters = 'abcde'
    codes = [(f'{letter.upper()}') for letter in letters]
    return ''.join(codes)

def question_02():
    codes = [last := c for c in [1,2,3,4,5]]
    return last

def question_03():
    codes = [last := c for c in [1,'2',3,4,'5'] if isinstance(c, int)]
    return last

def question_04():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    return tshirts[4]

def question_05():
    accumulated_gexp = sum((x for x in [1,2,3,4,5]))
    return accumulated_gexp

def question_06():
    return type(hash((10, 'alpha', [1, 2])))

def question_07():
    return [a for a in list(set(dir([1].__class__)) - set(dir((1).__class__))) if not a.startswith('__')]

def question_08():
    nums = [1, 2]
    letters = ['a', 'b']
    return [f'{letter}{num}' for letter in letters for num in nums]

def list_comp_questions():
    return [
        (question_01, [1,2,3]),
        (question_08, [['b1', 'b2', 'a1', 'a2'], ['1a', '2a', '1b', '2b']]),
        (question_02, [1,2,3]),
        (question_03, [1,2,3]),
        (question_04, [1,2,3]),
        (question_05, [1,2,3]),
        (question_06, [1,2,3]),
        (question_07, [1,2,3]),
    ]