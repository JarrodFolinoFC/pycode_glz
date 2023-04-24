from quiz.quiz_item import quiz_item


@quiz_item(choices=[3, None, 'enter'], tags=['with'])
def question_01():
    class LookingGlass:
        def __enter__(self):
            return 'enter'

        def __exit__(self, exc_type, exc_value, traceback):
            return 'exit'

    with LookingGlass() as what:
        return what


@quiz_item(choices=[7, 4], tags=['with'])
def question_02():
    pass
