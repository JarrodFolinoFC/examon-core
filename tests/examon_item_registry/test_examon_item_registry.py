from examon_item_registry import ExamonItemRegistry, ItemRegistryFilter
from question import MultiChoiceQuestion
from code_metrics import CodeMetrics

function_src = """
def question():
    return x + 3
"""


def add_question(tags, override_difficulty=None):
    metrics = CodeMetrics(function_src)
    if override_difficulty is not None:
        metrics.categorised_difficulty = override_difficulty
    question = MultiChoiceQuestion(
        tags=tags,
        function_src=function_src,
        correct_answer='1',
        metrics=metrics)
    ExamonItemRegistry.add(question)


class TestExamonItemRegistry:
    def test_adds_question(self):
        ExamonItemRegistry.reset()
        add_question([])
        assert len(ExamonItemRegistry.registry()) == 1

    def test_reset(self):
        ExamonItemRegistry.reset()
        add_question([])
        ExamonItemRegistry.reset()
        assert len(ExamonItemRegistry.registry()) == 0

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

    def test_query_by_tags_all_and_tags_any(self):
        ExamonItemRegistry.reset()
        add_question(['a', 'b', 'c'])
        add_question(['a', 'b'])
        add_question(['a'])
        add_question(['a', 'c'])
        registry_filter = ItemRegistryFilter(tags_any=['a', 'c'], tags_all=['a', 'b'])
        assert len(ExamonItemRegistry.registry(registry_filter)) == 2

    def test_query_difficult(self):
        ExamonItemRegistry.reset()
        add_question(['a', 'b', 'c'], 'Hard')
        add_question(['a', 'b'])
        add_question(['a'])
        add_question(['a', 'c'], 'Hard')
        assert len(ExamonItemRegistry.registry(ItemRegistryFilter(difficulty_category='Hard'))) == 2

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
