"""
    A collection of helper modules
"""

import argparse

try:
    from msvcrt import getch
except ImportError:
    from sys import stdin
    from termios import tcgetattr, tcsetattr, TCSADRAIN
    from tty import setraw

    def getch():
        """
            GetCh wrapper for linux
        """

        file_descriptor = stdin.fileno()
        old_settings = tcgetattr(file_descriptor)
        try:
            setraw(file_descriptor)
            character = stdin.read(1)
        finally:
            tcsetattr(file_descriptor, TCSADRAIN, old_settings)
        return character


def clear(clear_num=100):
    """
        clears the screen by printing too many blank lines
    """
    for _ in xrange(clear_num):
        print


def size_parser():
    """
        DEPRICATED: Parse Sizes
    """

    try:
        size_x = int(raw_input('Enter The Size-X (odd number)\n>'))
        size_y = int(raw_input('Enter The Size-Y (odd number)\n>'))
        if size_x < 8 or size_y < 8:
            print "Not that small dude ('-_-) "
            raise ValueError()
        if size_x > 80 or size_y > 40:
            print 'Size too much'
            raise ValueError()
        if size_x % 2 == 0:
            size_x = size_x + 1
        if size_y % 2 == 0:
            size_y = size_y + 1
    except ValueError:
        print 'Invalid Input. Assuming Defaults (35,15)'
        (size_x, size_y) = (35, 15)
    return (size_x, size_y)


def difficulty_parser():
    """
        DEPRICATED: Parse difficulty
    """

    try:
        difficulty = int(
            raw_input('Enter the difficulty (Number of Ghosts)\n>'))
        if difficulty < 0:
            print "Not that small dude ('-_-) "
            raise ValueError()
        if difficulty > 10:
            print 'Too many ghosts'
            raise ValueError()
    except ValueError:
        print 'Invalid Input. Assuming Defaults 4 Ghosts'
        difficulty = 4
    return difficulty


def argument_parser():
    """
        Parse arguments from the command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy", action='store_true')
    parser.add_argument('-d', '--difficulty', type=int, help="Enter the difficulty [0-10]", default=4)
    parser.add_argument('-x', '--size-x', type=int, help="Enter the width", default=35)
    parser.add_argument('-y', '--size-y', type=int, help="Enter the height", default=15)
    args = parser.parse_args()

    if args.legacy:
        size_x, size_y = size_parser()
        difficulty = difficulty_parser()
        return (size_x, size_y, difficulty)

    return (args.size_x, args.size_y, args.difficulty)
