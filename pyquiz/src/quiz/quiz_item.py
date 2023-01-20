from functools import wraps
from .quiz_item_registry import QuizItemRegistry
from models.py_question import PyQuestion
from factories.py_question_factory import PyQuestionFactory


def quiz_item(choices=None, tags=None, hints=None):
    def inner_function(function):
        processed_question = PyQuestionFactory.build(
            function=function, choice_list=choices, tags=tags, hints=hints)
        QuizItemRegistry.add(processed_question)

        @wraps(function)
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            return wrapper

    return inner_function


class ChoiceGenerator:
    @classmethod
    def boolean_answers(cls):
        return [None, True, False]

    @classmethod
    def int_answers(cls, minimum=0, maximum=1000, amount=3):
        return [None, True, False]

    @classmethod
    def boolean_tuple_pair_answers(cls):
        return [(True, False), (False, False), (False, True), (True, True)]
