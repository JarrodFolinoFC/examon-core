import logging


class ExamonItemRegistry:
    __registry = []

    @classmethod
    def add(cls, quiz_item):
        logging.debug(f'Adding {quiz_item} to registry')
        cls.__registry.append(quiz_item)

    @classmethod
    def reset(cls):
        cls.__registry = []

    @classmethod
    def registry(cls, tag=None):
        return [
            py_quiz_data
            for py_quiz_data in cls.__registry
            if tag in py_quiz_data.tags or tag is None
        ]
