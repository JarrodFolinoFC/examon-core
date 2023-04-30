from examon_core.models.fn_to_txt import function_as_txt


def function1():
    return 1 - 7


class TestFnToText:
    def test_converts_function_to_string(self):
        result = function_as_txt(function1, None)
        assert 'def function1():\n    return 1 - 7' in result

    def test_adds_hints(self):
        result = function_as_txt(function1, ['here is a hint'])
        assert '# here is a hint' in result
