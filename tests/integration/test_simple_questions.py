import pytest
from examon_core.examon_item import examon_item
from examon_core.models.question import \
    MultiChoiceQuestion, BaseQuestion, InputParameterQuestion
from examon_core.examon_item_registry import ExamonItemRegistry


def load_fixtures():
    @examon_item(choices=[1, 2, 3], tags=['anything'])
    def question_1():
        return 1

    @examon_item(tags=['anything'])
    def question_2():
        return 2

    @examon_item(param1=[1], tags=['anything'])
    def question_3(x):
        return x

    @examon_item(param1=[3], tags=['anything'])
    def question_4(y):
        z = 9
        x = 8
        return y * 7 - 8


@pytest.fixture(autouse=True)
def run_around_tests():
    ExamonItemRegistry.reset()
    load_fixtures()
    yield
    ExamonItemRegistry.reset()


class TestIntegrationSimpleQuestions:

    def test_count(self):
        assert len(ExamonItemRegistry.registry()) == 4

    def test_question_class(self):
        assert ExamonItemRegistry.registry()[0].__class__ == MultiChoiceQuestion
        assert ExamonItemRegistry.registry()[1].__class__ == BaseQuestion
        assert ExamonItemRegistry.registry()[2].__class__ == InputParameterQuestion
        assert ExamonItemRegistry.registry()[3].__class__ == InputParameterQuestion

    def test_question_tags(self):
        assert ExamonItemRegistry.registry()[0].tags == ['anything']
        assert ExamonItemRegistry.registry()[1].tags == ['anything']
        assert ExamonItemRegistry.registry()[2].tags == ['anything']
        assert ExamonItemRegistry.registry()[3].tags == ['anything']

    def test_question_unique_id(self):
        assert ExamonItemRegistry.registry()[0].unique_id == '24610570444134442526585499076789'
        assert ExamonItemRegistry.registry()[1].unique_id == '23636307171713722401703907507077'

        # only consistent because we have 1 param
        assert ExamonItemRegistry.registry()[2].unique_id == '56546634424136765434294751275575'
        # assert ExamonItemRegistry.registry()[3].unique_id == '56546634424136765434294751275575'

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
