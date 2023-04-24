class AnswerInputter:
    def __init__(
            self,
            message="Enter Choice: ",
            invalid_message="Invalid choice, try again:"):
        self.__message = message
        self.__invalid_message = invalid_message

    def prompt(self, question):
        valid_choices = question.choices.keys()
        value = input(self.__message)
        while value not in valid_choices:
            value = input(self.__invalid_message)

        return value

class FreeTextAnswerInputter:
    def prompt(self, _question):
        return input('Enter your answer\n\n')
