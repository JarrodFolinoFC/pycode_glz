from dataclasses import dataclass

@dataclass
class BaseQuestion:
    choices: dict = None
    function_src: str = None
    tags: list = None
    hints: list = None


@dataclass
class ExpectedResultQuestion(BaseQuestion):
    correct_answer: str = None

    def answer(self, choice):
        return self.choices[choice] == self.correct_answer

@dataclass
class InputParameterQuestion(BaseQuestion):
    return_value: str = None
    selected_param: str = None

    def answer(self, choice):
        return self.choices[choice] == self.selected_param
