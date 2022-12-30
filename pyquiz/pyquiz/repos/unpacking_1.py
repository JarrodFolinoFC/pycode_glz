def question_21():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates  # unpacking
    return latitude

def question_22():
    *rest, a, b = range(5)
    return rest[1]

def question_23():
    a, *rest, b = range(5)
    return rest[1]

def question_24():
    def fun(a, b, c, d, *rest):
        return a, b, c, d, rest

    return fun(*[1, 2], 3, *range(4, 7))[3]

def question_25():
    a, b, *rest = range(5)
    return b

def unpacking_questions():
    return [
        (question_21, [1,2,3]),
        (question_22, [1,2,3]),
        (question_23, [1,2,3]),
        (question_24, [1,2,3]),
        (question_25, [1,2,3]),
    ]