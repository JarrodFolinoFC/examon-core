from examon_core.code_execution.sandbox import Sandbox


class TestSandbox:
    def test_run_function(self):
        source_code = """
def f1():
    print('hello')
    print('hello2')
    return 3
print(f1())
"""

        print_logs = Sandbox.run_function(source_code)
        assert print_logs == ['hello', 'hello2', '3']

