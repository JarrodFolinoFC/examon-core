from .code_metrics import CodeMetricsFactory
from .factories.input_param_question_factory import InputParamQuestionFactory
from .factories.multichoice_question_factory import MultichoiceQuestionFactory
from .factories.base_question_factory import BaseQuestionFactory
from ..code_execution.sandbox import Sandbox
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
        result_choice_list = QuestionFactory.choice_list_as_string(kwargs)

        # Build
        if param1 is not None:
            question = InputParamQuestionFactory.build(function, param1)
        elif result_choice_list:
            question = MultichoiceQuestionFactory.build(function, result_choice_list)
        else:
            question = BaseQuestionFactory.build(function)

        question.metrics = CodeMetricsFactory.build(question.function_src)
        question.hints = hints
        question.internal_id = internal_id
        question.tags = tags
        question.unique_id = QuestionFactory.get_unique_id(question.function_src)
        logging.debug(f'QuestionFactory.build: {question}')
        return question

    @staticmethod
    def choice_list_as_string(kwargs):
        result_choice_list = []
        if 'choice_list' in kwargs and kwargs['choice_list'] is not None:
            result_choice_list = list(map(lambda x: str(x), kwargs['choice_list']))
        return result_choice_list

    @staticmethod
    def get_unique_id(function_src):
        m = hashlib.md5()
        m.update(function_src.encode())
        result = str(int(m.hexdigest(), 16))[0:32]
        return result

    @staticmethod
    def run_function(source_code):
        ces = Sandbox(source_code)
        ces.execute()

        return ces.print_logs
