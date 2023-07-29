import pytest
from examon_core.code_execution_sandbox import CodeExecutionSandbox


class TestCodeExecutionSandbox:
    def test_print_logs(self):
        source_code = """
def f1():
    print('hello')
    print('hello2')
    return 3
print(f1())
"""

        ces = CodeExecutionSandbox(source_code)
        ces.execute()

        assert ces.print_logs == ['hello', 'hello2', '3']

    @pytest.mark.skip(reason="pending")
    def test_complex_code(self):
            source_code = """
def f1():
    x = 0
    for a in [1,2,3,4,5]:
        x = x + a
        print(x)
    return x
print(f1())
    """

            ces = CodeExecutionSandbox(source_code)
            ces.execute()

            assert ces.print_logs == ['hello', 'hello2', '3']
    def test_print_logs_with_params(self):
        source_code = """
def f2(x):
    y = 5
    print(y)
    z = 9
    return y * 7 + x

print(f2(4))
"""

        ces = CodeExecutionSandbox(source_code)
        ces.execute()

        assert ces.print_logs == ['5', '39']


#     def test_unknown_error(self):
#         source_code = """
# def f2():
#     y = 5
#     z = 9
#     for x in range(8):
#         z = z + 8
#     return y * 7
#
# print(f2())
# """
#         ces = CodeExecutionSandbox(source_code)
#         ces.execute()
