from examon_core.models.quiz_item import quiz_item



@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        return array[1]

    return a([1, 2, 3, 4, 5, 6, 7])


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        sorted(array)
        return array[-1]

    return a([1, 2, 3, 4, 5, 6, 7])


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        return [a for a in array]

    return a([1, 2, 3, 4, 5, 6, 7])


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        return [a for a in array if isinstance(a, int)]

    return a([1, 2, 3, '4', 5, 6, 7, None])[2]

@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def filter(array):
        return [a for a in array if isinstance(a, int)]

    a = filter([1, 2, 3, '4', 5, 6, 7, None])
    sorted(a)
    return a[-2]

@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def filter(array):
        return [a for a in array if isinstance(a, int)]

    def dosort(a):
        sorted(a)

    a = filter([1, 2, 3, '4', 5, 6, 7, None])
    dosort(a)
    return a[-3]