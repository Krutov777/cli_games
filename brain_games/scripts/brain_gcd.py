#!/usr/bin/env python3

from brain_games.greeting import welcome_user
from brain_games.games.divisor import check_gcd
from brain_games.game_engine import check_answer


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    check_answer(check_gcd, name)


if __name__ == "__main__":
    main()
