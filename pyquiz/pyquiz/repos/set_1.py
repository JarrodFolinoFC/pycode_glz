def question_01():
    l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
    return len(list(set(l)))

def question_02():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    return x & y

def question_03():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    return x | y

def question_04():
    x = {"apple", "banana", "cherry"}
    return hash(x)

def question_05():
    x = frozenset(["apple", "banana", "cherry"])
    return hash(x)

def set_questions():
    return [
        (question_05, ['TypeError: TypeError("unhashable type: \'set\'")']),
        (question_04, ['TypeError: TypeError("unhashable type: \'set\'")']),
        (question_03, []),
        (question_02, []),
        (question_01, []),
    ]