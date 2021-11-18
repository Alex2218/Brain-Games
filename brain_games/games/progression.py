
from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'
SEQUENCE_LENGTH = randint(5, 10)


def question_and_answer():

    start, step = randint(1, 10), randint(1, 10)
    sequence = list(range(start, SEQUENCE_LENGTH * step + start, step))

    correct_answer = choice(sequence)
    task = ' '.join(
        '..' if number == correct_answer else str(number) for number in sequence
    )

    return task, str(correct_answer)
