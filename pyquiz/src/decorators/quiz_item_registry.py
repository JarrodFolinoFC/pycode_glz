class QuizItemRegistry:
    __registry = []

    @classmethod
    def add(cls, quiz_item):
        cls.__registry.append(quiz_item)

    @classmethod
    def registry(cls):
        return cls.__registry
