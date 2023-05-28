from function_raw_code import function_raw_code, \
    RawCodeFactory, AppendPrintDecorator, \
    SourceCodeCommentsDecorator


def function1():
    return 1 - 7


class TestFnToText:
    def test_converts_function_to_string2(self):
        result = RawCodeFactory.build(function1)
        assert 'def function1():\n    return 1 - 7' in result

    def test_converts_function_with_print_decorator(self):
        decorator = AppendPrintDecorator(function1.__name__)
        result = RawCodeFactory.build(function1, [decorator])
        assert 'def function1():\n    return 1 - 7' in result
        assert 'print(function1())' in result

    def test_converts_function_with_src_code_comments_decorator(self):
        decorator = SourceCodeCommentsDecorator(['hello', 'how are you'])
        result = RawCodeFactory.build(function1, [decorator])
        assert '# hello' in result
        assert '# how are you' in result

    def test_converts_function_to_string(self):
        result = function_raw_code(function1, [])
        assert 'def function1():\n    return 1 - 7' in result

    def test_adds_hints(self):
        result = function_raw_code(function1, ['here is a hint'])
        assert '# here is a hint' in result
