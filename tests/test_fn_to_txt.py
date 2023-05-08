import os
import sys
sys.path.append(f'{os.path.abspath("")}/examon_core')

from fn_to_txt import function_raw_code


def function1():
    return 1 - 7


class TestFnToText:
    def test_converts_function_to_string(self):
        result = function_raw_code(function1, None)
        assert 'def function1():\n    return 1 - 7' in result

    def test_adds_hints(self):
        result = function_raw_code(function1, ['here is a hint'])
        assert '# here is a hint' in result
