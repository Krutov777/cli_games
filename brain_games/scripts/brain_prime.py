#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.prime import present_number


def main():
    name = welcome_user()
    present_number(name)


if __name__ == '__main__':
    main()