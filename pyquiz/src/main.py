from repos.all import *
from factories.quiz_engine_factory import QuizEngineFactory
from decorators.quiz_item_registry import QuizItemRegistry

import argparse
from pygments.formatters import Terminal256Formatter
from pygments.formatters import TerminalFormatter
from pygments.formatters import NullFormatter
from pygments.formatters import TerminalTrueColorFormatter
from pygments.formatters import RawTokenFormatter
from collections import defaultdict

formatter_options = defaultdict(lambda: Terminal256Formatter)
formatter_options['terminal256'] = Terminal256Formatter
formatter_options['terminal'] = TerminalFormatter
formatter_options['null'] = NullFormatter
formatter_options['true'] = TerminalTrueColorFormatter
formatter_options['raw'] = RawTokenFormatter

import pprint

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="[run|overview]")
    parser.add_argument("--formatter", help=f'[{"|".join(formatter_options.keys())}]')
    parser.add_argument("--tag", help='"overview" command will list all tags')
    args = parser.parse_args()

    if args.command == 'run':
        registry = QuizItemRegistry.registry(args.tag)
        qe = QuizEngineFactory.build(registry, formatter_class=formatter_options[args.formatter])
        qe.run()
        pp.pprint(qe.summary())
    elif args.command == 'overview':
        registry = QuizItemRegistry.registry()
        qe = QuizEngineFactory.build(registry, formatter_class=TerminalFormatter)
        stats = qe.stats()
        print(f'Total: ({stats["total_questions"]})\n')
        print('Questions by Tag:')
        for tag in stats['tags']:
            print(f'* {tag} ({stats["tags"][tag]})')
    else:
        parser.print_help()


