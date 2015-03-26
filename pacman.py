#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Pacman implementation in python """

try:
    from sys import setrecursionlimit, stdin
    from random import randint
    from os import system, name
    from termios import tcgetattr, tcsetattr, TCSADRAIN
    from tty import setraw


    def getch():
        """ GetCh wrapper for linux """

        file_descriptor = stdin.fileno()
        old_settings = tcgetattr(file_descriptor)
        try:
            setraw(file_descriptor)
            character = stdin.read(1)
        finally:
            tcsetattr(file_descriptor, TCSADRAIN, old_settings)
        return character


except ImportError:

    from sys import setrecursionlimit
    from random import randint
    from os import system, name
    from msvcrt import getch

setrecursionlimit(10000)


class GameMaze(object):

    """Making A Maze Module For Game"""

    MAZE = dict(
        wall='X',
        ghost='G',
        pacman='P',
        coin='C',
        nothing='.',
        coinghost='CG',
        )
    COLORS = dict(
        wall='\033[95m',
        ghost='\033[37m',
        coin='\033[33m',
        pacman='\033[91m',
        coinghost='\033[47m',
        nothing='\033[36m',
        END='\033[0m',
        )

    def __init__(self, randomMaze=0, size=(35, 15)):
        object.__init__(self)
        self.position_x = size[0]
        self.position_y = size[1]
        self.coin_count = 0
        self.game_maze = [x[:] for x in [['.'] * self.position_x]
                          * self.position_y]
        self.free_space = set()
        for i in xrange(0, self.position_y):
            for j in [0, self.position_x - 1]:
                self.game_maze[i][j] = GameMaze.MAZE['wall']
        for i in xrange(0, self.position_x):
            for j in [0, self.position_y - 1]:
                self.game_maze[j][i] = GameMaze.MAZE['wall']
        if randomMaze == 0:
            pass
        else:
            self.fill_wall()

            self.game_maze[self.position_y * 3 / 4][self.position_x
                    / 2] = GameMaze.MAZE['pacman']
        self.fill_coin([x[:] for x in [[0] * self.position_x]
                       * self.position_y])

    def place_enemy(self):
        """ Places enemy on map"""

        position_x = randint(1, self.position_x - 1)
        position_y = randint(1, self.position_y - 1)
        while self.checkwall((position_x, position_y)) == True \
            and self.get_attribute((position_x, position_y)) \
            != GameMaze.MAZE['coinghost'] \
            and self.get_attribute((position_x, position_y)) \
            != GameMaze.MAZE['ghost'] \
            and self.get_attribute((position_x, position_y)) \
            != GameMaze.MAZE['coin'] and (position_x, position_y) \
            not in self.free_space:
            position_x = randint(1, self.position_x - 1)
            position_y = randint(1, self.position_y - 1)
        attribute = self.get_attribute((position_x, position_y))
        if attribute == GameMaze.MAZE['coin']:
            self.set_attribute((position_x, position_y),
                               GameMaze.MAZE['coinghost'])
        else:
            self.set_attribute((position_x, position_y),
                               GameMaze.MAZE['ghost'])
        return (position_x, position_y)

    def fill_wall(self, game_point=(2, 2), count=0.0):
        """ Fills Wall in map """

        point_1 = list(game_point)
        point_2 = [game_point[0], self.position_y - game_point[1] - 1]
        point_3 = [self.position_x - game_point[0] - 1, game_point[1]]
        point_4 = [self.position_x - game_point[0] - 1, self.position_y
                   - game_point[1] - 1]
        total = self.position_x * self.position_y
        while point_1[0] < self.position_x / 2 and point_1[1] \
            < self.position_y / 2:
            count += 4.0
            self.make_wall(point_1)
            self.make_wall(point_2)
            self.make_wall(point_3)
            self.make_wall(point_4)
            if randint(0, 1) == 0:
                point_1[0] += 1
                point_2[0] += 1
                point_3[0] -= 1
                point_4[0] -= 1
            else:
                point_1[1] += 1
                point_2[1] -= 1
                point_3[1] += 1
                point_4[1] -= 1
        if count / total < 0.3:
            self.fill_wall((randint(3, self.position_x - 3), randint(3,
                           self.position_x - 3)), count)

    def fill_coin(self, visited, game_point=(1, 1)):
        """ Fills coins on map """

        if self.checkwall(game_point) == True \
            or visited[game_point[1]][game_point[0]] == 1 \
            or self.get_attribute(game_point) == GameMaze.MAZE['pacman'
                ]:
            return
        self.free_space.add(game_point)
        visited[game_point[1]][game_point[0]] = 1
        if randint(0, 2) == 0:  # Probhablisticly fill with coin
            self.make_coin(game_point)
            self.coin_count = self.coin_count + 1
        self.fill_coin(visited, (game_point[0], game_point[1] + 1))
        self.fill_coin(visited, (game_point[0] + 1, game_point[1]))
        self.fill_coin(visited, (game_point[0], game_point[1] - 1))
        self.fill_coin(visited, (game_point[0] - 1, game_point[1]))

    def set_attribute(self, game_point, attribute):
        """ Sets attribute on point """

        self.game_maze[game_point[1]][game_point[0]] = attribute

    def get_attribute(self, game_point):
        """ Gets attribute on point """

        return self.game_maze[game_point[1]][game_point[0]]

    def checkwall(self, game_point):
        """ Checks Wall """

        return self.get_attribute(game_point) == GameMaze.MAZE['wall']

    def clear_all(self, game_point):
        """ Clears all on point """

        self.set_attribute(game_point, GameMaze.MAZE['nothing'])

    def make_wall(self, game_point):
        """ Makes Wall """

        self.set_attribute(game_point, GameMaze.MAZE['wall'])

    def make_coin(self, game_point):
        """ Makes Coin on point """

        self.set_attribute(game_point, GameMaze.MAZE['coin'])

    def __str__(self):
        string = ''
        for i in self.game_maze:
            for j in i:
                if j == GameMaze.MAZE['wall']:
                    string += GameMaze.COLORS['wall'] \
                        + GameMaze.MAZE['wall'] + GameMaze.COLORS['END'
                            ] + ' '
                elif j == GameMaze.MAZE['coin']:
                    string += GameMaze.COLORS['coin'] + j \
                        + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['pacman']:
                    string += GameMaze.COLORS['pacman'] + j \
                        + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['ghost']:
                    string += GameMaze.COLORS['ghost'] + j \
                        + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['coinghost']:
                    string += GameMaze.COLORS['coinghost'] \
                        + GameMaze.MAZE['ghost'] + GameMaze.COLORS['END'
                            ] + ' '
                elif j == GameMaze.MAZE['nothing']:
                    string += GameMaze.COLORS['nothing'] + j \
                        + GameMaze.COLORS['END'] + ' '
                else:
                    string += j + ' '
            string += '\n'
        return string

    __repr__ = __str__


