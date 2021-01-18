#!/usr/bin/env python3

from brain_games.greeting import welcome_user
from brain_games.games.progression import check_progression
from brain_games.game_engine import check_answer


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    check_answer(check_progression, name)


if __name__ == "__main__":
    main()
