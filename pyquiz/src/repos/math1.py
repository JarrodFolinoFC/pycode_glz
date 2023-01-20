from quiz.quiz_item import quiz_item

from math import ceil, floor, trunc, factorial, hypot, sqrt


@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    return  1 + 3

@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    return sqrt(9)


@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    return floor(9.6665456456)



@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    return ceil(9.6665456456)


@quiz_item(choices=[], tags=['math'])
def question():
    return trunc(9.6665456456)


@quiz_item(choices=[], tags=['math'])
def question():
    return hypot(5, 10)


@quiz_item(choices=[], tags=['math'])
def question():
    return factorial(9)
