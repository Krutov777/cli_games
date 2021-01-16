#!/usr/bin/env python3
import prompt


def welcome_user():
    print('Welcome {}!'.format('to the Brain Games'))
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
