from examon_core.models.question import InputParameterQuestion

function_src = """
def question(x):
    return x + 3
"""

choices = [3, 5]


class TestInputParameterQuestion:
    def test_answer_correctly(self):
        expected_result_question = InputParameterQuestion(
            function_src=function_src, return_value=6, param_one_choices=choices,
            selected_param=3
        )
        assert expected_result_question.answer(3) is True

    def test_answer_incorrectly(self):
        expected_result_question = InputParameterQuestion(
            function_src=function_src, return_value=6, param_one_choices=choices,
            selected_param=3
        )
        assert expected_result_question.answer(5) is False
