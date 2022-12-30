def question_01():
    d1 = dict(a=1, b=3)
    d2 = dict(a=2, b=4, c=6)

    chain = ChainMap(d1, d2)
    return chain['a']

def question_02():
    d1 = dict(a=1, b=3)
    d2 = dict(a=2, b=4, c=6)
    chain = ChainMap(d1, d2)
    return chain['c']

def question_03():
    od = OrderedDict()
    return set(dir(od.__class__)) - set(dir({}.__class__))

def question_04():
    dd = defaultdict()
    return set(dir(dd.__class__)) - set(dir({}.__class__))

def question_05():
    d = defaultdict(list)

    for i in range(5):
        d[i].append(i)
    return d

def question_06():
    ct = Counter('abracadabra')
    ct.update('aaaaazzz')
    return ct

def question_07():
    ct = Counter('aabbbbcccccc')

    return ct.most_common(2)

def question_08():
    ct = Counter({'a': 1, 'b': 2})
    ct.update('ab')
    return ct['b']

def question_10():
    from collections import abc
    return (issubclass(list, abc.MutableSequence), issubclass(tuple, abc.MutableSequence))

def question_10():
    from collections import abc
    return (issubclass(list, abc.Reversible), issubclass(tuple, abc.Reversible))

def collections_questions():
    return [
        (question_08, []),
    ]