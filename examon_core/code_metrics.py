import logging
from dataclasses import dataclass

from radon.raw import analyze
from radon.metrics import h_visit


class CalcDifficultyDefaultStrategy:

    def __init__(self, metrics):
        self.metrics = metrics

    def calc_difficulty(self):
        value = self.metrics.difficulty
        if value == 0:
            return "Easy"
        elif 0 < value <= 1:
            return "Medium"
        elif 1 < value < 3:
            return "Hard"
        elif value >= 3:
            return 'Very Hard'


@dataclass
class CodeMetrics:
    code_as_string: str
    no_of_functions: int = None
    loc: int = None
    lloc: int = None
    sloc: int = None
    difficulty: float = None
    categorised_difficulty: str = None

    def __repr__(self):
        return f'CodeMetrics(difficulty: {self.difficulty},' \
               f'no_of_functions: {self.no_of_functions}, ' \
               f'loc: {self.loc}, ' \
               f'lloc: {self.lloc}, ' \
               f'lloc: {self.sloc})'


class CodeMetricsFactory:
    @staticmethod
    def build(code_as_string):
        if code_as_string == '' or code_as_string is None:
            raise Exception('Cannot use empty string')
        cm = CodeMetrics(code_as_string)
        raw = analyze(cm.code_as_string)
        visit_data = h_visit(cm.code_as_string)

        cm.difficulty = round(visit_data.total.difficulty, 2)
        cm.no_of_functions = len(visit_data.functions)
        cm.loc = raw.loc
        cm.lloc = raw.lloc
        cm.sloc = raw.sloc
        cm.categorised_difficulty = CalcDifficultyDefaultStrategy(cm).calc_difficulty()
        logging.debug(f'CodeMetricsFactory.build: {cm}')

        return cm
