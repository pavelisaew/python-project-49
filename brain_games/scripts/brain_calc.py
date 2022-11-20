#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    
    from random import randint, choice
    
    
    correct_answer_counter = 0

    while (correct_answer_counter < 3):

        operator = choice(['+', '-', '*'])
        BEGIN_RANGE = 1
        END_RANGE = 50
        first_value = randint(BEGIN_RANGE, END_RANGE)
        second_value = randint(BEGIN_RANGE, END_RANGE)
        question = (f'{first_value} {operator} {second_value}')
        print("Question:", question)
        operation_result = (input('Your answer: '))
        if operator == '+':
            correct_answer = first_value + second_value
            if str(correct_answer) == operation_result:
                correct_answer_counter += 1
                print("Correct")
            else:
                correct_answer_counter = 0
                print(f"'{operation_result}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, Pavel!")
                break
        elif operator == '-':
            correct_answer = first_value - second_value
            if str(correct_answer) == operation_result:
                correct_answer_counter += 1
                print("Correct")
            else:
                correct_answer_counter = 0
                print(f"'{operation_result}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")
                break
        elif operator == '*':
            correct_answer = first_value * second_value
            if str(correct_answer) == operation_result:
                correct_answer_counter += 1
                print("Correct")
            else:
                correct_answer_counter = 0
                print(f"'{operation_result}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")
                break
        if correct_answer_counter == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
