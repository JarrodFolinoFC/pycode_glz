class QuizEngine:
    def __init__(self, questions, presenter):
        self.questions = questions
        self.presenter = presenter
        self.__total_questions = len(self.questions)
        self.__correct_answers = 0

    def run(self):
        for question in self.questions:
            self.presenter(question).present()
            choice = input("Enter Choice: ")
            if question.answer(choice):
                self.__correct_answers += 1

    def summary(self):
        return (self.__correct_answers, self.__total_questions)
