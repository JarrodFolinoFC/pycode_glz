class AnswerInputter:
    def __init__(
            self,
            message="Enter Choice: ",
            invalid_message="Invalid choice, try again:"):
        self.__message = message
        self.__invalid_message = invalid_message

    def prompt(self, valid_choices):
        value = input(self.__message)
        while value not in valid_choices:
            value = input(self.__invalid_message)

        return value
