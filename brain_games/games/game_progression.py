from random import randint


GAME_RULES = 'What number is missing in the progression?'
START_INITIAL_NUM = 1
FINISH_INITIAL_NUM = 10
START_LAST_NUM = 35
FINISH_LAST_NUM = 40
START_DIFFERENCE_NUM = 2
FINISH_DIFFERENCE_NUM = 5
START_RANDOM_NUM = 0


def calculate_progression(initial_term, last_term, difference):
    progression = []
    for i in range(initial_term, last_term, difference):
        progression.append(i)
    return progression


def constructing_question_string(progression, random_element):
    question_string = list(progression)
    question_string[random_element] = '..'
    question_string = ' '.join(map(str, question_string))
    return question_string


def get_question_and_correct_answer():
    initial_term = randint(START_INITIAL_NUM, FINISH_INITIAL_NUM)
    last_term = randint(START_LAST_NUM, FINISH_LAST_NUM)
    difference = randint(START_DIFFERENCE_NUM, FINISH_DIFFERENCE_NUM)
    progression = calculate_progression(initial_term, last_term, difference)
    random_element = randint(START_RANDOM_NUM, len(progression) - 1)
    question = constructing_question_string(progression, random_element)
    correct_answer = str(progression[random_element])
    return question, correct_answer
