def question_01():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates  # unpacking
    return latitude

def question_02():
    *rest, a, b = range(5)
    return rest[1]

def question_03():
    a, *rest, b = range(5)
    return rest[1]

def question_04():
    def fun(a, b, c, d, *rest):
        return a, b, c, d, rest

    return fun(*[1, 2], 3, *range(4, 7))[3]

def question_05():
    a, b, *rest = range(5)
    return b

def unpacking_questions():
    return [
        (question_01, [1,2,3]),
        (question_02, [1,2,3]),
        (question_03, [1,2,3]),
        (question_04, [1,2,3]),
        (question_05, [1,2,3]),
    ]