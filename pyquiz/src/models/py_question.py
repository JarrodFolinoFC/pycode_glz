class PyQuestion:
    def __init__(self, function_src, choices, correct_answer, tags=None):
        self.function_src = function_src
        self.choices = choices
        self.correct_answer = correct_answer
        self.tags = tags

    def answer(self, choice):
        return self.choices[choice] == self.correct_answer
