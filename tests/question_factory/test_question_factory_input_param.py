from examon_core.models.question_factory import QuestionFactory


class TestQuestionFactoryInputParam:
    def test_build_with_int_param(self):
        def question_fn_with_int_param(a):
            answer = 4 + a
            return answer

        question = QuestionFactory.build(
            function=question_fn_with_int_param, tags=[],
            hints=[], param1=[4])
        assert question.print_logs == ['8']

    def test_build_with_str_param(self):
        def question_fn_with_str_param(a):
            return f'Hello {a}'

        question = QuestionFactory.build(
            function=question_fn_with_str_param, tags=[],
            hints=[], param1=['Bob'])
        assert question.print_logs == ['Hello Bob']

    def test_build_with_str_param_and_quotes(self):
        def question_fn_with_str_param(a):
            return f'Hello {a}'

        question = QuestionFactory.build(
            function=question_fn_with_str_param, tags=[],
            hints=[], param1=['"Bob"'])
        assert question.print_logs == ['Hello "Bob"']

    def test_build_with_str_param_and_escape_characters(self):
        def question_fn_with_str_param(a):
            return f'Hello {a}'

        question = QuestionFactory.build(
            function=question_fn_with_str_param, tags=[],
            hints=[], param1=['\tBob'])
        assert question.print_logs == ['Hello \tBob']

    def test_build_with_dict_param(self):
        def question_fn_with_str_param(a):
            return list(a.keys())

        question = QuestionFactory.build(
            function=question_fn_with_str_param, tags=[],
            hints=[], param1=[{'a': 1, 'b': 2}])
        assert question.print_logs == ["['a', 'b']"]

    def test_build_with_array_of_int_param(self):
        def question_fn_array_of_int_param(a):
            return len(a)

        question = QuestionFactory.build(
            function=question_fn_array_of_int_param, tags=[],
            hints=[], param1=[[1, 2, 3, 4]])
        assert question.print_logs == ['4']

    def test_build_with_array_of_str_param(self):
        def question_fn_array_of_str_param(a):
            return len(a)

        question = QuestionFactory.build(
            function=question_fn_array_of_str_param, tags=[],
            hints=[], param1=[['a', 'b', 'c', 'd']])
        assert question.print_logs == ['4']
