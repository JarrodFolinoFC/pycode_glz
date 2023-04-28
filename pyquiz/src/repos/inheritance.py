from examon_core.models.quiz_item import quiz_item

from collections import OrderedDict


@quiz_item(choices=[], tags=['inheritancea'])
def question():
    class Parent(object):
        def hello(self):
            return 'hello'

    class Child1(Parent):
        def hello(self, key, value):
            super().hello()
            return f'{super().hello()} there'

    class Child2(Parent):
        def hello(self, key, value):
            super().hello()
            return f'{super().hello()} there'


@quiz_item(choices=[], tags=['inheritancea'])
def question():
    import collections

    class DoppelDict1(collections.UserDict):
        def __setitem__(self, key, value):
            super().__setitem__(key, [value] * 2)

    class DoppelDict2(dict):
        def __setitem__(self, key, value):
            super().__setitem__(key, [value] * 2)

    return DoppelDict1(one=1).values(), DoppelDict2(one=1).values()


@quiz_item(choices=[], tags=['inheritance'])
def question():
    class Root:
        pass

    class A(Root):
        pass

    class B(Root):
        pass

    class Leaf(A, B):
        pass

    return Leaf.__mro__


choices = [('Leaf.ping()->A.ping()->Root.ping()', 'B.pong()->Root.pong()')]


@quiz_item(choices=choices,
           tags=['inheritance'],
           hints=['How does the Python Method Resultion Order work',
                  'What would Leaf.__mro__ return?'])
def question():
    class Root:
        def ping(self): return f'Root.ping()'
        def pong(self): return f'Root.pong()'

    class A(Root):
        def ping(self): return f'A.ping()->{super().ping()}'

    class B(Root):
        def ping(self): return f'B.ping()->{super().ping()}'
        def pong(self): return f'B.pong()->{super().pong()}'

    class Leaf(A, B):
        def ping(self):
            return f'Leaf.ping()->{super().ping()}'

    return (Leaf().ping(), Leaf().pong())
