import random

from lib.choice_helper import *

class MultiChoiceFactory:

    @classmethod
    def build(cls, correct_answer, generate_choices, choice_list):
        if generate_choices == 'answer_plus_random':
            cls.add_incorrect_answer(choice_list, correct_answer)
        choices = cls.prepare_choices(choice_list, correct_answer)
        return choices


    @classmethod
    def add_incorrect_answer(cls, choice_list, correct_answer):
        if type(correct_answer) == int:
            generated_answer = correct_answer + 9
            choice_list.append(generated_answer)
        elif type(correct_answer) == str:
            generated_answer = correct_answer + ' meow'
            choice_list.append(generated_answer)
        elif type(correct_answer) == dict:
            choice_list.append(correct_answer | {'hello': 'there'})
        elif type(correct_answer) == set:
            choice_list.append({1,2})
        elif type(correct_answer) == bool:
            choice_list.append(False)
            choice_list.append(True)
            choice_list.append(None)

    @classmethod
    def prepare_choices(cls, choice_list, correct_answer):
        def append_answer(choices, answer):
            if answer not in choices:
                choices.append(answer)
            return choices

        def list_to_choices_dict(choices):
            choice_dict = {}
            for idx, choice in enumerate(choices):
                choice_dict[chr(97 + idx)] = choice
            return choice_dict

        choice_list = append_answer(choice_list, correct_answer)
        random.shuffle(choice_list)
        return list_to_choices_dict(choice_list)
