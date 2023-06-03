from examon_core.examon_item import examon_item
from examon_core.examon_item_registry import ExamonItemRegistry


@examon_item(choices=[1, 2, 3], tags=['anything'])
def question_1():
    return 1

@examon_item(tags=['anything'])
def question_2():
    return 2

@examon_item(param1=[1, 2, 3], tags=['anything'])
def question_3(x):
    return x

@examon_item(param1=[3, 7, 3], tags=['anything'])
def question_3(y):
    z = 9
    for x in range(8):
        z = z + 8
    return y * 7

class TestIntegrationSimpleQuestions:
    def test_count(self):
        assert len(ExamonItemRegistry.registry()) == 4

    def test_metrics(self):
        assert ExamonItemRegistry.registry()[0].metrics.difficulty == 0
        assert ExamonItemRegistry.registry()[0].metrics.no_of_functions == 0
        assert ExamonItemRegistry.registry()[0].metrics.loc == 3
        assert ExamonItemRegistry.registry()[0].metrics.lloc == 1
        assert ExamonItemRegistry.registry()[3].metrics.sloc == 1
