import argparse
from view.formatter_options import FormatterOptions
from view.input.quiz_arg_parse import QuizArgParse
from view.output.display_stats import display_stats
from models.factories.quiz_engine_factory import build_quiz_engine


class CliRuntime:
    @staticmethod
    def run():
        cli_args = QuizArgParse(argparse.ArgumentParser(), FormatterOptions()).parse()
        quiz_engine = build_quiz_engine(cli_args.tag, FormatterOptions()[cli_args.formatter])

        match cli_args.command:
            case 'run':
                quiz_engine.run()
                print(quiz_engine.summary())
            case 'overview':
                display_stats(quiz_engine.stats())
            case _:
                print(cli_args)
