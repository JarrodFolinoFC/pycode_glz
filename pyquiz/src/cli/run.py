import argparse
from .formatter_options import FormatterOptions
from .input.quiz_arg_parse import QuizArgParse
from .input.answer_question import AnswerInputter
from .output.question import QuestionOutputter
from utils.calc_stats import calc_stats
from models.quiz_engine import QuizEngine
from quiz.quiz_item_registry import QuizItemRegistry

def display_stats(stats):
    print(f'Total: ({stats["total_questions"]})\n')
    print('Questions by Tag:')
    for tag in stats['tags']:
        print(f'* {tag} ({stats["tags"][tag]})')

def run():
    def build_quiz_engine(tag, formatter_class):
        registry = QuizItemRegistry.registry(tag)
        question_outputter = QuestionOutputter(formatter_class)
        answer_inputter = AnswerInputter()
        return QuizEngine(
            questions=registry,
            outputter=question_outputter,
            stats_outputter=calc_stats,
            inputter=answer_inputter)

    cli_args = QuizArgParse(
        argparse.ArgumentParser(),
        FormatterOptions()).parse()
    quiz_engine = build_quiz_engine(
        cli_args.tag, FormatterOptions().fetch(
            cli_args.formatter))

    match cli_args.command:
        case 'run':
            quiz_engine.run()
            print(quiz_engine.summary())
        case 'overview':
            display_stats(quiz_engine.stats())
        case _:
            print(cli_args)
