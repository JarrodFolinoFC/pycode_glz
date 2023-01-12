import inspect
import re
import random
from models.py_question import PyQuestion

class PyQuestionFactory:
    @classmethod
    def build(cls, function, choices, tags):
        def run_function(function):
            try:
                return function()
            except Exception as e:
                return repr(e)

        correct_answer = run_function(function)
        choices = cls.prepare_choices(function, choices, correct_answer)
        src = cls.function_as_txt(function)
        return PyQuestion(src, choices, correct_answer, tags)

    @classmethod
    def function_as_txt(cls, function):
        def function_src(function):
            return inspect.getsource(function).strip()

        def format_src(src):
            src = re.sub('@quiz\_item\(.*\)', '', src)
            return src

        def append_print(function):
            return f'\n\nprint({function.__name__}())'

        src = function_src(function) + append_print(function)
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