#!/usr/bin/env python3
import prompt
import random


def even_odd(name):
    counter_input = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter_input < 3:
        number = random.randint(1, 100)
        print('Question: {}'.format(number))
        answer_input = ''
        answer_input = prompt.string('Your answer: ')
        if number % 2 == 0 and answer_input == 'yes':
            print('correct')
            counter_input += 1
        elif number % 2 == 1 and answer_input == 'no':
            print('correct')
            counter_input += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(" Let's try again, {}!".format(name))
            break
    if counter_input == 3:
        print('Congratulations, {}!'.format(name))
