import os
from pygments import highlight
from pygments.lexers import PythonLexer


class QuestionOutputter:
    def __init__(self, formatter_class):
        self.formatter_class = formatter_class

    def present(self, question, summary):
        os.system('clear')
        print(f'You are: {summary}')
        print('')
        print('What is the result of the last print statement?')
        print('')
        print(
            highlight(
                question.function_src,
                PythonLexer(),
                self.formatter_class()))
        print('')
        self.present_options(question)

    def present_options(self, question):
        print('Select an option')
        for key, choice in question.choices.items():
            print(f'{key}:\t{choice}')
