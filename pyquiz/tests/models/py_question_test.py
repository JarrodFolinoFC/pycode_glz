from pyquiz.src.models.py_question import PyQuestion


question = """
def question():
    return 3 + 3
"""

class TestPyQuestionAnswer:
    def test__init__1(self):
        q = PyQuestion(function_src=question, choices={'a': 6, 'b': 5},
                       correct_answer=6, hints=[], tags=[])
        assert q.answer('a') == True

    def test_answer_2(self):
        q = PyQuestion(function_src=question, choices={'a': 6, 'b': 5},
                       correct_answer=6, hints=[], tags=[])
        assert q.answer('a') == True

    def test_answer_3(self):
        q = PyQuestion(function_src=question, choices={'a': 6, 'b': 5},
                       correct_answer=6, hints=[], tags=[])
        assert q.answer('b') == False
