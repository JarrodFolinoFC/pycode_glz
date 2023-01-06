from models.quiz_engine import QuizEngine
from views.cli_presenter import CliPresenter
from factories.py_question_factory import PyQuestionFactory

class QuizEngineFactory:
    @classmethod
    def build(cls, quiz_items):
        qa = [PyQuestionFactory.build(quiz_item[0], quiz_item[1], quiz_item[2]) for quiz_item in quiz_items]
        return QuizEngine(qa, CliPresenter)
