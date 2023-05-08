import os
import sys
sys.path.append(f'{os.path.abspath("")}/examon_core')

from question import ExpectedResultQuestion

function_src = """
def question():
    return 3 + 3
"""


class TestExpectedResultQuestion:
    def test__init__1(self):
        choices = {'a': 6, 'b': 5}
        correct_answer = 6
        expected_result_question = ExpectedResultQuestion(
            function_src=function_src, choices=choices,
            correct_answer=correct_answer, hints=[], tags=[]
        )
        assert expected_result_question.function_src is function_src
        assert expected_result_question.choices is choices
        assert expected_result_question.correct_answer is correct_answer

    def test_answer_correctly(self):
        expected_result_question = ExpectedResultQuestion(
            function_src=function_src, choices=[6, 5],
            correct_answer=6, hints=[], tags=[]
        )
        assert expected_result_question.answer(6)

    def test_answer_incorrectly(self):
        expected_result_question = ExpectedResultQuestion(
            function_src=function_src, choices=[6, 5],
            correct_answer=6, hints=[], tags=[]
        )
        assert expected_result_question.answer(5) is False
