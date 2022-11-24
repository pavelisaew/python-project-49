from random import randint


END_RANGE = 100
BEGIN_STEP = 3
END_STEP = 10
BEGIN_LENGTH = 10
END_LENGTH = 20
TASK = 'What number is missing in the progression?'


def generate_progression(begin, step, length):
    """generating a sequence"""
    result = []

    for i in range(begin, begin + (step * length), step):
        result.append(str(i))

    return result


def get_question_correct_answer():
    begin_progression = randint(0, END_RANGE)
    step_progression = randint(BEGIN_STEP, END_STEP)
    length_progression = randint(BEGIN_LENGTH, END_LENGTH)
    progression = generate_progression(
        begin_progression, step_progression, length_progression)
    index_replace = randint(0, len(progression) - 1)
    correct_answer = progression[index_replace]
    progression[index_replace] = '..'
    question = ' '.join(progression)
    return question, correct_answer
