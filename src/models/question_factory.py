import os
import sys
sys.path.append(os.path.abspath(""))
sys.path.append(f'{os.path.abspath("")}/../ext')
from question import ExpectedResultQuestion, InputParameterQuestion, FreeTextQuestion
from multi_choice_factory import MultiChoiceFactory
from fn_to_txt import function_as_txt

from print_ext import PrintLog

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

        if kwargs['choice_list'] is not None:
            choices = MultiChoiceFactory.build(correct_answer,
                                               kwargs['generated_choices'],
                                               kwargs['choice_list'])
            return QuestionFactory.build_multichoice(choices, correct_answer,
                                                     function, hints, tags, print_logs)
        elif kwargs['param1'] is not None:
            param1 = kwargs['param1']
            choices = {}
            for idx, param in enumerate(param1):
                choices[chr(idx + 97)] = param

            selected_input = random.choice(param1)
            return_value = QuestionFactory.run_function_with_param(
                function, selected_input
            )

            return QuestionFactory.build_select_input(
                choices, return_value,
                function, hints, tags, selected_input, print_logs
            )
        else:
            return QuestionFactory.build_free_text(
                correct_answer, function, hints, tags, print_logs
            )

    @staticmethod
    def build_free_text(correct_answer, function, hints, tags, print_logs):
        question = FreeTextQuestion(
            tags=tags,
            hints=hints,
            function_src=function_as_txt(
                function=function,
                hints=hints),
            correct_answer=correct_answer,
            print_logs=print_logs)
        return question

    @staticmethod
    def build_multichoice(choices, correct_answer, function, hints, tags, print_logs):
        question = ExpectedResultQuestion(
            tags=tags,
            hints=hints,
            function_src=function_as_txt(
                function=function,
                hints=hints),
            correct_answer=correct_answer,
            choices=choices,
            print_logs=print_logs)
        return question

    @staticmethod
    def build_select_input(choices, correct_answer, function,
                           hints, tags, selected_param, print_logs):
        question = InputParameterQuestion(
            tags=tags,
            hints=hints,
            function_src=function_as_txt(
                function=function,
                hints=hints),
            selected_param=selected_param,
            return_value=correct_answer,
            choices=choices,
            print_logs=print_logs
        )
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
