from examon_core.models.question import MultiChoiceQuestion

function_src = """
def question():
    return 3 + 3
"""


class TestFreeTextQuestion:
    def test_answer_correctly(self):
        expected_result_question = MultiChoiceQuestion(
            function_src=function_src,
            correct_answer=6, hints=[], tags=[]
        )
        assert expected_result_question.answer(6)

    def test_answer_incorrectly(self):
        expected_result_question = MultiChoiceQuestion(
            function_src=function_src,
            correct_answer=6, hints=[], tags=[]
        )
        assert expected_result_question.answer(5) is False
