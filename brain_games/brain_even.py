from prompt import string
from random import randint


def check_for_parity():
    print("Welcome to the Brain Games!")
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_count = 3
    for _ in range(rounds_count):
        start_number = 1
        finish_number = 100
        question = randint(start_number, finish_number)
        print(f'Question: {question}')
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer_user = string('Your answer: ').lower()
        if answer_user == correct_answer:
            print('Correct!')
        elif answer_user != correct_answer:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return False
    print(f'Congratulations, {user_name}!')
