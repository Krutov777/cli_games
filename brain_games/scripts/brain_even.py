#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.check_even_odd import even_odd


def main():
    name = welcome_user()
    even_odd(name)


if __name__ == '__main__':
    main()