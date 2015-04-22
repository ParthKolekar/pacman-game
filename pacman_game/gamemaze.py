"""
    A GameMaze object which contains helpers for handling mazes
"""

from random import randint


class GameMaze(object):
    """
        Making A Maze Module For Game
    """

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

    def __init__(self, randomMaze=False, size=(35, 15)):
        object.__init__(self)
        self.size_x = size[0]
        self.size_y = size[1]
        self.coin_count = 0
        self.game_maze = [x[:] for x in [['.'] * self.size_x] * self.size_y]
        self.free_space = set()

        for i in xrange(0, self.size_y):
            for j in [0, self.size_x - 1]:
                self.game_maze[i][j] = GameMaze.MAZE['wall']
        for i in xrange(0, self.size_x):
            for j in [0, self.size_y - 1]:
                self.game_maze[j][i] = GameMaze.MAZE['wall']

        if randomMaze is False:
            pass
        else:
            self.fill_wall()

        self.game_maze[self.size_y * 3 / 4][self.size_x / 2] = GameMaze.MAZE['pacman']
        self.fill_coin([x[:] for x in [[0] * self.size_x] * self.size_y])

    def place_enemy(self):
        """
            Places enemy on map
        """

        size_x = randint(1, self.size_x - 1)
        size_y = randint(1, self.size_y - 1)
        while self.checkwall((size_x, size_y)) is True and self.get_attribute((size_x, size_y)) != GameMaze.MAZE['coinghost'] and self.get_attribute((size_x, size_y)) != GameMaze.MAZE['ghost'] and self.get_attribute((size_x, size_y)) != GameMaze.MAZE['coin'] and (size_x, size_y) not in self.free_space:
            size_x = randint(1, self.size_x - 1)
            size_y = randint(1, self.size_y - 1)
        attribute = self.get_attribute((size_x, size_y))
        if attribute == GameMaze.MAZE['coin']:
            self.set_attribute((size_x, size_y), GameMaze.MAZE['coinghost'])
        else:
            self.set_attribute((size_x, size_y), GameMaze.MAZE['ghost'])
        return (size_x, size_y)

    def fill_wall(self, game_point=(2, 2), count=0.0):
        """
            Fills Wall in map
        """

        point_1 = list(game_point)
        point_2 = [game_point[0], self.size_y - game_point[1] - 1]
        point_3 = [self.size_x - game_point[0] - 1, game_point[1]]
        point_4 = [self.size_x - game_point[0] - 1, self.size_y - game_point[1] - 1]

        total = self.size_x * self.size_y

        while point_1[0] < self.size_x / 2 and point_1[1] < self.size_y / 2:
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
            self.fill_wall((randint(3, self.size_x - 3), randint(3, self.size_x - 3)), count)

    def fill_coin(self, visited, game_point=(1, 1)):
        """
            Fills coins on map
        """

        if self.checkwall(game_point) is True or visited[game_point[1]][game_point[0]] is True or self.get_attribute(game_point) == GameMaze.MAZE['pacman']:
            return
        self.free_space.add(game_point)
        visited[game_point[1]][game_point[0]] = True
        if randint(0, 2) == 0:  # Probhablisticly fill with coin
            self.make_coin(game_point)
            self.coin_count = self.coin_count + 1
        self.fill_coin(visited, (game_point[0], game_point[1] + 1))
        self.fill_coin(visited, (game_point[0] + 1, game_point[1]))
        self.fill_coin(visited, (game_point[0], game_point[1] - 1))
        self.fill_coin(visited, (game_point[0] - 1, game_point[1]))

    def set_attribute(self, game_point, attribute):
        """
            Sets attribute on point
        """

        self.game_maze[game_point[1]][game_point[0]] = attribute

    def get_attribute(self, game_point):
        """
            Gets attribute on point
        """

        return self.game_maze[game_point[1]][game_point[0]]

    def checkwall(self, game_point):
        """
            Checks Wall
        """

        return self.get_attribute(game_point) == GameMaze.MAZE['wall']

    def clear_all(self, game_point):
        """
            Clears all on point
        """

        self.set_attribute(game_point, GameMaze.MAZE['nothing'])

    def make_wall(self, game_point):
        """
            Makes Wall
        """

        self.set_attribute(game_point, GameMaze.MAZE['wall'])

    def make_coin(self, game_point):
        """
            Makes Coin on point
        """

        self.set_attribute(game_point, GameMaze.MAZE['coin'])

    def __str__(self):
        string = ''
        for i in self.game_maze:
            for j in i:
                if j == GameMaze.MAZE['wall']:
                    string += GameMaze.COLORS['wall'] + j + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['coin']:
                    string += GameMaze.COLORS['coin'] + j + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['pacman']:
                    string += GameMaze.COLORS['pacman'] + j + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['ghost']:
                    string += GameMaze.COLORS['ghost'] + j + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['coinghost']:
                    string += GameMaze.COLORS['coinghost'] + GameMaze.MAZE['ghost'] + GameMaze.COLORS['END'] + ' '
                elif j == GameMaze.MAZE['nothing']:
                    string += GameMaze.COLORS['nothing'] + j + GameMaze.COLORS['END'] + ' '
                else:
                    string += j + ' '
            string += '\n'
        return string

    __repr__ = __str__
