#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.calculate import calc


def main():
    name = welcome_user()
    calc(name)


if __name__ == '__main__':
    main()
