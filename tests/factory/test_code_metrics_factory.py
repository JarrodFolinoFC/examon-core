from examon_core.code_metrics import CodeMetricsFactory
import os
import sys
sys.path.append(f'{os.path.abspath("")}/examon_core')


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


class TestFnToText:
    def test_converts_function_to_string(self):
        code_metrics = CodeMetricsFactory.build(code)

        assert code_metrics.difficulty == 1.67
        assert code_metrics.no_of_functions == 1
        assert code_metrics.loc == 20
        assert code_metrics.lloc == 14
        assert code_metrics.sloc == 14
