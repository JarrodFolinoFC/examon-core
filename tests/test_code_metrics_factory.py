import os
import sys
sys.path.append(f'{os.path.abspath("")}/examon_core')

from examon_core.code_metrics_factory import CodeMetricsFactory

code = '''
def function1():


    def function2():
        return 44

    def function3(n):
        for i in range(10):
            if n > 55:
                n = n - 1
        if n > 55:
            if n > 66:
                return 34
        else:
            return 55

    return function3(104) - function2()

print(function1())    
'''

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

class TestFnToText:
    def test_converts_function_to_string(self):
        code_metrics3 = CodeMetricsFactory.build(code)

        print(code_metrics3.metrics)
