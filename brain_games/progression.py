#!/usr/bin/env python3
import random
import prompt


def arithmetic_progression(name):
    counter_input = 0
    lenght = 10
    print('What number is missing in the progression?')
    while counter_input < 3:
        step = random.randint(1, 10)
        lst = []
        number = random.randint(1, 100)
        while len(lst) < lenght:
            lst.append(str(number))
            number += step
        random_index = random.randrange(0, len(lst))
        secret_number = lst[random_index]
        lst[random_index] = '..'
        lst = ' '.join(lst)
        print('Question: {}'.format(lst))
        answer = prompt.string('Your answer: ')
        if answer == secret_number:
            print('correct')
            counter_input += 1
        else:
            answer = answer + " is wrong answer ;(. "
            secret_number = "Correct answer was " + secret_number
            print(answer + secret_number)
            print("Let's try again, {}!".format(name))
            break
    if counter_input == 3:
        print('Congratulations, {}!'.format(name))
