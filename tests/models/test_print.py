import os
import sys
sys.path.append(f'{os.path.abspath("")}/src/ext')
from print_ext import PrintLog, print


import pytest

def question():
    print('test')
    a = 6
    print(a)
    a = a + 9
    print(a)
    result = a + 3
    print(result)
    return result

@pytest.fixture(scope="function", autouse=True)
def clear_print_logs():
    PrintLog.reset()

class TestPrint:
    def test_print_override_appends_logs(self):
        question()
        assert PrintLog.logs()[0] == ('test', 10)

    def test_print_override_appends_logs_from_exec(self):
        exec("print('test')")
        assert len(PrintLog.logs()) == 1