from random import randint


BEGIN_RANGE = 1
END_RANGE = 223
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(value):
    """check if the number is prime"""
    if value <= 1:
        return False

    if value % 2 == 0:
        return value == 2
    number = 3

    while number * number <= value and value % number != 0:
        number += 2
    return number * number > value


def get_question_correct_answer():
    question = randint(BEGIN_RANGE, END_RANGE)

    if is_prime_number(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(question), correct_answer
