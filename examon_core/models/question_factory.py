from .question import MultiChoiceQuestion, InputParameterQuestion, BaseQuestion
from .multi_choice_factory import MultiChoiceFactory
from .code_as_string_factory import default_code_as_string_factory
from .code_metrics import CodeMetricsFactory
from ..code_execution.sandbox import Sandbox
import random
import logging
import hashlib


class InvalidAnswerException(Exception):
    pass


class QuestionFactory:
    @staticmethod
    def build(**kwargs):
        function = kwargs['function']
        tags = kwargs['tags']
        internal_id = kwargs['internal_id'] if 'internal_id' in kwargs.keys() else None
        hints = kwargs['hints'] if 'hints' in kwargs.keys() else []
        param1 = kwargs['param1'] if 'param1' in kwargs else None
        result_choice_list = []
        if 'choice_list' in kwargs and kwargs['choice_list'] is not None:
            result_choice_list = list(map(lambda x: str(x), kwargs['choice_list']))

        # Build
        if param1 is not None:
            question = QuestionFactory.build_input_param_question(function, param1)
        elif result_choice_list:
            question = QuestionFactory.build_multichoice_question(function, result_choice_list)
        else:
            function_src = default_code_as_string_factory(function)
            print_logs = QuestionFactory.run_function(function_src)
            question = BaseQuestion(function_src=function_src,
                                    print_logs=print_logs,
                                    correct_answer=print_logs[-1])

        question.metrics = CodeMetricsFactory.build(question.function_src)
        question.hints = hints
        question.internal_id = internal_id
        question.tags = tags
        m = hashlib.md5()
        m.update(question.function_src.encode())
        question.unique_id = str(int(m.hexdigest(), 16))[0:32]
        logging.debug(f'QuestionFactory.build: {question}')
        return question

    @staticmethod
    def build_multichoice_question(function, choice_list):
        function_src = default_code_as_string_factory(function)
        print_logs = QuestionFactory.run_function(function_src)
        question = MultiChoiceQuestion(
            correct_answer=print_logs[-1],
            function_src=function_src,
            print_logs=print_logs,
            choices=(
                MultiChoiceFactory.build(
                    print_logs[-1],
                    choice_list
                )
            )
        )

        return question

    @staticmethod
    def build_input_param_question(function, param_one):
        selected_input_param = random.choice(param_one)
        function_src = default_code_as_string_factory(function, selected_input_param)
        print_logs = QuestionFactory.run_function(function_src)
        return_value = print_logs[-1]
        question = InputParameterQuestion(
            selected_param=selected_input_param,
            param_one_choices=param_one,
            function_src=function_src,
            print_logs=print_logs
        )
        question.return_value = return_value
        return question

    @staticmethod
    def run_function(source_code):
        ces = Sandbox(source_code)
        ces.execute()

        return ces.print_logs
