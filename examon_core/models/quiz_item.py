from functools import wraps
from .quiz_item_registry import QuizItemRegistry
from .question_factory import QuestionFactory


def quiz_item(choices=None, tags=None, hints=None,
              generated_choices=None, param1=None):
    def inner_function(function):
        processed_question = QuestionFactory.build(
            function=function, choice_list=choices,
            tags=tags, hints=hints,
            generated_choices=generated_choices,
            param1=param1)
        QuizItemRegistry.add(processed_question)

        @wraps(function)
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            return wrapper

    return inner_function
