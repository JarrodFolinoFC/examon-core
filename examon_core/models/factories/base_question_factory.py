from ..question import BaseQuestion
from .code_as_string_factory import default_code_as_string_factory
from ...code_execution.sandbox import Sandbox


class BaseQuestionFactory:
    @staticmethod
    def build(function):
        function_src = default_code_as_string_factory(function)
        print_logs = BaseQuestionFactory.run_function(function_src)
        question = BaseQuestion(function_src=function_src,
                                print_logs=print_logs,
                                correct_answer=print_logs[-1])
        return question

    @staticmethod
    def run_function(source_code):
        ces = Sandbox(source_code)
        ces.execute()

        return ces.print_logs


    @staticmethod
    def run_function(source_code):
        ces = Sandbox(source_code)
        ces.execute()

        return ces.print_logs
