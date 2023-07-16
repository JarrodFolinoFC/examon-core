import logging
from dataclasses import dataclass


from radon.raw import analyze
from radon.metrics import h_visit


@dataclass
class CodeMetrics:
    code_as_string: str
    no_of_functions: int = None
    loc: int = None
    lloc: int = None
    sloc: int = None
    difficulty: float = None

    def __repr__(self):
        return f'CodeMetrics(difficulty: {self.difficulty},' \
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
