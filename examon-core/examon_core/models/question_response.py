from dataclasses import dataclass
from .question import BaseQuestion

@dataclass
class QuestionResponse:
    question: BaseQuestion = None
    response: str = None
    correct: bool = None