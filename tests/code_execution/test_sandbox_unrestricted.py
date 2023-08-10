from examon_core.code_execution.sandbox import Sandbox
from examon_core.code_execution.unrestricted_driver import UnrestrictedDriver


class TestCodeExecutionSandbox:
    def test_print_logs(self):
        source_code = """
def f1():
    print('hello')
    print('hello2')
    return 3
print(f1())
"""

        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()

        assert ces.print_logs == ['hello', 'hello2', '3']

    def test_complex_code(self):
        source_code = """
def f1():
    x = 0
    for a in [1, 2, 3]:
        x = x + a
        print(x)
    return x
print(f1())
    """

        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()

        assert ces.print_logs == ['1', '3', '6', '6']

    def test_print_logs_with_params(self):
        source_code = """
def f2(x):
    y = 5
    print(y)
    z = 9
    return y * 7 + x

print(f2(4))
"""

        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()

        assert ces.print_logs == ['5', '39']

    def test_unknown_error(self):
        source_code = """
def f2():
    y = 5
    z = 9
    for x in range(8):
        z = z + 8
    return y * 7

print(f2())
"""
        ces = Sandbox(source_code)
        ces.execute()

    def test_functools_(self):
        source_code = """
from functools import lru_cache

@lru_cache
def go():
    return 1
print(go())
"""
        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()

    def test_with_(self):
        source_code = """
def question_01():
    class LookingGlass:
        def __enter__(self):
            return 'enter'

        def __exit__(self, exc_type, exc_value, traceback):
            return 'exit'

    with LookingGlass() as what:
        return what
print(question_01())
"""
        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()

    def test_unpack(self):
        source_code = """
def question_01():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    return latitude

print(question_01())
"""
        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()


    def test_unpack_2(self):
        source_code = """
def question():
    *rest, a, b = range(5)
    return rest[1]

print(question())
"""
        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()


    def test_class(self):
        source_code = """
def question():
    class A:
        pass

    return A()

print(question())
"""
        ces = Sandbox(source_code, UnrestrictedDriver)
        ces.execute()
