#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    from random import randint
    
    
    correct_answer_counter = 0

    while (correct_answer_counter < 3):
    
    
        BEGIN_RANGE = 1
        END_RANGE = 10
        first_value = randint(BEGIN_RANGE, END_RANGE)
        second_value = randint(BEGIN_RANGE, END_RANGE)
        question = f'{first_value} {second_value}'
        print("Question:", question)
        operation_result = (input('Your answer: '))
        while first_value != 0 and second_value != 0:
            if first_value >= second_value:
                first_value %= second_value
            else:
                second_value %= first_value
        if first_value == 0:
            correct_answer = second_value
        if second_value == 0:
            correct_answer = first_value
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
