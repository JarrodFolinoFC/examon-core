from .examon_item_registry import ExamonItemRegistry
from .models.question_factory import QuestionFactory


def examon_item(internal_id=None, choices=None,
                tags=None, hints=None,
                generated_choices=None, param1=None):
    def inner_function(function):
        processed_question = QuestionFactory.build(
            function=function, choice_list=choices,
            tags=tags, hints=hints, internal_id=internal_id,
            version=1,
            generated_choices=generated_choices,
            param1=param1, metrics=True)
        ExamonItemRegistry.add(processed_question)
        return function

    return inner_function
