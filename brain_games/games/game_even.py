from random import randint


GAME_RULES = 'Answer "yes" if the number is even,'\
                     ' otherwise answer "no".'
START_NUMBER = 1
FINISH_NUMBER = 100


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_question_and_correct_answer():
    question = randint(START_NUMBER, FINISH_NUMBER)
    correct_answer = is_even(question)
    return question, correct_answer
