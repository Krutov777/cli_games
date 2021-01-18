#!/usr/bin/env python3

from brain_games.greeting import welcome_user
from brain_games.games.prime import check_prime
from brain_games.game_engine import check_answer


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    check_answer(check_prime, name)


if __name__ == "__main__":
    main()
