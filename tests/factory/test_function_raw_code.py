from function_raw_code import function_raw_code, \
    RawCodeFactory, AppendPrintDecorator, \
    SourceCodeCommentsDecorator, \
    RemoveQuizItemDecorator


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
        assert 'def function1():\n    return 1 - 7' in result

    def test_converts_function_to_string(self):
        result = function_raw_code(function1, [])
        assert 'def function1():\n    return 1 - 7' in result

    def test_all(self):
        decorator1 = SourceCodeCommentsDecorator(['hello', 'how are you'])
        decorator2 = AppendPrintDecorator(function1.__name__)
        decorator3 = RemoveQuizItemDecorator()
        result = RawCodeFactory.build(
            function1, [decorator1, decorator2, decorator3])
        assert '# hello' in result
        assert '# how are you' in result
        assert '@examon' not in result
        assert 'def function1():\n    return 1 - 7' in result
        assert 'print(function1())' in result
