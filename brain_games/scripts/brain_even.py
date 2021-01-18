#!/usr/bin/env python3

from brain_games.greeting import welcome_user
from brain_games.games.parity import check_parity
from brain_games.game_engine import check_answer


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    check_answer(check_parity, name)


if __name__ == "__main__":
    main()
