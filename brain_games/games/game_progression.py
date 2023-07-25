from random import randint


GAME_RULES = 'What number is missing in the progression?'
MIN_INITIAL_NUMBER = 1
MAX_INITIAL_NUMBER = 10
MIN_LAST_NUM = 35
MAX_LAST_NUM = 40
MIN_DIFF_PROGRESSION = 2
MAX_DIFF_PROGRESSION = 5
MIN_HIDDEN_NUM = 0


def calculate_progression(initial_term, last_term, difference):
    progression = []
    for i in range(initial_term, last_term, difference):
        progression.append(i)
    return progression


def make_question_string(progression, hidden_element):
    question_string = list(progression)
    question_string[hidden_element] = '..'
    question_string = ' '.join(map(str, question_string))
    return question_string


def get_question_and_correct_answer():
    initial_term = randint(MIN_INITIAL_NUMBER, MAX_INITIAL_NUMBER)
    last_term = randint(MIN_LAST_NUM, MAX_LAST_NUM)
    difference = randint(MIN_DIFF_PROGRESSION, MAX_DIFF_PROGRESSION)
    progression = calculate_progression(initial_term, last_term, difference)
    hidden_element = randint(MIN_HIDDEN_NUM, len(progression) - 1)
    question = make_question_string(progression, hidden_element)
    correct_answer = str(progression[hidden_element])
    return question, correct_answer
