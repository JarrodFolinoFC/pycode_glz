from decorators.quiz_item import quiz_item

# @quiz_item(choices=[], tags=['monkey patching'])
# def question_01():
#     class A:
#         def __init__(self):
#             self.value = ''
#
#     a = A()
#     def concat(a, other_value):
#         a.value = a.value + other_value
#
#     A.concat = concat
#     a.concat('b')
#     return a.value
#
# @quiz_item(choices=[], tags=['monkey patching'])
# def question_02():
#     from collections.abc import Sized  # Sized needs __len__
#     class SizedClass(Sized):
#         def __init__(self):
#             pass
#
#     return SizedClass()

# @quiz_item(choices=[['m2'], ['m1', 'm2']], tags=['abc'])
# def question_03():
#     from abc import ABC, abstractmethod
#     class Abstract(ABC):
#         @abstractmethod
#         def m1(self): pass
#         @abstractmethod
#         def m2(self): pass
#         def m1(self): pass
#
#     return list(Abstract.__abstractmethods__)

# @quiz_item(choices=[['m2'], ['m1', 'm2']], tags=['abc'])
# def question_04():
#     import abc
#
#     class Base(abc.ABC):
#         @abc.abstractmethod
#         def m1(self, iterable): pass
#         @abc.abstractmethod
#         def m2(self): pass
#
#     class C1(Base):
#         def m1(self): pass
#         def __repr__(self): return f'C1()'
#
#     class C2(Base):
#         def m1(self): pass
#         def m2(self): pass
#         def __repr__(self): return f'C2()'
#
#     @Base.register
#     class C3:
#         def __repr__(self): return f'C4()'
#
#     try: a = C1()
#     except Exception as e: a = repr(e)
#
#     try: b = C2()
#     except Exception as e: b = repr(e)
#
#     try: c = C3()
#     except Exception as e: c = repr(e)
#
#     return (a, b, c)

# @quiz_item(choices=[['m2'], ['m1', 'm2']], tags=['abc'])
# def question_05():
#     import abc
#
#     class Base(abc.ABC):
#         @abc.abstractmethod
#         def m1(self, iterable): pass
#         @abc.abstractmethod
#         def m2(self): pass
#
#     @Base.register
#     class C1:
#         def __repr__(self): return f'C4()'
#
#     return (
#         isinstance(C1(), Base),
#         issubclass(C1, Base),
#         isinstance(C1(), abc.ABC),
#         issubclass(C1, abc.ABC)
#     )

# @quiz_item(choices=[['m2'], ['m1', 'm2']], tags=['abc'])
# def question_05():
#     class A(type):
#         def __subclasscheck__(cls, sub):
#             attr = getattr(cls, 'L', [])
#             if sub in attr:
#                 return True
#             return False
#
#     class B(metaclass=A):
#         L = [1, 2, 3, 4, 5]
#
#     class C(metaclass=A):
#         L = ["Subclass"]
#
#     return (issubclass(1, B), issubclass("Subclass", B), issubclass("Subclass", C))
#
# @quiz_item(choices=[['m2'], ['m1', 'm2']], tags=['abc'])
# def question_06():
#     from typing import TypeVar, Protocol
#
#     T = TypeVar('T')
#
#     class Repeatable(Protocol):
#         def __mul__(self: T, repeat_count: int) -> T: ...
#     RT = TypeVar('RT', bound=Repeatable)
#
#     def double(x: RT) -> RT:
#         return x * 2
#
# @quiz_item(choices=[], tags=['abc'])
# def question_07():
#     from typing import Protocol
#
#     class Flyer(Protocol):
#         def fly(self) -> str: ...
#
#     class Bird:
#         def fly(self): return 'bird is flying'
#
#     class Plane:
#         def fly(self): return 'plane is flying'
#
#     def call(flyer: Flyer):
#         return flyer.fly()
#
#     return [call(flyer) for flyer in [Bird(), Plane()]]
#
# @quiz_item(choices=[], tags=['abc'])
# def question_08():
#     from typing import Protocol
#
#     class Flyer(Protocol):
#         def fly(self) -> str: ...
#
#     class Bird:
#         def fly(self): return 'bird is flying'
#
#     class Car:
#         def drive(self): return 'plane is flying'
#
#     def call(flyer: Flyer):
#         return flyer.fly()
#
#     return [call(flyer) for flyer in [Bird(), Car()]]

# @quiz_item(choices=[], tags=['abc'])
# def question_09():
#     from typing import SupportsInt
#     class A:
#         __slots__ = ()
#
#         def __int__(self) -> complex:
#             4
#
#     return isinstance(A(), SupportsInt)