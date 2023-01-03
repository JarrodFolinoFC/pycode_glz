def question_01():
    a = [1, 2, 3]
    b = a
    a.append(4)
    return b

def question_02():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    return (lewis is charles, alex is charles)

def question_03():
    return x is None

def question_04():
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = l1[:]
    return l1 is l2

def question_05():
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1[1].remove(55)
    return l2 == [3, [66, 55, 44], (7, 8, 9)]

def question_06():
    def f(obj):
        obj['a'] = 1
        return a

    d1 = {}
    return d1 == f(d1)

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

def question_09():
    import weakref

    def bye():
        pass

    a = [1,2,3]
    b = a
    ender = weakref.finalize(a, bye)
    return ender.alive

def question_10():
    a = 3
    del a
    return a

def question_11():
    import weakref

    def bye():
        pass

    a = 4
    b = a
    ender = weakref.finalize(a, bye)
    return ender.alive

def question_12():
    import weakref

    def bye():
        pass

    a = {4}
    b = a
    ender = weakref.finalize(a, bye)
    return ender.alive

def question_13():
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    t3 = t1[:]
    return (t2 is t1, t3 is t1)

def reference_questions():
    return [
        (question_12, [True, False, TypeError("cannot create weak reference to 'int' object")]),
        (question_11, [True, False, TypeError("cannot create weak reference to 'int' object")]),
        (question_09, [True, False, TypeError("cannot create weak reference to 'list' object")]),
        (question_10, [UnboundLocalError("local variable 'a' referenced before assignment"), None])
    ]