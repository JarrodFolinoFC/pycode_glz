def question_2():
    class MyClass(object):
        def __len__(self):
            return 3

    return len(MyClass())

def question_3():
    class A:
        def __init__(self, item):
            self.item = item
        def __getitem__(self, index):
            return self.item[index]

    return A([2,3,4,5,6,7])[3]

def question_4():
    class A:
        def __init__(self, item):
            self.item = item
        def __getitem__(self, index):
            return self.item[index]

    return A(2,3,4,5,6,7)[3]

def question_5():
    class A:
        def __init__(self, item):
            self.item = item

        def __getitem__(self, index):
            return self.item[index]

    return A([2,3,4,5,6,7])[6]

def question_6():
    class MagicWord:
        def __init__(self, value='', multiplier = 1):
            self.value = value
            self.multiplier = multiplier

        def __add__(self, other):
            return f'{self.value * self.multiplier}{other.value * other .multiplier}'

    return MagicWord('a', 2) + MagicWord('b', 3)

def question_7():
    class YesNo:
        def __init__(self, value=''):
            self.value = value

        def __bool__(self):
            return self.value.lower == 'yes'

    return bool(YesNo('yeS'))

def question_8():
    class Represent:
        def __init__(self, value=''):
            self.value = value

        def __repr__(self):
            return f'--{self.value}--'

    return str(Represent('value'))

def question_9():
    class Multi:
        def __init__(self, value=7):
            self.value = value

        def __mul__(self, other):
            return (self.value + 1) * (other.value - 1)

    return Multi(2) * Multi(4)

def question_10():
    class MyClass:
        def __init__(self, item):
            self.item = item

        def __add__(self, other):
            return self.item + other.item

        def __iadd__(self, other):
            return self.item + other.item + 1


    a = MyClass(5)
    a += MyClass(4)
    return a

def question_11():
    class Person:
        def __init__(self, name):
            self.name = name

        def __ge__(self, other):
            if self.name == 'Chuck Norris':
                return True
            else:
                return self.name > other.name

    return Person('Chuck Norris') > Person('Bob')

def dunder_questions():
    return [
        (question_11, [True, "TypeError(\"'>' not supported between instances of 'Person' and 'Person'\")"]),
        (question_2, [1,2,3]),
        (question_3, [1,2,3]),
        (question_4, [1,2,3]),
        (question_5, [1,2,3]),
        (question_6, [1,2,3]),
        (question_7, [1,2,3]),
        (question_9, [1,2,3]),
        (question_10, [1,2,3]),
    ]