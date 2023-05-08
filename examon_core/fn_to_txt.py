import inspect
import re


def function_raw_code(function, hints):
    def build_hints(hints):
        hint_summary = ''
        if hints is None:
            return hint_summary
        else:
            for hint in hints:
                hint_summary += f'# {hint}\n'
        return f'# Hints:\n{hint_summary}\n\n'

    def function_src(function):
        return inspect.getsource(function).strip()

    def remove_quiz_item_decorator(src):
        src = re.sub('@quiz\\_item\\(.*\\)', '', src)
        return src

    def append_print(function):
        return f'\n\nprint({function.__name__}())'

    src = function_src(function) + append_print(function)
    src = remove_quiz_item_decorator(src)
    return build_hints(hints) + src
