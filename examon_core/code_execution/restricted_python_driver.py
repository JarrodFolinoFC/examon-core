from RestrictedPython import compile_restricted
from RestrictedPython.Eval import default_guarded_getiter
from RestrictedPython.Guards import safe_builtins
from .print_collector import PrintCollector


class RestrictedPythonDriver:

    def setup(self):
        pass

    def teardown(self):
        pass

    def execute(self, source_code):
        _print_ = PrintCollector   # noqa: E731,F841

        def inplacevar_wrapper(op, x, y):
            globs = {'x': x, 'y': y}
            exec('x' + op + 'y')
            return globs['x']

        try:
            safe_globals = safe_builtins | {
                '_print_': PrintCollector,
                '_getattr_': getattr,
                '_getiter_': default_guarded_getiter,
                '_inplacevar_': inplacevar_wrapper,
                '__name__': 'restricted namespace'
            }

            compiled_code = compile_restricted(source_code, '<string>', 'exec')
            exec(compiled_code, safe_globals)
            return safe_globals['_print']().rstrip().split('\n')
        finally:
            PrintCollector.reset()
