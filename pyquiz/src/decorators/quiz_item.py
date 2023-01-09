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
