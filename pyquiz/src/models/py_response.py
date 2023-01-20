from dataclasses import dataclass
from .py_question import PyQuestion

@dataclass
class PyResponse:
    py_question: PyQuestion = None
    response: str = None
    correct: bool = None