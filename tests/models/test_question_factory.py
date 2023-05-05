import os
import sys
sys.path.append(f'{os.path.abspath("")}/src/models')
sys.path.append(f'{os.path.abspath("")}/src/ext')

from question_factory import QuestionFactory
from question import ExpectedResultQuestion
from print_ext import print, PrintLog

def question_fn():
    print('test')
    answer = 4 + 3
    print(answer)
    return answer


class TestQuestionFactory:
    def test_build(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'], hints=[], choice_list=[7, 6],
            generated_choices=None, param1=None)
        assert isinstance(question, ExpectedResultQuestion)
        assert question.tags == ['a']
        assert len(question.choices) == 2
        assert len(question.print_logs) == 2

    def test_print_logs(self):
        question = QuestionFactory.build(
            function=question_fn, tags=['a'], hints=[], choice_list=[7, 6],
            generated_choices=None, param1=None)
        assert question.print_logs[0] == ('test', 1)