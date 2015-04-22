#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Pacman implementation in python
"""

from .game import Game
from .gamemaze import GameMaze
from .ghost import Ghost
from .utils import clear, difficulty_parser, getch, size_parser


def main():
    """
        Main function
    """

    (size_x, size_y) = size_parser()
    game_maze = GameMaze(1, (size_x, size_y))
    difficulty = difficulty_parser()
    game = Game(difficulty, game_maze)
    for _ in xrange(0, difficulty):
        game.ghosts.append(Ghost(game.game_maze.place_enemy()))
    character = getch()
    while True:
        clear()  # default would be enough
        game.multiple_move_next(game.pacman)
        for i in game.ghosts:
            game.multiple_move_next(i)
        print 'Score : ' + str(game.pacman.score)
        print game.game_maze
        character = getch()
        while character not in ['q', 'w', 'a', 's', 'd']:
            character = getch()
        if character == 'q':
            exit(0)
        elif character == 'w':
            game.pacman.move_up()
        elif character == 'a':
            game.pacman.move_left()
        elif character == 's':
            game.pacman.move_down()
        elif character == 'd':
            game.pacman.move_right()
        if game.game_maze.coin_count == 0:
            print 'LEVEL WON! BOND!!!'
            character = getch()
            game_maze = GameMaze(1, (size_x, size_y))
            game = Game(difficulty, game_maze, game.pacman.score)
            for i in xrange(0, difficulty):
                game.ghosts.append(Ghost(game.game_maze.place_enemy()))


if __name__ == '__main__':
    main()
