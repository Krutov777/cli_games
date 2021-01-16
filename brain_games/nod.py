#!/usr/bin/env python3
import random
import prompt

def nod(name):
    number1 = 1
    number2 = 1
    counter_input = 0
    print('Find the greatest common divisor of given numbers.')
    while counter_input < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print('Question: {} {}'.format(number1, number2))
        while number1 != 0 and number2 != 0:
            if number1 > number2:
                number1 %= number2
            else:
                number2 %= number1      
        nod = number1 + number2
        answer = prompt.string('Your answer: ')
        if int(answer) == nod:
            print('correct')
            counter_input += 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}.Let's try again, {}!.".format(answer, nod, name))
            break
    if counter_input == 3:
        print('Congratulations, {}!'.format(name))