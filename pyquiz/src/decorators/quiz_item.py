from functools import wraps
from collections import namedtuple
from .quiz_item_registry import QuizItemRegistry

PyQuizData = namedtuple('QuizItem', ['function', 'choices', 'tags'])

def quiz_item(choices=None, tags=None):
    def inner_function(function):
        QuizItemRegistry.add(PyQuizData(function, choices, tags))

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
    def int_answers(cls, min=0, max=1000, amount=3):
        return [None, True, False]

    @classmethod
    def boolean_tuple_pair_answers(cls):
        return [(True, False), (False, False), (False, True), (True, True)]
