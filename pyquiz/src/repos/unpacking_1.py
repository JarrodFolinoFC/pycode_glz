from examon_core.models.quiz_item import quiz_item



@quiz_item(choices=[], tags=['unpacking'])
def question_01():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    return latitude


@quiz_item(choices=[], tags=['unpacking'])
def question_02():
    *rest, a, b = range(5)
    return rest[1]


@quiz_item(choices=[], tags=['unpacking'])
def question_03():
    a, *rest, b = range(5)
    return rest[1]


@quiz_item(choices=[], tags=['unpacking'])
def question_04():
    def fun(a, b, c, d, *rest):
        return a, b, c, d, rest

    return fun(*[1, 2], 3, *range(4, 7))[3]


@quiz_item(choices=[], tags=['unpacking'])
def question_05():
    a, b, *rest = range(5)
    return b


@quiz_item(choices=[], tags=['unpacking'])
def question_06():
    def my_function(*args, **kwargs):
        return (args, kwargs)

    return my_function(1, 2, b=3, c=4)
