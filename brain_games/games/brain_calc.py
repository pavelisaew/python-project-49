from random import randint, choice


BEGIN_RANGE = 1
END_RANGE = 10
TASK = 'What is the result of the expression?'


def get_math_action(first_value, second_value, operator):
    """assign a mathematical operation to the symbol"""
    operation_result = 0

    if operator == '+':
        operation_result = first_value + second_value
    elif operator == '-':
        operation_result = first_value - second_value
    elif operator == '*':
        operation_result = first_value * second_value

    return operation_result


def get_question_correct_answer():
    operator = choice(['+', '-', '*'])
    first_value = randint(BEGIN_RANGE, END_RANGE)
    second_value = randint(BEGIN_RANGE, END_RANGE)
    question = f'{first_value} {operator} {second_value}'
    correct_answer = str(get_math_action(first_value, second_value, operator))
    return question, correct_answer
