from examon_core.models.quiz_item import quiz_item

@quiz_item(choices=['São Paulo'], tags=['seed'])
def question_01():
    import random

    random.seed(10)
    return random.random() == random.random()
