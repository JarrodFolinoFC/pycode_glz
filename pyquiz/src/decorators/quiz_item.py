from functools import wraps
from collections import namedtuple
from .quiz_item_registry import QuizItemRegistry

QuizItem = namedtuple('QuizItem', ['function', 'choices', 'tags'])

def quiz_item(choices=None, tags=None):
    def inner_function(function):
        QuizItemRegistry.add(QuizItem(function, choices, tags))

        @wraps(function)
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            return wrapper

    return inner_function
