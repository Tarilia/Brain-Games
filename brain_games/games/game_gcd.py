from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_correct_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer
