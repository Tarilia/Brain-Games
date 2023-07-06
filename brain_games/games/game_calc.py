from random import randint
from random import choice


def ask_a_question():
    condition_game = 'What is the result of the expression?'
    return condition_game


def create_a_game():
    start_number = 1
    finish_number = 100
    symbols = ["+", "-", "*"]
    first_number = randint(start_number, finish_number)
    second_number = randint(start_number, finish_number)
    operator = choice(symbols)
    question = f' {first_number} {operator} {second_number}'
    if operator == '+':
        correct_answer = str(first_number + second_number)
    elif operator == '-':
        correct_answer = str(first_number - second_number)
    elif operator == '*':
        correct_answer = str(first_number * second_number)
    return question, correct_answer
