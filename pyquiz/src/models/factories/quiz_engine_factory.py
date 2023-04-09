from view.input.answer_question import AnswerInputter
from view.output.question import QuestionOutputter
from lib.calc_stats import calc_stats
from models.quiz_engine import QuizEngine
from quiz.quiz_item_registry import QuizItemRegistry

def build_quiz_engine(tag, formatter_class):
    registry = QuizItemRegistry.registry(tag)
    question_outputter = QuestionOutputter(formatter_class)
    answer_inputter = AnswerInputter()
    return QuizEngine(
        questions=registry,
        outputter=question_outputter,
        stats_outputter=calc_stats,
        inputter=answer_inputter)