from models.py_question import PyQuestion
from utils.fn_to_txt import *
from utils.choice_helper import *


class PyQuestionFactory:
    @classmethod
    def build(cls, **kwargs):
        def run_function(function):
            try:
                return function()
            except Exception as e:
                return repr(e)

        correct_answer = run_function(function=kwargs['function'])
        question = PyQuestion(
            tags=kwargs['tags'],
            hints=kwargs['hints'],
            function_src=function_as_txt(
                function=kwargs['function'],
                hints=kwargs['hints']),
            correct_answer=correct_answer,
            choices=prepare_choices(
                kwargs['choice_list'],
                correct_answer))
        return question
