from quiz.quiz_item import quiz_item

@quiz_item(tags=['basic'])
def question_01():
    return 'hello'

@quiz_item(choices=[None, ''], tags=['basic'])
def question_01():
    return 'hello'

@quiz_item(choices=[None, ''], tags=['basic'])
def question_01():
    return 'hello'[:1]

@quiz_item(choices=[23], tags=['basic'])
def question_02():
    return 2 + 3

@quiz_item(choices=[70, None], tags=['basic'])
def question_03():
    return 7 - 0

@quiz_item(choices=[70, 2, 8], tags=['basic'])
def question_03():
    return 7 - 4

@quiz_item(param1=list(range(0, 10)), tags=['basic', 'param'])
def question_04(param1):
    return 7 - param1

@quiz_item(param1=list(range(0, 5)), tags=['basic', 'param'])
def question_04(param1):
    return 'hi there'[0:param1]
