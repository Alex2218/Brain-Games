#!/usr/bin/env python
import prompt

ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_user))
    print(game.DESCRIPTION)

    for _ in range(ROUNDS_COUNT):
        task, correct_answer = game.question_and_answer()
        print('Question: {0}'.format(task))
        answer_user = prompt.string('Your answer: ')
        if answer_user == correct_answer:
            print('Correct!')
            continue
        show_game_over(answer_user, correct_answer, name_user)
        break
    else:
        print('Congratulations, {0}!'.format(name_user))


def show_game_over(answer_user, correct_answer, name_user):
 
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
        answer_user,
        correct_answer,
    ))
    print("Let's try again, {0}!".format(name_user))