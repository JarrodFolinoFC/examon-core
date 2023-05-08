from radon.raw import analyze
from radon.metrics import h_visit

from .code_metrics import CodeMetrics

# {
#     'rank': [Function(name='function1', lineno=2, col_offset=0, endline=18, is_method=False, classname=None, closures=[Function(name='function2', lineno=5, col_offset=4, endline=6, is_method=False, classname=None, closures=[], complexity=1), Function(name='function3', lineno=8, col_offset=4, endline=16, is_method=False, classname=None, closures=[], complexity=5)], complexity=1)],
#  'v': <radon.visitors.ComplexityVisitor object at 0x105d8ba00>,
# 'analyze': Module(loc=20, lloc=14, sloc=14, comments=0, multi=0, blank=6, single_comments=0),
# 'halstead': Halstead(total=HalsteadReport(h1=2, h2=6, N1=5, N2=10, vocabulary=8,
#                                           length=15, calculated_length=17.509775004326936, volume=45.0,
#                                           difficulty=1.6666666666666667, effort=75.0,
#                                           time=4.166666666666667, bugs=0.015),
#                      functions=[
#                          ('function1', HalsteadReport(h1=2, h2=6, N1=5, N2=10, vocabulary=8, length=15, calculated_length=17.509775004326936, volume=45.0, difficulty=1.6666666666666667, effort=75.0, time=4.166666666666667, bugs=0.015))])}


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
