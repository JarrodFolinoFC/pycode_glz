from examon_core.models.quiz_item import quiz_item, ChoiceGenerator


@quiz_item(choices=[1,2,3,4,5,6], tags=['itertools'])
def question():
    from itertools import accumulate
    GFG = [5, 3, 6, 2, 1, 9, 1]
    iter = accumulate(GFG, max)
    next(iter)
    next(iter)
    return next(iter)


@quiz_item(choices=[1,2,3,4,5,6], tags=['itertools'])
def question():
    from itertools import count
    iter = count(1, 3)
    next(iter)
    next(iter)
    return next(iter)


@quiz_item(choices=[1,2,3,4,5,6], tags=['itertools'])
def question():
    from itertools import groupby
    return [list(i[1]) for i in groupby('12216')]


@quiz_item(choices=[1,2,3,4,5,6], tags=['itertools'])
def question():
    from itertools import dropwhile
    return list(dropwhile(lambda x: x < 6, [1, 2, 2, 1, 6, 18, 9]))
