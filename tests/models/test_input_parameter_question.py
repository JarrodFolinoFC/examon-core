import os
import sys
sys.path.append(f'{os.path.abspath("")}/src/models')

from question import InputParameterQuestion

function_src = """
def question(x):
    return x + 3
"""

choices = {'a': 3, 'b': 5}


class TestFreeTextQuestion:
    def test_answer_correctly(self):
        expected_result_question = InputParameterQuestion(
            function_src=function_src, return_value=6, choices=choices,
            hints=[], tags=[], selected_param=3
        )
        assert expected_result_question.answer('a') is True

    def test_answer_incorrectly(self):
        expected_result_question = InputParameterQuestion(
            function_src=function_src, return_value=6, choices=choices,
            hints=[], tags=[], selected_param=5
        )
        assert expected_result_question.answer('a') is False
