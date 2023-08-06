from examon_core.models.code_as_string_factory import default_code_as_string_factory, \
    CodeAsStringFactory, AppendPrintDecorator, \
    SourceCodeCommentsDecorator, \
    RemoveQuizItemDecorator


def examon_item(choices=None, tags=None, hints=None,
                generated_choices=None, param1=None):
    def inner_function(function):
        return function
    return inner_function


def function1():
    return 1 - 7


@examon_item(choices=['Hello, Bob. How are you?'], tags=['strings', 'beginner'])
def question_with_decorator():
    name = 'Jeff'
    name = 'Bob'
    greeting = f'Hello, {name}'
    greeting += ". How are you?"
    return greeting

@examon_item(
    choices=['Hello, Bob. How are you?'],
    tags=['strings', 'beginner']
)
def question_with_decorator_mutliline():
    name = 'Jeff'
    name = 'Bob'
    greeting = f'Hello, {name}'
    greeting += ". How are you?"
    return greeting

class TestCodeAsStringFactory:
    def test_default_code_with_decorator_one_line(self):
        result = default_code_as_string_factory(question_with_decorator)
        print(result)
        assert '@examon_item' not in result

    def test_default_code_with_decorator_multi_line(self):
        result = default_code_as_string_factory(question_with_decorator_mutliline)
        print(result)
        assert '@examon_item' not in result

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
