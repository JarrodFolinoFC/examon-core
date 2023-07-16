import inspect
import re
import logging


class RawCodeFactory:
    @staticmethod
    def build(function, decorators=[]):
        src_code = RawCodeFactory.function_src(function)
        for decorator in decorators:
            logging.debug(f'RawCodeFactory.build: {decorator}')
            src_code = decorator.decorate(src_code)
            logging.debug(f'RawCodeFactory.build: {src_code}')

        logging.debug(f'RawCodeFactory.build: {src_code}')
        return src_code

    @staticmethod
    def function_src(function):
        logging.debug(f'RawCodeFactory.function_src: {function}')
        return inspect.getsource(function).strip()


class SourceCodeCommentsDecorator:
    def __init__(self, hints):
        self.hints = hints

    def decorate(self, src_code):
        all_hints = ''
        if self.hints is None:
            return all_hints
        else:
            for hint in self.hints:
                all_hints += f'# {hint}\n'
        all_hints = f'# Hints:\n{all_hints}\n\n'
        return all_hints + src_code


class RemoveQuizItemDecorator:
    def decorate(self, src_code):
        return re.sub('@examon\\_item\\(.*\\)', '', src_code)


class AppendPrintDecorator:
    def __init__(self, function_name):
        self.function_name = function_name

    def decorate(self, src_code):
        println = f'\n\nprint({self.function_name}())'
        return src_code + println


def function_raw_code(function, hints):
    append_print_decorator = AppendPrintDecorator(function.__name__)
    remove_quiz_item_decorator = RemoveQuizItemDecorator()
    decorators = [remove_quiz_item_decorator, append_print_decorator]
    return RawCodeFactory.build(function, decorators)
