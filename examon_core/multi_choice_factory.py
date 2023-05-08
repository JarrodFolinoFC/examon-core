class MultiChoiceFactory:

    @classmethod
    def build(cls, correct_answer, choice_list):
        choices = cls.append_answer(choice_list, correct_answer)
        return choices

    @classmethod
    def append_answer(cls, choice_list, answer):
        if answer not in choice_list:
            choice_list.append(answer)
        return choice_list

