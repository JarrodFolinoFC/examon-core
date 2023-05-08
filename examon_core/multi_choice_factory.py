class MultiChoiceFactory:

    @classmethod
    def build(cls, correct_answer, choice_list):
        if correct_answer not in choice_list:
            choice_list.append(correct_answer)
        return choice_list
