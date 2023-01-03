def question_01():
    letters = ['a', 'b', 'c']
    letters.pop()
    return letters

def question_02():
    letters = ['a', 'b', 'c']
    popped = letters.pop()
    return letters + [popped]

def question_03():
    from array import array
    nums = array('i', [1,2,3,4,5])
    nums2 = array('i', [1,2,3,4,5,6,7,8])
    return (nums.itemsize, nums2.itemsize)

def question_04():
    from array import array
    nums = array('i', [1,2,3,4,5])
    return set(dir(nums.__class__)) - set(dir([].__class__))

def list_questions():
    return [
        (question_04, []),
        (question_03, [(4, 4), (5,8), (4,7), (4, 8)]),
        (question_02, [['a', 'b', 'c'], ['a', 'b'], ['c', 'a', 'b'], ['b', 'c', 'a']]),
        (question_01, [['a', 'b', 'c']]),
    ]