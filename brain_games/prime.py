#!/usr/bin/env python3
import prompt
import random


def present_number(name):
    counter_input = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while counter_input < 3:
        number = random.randint(1, 100)
        flag = 'yes'
        divider = 2
        while divider < number:
            if number % divider == 0:
                flag = 'no'
            divider += 1
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == flag:
            print('Correct!')
            counter_input += 1
        else:
            print("{} is wrong answer ;(. Let's try again, {}!".format(answer, name))
            break
    if counter_input == 3:
        print('Congratulations, {}!'.format(name))