#!/usr/bin/env python3

import random
import math


def check_gcd():
    """
    Generates two random integers and finds the greatest
    common divisor of generated integers.
    :return: gcd and integers
    """
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f"{number_1} {number_2}"
    answer = math.gcd(number_1, number_2)
    return (str(answer), expression)
