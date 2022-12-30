def question_01():
    from collections import ChainMap
    d1 = dict(a=1, b=3)
    d2 = dict(a=2, b=4, c=6)

    chain = ChainMap(d1, d2)
    return chain['a']

def question_01_answers():
    return [ 1, 2, 'keyerror: keyerror(\'a\')' ]

def question_02():
    from collections import ChainMap
    d1 = dict(a=1, b=3)
    d2 = dict(a=2, b=4, c=6)
    chain = ChainMap(d1, d2)
    return chain['c']

def question_02_answers():
    return [6, 'keyerror: keyerror(\'iia\')']

def question_03():
    from collections import OrderedDict
    od = OrderedDict()
    return set(dir(od.__class__)) - set(dir({}.__class__))

def question_03_answers():
    answer = question_03()
    return []
    
def question_04():
    from collections import defaultdict
    dd = defaultdict()
    return set(dir(dd.__class__)) - set(dir({}.__class__))

def question_04_answers():
    answer = question_04()
    return [answer - {'__dict__'}]
    
def question_05():
    from collections import defaultdict
    d = defaultdict(list)

    for i in range(5):
        d[i].append(i)
    return d

def question_05_answers():
    return []
    
def question_06():
    from collections import Counter
    ct = Counter('abracadabra')
    ct.update('aaaaazzz')
    return ct

def question_06_answers():
    return []
    
def question_07():
    from collections import Counter
    ct = Counter('aabbbbcccccc')
    return ct.most_common(2)

def question_07_answers():
    return []
    
def question_08():
    from collections import Counter
    ct = Counter({'a': 1, 'b': 2, 'a': 1, 'a': -1})
    ct.update('ab')
    return ct['b']

def question_08_answers():
    answer = question_08()
    return [answer - 1, answer + 1]
    
def question_09():
    from collections import abc
    return (issubclass(list, abc.Sequence), issubclass(tuple, abc.Sequence))
    
def question_10():
    from collections import abc
    return (issubclass(list, abc.MutableSequence), issubclass(tuple, abc.MutableSequence))
    
def question_11():
    from collections import abc
    return (issubclass(list, abc.Reversible), issubclass(tuple, abc.Reversible))

def boolean_tuple_answers():
    return [(True, False), (False, True), (True, True), (False, False)]
    
def collections_questions():
    return [
        (question_01, question_01_answers()),
        (question_02, question_02_answers()),
        (question_03, question_03_answers()),
        (question_04, question_04_answers()),
        (question_05, question_05_answers()),
        (question_06, question_06_answers()),
        (question_07, question_07_answers()),
        (question_08, question_08_answers()),
        (question_09, boolean_tuple_answers()),
        (question_10, boolean_tuple_answers()),
        (question_11, boolean_tuple_answers()),
    ]