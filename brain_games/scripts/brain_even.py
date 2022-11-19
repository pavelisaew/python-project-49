#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    from random import randint


    correct_answer_counter = 0

    while (correct_answer_counter < 3):

        rand_number = randint(0, 999)
        print("Question:", rand_number)
        answer = (input('Your answer: '))
        if rand_number % 2 == 0:
            if answer == "yes":
                correct_answer_counter += 1
                print("Correct")
            else:
                correct_answer_counter = 0
                print(f"'{answer}' is wrong answer ;(. Correct answer was \'yes\'. Let's try again, {name}!")
                break
        elif rand_number % 2 == 1:
            if answer == "no":
                correct_answer_counter += 1
                print("Correct")
            else:
                correct_answer_counter = 0
                print(f"'{answer}' is wrong answer ;(. Correct answer was \'no\'. Let's try again, {name}!")
                break
        if correct_answer_counter == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

