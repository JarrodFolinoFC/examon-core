from code_metrics import CodeMetrics

from dataclasses import dataclass
from typing import Any


@dataclass
class BaseQuestion:
    choices: dict = None
    function_src: str = None
    tags: list = None
    hints: list = None
    print_logs: list = None
    metrics: CodeMetrics = None


@dataclass
class ExpectedResultQuestion(BaseQuestion):
    correct_answer: str = None

    def answer(self, given_answer):
        return self.correct_answer == given_answer


@dataclass
class InputParameterQuestion(BaseQuestion):
    return_value: str = None
    selected_param: str = None

    def answer(self, choice):
        return choice == self.selected_param
