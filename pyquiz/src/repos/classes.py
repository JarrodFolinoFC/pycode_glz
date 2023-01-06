from decorators.quiz_item import quiz_item


@quiz_item(choices=['Vector2d(1, 2)'], tags=['classes'])
def question_01():
    from array import array
    import math

    class Vector2d:
        typecode = 'd'

        def __init__(self, x, y):
            self.x = float(x)
            self.y = float(y)

        def __iter__(self): return (i for i in (self.x, self.y))

        def __repr__(self):
            class_name = type(self).__name__
            return '{}({!r}, {!r})'.format(class_name, *self)

        def __str__(self): return str(tuple(self))

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) +
                    bytes(array(self.typecode, self)))

        def __eq__(self, other): return tuple(self) == tuple(other)

        def __abs__(self): return math.hypot(self.x, self.y)

        def __bool__(self): return bool(abs(self))

    return Vector2d(1, 2).__repr__()


@quiz_item(choices=[('Bob', None)],
           tags=['classes'])
def question_02():
    class Student:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, newname):
            self._name = newname

    student = Student('Bob')
    return (student._name, student.name)


@quiz_item(choices=['XYZ School', 'display'], tags=['classes'])
def question_03():
    class Student:
        __schoolName = 'XYZ School'

        def __init__(self, name):
            self.__name = name

        def __display(self):
            return 'display'

    student = Student('Bob')
    return (student.__display())


@quiz_item(choices=[], tags=['classes'])
def question_04():
    class Student:
        __schoolName = 'XYZ School'

        def __init__(self, name):
            self.__name = name

        def __display(self):
            return 'private method'

    student = Student('Bob')
    return (student._Student__display())


@quiz_item(choices=['static_foo', 'class_foo'], tags=['classes'])
def question_05():
    class A(object):
        def foo(self, x):
            print(f"executing foo({self}, {x})")

        @classmethod
        def class_foo(cls):
            return 'class_foo'

        @staticmethod
        def static_foo():
            return 'static_foo'

    return (A.class_foo(), A.static_foo())
