from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_correct_answer():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
