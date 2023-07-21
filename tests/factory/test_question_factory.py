from examon_core.question_factory import QuestionFactory, InvalidChoiceException
from examon_core.print_ext import print, PrintLogItem

import pytest


def question_fn():
    print('test')
    answer = 4 + 3
    print(answer)
    return answer


class TestQuestionFactory:
    def test_build(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'],
            hints=[], choice_list=[7, 6])
        assert question.tags == ['a']
        assert len(question.choices) == 2
        assert len(question.print_logs) == 2

    def test_build_with_tuple_choices(self):
        with pytest.raises(InvalidChoiceException) as exc_info:
            QuestionFactory.build(function=question_fn, tags=[], choice_list=[(7, 6)])
        assert exc_info.value.args[0] == 'Cannot use a <tuple> as a choice'
        assert str(exc_info.value) == 'Cannot use a <tuple> as a choice'

    def test_print_logs(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'],
            hints=[], choice_list=[7, 6])
        assert question.print_logs[0] == PrintLogItem('test', 1)

    def test_choices(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'],
            hints=[], choice_list=[7, 6])
        assert question.choices == [7, 6]
