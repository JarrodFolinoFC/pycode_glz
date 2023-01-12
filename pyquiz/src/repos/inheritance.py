from decorators.quiz_item import quiz_item
from collections import OrderedDict


@quiz_item(choices=[], tags=['inheritance'])
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


@quiz_item(choices=[], tags=['inheritance'])
def question():
    import collections

    class DoppelDict1(collections.UserDict):
        def __setitem__(self, key, value):
            super().__setitem__(key, [value] * 2)

    class DoppelDict2(dict):
        def __setitem__(self, key, value):
            super().__setitem__(key, [value] * 2)

    return DoppelDict1(one=1).values(), DoppelDict2(one=1).values()
