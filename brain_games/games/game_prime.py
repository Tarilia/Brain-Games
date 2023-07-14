from random import randint


def ask_a_question():
    condition_games = 'Answer "yes" if given number is prime. ' \
                      'Otherwise answer "no".'
    return condition_games


def is_prime(question):
    if question < 2:
        return False
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            return False
    else:
        return True


def create_a_game():
    start_number = 0
    finish_number = 100
    question = randint(start_number, finish_number)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
