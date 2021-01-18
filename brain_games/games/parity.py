#!/usr/bin/env python3

import random


def check_parity():
    """
    Generates a random integer and checks if it is even.
    :return: correct answer and integer
    """
    expression = random.randint(1, 100)
    if expression % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return (answer, expression)
