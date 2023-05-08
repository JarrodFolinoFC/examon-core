class CodeMetrics:
    def __init__(self, code_as_string):
        self.code_as_string = code_as_string
        self.metrics = {
            'difficulty': None,
            'no_of_functions': None,
            'loc': None,
            'lloc': None,
            'sloc': None
        }
