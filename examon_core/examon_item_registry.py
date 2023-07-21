from dataclasses import dataclass
import logging


@dataclass
class ItemRegistryFilter:
    tags_any: list = None
    difficulty: str = None
    tags_all: list = None
    max_questions: int = None


class ExamonItemRegistry:
    __registry = []
    __tags = []

    @classmethod
    def add(cls, examon_item):
        logging.debug(f'Adding {examon_item} to registry')
        cls.__registry.append(examon_item)
        for tag in examon_item.tags:
            if tag not in cls.__tags:
                cls.__tags.append(tag)

    @classmethod
    def reset(cls):
        cls.__registry = []
        cls.__filter = None

    @classmethod
    def registry(cls, examon_filter=None):
        def intersection(lst1, lst2):
            return list(set(lst1) & set(lst2))

        results = cls.__registry
        if examon_filter is None:
            return results
        elif examon_filter.tags_any is not None:
            results = [
                py_quiz_data
                for py_quiz_data in cls.__registry
                if len(intersection(examon_filter.tags_any, py_quiz_data.tags)) > 0
            ]
        elif examon_filter.tags_all is not None:
            results = [
                py_quiz_data
                for py_quiz_data in cls.__registry
                if len(intersection(examon_filter.tags_all, py_quiz_data.tags)) == len(py_quiz_data.tags)
            ]
        if examon_filter.max_questions is not None:
            return results[0:examon_filter.max_questions]
        else:
            return results

    @classmethod
    def unique_tags(cls):
        return cls.__tags
