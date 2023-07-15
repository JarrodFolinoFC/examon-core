from print_ext import PrintLog, print, PrintLogItem


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
    def test_print_overrides_and_appends_print_log_logs(self):
        question()
        assert PrintLog.logs()[0] == PrintLogItem('test', 7)
        assert PrintLog.logs()[1] == PrintLogItem('6', 9)
        assert PrintLog.logs()[2] == PrintLogItem('15', 11)

    def test_print_override_appends_logs_from_exec(self):
        exec("print('test')")
        assert len(PrintLog.logs()) == 1

    def test_print_logs_apply_offset(self):
        question()
        PrintLog.apply_offset(2)
        assert PrintLog.logs()[0] == PrintLogItem('test', 5)
        assert PrintLog.logs()[1] == PrintLogItem('6', 7)
        assert PrintLog.logs()[2] == PrintLogItem('15', 9)
