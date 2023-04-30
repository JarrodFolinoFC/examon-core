from examon_core.models.question_factory import QuestionFactory
from examon_core.models.question import ExpectedResultQuestion


def question_fn():
    return 4 + 3


class TestQuestionFactory:
    def test_build(self):
        question = QuestionFactory.build(
            function=question_fn, tags=[], hints=[], choice_list=[7, 6],
            generated_choices=None, param1=None)
        assert isinstance(question, ExpectedResultQuestion)
