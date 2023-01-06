from decorators.quiz_item import quiz_item

@quiz_item(choices=[], tags=['references'])
def question_01():
    a = [1, 2, 3]
    b = a
    a.append(4)
    return b

@quiz_item(choices=[], tags=['references'])
def question_02():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    return (lewis is charles, alex is charles)

@quiz_item(choices=[], tags=['references'])
def question_03():
    return x is None

@quiz_item(choices=[], tags=['references'])
def question_04():
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = l1[:]
    return l1 is l2

@quiz_item(choices=[], tags=['references'])
def question_05():
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1[1].remove(55)
    return l2 == [3, [66, 55, 44], (7, 8, 9)]

@quiz_item(choices=[], tags=['references'])
def question_06():
    def f(obj):
        obj['a'] = 1
        return a

    d1 = {}
    return d1 == f(d1)

@quiz_item(choices=[], tags=['references'])
def question_07():
    class Bus:
        def __init__(self, passengers=[]):
            self.passengers = passengers

        def pick(self, name):
            self.passengers.append(name)

        def drop(self, name):
            self.passengers.remove(name)

    bus2 = Bus()
    bus2.pick('Carrie')
    bus2.passengers
    bus3 = Bus()
    bus3.passengers
    bus3.pick('Dave')
    return bus2.passengers


@quiz_item(choices=[], tags=['references'])
def question_08():
    class Bus:
        def __init__(self, passengers=None):
            if passengers is None:
                self.passengers = []
            else:
                self.passengers = passengers

        def pick(self, name):
            self.passengers.append(name)

        def drop(self, name):
            self.passengers.remove(name)

    bus2 = Bus()
    bus2.pick('Carrie')
    bus2.passengers
    bus3 = Bus()
    bus3.passengers
    bus3.pick('Dave')
    return bus2.passengers

@quiz_item(choices=[], tags=['references'])
def question_09():
    import weakref

    def bye():
        pass

    a = [1,2,3]
    b = a
    ender = weakref.finalize(a, bye)
    return ender.alive

@quiz_item(choices=[], tags=['references'])
def question_10():
    a = 3
    del a
    return a

@quiz_item(choices=[], tags=['references'])
def question_11():
    import weakref

    def bye():
        pass

    a = 4
    b = a
    ender = weakref.finalize(a, bye)
    return ender.alive

@quiz_item(choices=[], tags=['references'])
def question_12():
    import weakref

    def bye():
        pass

    a = {4}
    b = a
    ender = weakref.finalize(a, bye)
    return ender.alive

@quiz_item(choices=[], tags=['references'])
def question_13():
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    t3 = t1[:]
    return (t2 is t1, t3 is t1)

@quiz_item(choices=[], tags=['references'])
def question_14():
    import weakref

    class ExpensiveObject(object):
        def __del__(self):
            print
            '(Deleting %s)' % self

    obj = ExpensiveObject()
    r1 = weakref.ref(obj)
    del obj
    return r1()

@quiz_item(choices=[], tags=['references'])
def question_15():
    import ctypes
    my_list = [1, 2, 3]
    my_list_address = id(my_list)
    return ctypes.c_long.from_address(my_list_address).value
