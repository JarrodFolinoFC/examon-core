import builtins
from contextlib import redirect_stdout
import io
from inspect import getframeinfo, stack


class PrintLog:
    print_logs = []

    @classmethod
    def append(cls, value):
        cls.print_logs.append(value)

    @classmethod
    def logs(cls):
        return cls.print_logs

    @classmethod
    def apply_offset(cls, offset):
        cls.print_logs = list(
            map(lambda x: (x[0], x[1] - offset), cls.print_logs)
        )

    @classmethod
    def reset(cls):
        cls.print_logs = []


def print(*args, **kwargs):
    caller = getframeinfo(stack()[1][0])
    f = io.StringIO()

    with redirect_stdout(f):
        builtins.print(*args, **kwargs)
    s = f.getvalue().rstrip()
    PrintLog.append((s, caller.lineno))
