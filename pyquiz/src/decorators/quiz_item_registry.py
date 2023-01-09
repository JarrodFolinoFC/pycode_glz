class QuizItemRegistry:
    __registry = []

    @classmethod
    def add(cls, quiz_item):
        cls.__registry.append(quiz_item)

    @classmethod
    def registry(cls, tag=None):
        return [py_quiz_data for py_quiz_data in cls.__registry if tag in py_quiz_data.tags or tag is None]
