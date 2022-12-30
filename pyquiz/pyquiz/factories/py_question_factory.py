import pprint
import inspect
import re
import random
from models.py_question import PyQuestion

class PyQuestionFactory:
    @classmethod
    def build(cls, function, choices):
        correct_answer = cls.run_function(function)
        choices = cls.prepare_choices(function, choices, correct_answer)
        src = cls.function_as_txt(function)
        return PyQuestion(src, choices, correct_answer)

    @classmethod
    def run_function(cls, function):
        try:
            return function()
        except Exception as e:
            return f'{e.__class__.__name__}: {repr(e)}'

    @classmethod
    def function_as_txt(cls, function):
        def function_src(function):
            return inspect.getsource(function).strip()

        def format_src(src):
            lambda_regex = '(?![0-9])\w+\s*=\s*lambda\s*:\s'
            inline_lambda_start_regex = 'ask\_question\(\s*lambda\s*:\s'
            inline_lambda_end_regex = '\s*\,\s*\[.*\]\s*\)\s*'
            defined_function = 'def\s+(?![0-9])\w+\(\):\\n'

            for regex in [lambda_regex, defined_function]:
                src = re.sub(regex, '', src)

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

        answer = cls.run_function(function)
        choices = append_answer(choices, answer)
        random.shuffle(choices)
        return list_to_choices_dict(choices)