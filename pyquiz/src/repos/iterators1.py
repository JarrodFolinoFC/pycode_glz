from quiz.quiz_item import quiz_item, ChoiceGenerator


@quiz_item(choices=ChoiceGenerator.boolean_tuple_pair_answers(),
           tags=['iterators'], hints=['here is a hint'])
def question():
    from collections import abc

    class A:
        def __getitem__(self, i):
            return None

    class B:
        def __iter__(self):
            pass

    return (isinstance(A(), abc.Iterable), isinstance(B(), abc.Iterable))


@quiz_item(choices=ChoiceGenerator.boolean_answers(), tags=['iterators'])
def question():
    from collections import abc

    def m1():
        return 4

    return isinstance(iter(m1, 1), abc.Iterable)


@quiz_item(choices=ChoiceGenerator.boolean_answers(), tags=['iterators'])
def question():
    from collections import abc
    return set(dir(abc.Iterator)) - set(dir(abc.Iterable))


@quiz_item(choices=ChoiceGenerator.boolean_answers(), tags=['iterators'])
def question():
    import re
    RE_WORD = re.compile(r'\w+')

    class Sentence:
        def __init__(self, text):
            self.text = text
            self.words = RE_WORD.findall(text)

        def __getitem__(self, index): return self.words[index]
        def __len__(self): return len(self.words)

    return list(Sentence('the quick brown fox'))
