from .question import ExpectedResultQuestion, InputParameterQuestion, FreeTextQuestion
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
        first_line_no = function.__code__.co_firstlineno
        PrintLog.reset()
        correct_answer = QuestionFactory.run_function(function=function)
        PrintLog.apply_offset(first_line_no)
        print_logs = PrintLog.logs()
        PrintLog.reset()

        fn_string = function_as_txt(function, hints)
        if kwargs['choice_list'] is not None:
            choices = MultiChoiceFactory.build(correct_answer,
                                               kwargs['choice_list'])
            question = ExpectedResultQuestion(choices=choices)
        elif kwargs['param1'] is not None:
            selected_input = random.choice(kwargs['param1'])
            return_value = QuestionFactory.run_function_with_param(
                function, selected_input
            )

            question = QuestionFactory.build_select_input(
                kwargs['param1'], return_value,
                selected_input
            )
        else:
            question = FreeTextQuestion()


        code_metrics = CodeMetricsFactory.build(fn_string)
        question.metrics = code_metrics
        question.correct_answer = correct_answer
        question.hints = hints
        question.tags = tags
        question.print_logs = print_logs
        question.function_src = fn_string
        return question


    @staticmethod
    def build_select_input(choices, selected_param):
        return InputParameterQuestion(
            selected_param=selected_param,
            choices=choices
        )

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
