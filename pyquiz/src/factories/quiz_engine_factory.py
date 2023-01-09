from models.quiz_engine import QuizEngine
from views.cli_presenter import CliPresenter
from factories.py_question_factory import PyQuestionFactory
from pygments.formatters import Terminal256Formatter
from pygments.formatters import TerminalFormatter
from pygments.formatters import NullFormatter
from pygments.formatters import TerminalTrueColorFormatter
from pygments.formatters import RawTokenFormatter

class QuizEngineFactory:
    @classmethod
    def build(cls, quiz_items, formatter_class):
        presenter = CliPresenter(formatter_class)
        qa = [PyQuestionFactory.build(quiz_item[0], quiz_item[1], quiz_item[2]) for quiz_item in quiz_items]
        return QuizEngine(qa, presenter)
