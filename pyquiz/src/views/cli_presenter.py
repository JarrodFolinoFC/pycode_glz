import pprint
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter

class CliPresenter:
    def __init__(self, question):
        self.question = question

    def present(self):
         pp = pprint.PrettyPrinter(indent=4)
         print('What is the result of this?')
         print('')
         print(highlight(self.question.function_src, PythonLexer(), Terminal256Formatter()))
         print('')
         self.present_options()


    def present_options(self):
        print('Select an option')
        for key, choice in self.question.choices.items():
            print(f'{key}:\t{choice}')