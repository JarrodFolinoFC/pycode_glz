from quiz.quiz_item import quiz_item


# @quiz_item(choices=[], tags=['pattern matching'])
# def question_01():
#     def pm(input):
#         match input:
#             case('Hello'):
#                 return 'hello tuple'
#             case(_, _):
#                 return 'two element tuple'
#             case _:
#                 return 'other'
#     return pm(('blah'))
#
#
# @quiz_item(choices=[], tags=['pattern matching'])
# def question_02():
#     def go(record):
#         match record:
#             case {'type': 'book', 'author': name}:
#                 return [name]
#             case {'type': 'book'}:
#                 return None
#             case _:
#                 raise ValueError(f'Invalid record: {record!r}')
#     return go({'type': 'book', 'author': 'Bob'})
#
#
# @quiz_item(choices=[], tags=['pattern matching'])
# def question_03():
#     def fun(x):
#         match x:
#             case str():
#                 return 'str'
#             case float:
#                 return 'float'
#
#     return (fun(1.1), fun('a'), fun({}))
#
#
# @quiz_item(choices=[], tags=['pattern matching'])
# def question_04():
#     import typing
#
#     class City(typing.NamedTuple):
#         continent: str
#         name: str
#         country: str
#
#     def asian_city(city):
#         match city:
#             case City(continent='Asia'):
#                 return True
#             case _:
#                 return False
#
#     return asian_city(City('Asia', 'Tokyo', 'JP'))
#
#
# @quiz_item(choices=[], tags=['pattern matching'])
# def question_04():
#     def go(x):
#         match x:
#             case int(x) | float(x):
#                 return 'Number'
#             case str(x):
#                 return 'String'
#
#     return (go(1), go('1'))
