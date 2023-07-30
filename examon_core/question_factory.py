from .question import MultiChoiceQuestion, InputParameterQuestion, BaseQuestion
from .multi_choice_factory import MultiChoiceFactory
from .code_as_string_factory import default_code_as_string_factory
from .code_metrics import CodeMetricsFactory
from .code_execution_sandbox import CodeExecutionSandbox
import random
import logging


class InvalidAnswerException(Exception):
    pass


class QuestionFactory:
    @staticmethod
    def build(**kwargs):
        function = kwargs['function']
        tags = kwargs['tags']
        hints = kwargs['hints'] if 'hints' in kwargs.keys() else []
        param1 = kwargs['param1'] if 'param1' in kwargs else None
        choice_list = []
        if 'choice_list' in kwargs and kwargs['choice_list'] is not None:
            choice_list = list(map(lambda x: str(x), kwargs['choice_list']))

        # Build
        if param1 is not None:
            fn_string, metrics, question = QuestionFactory.build_input_param_question(function, param1)
        else:
            fn_string, metrics, question = QuestionFactory.method_name1(choice_list, function)

        question.metrics = metrics
        question.hints = hints
        question.tags = tags
        question.function_src = fn_string
        logging.debug(f'QuestionFactory.build: {question}')
        return question

    @staticmethod
    def method_name1(choice_list, function):
        function_src = default_code_as_string_factory(function)
        metrics = CodeMetricsFactory.build(function_src)
        print_logs = QuestionFactory.run_function(function_src)
        if choice_list is not None:
            question = MultiChoiceQuestion(
                correct_answer=print_logs[-1],
                print_logs=print_logs,
                choices=(
                    MultiChoiceFactory.build(
                        print_logs[-1],
                        choice_list
                    )
                )
            )
        else:
            question = BaseQuestion(function_src=function_src,
                                    print_logs=print_logs,
                                    correct_answer=print_logs[-1])
        return function_src, metrics, question

    @staticmethod
    def build_input_param_question(function, param1):
        selected_input_param = random.choice(param1)
        function_src = default_code_as_string_factory(function, selected_input_param)
        print_logs = QuestionFactory.run_function(function_src)
        metrics = CodeMetricsFactory.build(function_src)
        return_value = print_logs[-1]
        question = InputParameterQuestion(
            selected_param=selected_input_param,
            choices=param1,
            function_src=function_src,
            print_logs=print_logs
        )
        question.return_value = return_value
        return function_src, metrics, question

    @staticmethod
    def run_function(source_code):
        ces = CodeExecutionSandbox(source_code)
        ces.execute()

        return ces.print_logs
