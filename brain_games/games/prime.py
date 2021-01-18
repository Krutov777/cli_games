#!/usr/bin/env python3

import random


def check_prime():
    """
    Generates a random integer and checks if it is a prime number.
    :return: correct answer and integer
    """
    expression = random.randint(1, 100)
    composite_dividers = list(range(2, expression))
    for i in composite_dividers:
        if expression % i == 0:
            answer = "no"
            return (answer, expression)
    return ("yes", expression)
