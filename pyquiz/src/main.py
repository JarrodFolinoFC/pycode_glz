from repos.assigment import *
from repos.bytes import *
from repos.classes import *
from repos.collections_1 import *
from repos.decorators_1 import *
from repos.dict_1 import *
from repos.dataclasses import *
from repos.dunder_1 import *
from repos.list_comps_1 import *
from repos.list_1 import *
from repos.pattern_matching_1 import *
from repos.repo_1 import *
from repos.set_1 import *
from repos.slicing_1 import *
from repos.protocols import *
from repos.unpacking_1 import *
from repos.operator_overloading import *
from repos.references import *
from repos.first_class_functions import *
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
        print(qe.stats())
    else:
        args.echo


