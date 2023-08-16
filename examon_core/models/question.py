from dataclasses import dataclass
from typing import Any


@dataclass
class BaseQuestion:
    unique_id: str = None
    function_src: str = None
    tags: list = None
    hints: list = None
    print_logs: list = None
    correct_answer: str = None
    metrics: Any = None

    def answer(self, given_answer):
        return str(self.correct_answer) == str(given_answer)


@dataclass
class MultiChoiceQuestion(BaseQuestion):
    choices: dict = None


@dataclass
class InputParameterQuestion(BaseQuestion):
    return_value: str = None
    param_one_choices: dict = None
    selected_param: str = None

    def answer(self, choice):
        return choice == self.selected_param


@dataclass
class InputParameterQuestionV2(BaseQuestion):
    result_matrix: dict[Any, Any] = None

    def answer(self, choice):
        return choice == self.result_matrix[choice]
