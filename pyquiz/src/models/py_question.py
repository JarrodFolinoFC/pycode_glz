from dataclasses import dataclass


@dataclass
class PyQuestion:
    choices: dict = None
    function_src: str = None
    correct_answer: str = None
    tags: list = None
    hints: list = None

    def answer(self, choice):
        return self.choices[choice] == self.correct_answer
