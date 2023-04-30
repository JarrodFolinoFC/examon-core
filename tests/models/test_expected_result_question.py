from examon_core.models.question import ExpectedResultQuestion

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
        assert expected_result_question.function_src == function_src
        assert expected_result_question.choices == choices
        assert expected_result_question.correct_answer == correct_answer

    def test_answer_correctly(self):
        expected_result_question = ExpectedResultQuestion(
            function_src=function_src, choices={'a': 6, 'b': 5},
            correct_answer=6, hints=[], tags=[]
        )
        assert expected_result_question.answer('a') == True

    def test_answer_incorrectly(self):
        expected_result_question = ExpectedResultQuestion(
            function_src=function_src, choices={'a': 6, 'b': 5},
            correct_answer=6, hints=[], tags=[]
        )
        assert expected_result_question.answer('b') == False
