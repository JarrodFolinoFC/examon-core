from examon_core.code_as_string_factory import default_code_as_string_factory, \
    CodeAsStringFactory, AppendPrintDecorator, \
    SourceCodeCommentsDecorator, \
    RemoveQuizItemDecorator


def function1():
    return 1 - 7


class TestCodeAsStringFactory:
    def test_default_code_as_string_factory(self):
        result = default_code_as_string_factory(function1)
        assert 'def function1():\n    return 1 - 7' in result

    def test_converts_function_to_string2(self):
        result = CodeAsStringFactory.build(function1)
        assert 'def function1():\n    return 1 - 7' in result

    def test_converts_function_with_print_decorator(self):
        decorator = AppendPrintDecorator(function1.__name__)
        result = CodeAsStringFactory.build(function1, [decorator])
        assert 'def function1():\n    return 1 - 7' in result
        assert 'print(function1())' in result

    def test_converts_function_with_src_code_comments_decorator(self):
        decorator = SourceCodeCommentsDecorator(['hello', 'how are you'])
        result = CodeAsStringFactory.build(function1, [decorator])
        assert '# hello' in result
        assert '# how are you' in result
        assert 'def function1():\n    return 1 - 7' in result

    def test_all(self):
        decorator2 = AppendPrintDecorator(function1.__name__)
        decorator3 = RemoveQuizItemDecorator()
        result = CodeAsStringFactory.build(
            function1, [decorator2, decorator3])
        assert '@examon' not in result
        assert 'def function1():\n    return 1 - 7' in result
        assert 'print(function1())' in result
