def question_01():
    def pm(input):
        match input:
            case ('Hello'):
                return 'hello tuple'
            case (_, _):
                return 'two element tuple'
            case _:
                return 'other'
    return pm(('blah'))

def question_02():
    def go(record):
        match record:
            case {'type': 'book', 'author': name}:
                return [name]
            case {'type': 'book'}:
                return None
            case _:
                raise ValueError(f'Invalid record: {record!r}')
    return go({'type': 'book', 'author': 'Bob'})

def pm_questions():
    return [
#         (question_01, [1,2,3]),
        (question_02, [1,2,3]),
    ]