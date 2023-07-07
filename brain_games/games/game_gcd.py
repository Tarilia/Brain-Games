from random import randint
from math import gcd


def ask_a_question():
    condition_game = 'Find the greatest common divisor of given numbers.'
    return condition_game


def create_a_game():
    start_number = 1
    finish_number = 100
    first_number = randint(start_number, finish_number)
    second_number = randint(start_number, finish_number)
    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer
