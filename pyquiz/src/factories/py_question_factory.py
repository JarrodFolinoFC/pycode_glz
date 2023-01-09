import pprint
import inspect
import re
import random
from models.py_question import PyQuestion

class PyQuestionFactory:
    @classmethod
    def build(cls, function, choices, tags):
        correct_answer = cls.run_function(function)
        choices = cls.prepare_choices(function, choices, correct_answer)
        src = cls.function_as_txt(function)
        src = src + cls.append_print(function)
        return PyQuestion(src, choices, correct_answer, tags)

    @classmethod
    def run_function(cls, function):
        try:
            return function()
        except Exception as e:
            return repr(e)

    @classmethod
    def append_print(cls, function):
        return f'\n\nprint({function.__name__}())'

    @classmethod
    def function_as_txt(cls, function):
        def function_src(function):
            return inspect.getsource(function).strip()

        def format_src(src):
            src = re.sub('@quiz\_item\(.*\)', '', src)
            return src
        src = function_src(function)
        return format_src(src)

    @classmethod
    def prepare_choices(cls, function, choices, answer):
        def append_answer(choices, answer):
            if not answer in choices:
                choices.append(answer)
            return choices

        def list_to_choices_dict(choices):
          choice_dict = {}
          for idx, x in enumerate(choices):
            choice_dict[chr(97 + idx)] = x
          return choice_dict

        choices = append_answer(choices, answer)
        random.shuffle(choices)
        return list_to_choices_dict(choices)