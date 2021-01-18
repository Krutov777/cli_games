#!/usr/bin/env python3


def check_answer(game, name):
    """
    Asks a question and takes a user input.
    Compares the correct answer with the user input.
    Shows results.
    :param game: the correct answer and the question
    :param name: user name
    :return: None
    """
    for _ in range(3):
        answer, expression = game()
        print(f"Question: {expression}")
        user_input = input("Your answer: ")
        if user_input == answer:
            print("Correct!")
            continue
        if user_input != answer:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'. \nLet's try again, {name}! ")
            return
    print(f"Congratulations, {name}!")
