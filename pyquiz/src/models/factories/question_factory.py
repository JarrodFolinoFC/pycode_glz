from models.question import ExpectedResultQuestion, InputParameterQuestion
from lib.fn_to_txt import *
from lib.choice_helper import *
from models.factories.multi_choice_factory import MultiChoiceFactory
import random


class QuestionFactory:
    @staticmethod
    def build(**kwargs):
        function = kwargs['function']
        tags = kwargs['tags']
        hints = kwargs['hints']

        if kwargs['choice_list'] != None:
            correct_answer = QuestionFactory.run_function(function=function)
            choices = MultiChoiceFactory.build(correct_answer,
                                               kwargs['generated_choices'],
                                               kwargs['choice_list'])
            return QuestionFactory.build_multichoice(choices, correct_answer,
                                                   function, hints, tags)
        elif kwargs['param1'] != None:
            param1 = kwargs['param1']
            choices = {}
            for idx, param in enumerate(param1):
                choices[chr(idx + 97)] = param

            selected_input = random.choice(param1)
            return_value = QuestionFactory.run_function_with_param(function, selected_input)

            return QuestionFactory.build_select_input(choices, return_value,
                                                       function, hints, tags, selected_input)

    @staticmethod
    def build_multichoice(choices, correct_answer, function, hints, tags):
        question = ExpectedResultQuestion(
            tags=tags,
            hints=hints,
            function_src=function_as_txt(
                function=function,
                hints=hints),
            correct_answer=correct_answer,
            choices=choices)
        return question

    @staticmethod
    def build_select_input(choices, correct_answer, function, hints, tags, selected_param):
        question = InputParameterQuestion(
            tags=tags,
            hints=hints,
            function_src=function_as_txt(
                function=function,
                hints=hints),
            selected_param=selected_param,
            return_value=correct_answer,
            choices=choices)
        return question


    @staticmethod
    def run_function(function):
        try:
            return function()
        except Exception as e:
            return repr(e)

    @staticmethod
    def run_function_with_param(function, param):
        try:
            return function(param)
        except Exception as e:
            return repr(e)
