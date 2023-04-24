import os
from pygments import highlight
from pygments.lexers import PythonLexer

class BaseQuestionOutputter():
    def __init__(self, formatter_class):
        self.formatter_class = formatter_class

    def present_summary(self, summary):
        os.system('clear')
        print(f'You are: {summary}')

    def present_question(self, question):
        print(
            highlight(
                question.function_src,
                PythonLexer(),
                self.formatter_class()))

    def present_options(self, question):
        for key, choice in question.choices.items():
            print(f'{key}:\t{choice}')


class InputParameterQuestionOutputter(BaseQuestionOutputter):
    def present_question(self, question):
        print('')
        print('')
        super().present_question(question)
        print('')

    def present_options(self, question):
        print(f'Which value does the first paremeter need to be to return: {question.return_value}')
        super().present_options(question)


class ExpectedResultQuestionOutputter(BaseQuestionOutputter):
    def present_question(self, question):
        print('')
        print('What is the result of the last print statement?')
        print('')
        super().present_question(question)
        print('')

    def present_options(self, question):
        print('Select an option')
        super().present_options(question)

class FreeTextQuestionOutputter(BaseQuestionOutputter):
    def present_question(self, question):
        print('')
        print('')
        super().present_question(question)
        print('')
        print('What will this return?')

    def present_options(self, question):
        pass