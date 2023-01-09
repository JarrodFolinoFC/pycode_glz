from collections import Counter

class QuizEngine:
    def __init__(self, questions, presenter):
        self.__questions = questions
        self.presenter = presenter
        self.__correct_answers = 0
        self.__analyse()

    def run(self):
        for question in self.__questions:
            self.presenter.present(question)
            choice = input("Enter Choice: ")
            while choice not in question.choices.keys():
                choice = input("Invalid choice, try again: ")
            if question.answer(choice):
                self.__correct_answers += 1

    def summary(self):
        return (self.__correct_answers, self.__total_question_count)

    def stats(self):
        return {
            'total_questions': self.__total_question_count,
            'tags_summary': self.tags,
            'tags': self.__tag_count,
        }

    def __analyse(self):
        self.__total_question_count = len(self.__questions)
        tag_set = set()
        [[tag_set.add(tag) for tag in q.tags] for q in self.__questions]
        self.tags = list(tag_set)
        ct = Counter()
        [ct.update(q.tags) for q in self.__questions]
        self.__tag_count = ct
        pass