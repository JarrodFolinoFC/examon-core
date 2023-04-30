from examon_core.models.quiz_item_registry import QuizItemRegistry
from examon_core.models.question import FreeTextQuestion

function_src = """
def question(x):
    return x + 3
"""


class TestQuizItemRegistry:
    def test_adds_question(self):
        registry = QuizItemRegistry()
        question = FreeTextQuestion(
            tags=[],
            hints=None,
            function_src='def hello:'
                         '  return 1',
            correct_answer='1')
        registry.add(question)
        assert len(registry.registry()) == 1
