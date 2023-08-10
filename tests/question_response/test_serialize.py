from examon_core.models.question import InputParameterQuestion
from examon_core.models.question_response import QuestionResponse
from examon_core.models.code_metrics import CodeMetricsFactory

from dataclasses_serialization.json import JSONSerializer


function_src = """
def question(x):
    print(1)
    return (x + 3, 9)
"""

choices = [3, 5, [3, 5]]


class TestInputParameterQuestion:
    def test_to_json(self):
        question = InputParameterQuestion(
            function_src=function_src,
            return_value=6,
            param_one_choices=choices,
            hints=[],
            tags=[],
            selected_param=3,
            metrics=CodeMetricsFactory.build(function_src))
        question_response = QuestionResponse(question, 2, True)

        serialized = JSONSerializer.serialize(question_response)

        assert serialized['correct'] == question_response.correct
        assert serialized['response'] == question_response.response
        assert serialized['question']['param_one_choices'] == question_response.question.param_one_choices
        assert serialized['question']['return_value'] == question_response.question.return_value
        assert serialized['question']['selected_param'] == question_response.question.selected_param
        assert serialized['question']['tags'] == question_response.question.tags
        assert serialized['question']['function_src'] == question_response.question.function_src
        assert serialized['question']['print_logs'] == question_response.question.print_logs
        assert serialized['question']['metrics']['difficulty'] == 0.5
