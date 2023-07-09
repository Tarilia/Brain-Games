from random import randint


def ask_a_question():
    condition_games = 'What number is missing in the progression?'
    return condition_games


def create_a_game():
    start_number = randint(1, 10)
    finish_number = randint(35, 40)
    progression_step = randint(2, 5)
    arithmetic_progression = []
    for i in range(start_number, finish_number, progression_step):
        arithmetic_progression.append(i)
    random_element = randint(0, len(arithmetic_progression) - 1)
    correct_answer = str(arithmetic_progression[random_element])
    arithmetic_progression[random_element] = '..'
    question = ' '.join(map(str, arithmetic_progression))
    return question, correct_answer
