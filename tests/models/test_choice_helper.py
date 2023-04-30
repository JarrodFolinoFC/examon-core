from examon_core.models.choice_helper import prepare_choices

class TestChoiceHelper:
    def test_returns_dict(self):
        choices = prepare_choices([1,2,3], 3, shuffle=False)
        assert choices == {
            'a': 1,
            'b': 2,
            'c': 3
        }

    def test_adds_correct_answer_if_not_present(self):
        choices = prepare_choices([1,2,3,4,5], 6)
        assert len(choices) == 6

    def test_does_not_add_correct_answer_if_present(self):
        choices = prepare_choices([1, 2, 3, 4, 5, 6], 6)
        assert len(choices) == 6