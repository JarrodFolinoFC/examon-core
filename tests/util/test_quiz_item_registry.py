from examon_item_registry import ExamonItemRegistry
from question import ExpectedResultQuestion

function_src = """
def question(x):
    return x + 3
"""


class TestQuizItemRegistry:
    def test_adds_question(self):
        ExamonItemRegistry.reset()
        question = ExpectedResultQuestion(
            tags=[],
            hints=None,
            function_src='def hello:'
                         '  return 1',
            correct_answer='1')
        ExamonItemRegistry.add(question)
        assert len(ExamonItemRegistry.registry()) == 1
