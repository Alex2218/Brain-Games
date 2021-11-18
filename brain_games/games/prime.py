from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    question = randint(1, 10)
    result = 'yes'if is_prime(question) else 'no'
    return result, str(question)


def is_prime(num):
    if (num < 2):
        return False

    divider = 2

    while divider <= num / 2:
        if num % divider == 0:
            return False
        divider += 1

    return True
