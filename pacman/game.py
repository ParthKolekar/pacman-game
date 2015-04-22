"""
    Game Class which has bound multiple elements
    It also defines moves for the same
"""

from .gamemaze import GameMaze
from .pacman import Pacman


class Game(object):
    """
        Game Class.
        Creates a new instance of this every resulting in a new game.
    """

    def __init__(self, difficulty=4, game_maze=GameMaze(randomMaze=True), score=0):
        object.__init__(self)
        self.difficulty = difficulty
        self.game_maze = game_maze
        self.ghosts = []
        self.pacman = Pacman(
            (game_maze.size_x / 2, game_maze.size_y * 3 / 4), score)

    def pacman_move_next(self, pacman):
        """
            Move next for Pacman
        """

        game_point = pacman.get_current()
        if not self.game_maze.checkwall(pacman.get_next()):
            pacman.move_next()

        if self.game_maze.get_attribute(pacman.get_current()) == GameMaze.MAZE['ghost'] or self.game_maze.get_attribute(pacman.get_current()) == GameMaze.MAZE['coinghost']:
            print GameMaze.COLORS['pacman'] + 'You cannot kill Ghosts' + GameMaze.COLORS['END']
            exit(0)

        if self.game_maze.get_attribute(pacman.get_current()) == GameMaze.MAZE['coin']:
            pacman.change_score(1)
            self.game_maze.coin_count = self.game_maze.coin_count - 1

        self.game_maze.clear_all(game_point)

        self.game_maze.set_attribute(pacman.get_current(), GameMaze.MAZE['pacman'])

    def ghost_move_next(self, ghost):
        """
            Move next for ghost
        """

        game_point = ghost.get_current()
        ghost.think_next(self.game_maze, self.pacman)
        if not self.game_maze.checkwall(ghost.get_next()) and self.game_maze.get_attribute(ghost.get_next()) != GameMaze.MAZE['ghost'] and self.game_maze.get_attribute(ghost.get_next()) != GameMaze.MAZE['coinghost']:
            ghost.move_next()
        if self.game_maze.get_attribute(ghost.get_current()) == GameMaze.MAZE['pacman']:
            print GameMaze.COLORS['pacman'] + 'The AI killed you off. :(' + GameMaze.COLORS['END']
            exit(0)

        if self.game_maze.get_attribute(game_point) == GameMaze.MAZE['coinghost']:
            self.game_maze.set_attribute(game_point, GameMaze.MAZE['coin'])
        else:
            self.game_maze.clear_all(game_point)

        if self.game_maze.get_attribute(ghost.get_current()) == GameMaze.MAZE['coin']:
            self.game_maze.set_attribute(
                ghost.get_current(), GameMaze.MAZE['coinghost'])
        else:
            self.game_maze.set_attribute(
                ghost.get_current(), GameMaze.MAZE['ghost'])

    def multiple_move_next(self, thing):
        """ Move Next for all objects """

        if thing.__class__.__name__ == 'Pacman':
            self.pacman_move_next(thing)
        elif thing.__class__.__name__ == 'Ghost':
            self.ghost_move_next(thing)
        else:
            print 'Whoa Dude! How Do You Even?'

    def check_ghost(self):
        """
            Check if ghost on spot
        """

        return self.game_maze.get_attribute(self.pacman.get_current()) == GameMaze.MAZE['ghost']
