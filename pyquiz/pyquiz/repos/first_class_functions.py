def question_01():
    def reverse(word):
        return word[::-1]

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    sorted(fruits, key=reverse)

    return fruits


def question_02():
    from functools import reduce
    from operator import add
    return (reduce(add, range(50)), sum(range(50)))


def question_03():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    sorted(fruits, key=lambda word: word[::-1])
    return fruits


def question_04():
    class CallableClass:

        def __init__(self, thing):
            self.thing = thing

    def __call__(self):
        return f'class called: {self.thing}'

    cc = CallableClass('meow')
    return cc()


def question_05():
    def args(normal, *star_args, key=None, **attrs):
        return f'{normal}, {star_args}, {key}, {attrs}'

    return args('a', 'b', 'c', key='k', s=8)


def question_06():
    def f(*, a, b, c, d):
        return f'{a}, {b}, {c}, {d}'

    return (f(a=1, b=2, c=3, d=4), f(1, 2, 3, 4))


def question_07():
    def add(x, y, /, z):
        return x + y + z

    return add(1, 2, 3) + add(1, 2, z=3)

def question_08():
    from functools import reduce

    def factorial(n):
        return reduce(lambda a, b: a * b, range(1, n + 1))

    return factorial(3)

def question_09():
    from functools import reduce

    def add_together(nums):
        return reduce(lambda a, b: a + b, nums)

    return add_together([1,2,3,4,5,6])

def question_10():
    from functools import reduce
    from operator import mul

    def factorial(n):
        return reduce(mul, range(1, n + 1))

    return factorial(3)

def question_11():
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
       ]
    from operator import itemgetter
    sorted_items = []
    for city in sorted(metro_data, key=itemgetter(1)):
        sorted_items.append(city)

    return [a[0] for a in sorted_items]

def question_12():
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
       ]
    from operator import itemgetter
    sorted_items = []
    cc_name = itemgetter(1, 0)
    for city in metro_data:
        sorted_items.append(cc_name(city))
    return sorted_items

def question_13():
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    from collections import namedtuple
    LatLon = namedtuple('LatLon', 'lat lon')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]

    from operator import attrgetter
    name_lat = attrgetter('name', 'coord.lat')

    sorted_cities = []
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        sorted_cities.append(name_lat(city))

    return sorted_cities[1][0]

def question_14():
    from operator import mul
    from functools import partial
    triple = partial(mul, 3)
    return triple(7)

def first_class_function_questions():
    return [
        (question_13, []),
        (question_12, []),
        (question_11, []),
        (question_09, []),
        (question_08, []),
        (question_07, []),
        (question_06, []),
        (question_05, [])
    ]
