from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(question):
    if question < 2:
        return False
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            return False
    else:
        return True


def get_question_and_correct_answer():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
