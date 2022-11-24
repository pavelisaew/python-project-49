import prompt

MAX_ATTEMPTS = 3


def engine_play(game):
    """game engine"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}')
    print(game.TASK)
    attempt = 0

    while attempt < MAX_ATTEMPTS:
        question, correct_answer = game.get_question_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct !')
            attempt += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {name}!"
            )
            return

    print(f'Congratulations, {name}!')
