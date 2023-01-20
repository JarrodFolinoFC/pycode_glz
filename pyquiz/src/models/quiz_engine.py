from models.py_response import PyResponse

class QuizEngine:
    def __init__(self, questions=None,
                 outputter=None,
                 stats_outputter=None,
                 inputter=None):
        self.questions = questions
        self.correct_answers = 0
        self.responses = []

        # I/O
        self.__output = outputter
        self.__stats_outputter = stats_outputter
        self.__input = inputter

    def run(self):
        for question in self.questions:

            self.__output.present(question, self.summary())
            choice = self.__input.prompt(question.choices.keys())
            correct = question.answer(choice)
            if correct:
                self.correct_answers += 1

            self.responses.append(PyResponse(question, choice, correct))

    def summary(self):
        return self.correct_answers, len(self.questions)

    def stats(self):
        return self.__stats_outputter(self.questions)
