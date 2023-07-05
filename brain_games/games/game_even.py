from random import randint


def ask_a_question():
    condition_game = 'Answer "yes" if number is even otherwise answer "no".'
    return condition_game


def create_a_game():
    start_number = 1
    finish_number = 100
    question = randint(start_number, finish_number)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
