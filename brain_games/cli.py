#!/usr/bin/env python3

import prompt


def welcome_user():
    """
    Asks for a name and takes a user input.
    Greets the user.
    :return: user input
    """
    name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    return name