class Person(object):

    """ Generic object """

    def __init__(self, position):
        object.__init__(self)
        self.position = list(position)
        self.direction_vector = (0, 0)

    def move_up(self):
        """ Moves move_up """

        self.direction_vector = (0, -1)

    def move_down(self):
        """ Moves move_down"""

        self.direction_vector = (0, 1)

    def move_left(self):
        """ Moves left """

        self.direction_vector = (-1, 0)

    def move_right(self):
        """ Moves move_right"""

        self.direction_vector = (1, 0)

    def get_current(self):
        """ Gets Current position"""

        return self.position[::]

    def move_next(self):
        """ Moves Next position"""

        self.position[0] += self.direction_vector[0]
        self.position[1] += self.direction_vector[1]

    def get_next(self):
        """ Gets tentative next position"""

        return (self.position[0] + self.direction_vector[0],
                self.position[1] + self.direction_vector[1])


class Pacman(Person):

    """Generic Pacman Object. """

    def __init__(self, position, score):
        Person.__init__(self, position)
        self.score = score

    def change_score(self, number):
        """ changes score """

        self.score += number

    collectCoin = change_score


class Ghost(Person):

    """Made this just in Case I end Up using it."""

    def __init__(self, position):
        Person.__init__(self, position)


class Game(object):

    """Game Class. Make a new instance of this every new game."""

    def __init__(
        self,
        difficulty=4,
        game_maze=GameMaze(1),
        score=0,
        ):

        object.__init__(self)
        self.difficulty = difficulty
        self.game_maze = game_maze
        self.ghosts = []
        self.pacman = Pacman((game_maze.position_x / 2,
                             game_maze.position_y * 3 / 4), score)

    def pacman_move_next(self, pacman):
        """ Move next for Pacman """

        game_point = pacman.get_current()
        if not self.game_maze.checkwall(pacman.get_next()):
            pacman.move_next()
        if self.game_maze.get_attribute(pacman.get_current()) \
            == GameMaze.MAZE['ghost'] \
            or self.game_maze.get_attribute(pacman.get_current()) \
            == GameMaze.MAZE['coinghost']:
            print GameMaze.COLORS['pacman'] + 'You cannot kill Ghosts' \
                + GameMaze.COLORS['END']
            exit(0)
        if self.game_maze.get_attribute(pacman.get_current()) \
            == GameMaze.MAZE['coin']:
            pacman.change_score(1)
            self.game_maze.coin_count = self.game_maze.coin_count - 1
        self.game_maze.clear_all(game_point)
        self.game_maze.set_attribute(pacman.get_current(),
                GameMaze.MAZE['pacman'])

    def ghost_move_next(self, ghost):
        """ Move next for ghost """

        game_point = ghost.get_current()
        random_number = randint(0, 4)  # 1/5 to maintain too
        if random_number == 0:
            ghost.move_up()
        elif random_number == 1:
            ghost.move_down()
        elif random_number == 2:
            ghost.move_left()
        elif random_number == 3:
            ghost.move_right()
        if not self.game_maze.checkwall(ghost.get_next()) \
            and self.game_maze.get_attribute(ghost.get_next()) \
            != GameMaze.MAZE['ghost'] \
            and self.game_maze.get_attribute(ghost.get_next()) \
            != GameMaze.MAZE['coinghost']:
            ghost.move_next()
        if self.game_maze.get_attribute(ghost.get_current()) \
            == GameMaze.MAZE['pacman']:
            print GameMaze.COLORS['pacman'] \
                + 'The AI killed you off. :(' + GameMaze.COLORS['END']
            exit(0)
        if self.game_maze.get_attribute(game_point) \
            == GameMaze.MAZE['coinghost']:
            self.game_maze.set_attribute(game_point,
                    GameMaze.MAZE['coin'])
        else:
            self.game_maze.clear_all(game_point)
        if self.game_maze.get_attribute(ghost.get_current()) \
            == GameMaze.MAZE['coin']:
            self.game_maze.set_attribute(ghost.get_current(),
                    GameMaze.MAZE['coinghost'])
        else:
            self.game_maze.set_attribute(ghost.get_current(),
                    GameMaze.MAZE['ghost'])

    def multiple_move_next(self, thing):
        """ Move Next for all objects """

        if thing.__class__.__name__ == 'Pacman':
            self.pacman_move_next(thing)
        elif thing.__class__.__name__ == 'Ghost':
            self.ghost_move_next(thing)
        else:
            print 'Whoa Dude! How Do position_you Even?'

    def check_ghost(self):
        """ check if ghost on spot """

        return self.game_maze.get_attribute(self.pacman.get_current()) \
            == GameMaze.MAZE['ghost']


def size_parser():
    """ Parse Sizes """

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
    """ Parse difficulty """

    try:
        difficulty = \
            int(raw_input('Enter the difficulty (Number of Ghosts)\n>'))
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


def main():
    """ Main function """

    (size_x, size_y) = size_parser()
    game_maze = GameMaze(1, (size_x, size_y))
    difficulty = difficulty_parser()
    game = Game(difficulty, game_maze)
    for _ in xrange(0, difficulty):
        game.ghosts.append(Ghost(game.game_maze.place_enemy()))
    character = getch()
    while True:
        system(('cls' if name == 'nt' else 'clear'))
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
