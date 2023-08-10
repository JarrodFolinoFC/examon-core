import random
from ..question import InputParameterQuestion
from .code_as_string_factory import default_code_as_string_factory
from ...code_execution.sandbox import Sandbox


class InputParamQuestionFactory:
    @staticmethod
    def build(function, param_one):
        selected_input_param = random.choice(param_one)
        function_src = default_code_as_string_factory(function, selected_input_param)
        print_logs = InputParamQuestionFactory.run_function(function_src)
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

    @staticmethod
    def build_multichoice_question(function, choice_list):
        function_src = default_code_as_string_factory(function)
        print_logs = InputParamQuestionFactory.run_function(function_src)
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
    def run_function(source_code):
        ces = Sandbox(source_code)
        ces.execute()

        return ces.print_logs
