import random


def prepare_choices(choice_list, correct_answer):
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
