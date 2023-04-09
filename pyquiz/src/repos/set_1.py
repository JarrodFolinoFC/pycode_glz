from quiz.quiz_item import quiz_item


@quiz_item(choices=[True, None, {}], tags=['sets'], generated_choices='answer_plus_random')
def question_01():
    l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
    return len(list(set(l)))


@quiz_item(choices=[{"apple", "banana", "cherry", "google", "microsoft"}],
           tags=['sets1'], generated_choices='answer_plus_random')
def question_02():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    return x & y


@quiz_item(choices=[], tags=['sets'])
def question_03():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    return x | y


@quiz_item(choices=[], tags=['sets'])
def question_04():
    x = {"apple", "banana", "cherry"}
    return hash(x)


@quiz_item(choices=[], tags=['sets'])
def question_05():
    x = frozenset(["apple", "banana", "cherry"])
    return hash(x)
