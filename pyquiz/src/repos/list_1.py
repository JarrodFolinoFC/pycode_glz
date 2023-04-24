from quiz.quiz_item import quiz_item


@quiz_item(choices=[], tags=['list'])
def question_01():
    letters = ['a', 'b', 'c']
    letters.pop()
    return letters


@quiz_item(choices=[], tags=['list'])
def question_02():
    letters = ['a', 'b', 'c']
    popped = letters.pop()
    return letters + [popped]


@quiz_item(choices=[], tags=['list'])
def question_03():
    from array import array
    nums = array('i', [1, 2, 3, 4, 5])
    nums2 = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
    return (nums.itemsize, nums2.itemsize)


@quiz_item(choices=[], tags=['list'])
def question_04():
    from array import array
    nums = array('i', [1, 2, 3, 4, 5])
    return set(dir(nums.__class__)) - set(dir([].__class__))
