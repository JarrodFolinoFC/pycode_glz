from decorators.quiz_item import quiz_item

@quiz_item(choices=[], tags=['decorators'])
def question_01():
    def deco(func):
        def inner():
            return 'a'

        return inner

    @deco
    def target():
        return 'b'

    return target()


@quiz_item(choices=[], tags=['decorators'])
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


@quiz_item(choices=[], tags=['decorators'])
def question_03():
    b = 6

    def f3(a):
        global b
        b = 1 + a

    f3(4)
    return b


@quiz_item(choices=[], tags=['decorators'])
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


@quiz_item(choices=[], tags=['decorators'])
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


@quiz_item(choices=[], tags=['decorators'])
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

@quiz_item(choices=[], tags=['decorators'])
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

@quiz_item(choices=[], tags=['decorators'])
def question_08():
    from functools import singledispatch

    @singledispatch
    def overload(_: object) -> str:
        return 'object'

    @overload.register
    def _(_: str) -> str:
        return 'string'

    return (overload({}), overload(''))

@quiz_item(choices=[], tags=['decorators'])
def question_09():
    registry = set()
    def register(active=True):
        def decorate(func):
            if active:
                registry.add(func)
            else:
                registry.discard(func)
            return func

        return decorate

    @register(active=False)
    def f1():
        pass
    @register()
    def f2():
        pass

    @register(active=True)
    def f3():
        pass

    def f4():
        pass

    return len(registry)

@quiz_item(choices=[], tags=['decorators'])
def question_10():
    class function_wrapper(object):
        def __init__(self, wrapped):
            self.wrapped = wrapped

        def __call__(self, *args, **kwargs):
            return f'{self.wrapped(*args, **kwargs)}---'

    @function_wrapper
    def a():
        return 'a'

    return a()

@quiz_item(choices=[], tags=['decorators'])
def question_11():
    def function_wrapper(wrapped):
        def _wrapper(*args, **kwargs):
            return wrapped(*args, **kwargs)

        _wrapper.__name__ = wrapped.__name__
        _wrapper.__doc__ = wrapped.__doc__
        return _wrapper

    @function_wrapper
    def function():
        pass

    return function.__name__

@quiz_item(choices=[], tags=['decorators'])
def question_12():
    import functools

    def function_wrapper(wrapped):
        @functools.wraps(wrapped)
        def _wrapper(*args, **kwargs):
            return wrapped(*args, **kwargs)

        return _wrapper

    @function_wrapper
    def function():
        pass

    return function.__name__

@quiz_item(choices=[], tags=['decorators'])
def question_13():
    import functools
    class function_wrapper(object):
        def __init__(self, wrapped):
            self.wrapped = wrapped
            functools.update_wrapper(self, wrapped)

        def __call__(self, *args, **kwargs):
            return self.wrapped(*args, **kwargs)


    @function_wrapper
    def function():
        pass

    return function.__name__

@quiz_item(choices=[], tags=['decorators'])
def question_14():
    import functools
    def function_wrapper(wrapped):
        @functools.wraps(wrapped)
        def _wrapper(*args, **kwargs):
            return wrapped(*args, **kwargs)

        return _wrapper
    class Class(object):
        @function_wrapper
        def method(self):
            pass
        @classmethod
        @function_wrapper
        def cmethod(cls):
            return 'cmethod'
        @staticmethod
        def smethod():
            pass

    return Class.cmethod()
