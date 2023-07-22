from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'
START_NUMBER = 1
FINISH_NUMBER = 100


def get_question_and_correct_answer():
    first_number = randint(START_NUMBER, FINISH_NUMBER)
    second_number = randint(START_NUMBER, FINISH_NUMBER)
    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer
