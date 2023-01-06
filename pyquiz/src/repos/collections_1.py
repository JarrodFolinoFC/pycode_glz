from decorators.quiz_item import quiz_item

bool_tuple_choices = [(True, False), (False, True), (True, True), (False, False)]

@quiz_item(choices=[1, 2, 'keyerror: keyerror(\'a\')'], tags=['collections'])
def question_01():
    from collections import ChainMap
    d1 = dict(a=1, b=3)
    d2 = dict(a=2, b=4, c=6)

    chain = ChainMap(d1, d2)
    return chain['a']

@quiz_item(choices=[6, 'keyerror: keyerror(\'c\')'], tags=['collections'])
def question_02():
    from collections import ChainMap
    d1 = dict(a=1, b=3)
    d2 = dict(a=2, b=4, c=6)
    chain = ChainMap(d1, d2)
    return chain['c']

@quiz_item(choices=[], tags=['collections'])
def question_03():
    from collections import OrderedDict
    od = OrderedDict()
    return set(dir(od.__class__)) - set(dir({}.__class__))

@quiz_item(choices=[], tags=['collections'])
def question_04():
    from collections import defaultdict
    dd = defaultdict()
    return set(dir(dd.__class__)) - set(dir({}.__class__))


@quiz_item(choices=[[]], tags=['collections'])
def question_05():
    from collections import defaultdict
    d = defaultdict(list)

    for i in range(5):
        d[i].append(i)
    return d.keys()

@quiz_item(choices=[[]], tags=['collections'])
def question_06():
    from collections import Counter
    ct = Counter('abracadabra')
    ct.update('aaaaazzz')
    return ct


@quiz_item(choices=[[]], tags=['collections'])
def question_07():
    from collections import Counter
    ct = Counter('aabbbbcccccc')
    return ct.most_common(2)

@quiz_item(choices=[[]], tags=['collections'])
def question_08():
    from collections import Counter
    ct = Counter({'a': 1, 'b': 2, 'a': 1, 'a': -1})
    ct.update('ab')
    return ct['b']

@quiz_item(choices=[bool_tuple_choices], tags=['collections'])
def question_09():
    from collections import abc
    return (issubclass(list, abc.Sequence), issubclass(tuple, abc.Sequence))
    
@quiz_item(choices=[bool_tuple_choices], tags=['collections'])
def question_10():
    from collections import abc
    return (issubclass(list, abc.MutableSequence), issubclass(tuple, abc.MutableSequence))
    
@quiz_item(choices=[bool_tuple_choices], tags=['collections'])
def question_11():
    from collections import abc
    return (issubclass(list, abc.Reversible), issubclass(tuple, abc.Reversible))

@quiz_item(choices=[[]], tags=['collections'])
def question_12():
    from collections import deque
    dq = deque(range(3), maxlen=10)
    dq.rotate(1)
    return list(dq)

@quiz_item(choices=[[]], tags=['collections'])
def question_13():
    from collections import deque
    dq = deque(range(3), maxlen=10)
    dq.rotate(1)
    dq2 = dq
    dq2.rotate(1)
    return (list(dq), list(dq2))

@quiz_item(choices=[[]], tags=['collections'])
def question_14():
    from collections import deque
    return list(deque(range(10), maxlen=4))
