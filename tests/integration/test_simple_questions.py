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
def question_4(y):
    z = 9
    x = 8
    return y * 7 - 8


class TestIntegrationSimpleQuestions:
    def test_questions_callable(self):
        assert question_1() == 1

    def test_count(self):
        assert len(ExamonItemRegistry.registry()) == 4

    def test_metrics_difficulty(self):
        assert ExamonItemRegistry.registry()[0].metrics.difficulty == 0
        assert ExamonItemRegistry.registry()[1].metrics.difficulty == 0
        assert ExamonItemRegistry.registry()[2].metrics.difficulty == 0
        assert ExamonItemRegistry.registry()[3].metrics.difficulty == 1

    def test_metrics_loc(self):
        assert ExamonItemRegistry.registry()[0].metrics.loc == 4
        assert ExamonItemRegistry.registry()[1].metrics.loc == 4
        assert ExamonItemRegistry.registry()[2].metrics.loc == 4
        assert ExamonItemRegistry.registry()[3].metrics.loc == 6
