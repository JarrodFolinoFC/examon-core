import os
import sys
sys.path.append(f'{os.path.abspath("")}/examon_core')

from quiz_item_registry import QuizItemRegistry
from question import ExpectedResultQuestion

function_src = """
def question(x):
    return x + 3
"""


class TestQuizItemRegistry:
    def test_adds_question(self):
        registry = QuizItemRegistry()
        question = ExpectedResultQuestion(
            tags=[],
            hints=None,
            function_src='def hello:'
                         '  return 1',
            correct_answer='1')
        registry.add(question)
        assert len(registry.registry()) == 1
