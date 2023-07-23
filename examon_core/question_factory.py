from .question import ExpectedResultQuestion, InputParameterQuestion, BaseQuestion
from .multi_choice_factory import MultiChoiceFactory
from .function_raw_code import function_raw_code
from .print_ext import PrintLog
from .code_metrics import CodeMetricsFactory

import random
import logging


class QuestionFactory:
    @staticmethod
    def build(**kwargs):
        function = kwargs['function']
        tags = kwargs['tags']
        hints = kwargs['hints'] if 'hints' in kwargs.keys() else []
        param1 = kwargs['param1'] if 'param1' in kwargs else None
        choice_list = kwargs['choice_list']
        fn_string = function_raw_code(function, hints)
        first_line_no = function.__code__.co_firstlineno

        # Code Metrics
        metrics = CodeMetricsFactory.build(fn_string)

        # Build
        if param1 is not None:
            selected_input_param = random.choice(param1)
            PrintLog.reset()
            return_value = QuestionFactory.run_function_with_param(
                function, selected_input_param
            )
            PrintLog.apply_offset(first_line_no)
            print_logs = PrintLog.logs()
            PrintLog.reset()

            question = InputParameterQuestion(
                selected_param=selected_input_param,
                choices=param1
            )
            question.return_value = return_value
        else:
            # Print Logs
            PrintLog.reset()
            correct_answer = QuestionFactory.run_function(function=function)
            PrintLog.apply_offset(first_line_no)
            print_logs = PrintLog.logs()
            PrintLog.reset()

            if choice_list is not None:
                question = ExpectedResultQuestion(
                    choices=(
                        MultiChoiceFactory.build(
                            correct_answer,
                            choice_list)))
            else:
                question = BaseQuestion()
            question.correct_answer = correct_answer

        question.metrics = metrics
        question.hints = hints
        question.tags = tags
        question.print_logs = print_logs
        question.function_src = fn_string
        logging.debug(f'QuestionFactory.build: {question}')
        return question

    @staticmethod
    def run_function(function):
        try:
            result = function()
            return result
        except Exception as e:
            return repr(e)

    @staticmethod
    def run_function_with_param(function, param):
        try:
            return str(function(param))
        except Exception as e:
            return repr(e)
