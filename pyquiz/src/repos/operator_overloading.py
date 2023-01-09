from decorators.quiz_item import quiz_item


# @quiz_item(choices=[], tags=['operator_overloading'])
# def question_01():
#     import decimal
#     ctx = decimal.getcontext()
#     ctx.prec = 40
#     one_third = decimal.Decimal('1') / decimal.Decimal('3')
#     result1 = one_third == +one_third
#     ctx.prec = 28
#     result2 = one_third == +one_third
#     return (result1, result2)
#
#
# @quiz_item(choices=[], tags=['operator_overloading'])
# def question_02():
#     from collections import Counter
#     ct = Counter('abracadabra')
#     ct['r'] = -3
#     ct['d'] = 0
#     ct2 = +ct
#     return ct == ct2

# @quiz_item(choices=[], tags=['operator_overloading'])
# def question_03():
#     import math as M
#
#     class Circle:
#         __slots__ = ['radius']
#
#         def __init__(self, radius):
#             self.radius = radius
#
#         def area(self):
#             return M.pi * self.radius ** 2
#
#         def diameter(self):
#             return 2 * self.radius
#
#         def __repr__(self):
#             return f'Circle({self.radius})'
#
#         def __add__(self, other):
#             total_area = self.area() + other.area()
#             radius = M.sqrt(total_area / M.pi)
#             return Circle(radius)
#
#     return Circle(2) + Circle(6)

@quiz_item(choices=[], tags=['operator_overloading'])
def question_03():
    class Number:
        def __init__(self, value):
            self.value = value

        def __mul__(self, other):
            return self.calc(other)

        def calc(self, other):
            if isinstance(other, int):
                other_value = other
            elif isinstance(other, Number):
                other_value = other.value
            return Number(self.value * other_value)

        def __rmul__(self, other):
            return self.calc(other)

        def __repr__(self):
            return f'Number({self.value})'

    return (Number(2) * 4, Number(2) * Number(2), 4 * Number(1))

