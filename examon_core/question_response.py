from dataclasses import dataclass
from examon_core.question import BaseQuestion


@dataclass
class QuestionResponse:
    question: BaseQuestion = None
    response: str = None
    correct: bool = None
