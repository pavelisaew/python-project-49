from random import randint
from math import gcd


BEGIN_RANGE = 1
END_RANGE = 100
TASK = 'Find the greatest common divisor of given numbers.'


def get_question_correct_answer():
    first_value = randint(BEGIN_RANGE, END_RANGE)
    second_value = randint(BEGIN_RANGE, END_RANGE)
    question = f'{first_value} {second_value}'
    correct_answer = str(gcd(first_value, second_value))
    return question, correct_answer
