import logging


class MultiChoiceFactory:

    @classmethod
    def build(cls, correct_answer, choice_list):
        if correct_answer not in choice_list:
            logging.debug(
                f'MultiChoiceFactory.build: {correct_answer} not in {choice_list}')
            choice_list.append(correct_answer)

        logging.debug(f'MultiChoiceFactory.build: {choice_list}')
        return choice_list
