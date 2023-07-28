from RestrictedPython import compile_restricted


class PrintCollector:
    output = []

    def __init__(self, _getattr_=None):
        self._getattr_ = _getattr_

    def write(self, text):
        PrintCollector.output.append(text)

    def __call__(self):
        return ''.join(PrintCollector.output)

    def _call_print(self, *objects, **kwargs):
        if kwargs.get('file', None) is None:
            kwargs['file'] = self
        else:
            self._getattr_(kwargs['file'], 'write')

        print(*objects, **kwargs)

    @staticmethod
    def reset():
        PrintCollector.output = []


class CodeExecutionSandbox:
    def __init__(self, source_code):
        self.source_code = source_code
        self.print_logs = None

    def execute(self):
        _print_ = PrintCollector

        loc = {'_print_': PrintCollector, '_getattr_': getattr}

        compiled_code = compile_restricted(self.source_code, '<string>', 'exec')
        exec(compiled_code, loc)
        self.print_logs = loc['_print']().rstrip().split('\n')
        PrintCollector.reset()
