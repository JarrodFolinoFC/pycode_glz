from examon_core.models.quiz_item import quiz_item


@quiz_item(choices=[3, 4, 'Exception'], tags=['assignment'])
def question_01():
    A = 3
    A = 4
    return A


@quiz_item(choices=[7, 4], tags=['assignment'])
def question_02():
    a = 3
    a *= 4
    return a
