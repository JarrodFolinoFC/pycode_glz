def question_01():
    def deco(func):
        def inner():
            return 'a'

        return inner

    @deco
    def target():
        return 'b'

    return target()


def question_02():
    registry = []

    def register(func):
        registry.append(func)
        return func

    @register
    def f1():
        pass

    @register
    def f2():
        pass

    def f3():
        pass

    f2()
    f2()
    f2()

    return len(registry)


def question_03():
    b = 6

    def f3(a):
        global b
        b = 1 + a

    f3(4)
    return b


def question_04():
    def make_averager():
        series = []

        def averager(new_value):
            series.append(new_value)
            total = sum(series)
            return total / len(series)

        return averager

    avg = make_averager()

    avg(5)
    avg(10)
    return avg(15)


def question_05():
    def make_averager():
        series = []

        def averager(new_value):
            series.append(new_value)
            total = sum(series)
            return total / len(series)

        return averager

    avg = make_averager()
    return (avg.__code__.co_varnames, avg.__code__.co_freevars)


def question_06():
    def make_averager():
        count = 0
        total = 0

        def averager(new_value):
            nonlocal count, total
            count += 1
            total += new_value
            return total / count

        return averager

    avg = make_averager()
    avg(2)
    return avg(5)

def question_07():
    from functools import wraps
    def append_year(func):
        @wraps(func)
        def appended_year(*args, **kwargs):
            return func(*args, **kwargs) + ', 2023'
        return appended_year

    @append_year
    def hello():
        return 'Hello'

    return hello()


def question_08():
    from functools import singledispatch

    @singledispatch
    def overload(_: object) -> str:
        return 'object'

    @overload.register
    def _(_: str) -> str:
        return 'string'

    return (overload({}), overload(''))



def deco_questions():
    return [
        (question_08, []),
        (question_07, []),
        (question_05, []),
        (question_04, []),
        (question_03, []),
        (question_02, []),
        (question_01, []),
    ]
