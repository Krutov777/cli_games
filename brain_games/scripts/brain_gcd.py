#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.nod import nod


def main():
    name = welcome_user()
    nod(name)


if __name__ == '__main__':
    main()
