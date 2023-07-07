import logging

from radon.raw import analyze
from radon.metrics import h_visit


class CodeMetrics:
    def __init__(self, code_as_string):
        self.code_as_string = code_as_string
        self.difficulty = None
        self.no_of_functions = None
        self.loc = None
        self.lloc = None
        self.sloc = None

    def __repr__(self):
        return f'CodeMetrics(difficulty: {self.difficulty},' \
               f'difficulty: {self.difficulty}, ' \
               f'no_of_functions: {self.no_of_functions}, ' \
               f'loc: {self.loc}, ' \
               f'lloc: {self.lloc}, ' \
               f'lloc: {self.sloc})'


class CodeMetricsFactory:
    @staticmethod
    def build(code_as_string):
        cm = CodeMetrics(code_as_string)
        raw = analyze(cm.code_as_string)
        visit_data = h_visit(cm.code_as_string)

        cm.difficulty = round(visit_data.total.difficulty, 2)
        cm.no_of_functions = len(visit_data.functions)
        cm.loc = raw.loc
        cm.lloc = raw.lloc
        cm.sloc = raw.sloc
        logging.debug(f'CodeMetricsFactory.build: {cm}')

        return cm
