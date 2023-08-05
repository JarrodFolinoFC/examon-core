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
