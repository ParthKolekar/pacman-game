#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    A unittest for the pacman game
"""

import unittest
from ..pacman.pacman import Pacman
from ..pacman.ghost import Ghost
from ..pacman.game import Game
from ..pacman.gamemaze import GameMaze


class TestPacmanModule(unittest.TestCase):
    """
        Test Module
    """

    def test_ghost(self):
        """
            Tests if ghost is created
        """

        ghost = Ghost((10, 10))
        self.assertEqual(ghost.position[1], 10)
        self.assertEqual(ghost.position[1], 10)

        ghost.move_up()
        self.assertEqual(ghost.position[1], 10)

        ghost.move_up()
        self.assertEqual(ghost.position[1], 10)

        ghost.move_next()
        self.assertEqual(ghost.position[1], 9)

        ghost = Ghost((10, 10))
        self.assertEqual(ghost.position[1], 10)
        self.assertEqual(ghost.position[1], 10)

        ghost.move_down()
        self.assertEqual(ghost.position[1], 10)

        ghost.move_down()
        self.assertEqual(ghost.position[1], 10)

        ghost.move_next()
        self.assertEqual(ghost.position[1], 11)

        ghost = Ghost((10, 10))
        self.assertEqual(ghost.position[0], 10)
        self.assertEqual(ghost.position[0], 10)

        ghost.move_left()
        self.assertEqual(ghost.position[0], 10)

        ghost.move_left()
        self.assertEqual(ghost.position[0], 10)

        ghost.move_next()
        self.assertEqual(ghost.position[0], 9)

        ghost = Ghost((10, 10))
        self.assertEqual(ghost.position[0], 10)
        self.assertEqual(ghost.position[0], 10)

        ghost.move_right()
        self.assertEqual(ghost.position[0], 10)

        ghost.move_right()
        self.assertEqual(ghost.position[0], 10)

        ghost.move_next()
        self.assertEqual(ghost.position[0], 11)

    def test_the_pacman(self):
        """
            Tests if pacman is created
        """

        pacman = Pacman((10, 10), 0)
        self.assertEqual(pacman.position[1], 10)
        self.assertEqual(pacman.position[1], 10)

        pacman.move_up()
        self.assertEqual(pacman.position[1], 10)

        pacman.move_up()
        self.assertEqual(pacman.position[1], 10)

        pacman.move_next()
        self.assertEqual(pacman.position[1], 9)

        pacman = Pacman((10, 10), 0)
        self.assertEqual(pacman.position[1], 10)
        self.assertEqual(pacman.position[1], 10)

        pacman.move_down()
        self.assertEqual(pacman.position[1], 10)

        pacman.move_down()
        self.assertEqual(pacman.position[1], 10)

        pacman.move_next()
        self.assertEqual(pacman.position[1], 11)

        pacman = Pacman((10, 10), 0)
        self.assertEqual(pacman.position[0], 10)
        self.assertEqual(pacman.position[0], 10)

        pacman.move_left()
        self.assertEqual(pacman.position[0], 10)

        pacman.move_left()
        self.assertEqual(pacman.position[0], 10)

        pacman.move_next()
        self.assertEqual(pacman.position[0], 9)

        pacman = Pacman((10, 10), 0)
        self.assertEqual(pacman.position[0], 10)
        self.assertEqual(pacman.position[0], 10)

        pacman.move_right()
        self.assertEqual(pacman.position[0], 10)

        pacman.move_right()
        self.assertEqual(pacman.position[0], 10)

        pacman.move_next()
        self.assertEqual(pacman.position[0], 11)

        self.assertEqual(pacman.score, 0)
        pacman.change_score(10)
        self.assertEqual(pacman.score, 10)

    def test_game_entropy(self):
        """
            Tests if maze is random or not
        """

        game_maze = GameMaze()
        string = str(game_maze)
        game_maze = GameMaze()
        self.assertEqual(string != str(game_maze), True)

    def test_instances(self):
        """
            Tests if proper instances
        """

        game = Game()
        self.assertEqual(isinstance(game, Game), True)
        self.assertEqual(isinstance(game.pacman, Pacman), True)
        self.assertEqual(isinstance(game.game_maze, GameMaze), True)

    def test_maze_bind(self):
        """
            Tests if game_maze is bound to game
        """

        game_maze = GameMaze()
        game = Game(game_maze=game_maze)

        self.assertEqual(str(game_maze), str(game.game_maze))

    def test_ghost_bind(self):
        """
            Tests if ghost is bound to game
        """

        game = Game()
        ghost = Ghost(game.game_maze.place_enemy())
        game.ghosts.append(ghost)

        self.assertEqual(ghost, game.ghosts[0])
