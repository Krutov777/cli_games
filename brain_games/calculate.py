#!/usr/bin/env python3
import prompt
import random
import operator
from brain_games.cli import welcome_user


def calc(name):
    counter_input = 0
    print('What is the result of the expression?')
    while counter_input < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operations = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul}
        op = random.choice(list(operations.keys()))
        answer = operations[op](number1, number2)
        expression = f"{number1} {op} {number2}"
        print('Question: {}'.format(expression))
        inpt = prompt.string('Your answer: ')
        if answer == int(inpt):
            print('Correct!')
            counter_input += 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}.".format(inpt, answer))
            break
    if counter_input == 3:
        print('Congratulations, {}!'.format(name))