from random import randint


BEGIN_RANGE = 2
END_RANGE = 10
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_the_correct_answer(value):
    """parity check"""
    return 'yes' if value % 2 == 0 else 'no'


def get_question_correct_answer():
    question = randint(BEGIN_RANGE, END_RANGE)
    correct_answer = get_the_correct_answer(question)
    return str(question), correct_answer
