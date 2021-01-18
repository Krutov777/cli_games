#!/usr/bin/env python3

import prompt


def welcome_user():
    name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    return name
