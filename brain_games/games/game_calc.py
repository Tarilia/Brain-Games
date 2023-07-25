from random import randint
from random import choice


GAME_RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
SIMBOLS = ["+", "-", "*"]


def get_question_and_correct_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(SIMBOLS)
    question = f'{first_number} {operator} {second_number}'
    if operator == '+':
        correct_answer = str(first_number + second_number)
    elif operator == '-':
        correct_answer = str(first_number - second_number)
    elif operator == '*':
        correct_answer = str(first_number * second_number)
    return question, correct_answer
