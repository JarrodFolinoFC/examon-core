from .multi_choice_factory import MultiChoiceFactory
from ..question import MultiChoiceQuestion
from .code_as_string_factory import default_code_as_string_factory
from ...code_execution.sandbox import Sandbox


class MultichoiceQuestionFactory:
    @staticmethod
    def build(function, choice_list):
        function_src = default_code_as_string_factory(function)
        print_logs = Sandbox.run_function(function_src)
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
