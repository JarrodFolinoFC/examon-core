from .question import ExpectedResultQuestion, InputParameterQuestion, BaseQuestion
from .multi_choice_factory import MultiChoiceFactory
from .fn_to_txt import function_as_txt
from .print_ext import PrintLog
from .code_metrics_factory import CodeMetricsFactory

import random


class QuestionFactory:
    @staticmethod
    def build(**kwargs):
        function = kwargs['function']
        tags = kwargs['tags']
        hints = kwargs['hints']
        param1 = kwargs['param1']
        choice_list = kwargs['choice_list']
        fn_string = function_as_txt(function, hints)

        # Print Logs
        first_line_no = function.__code__.co_firstlineno
        PrintLog.reset()
        correct_answer = QuestionFactory.run_function(function=function)
        PrintLog.apply_offset(first_line_no)
        print_logs = PrintLog.logs()
        PrintLog.reset()

        # Code Metrics
        metrics = CodeMetricsFactory.build(fn_string)

        # Build
        if param1 is not None:
            selected_input_param = random.choice(param1)
            return_value = QuestionFactory.run_function_with_param(
                function, selected_input_param
            )

            question = InputParameterQuestion(
                selected_param=selected_input_param,
                choices=param1
            )
            question.return_value = return_value
        else:
            if choice_list is not None:
                question = ExpectedResultQuestion(
                    choices=(MultiChoiceFactory.build(correct_answer, choice_list))
                )
            else:
                question = BaseQuestion()

        question.metrics = metrics
        question.correct_answer = correct_answer
        question.hints = hints
        question.tags = tags
        question.print_logs = print_logs
        question.function_src = fn_string
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
            return function(param)
        except Exception as e:
            return repr(e)
