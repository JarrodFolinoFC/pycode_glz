from quiz.quiz_item import quiz_item


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_01():
    letters = 'abcde'
    codes = [(f'{letter.upper()}') for letter in letters]
    return ''.join(codes)


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_02():
    codes = [last := c for c in [1, 2, 3, 4, 5]]
    return last


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_03():
    codes = [last := c for c in [1, '2', 3, 4, '5'] if isinstance(c, int)]
    return last


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_04():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    return tshirts[4]


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_05():
    accumulated_gexp = sum((x for x in [1, 2, 3, 4, 5]))
    return accumulated_gexp


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_06():
    return type(hash((10, 'alpha', [1, 2])))


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_07():
    return [a for a in list(set(dir([1].__class__)) -
                            set(dir((1).__class__))) if not a.startswith('__')]


@quiz_item(choices=[], tags=['list_comphrehensions'])
def question_08():
    nums = [1, 2]
    letters = ['a', 'b']
    return [f'{letter}{num}' for letter in letters for num in nums]
