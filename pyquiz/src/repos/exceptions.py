from examon_core.models.quiz_item import quiz_item


# @quiz_item(choices=[True, False], tags=['assert', 'pcap'])
# def question():
#     assert 0
#     assert True
#     return 1
#
# @quiz_item(choices=[True, False], tags=['exceptions', 'pcap'])
# def question():
#     try:
#         1 / 0
#     except ZeroDivisionError:
#         return 'ZeroDivisionError'
#     return None
#
# @quiz_item(choices=[True, False], tags=['list_comprehensions', 'pcap'])
# def question():
#     return [ex // 2 for ex in range(5)]
#
# @quiz_item(choices=[True, False], tags=['ranges', 'pcap'])
# def question():
#     return range(5)[1:]
#
# @quiz_item(choices=[True, False], tags=['ranges', 'pcap'])
# def question():
#     return [[i for i in 'Hello there'] for j in range(3)]
#
# @quiz_item(choices=[True, False], tags=['ranges', 'pcap', 'lambda'])
# def question():
#     def sum_list(args, fun):
#         z = 0
#         for x in args:
#             z = z + fun(x)
#         return z
#
#     return sum_list([ex // 2 for ex in range(5)], lambda x: 1 if x > 1 else 0)
#
# @quiz_item(choices=[True, False], tags=['ranges', 'pcap', 'lambda'])
# def question():
#     def myfunc(n):
#         res = 1
#         for i in range(n, n + 2, 1):
#             yield res
#             res *= 2
#
#     y = [x for x in myfunc(3)]
#     return y
#
# @quiz_item(choices=[True, False], tags=['ranges', 'pcap', 'lambda'])
# def question():
# return ("Hello Again!".find("a", 7, 14), "Hello Again!".find("e", 1,
# 14), "Hello Again!".find("z", 1, 14))


@quiz_item(choices=[(1, 2), (1, None), (None, 2),
           (None, None)], tags=['oo', 'pcap'])
def question():
    class A:
        static_var = 1
        __static_var2 = 2

    return (A.static_var, A._A__static_var2)
