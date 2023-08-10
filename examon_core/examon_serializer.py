from dataclasses_serialization.json import JSONSerializer


class ExamonSerializer:
    @staticmethod
    def serialize(question_response):
        return JSONSerializer.serialize(question_response)
