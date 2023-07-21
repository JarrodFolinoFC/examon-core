from examon_item_registry import ExamonItemRegistry, ItemRegistryFilter
from question import ExpectedResultQuestion

function_src = """
def question():
    return x + 3
"""


def add_question(tags):
    question = ExpectedResultQuestion(
        tags=tags,
        function_src=function_src,
        correct_answer='1')
    ExamonItemRegistry.add(question)


class TestQuizItemRegistry:
    def test_adds_question(self):
        ExamonItemRegistry.reset()
        add_question([])
        assert len(ExamonItemRegistry.registry()) == 1

    def test_query_by_tag(self):
        ExamonItemRegistry.reset()
        add_question(['a'])
        add_question(['a'])
        add_question(['a'])
        add_question(['c'])
        assert len(ExamonItemRegistry.registry(ItemRegistryFilter(tags_all=['a']))) == 3

    def test_query_by_tags_any(self):
        ExamonItemRegistry.reset()
        add_question(['a'])
        add_question(['a'])
        add_question(['a'])
        add_question(['c'])
        assert len(ExamonItemRegistry.registry(ItemRegistryFilter(tags_any=['a', 'c']))) == 4

    def test_query_by_tags_all(self):
        ExamonItemRegistry.reset()
        add_question(['a', 'b', 'c'])
        add_question(['a', 'b'])
        add_question(['a'])
        add_question(['a', 'c'])
        assert len(ExamonItemRegistry.registry(ItemRegistryFilter(tags_all=['a', 'b']))) == 2

    def test_query_max_questions(self):
        ExamonItemRegistry.reset()
        add_question(['a', 'b', 'c'])
        add_question(['a', 'b'])
        add_question(['a'])
        add_question(['a', 'c'])
        assert len(ExamonItemRegistry.registry(ItemRegistryFilter(max_questions=2))) == 2

    def test_unique_tags(self):
        ExamonItemRegistry.reset()
        add_question(['a', 'b', 'c'])
        add_question(['a', 'b'])
        add_question(['a'])
        add_question(['a', 'c'])
        assert ExamonItemRegistry.unique_tags() == ['a', 'c', 'b']
