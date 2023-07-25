from prompt import string


def fulfill(game):
    print("Welcome to the Brain Games!")
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULES)
    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = game.get_question_and_correct_answer()
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
