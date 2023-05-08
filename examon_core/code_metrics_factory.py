from radon.raw import analyze
from radon.metrics import h_visit

class CodeMetrics:
    def __init__(self, code_as_string):
        self.code_as_string = code_as_string
        self.metrics = {
            'difficulty': None,
            'no_of_functions': None,
            'loc': None,
            'lloc': None,
            'sloc': None
        }


class CodeMetricsFactory:
    @staticmethod
    def build(code_as_string):
        cm = CodeMetrics(code_as_string)
        raw = analyze(cm.code_as_string)
        visit_data = h_visit(cm.code_as_string)

        cm.metrics['difficulty'] = round(visit_data.total.difficulty, 2)
        cm.metrics['no_of_functions'] = len(visit_data.functions)
        cm.metrics['loc'] = raw.loc
        cm.metrics['lloc'] = raw.lloc
        cm.metrics['sloc'] = raw.sloc
        return cm
