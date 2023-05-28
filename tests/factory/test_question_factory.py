from examon_core.question_factory import QuestionFactory
from examon_core.print_ext import print

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

    def test_print_logs(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'],
            hints=[], choice_list=[7, 6])
        assert question.print_logs[0] == ('test', 1)

    def test_choices(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'],
            hints=[], choice_list=[7, 6])
        assert question.choices == [7, 6]