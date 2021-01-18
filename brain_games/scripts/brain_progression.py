#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.progression import arithmetic_progression


def main():
    name = welcome_user()
    arithmetic_progression(name)


if __name__ == '__main__':
    main()
