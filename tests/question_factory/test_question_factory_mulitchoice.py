from examon_core.models.question_factory import QuestionFactory
from examon_core.models.question import MultiChoiceQuestion
from dataclasses_serialization.json import JSONSerializer


def question_fn():
    print('test')
    answer = 4 + 3
    print(answer)
    return answer


def question_fn_tuple_answer():
    print('test')
    answer = 4 + 3
    print(answer)
    return answer


class TestQuestionFactoryExpectedResult:
    def test_build_print_logs(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'],
            choice_list=['a'],
            hints=[])
        assert question.__class__ == MultiChoiceQuestion
        assert question.print_logs == ['test', '7', '7']

    def test_build_unique_id(self):
        for i in range(0, 10):
            question = QuestionFactory.build(
                function=question_fn, tags=['a'],
                choice_list=['a'],
                hints=[])
            assert question.unique_id == '10549360651236169307812175599540'
            assert question.__class__ == MultiChoiceQuestion


    def test_build_internal_id(self):
        question = QuestionFactory.build(
            internal_id="some_id",
            function=question_fn, tags=['a'], choice_list=['a'],
            hints=[])
        for i in range(0, 10):
            assert question.internal_id == 'some_id'

    def test_can_serialize(self):
        question = QuestionFactory.build(function=question_fn_tuple_answer,
                                         tags=[], choice_list=[(7, (1, 2, 4), 6)])
        JSONSerializer.serialize(question)
