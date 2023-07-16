from dataclasses import dataclass
import builtins
from contextlib import redirect_stdout
import io
from inspect import getframeinfo, stack


@dataclass
class PrintLogItem:
    output: str
    line_no: int


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
        def offset_pl(print_log_item):
            return PrintLogItem(
                print_log_item.output,
                print_log_item.line_no - offset)

        cls.print_logs = list(map(offset_pl, cls.print_logs))

    @classmethod
    def reset(cls):
        cls.print_logs = []


def print(*args, **kwargs):
    caller = getframeinfo(stack()[1][0])
    f = io.StringIO()

    with redirect_stdout(f):
        builtins.print(*args, **kwargs)
    s = f.getvalue().rstrip()
    PrintLog.append(PrintLogItem(s, caller.lineno))
