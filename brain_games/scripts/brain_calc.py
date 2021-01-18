#!/usr/bin/env python3

from brain_games.greeting import welcome_user
from brain_games.games.calc import check_calculator
from brain_games.game_engine import check_answer


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    check_answer(check_calculator, name)


if __name__ == "__main__":
    main()
