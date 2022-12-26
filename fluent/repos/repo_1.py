from collections import namedtuple

question_1 = lambda : 1 + 2

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
    Student = namedtuple('Student', ['name', 'age'])
    s = Student('Bob', 22)
    return getattr(s, 'age')

def question_11():
    letters = 'abcde'
    codes = [(f'{letter.upper()}') for letter in letters]
    return codes

def question_12():
    codes = [last := c for c in [1,2,3,4,5]]
    return last

def question_13():
    codes = [last := c for c in [1,'2',3,4,'5'] if isinstance(c, int)]
    return last

def question_14():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    return tshirts[4]

def question_15():
    accumulated_gexp = sum((x for x in [1,2,3,4,5]))
    return accumulated_gexp

def question_16():
    a = (10, 'alpha', [1, 2])
    b = (10, 'alpha', [1, 2])
    return a == b

def question_17():
    a = (10, 'alpha', [1, 2])
    b = (10, 'alpha', [1, 2])
    b[-1].append(99)
    return a == b

def question_18():
    return type(hash((10, 'alpha', (1, 2))))

def question_19():
    return type(hash((10, 'alpha', [1, 2])))

def question_20():
    return [a for a in list(set(dir([1].__class__)) - set(dir((1).__class__))) if not a.startswith('__')]

def question_21():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates  # unpacking
    return latitude

def question_21():
    a, b, *rest = range(5)
    return b

def question_22():
    *rest, a, b = range(5)
    return rest[1]

def question_23():
    a, *rest, b = range(5)
    return rest[1]

def question_24():
    def fun(a, b, c, d, *rest):
        return a, b, c, d, rest

    return fun(*[1, 2], 3, *range(4, 7))[3]

def question_25():
    def pm(input):
        match input:
            case ('Hello'):
                return 'hello tuple'
            case (_, _):
                return 'two element tuple'
            case _:
                return 'other'
    return pm(('blah'))

def question_26():
    l = [10, 20, 30, 40, 50, 60]
    return l[2:]

def question_27():
    l = [10, 20, 30, 40, 50, 60]
    return l[:2]

def question_28():
    s = 'bicycle'
    return s[::3]

def question_29():
    s = 'bicycle'
    return s[::1]

def question_3x():
    l = list(range(10))
    l[2:5] = [20, 30]
    return l

def question_3x():
    l = list(range(10))
    del l[5:7]
    return l

def question_3x():
    l = list(range(10))
    l[3::2] = [11, 22]
    return l

def question_40():
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

def question_41():
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

def question_42():
    l = [2,3,4,5]
    return sorted(l, reverse= True) == l.sort().reverse()

def questions():
    return [
        (question_1, [1,2,3]),
        (question_2, [1,2,3]),
        (question_3, [1,2,3]),
        (question_4, [1,2,3]),
        (question_5, [1,2,3]),
        (question_6, [1,2,3]),
        (question_7, [1,2,3]),
        (question_9, [1,2,3]),
        (question_10, [1,2,3]),
        (question_11, [1,2,3]),
        (question_12, [1,2,3]),
        (question_13, [1,2,3]),
        (question_14, [1,2,3]),
        (question_15, [1,2,3]),
        (question_16, [1,2,3]),
        (question_17, [1,2,3]),
        (question_19, [1,2,3]),
        (question_20, [1,2,3]),
        (question_21, [1,2,3]),
        (question_22, [1,2,3]),
        (question_23, [1,2,3]),
        (question_24, [1,2,3]),
        (question_25, [1,2,3]),
        (question_26, [1,2,3]),
        (question_27, [1,2,3]),
        (question_29, [1,2,3]),
        (question_20, [1,2,3]),
    ]