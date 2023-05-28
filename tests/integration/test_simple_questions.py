from examon_core.examon_item import examon_item
from examon_core.examon_item_registry import ExamonItemRegistry


@examon_item(choices=[1, 2, 3], tags=['anything'])
def question_1():
    return 1

@examon_item(tags=['anything'])
def question_2():
    return 2


class TestIntegrationSimpleQuestions:
    def test__init__1(self):
        assert len(ExamonItemRegistry.registry()) == 2
