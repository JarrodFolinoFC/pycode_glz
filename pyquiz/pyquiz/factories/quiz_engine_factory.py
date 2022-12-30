from models.quiz_engine import QuizEngine
from views.cli_presenter import CliPresenter
from factories.py_question_factory import PyQuestionFactory

class QuizEngineFactory:
    @classmethod
    def build(cls, questions):
        qa = [PyQuestionFactory.build(q[0], q[1]) for q in questions]
        return QuizEngine(qa, CliPresenter)
