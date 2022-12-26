import pprint

class CliPresenter:
    def __init__(self, question):
        self.question = question

    def present(self):
         pp = pprint.PrettyPrinter(indent=4)
         print('What is the result of this?')
         print('')
         print(self.question.function_src)
         print('')
         print('Select an option')
         pp.pprint(self.question.choices)