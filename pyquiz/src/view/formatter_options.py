from pygments.formatters import Terminal256Formatter
from pygments.formatters import TerminalFormatter
from pygments.formatters import NullFormatter
from pygments.formatters import TerminalTrueColorFormatter
from pygments.formatters import RawTokenFormatter
from collections import defaultdict

OPTIONS = [
    ('terminal256', Terminal256Formatter),
    ('terminal', TerminalFormatter),
    ('null', NullFormatter),
    ('true', TerminalTrueColorFormatter),
    ('raw', RawTokenFormatter)
]

class FormatterOptions:
    def __init__(self):
        self.formatter_options = defaultdict(lambda: Terminal256Formatter)
        for option in OPTIONS:
            self.formatter_options[option[0]] = option[1]

    def __getitem__(self, item):
        return self.formatter_options[item]

    def __str__(self):
        return "|".join(self.formatter_options.keys())
