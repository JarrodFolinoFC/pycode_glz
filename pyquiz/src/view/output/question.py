import os
from pygments import highlight
from pygments.lexers import PythonLexer

from models.question import ExpectedResultQuestion, InputParameterQuestion

class BaseQuestionOutputter():
    def __init__(self, question, formatter_class):
        self.question = question
        self.formatter_class = formatter_class

    def present_question(self):
        print(
            highlight(
                self.question.function_src,
                PythonLexer(),
                self.formatter_class()))

    def present_options(self):
        for key, choice in self.question.choices.items():
            print(f'{key}:\t{choice}')


class InputParameterQuestionOutputter(BaseQuestionOutputter):
    def present_question(self):
        print('')
        print('')
        super().present_question()
        print('')

    def present_options(self):
        print(f'Which value does the first paremeter need to be to return: {self.question.return_value}')
        super().present_options()


class ExpectedResultQuestionOutputter(BaseQuestionOutputter):
    def present_question(self):
        print('')
        print('What is the result of the last print statement?')
        print('')
        super().present_question()
        print('')

    def present_options(self):
        print('Select an option')
        super().present_options()


class QuestionOutputter:
    def __init__(self, formatter_class):
        self.formatter_class = formatter_class

    def present(self, question, summary):
        os.system('clear')
        print(f'You are: {summary}')
        presenter = None
        if question.__class__ == ExpectedResultQuestion:
            presenter = ExpectedResultQuestionOutputter(question, self.formatter_class)
        elif question.__class__ == InputParameterQuestion:
            presenter = InputParameterQuestionOutputter(question, self.formatter_class)

        presenter.present_question()
        presenter.present_options()
