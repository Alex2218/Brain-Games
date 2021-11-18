from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    question = f"{str(num1)} {str(num2)}"
    result = find_gcd(num1, num2)
    return str(result), question


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
        result = num1 + num2
    return result
