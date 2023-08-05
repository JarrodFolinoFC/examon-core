import builtins
import io
from contextlib import redirect_stdout


class UnrestrictedDriver:
    def __init__(self):
        self.default_print = builtins.print

    def setup(self):
        builtins.print = self.default_print

    def teardown(self):
        builtins.print = self.default_print

    def execute(self, source_code):
        logs = []

        def new_print(*args, **kwargs):
            f = io.StringIO()
            with redirect_stdout(f):
                self.default_print(*args, **kwargs)
            out = f.getvalue().rstrip()
            logs.append(out)
            return None

        builtins.print = new_print
        exec(source_code)
        return logs
