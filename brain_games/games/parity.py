#!/usr/bin/env python3

import random


def check_parity():
    expression = random.randint(1, 100)
    if expression % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return (answer, expression)
