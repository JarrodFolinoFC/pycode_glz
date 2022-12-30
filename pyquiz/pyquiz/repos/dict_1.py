from collections import OrderedDict, defaultdict
from collections import ChainMap
from collections import Counter

def question_01():
    num_words = {
        1: 'one', 2: 'two',
        3: 'three', 4: 'four',
        5: 'five',
    }
    return {key for key, value in num_words.items()}

def question_02():
    def dump(**kwargs):
        return kwargs

    return dump(**{'x': 1}, y=2, **{'z': 3})

def question_03():
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    return d1 | d2

def question_04():
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    d1 |= d2
    return d1

def question_05():
    return isinstance({}, abc.Mapping) == isinstance({}, abc.MutableMapping)

def question_06():
    car1 = { "model": "Mustang", "year": 1964 }
    car2 = { "model": "Mustang", "year": 1964, 'color': 'blue' }
    car1.setdefault("color", "white")
    car2.setdefault("color", "white")
    return (car1['color'], car2['color'])

def question_07():
    od = OrderedDict()
    od['b'] = 2
    od['a'] = 1
    od['d'] = 4
    od['c'] = 3
    return [x for x in od.keys()]

def question_12():
    d = {}
    return d.get('a', 'not found')

def question_13():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 2, 'c': 3}
    return d1.keys() & d2.keys()

def question_14():
    def def_value():
        return "Not Present"
    dd = defaultdict(def_value)
    return dd['?']

def question_16():
    class StrKeyDict0(dict):

        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]

        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default

        def __contains__(self, key):
            return key in self.keys() or str(key) in self.keys()

    skd = StrKeyDict0({'a': 1, 'b': 2})
    return skd['c']

def dict_questions():
    return [
        (question_01, [1,2,7,88, 'No idea']),
        (question_02, []),
        (question_03, []),
        (question_04, []),
    ]