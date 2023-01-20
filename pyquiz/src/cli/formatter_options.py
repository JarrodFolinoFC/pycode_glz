from pygments.formatters import Terminal256Formatter
from pygments.formatters import TerminalFormatter
from pygments.formatters import NullFormatter
from pygments.formatters import TerminalTrueColorFormatter
from pygments.formatters import RawTokenFormatter
from collections import defaultdict


class FormatterOptions:
    def __init__(self):
        self.formatter_options = defaultdict(lambda: Terminal256Formatter)
        self.formatter_options['terminal256'] = Terminal256Formatter
        self.formatter_options['terminal'] = TerminalFormatter
        self.formatter_options['null'] = NullFormatter
        self.formatter_options['true'] = TerminalTrueColorFormatter
        self.formatter_options['raw'] = RawTokenFormatter

    def fetch(self, value):
        return self.formatter_options[value]

    def __str__(self):
        return "|".join(self.formatter_options.keys())
