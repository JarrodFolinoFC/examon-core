from examon_core.models.code_metrics import CodeMetricsFactory,\
    CalcDifficultyDefaultStrategy
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


class TestCalcDifficultyDefaultStrategy:
    def test_converts_function_to_string(self):
        code_metrics = CodeMetricsFactory.build(code)

        assert CalcDifficultyDefaultStrategy(code_metrics).calc_difficulty() == 'Hard'
