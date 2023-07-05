from prompt import string
from random import randint


def start_the_game(game):
    print("Welcome to the Brain Games!")
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    condition_game = game.ask_a_question()
    print(condition_game)
    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = game.create_a_game()
        print(f'Question: {question}')
        answer_user = string('Your answer: ').lower()
        if answer_user == correct_answer:
            print('Correct!')
        elif answer_user != correct_answer:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return False
    print(f'Congratulations, {user_name}!')
