#!/usr/bin/env python3

import random


def check_progression():
    """
    Creates an arithmetic progression with random length,
    step, start and end points. Randomly replace an integer
    from progression with two dots ("..").
    :return: replaced integer and progression
    """
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    stop = start + (step * length)
    succession = [str(_) for _ in range(start, stop, step)]
    answer = random.randrange(start, stop, step)
    new_succession = " ".join(succession)
    expression = new_succession.replace(str(answer), "..")
    return (str(answer), expression)
