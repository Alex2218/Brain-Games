from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def question_and_answer():
    progression_length = randint(5, 10)
    start = randint(1, 20)
    position_of_indefinite_num = randint(0, progression_length - 1)
    step = randint(1, 5)
    index_of_num = 1
    question = ''
    while index_of_num < progression_length:
        if index_of_num == position_of_indefinite_num:
            question += '. . '
            index_of_num += 1
        else:
            question += f'{start + step * index_of_num} '
            index_of_num += 1
    result = start + step * position_of_indefinite_num
    return str(result), question.rstrip()
