from .examon_item_registry import ExamonItemRegistry
from .question_factory import QuestionFactory


def examon_item(choices=None, tags=None, hints=None,
                generated_choices=None, param1=None):
    def inner_function(function):
        processed_question = QuestionFactory.build(
            function=function, choice_list=choices,
            tags=tags, hints=hints,
            generated_choices=generated_choices,
            param1=param1, metrics=True)
        ExamonItemRegistry.add(processed_question)
        return function

    return inner_function
