#!/usr/bin/env python3

import prompt


def welcome_user():
    """
    Welcomes, asks for a name and takes a user input.
    Greets the user in the game.
    :return: user input
    """
    print("Welcome to the Brain Games!")
    name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    return name
