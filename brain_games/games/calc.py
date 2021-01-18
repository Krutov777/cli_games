#!/usr/bin/env python3

import random
import operator


def check_calculator():
    """
    Generates two random integers. Randomly chooses an operator
    of addition, subtraction or multiplication. Calculates the
    expression using chosen operator.
    :return: correct answer and expression
    """
    number_1 = random.randint(1, 25)
    number_2 = random.randint(1, 25)
    operations = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul}
    op = random.choice(list(operations.keys()))
    answer = operations[op](number_1, number_2)
    expression = f"{number_1} {op} {number_2}"

    return (str(answer), expression)
