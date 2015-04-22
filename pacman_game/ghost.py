"""
    A smart AI based Ghost
"""

from random import randint

from .person import Person


class Ghost(Person):
    """
        Smart AI based Ghosts
    """

    def __init__(self, position, intelligence=0):
        Person.__init__(self, position)
        self.intelligence = intelligence

    def move_towards_pacman_greedy(self, pacman):
        """
            Greedily move towards pacman.
            Might get stuck. (Intendended for dumb AI)
        """
        pass  # TODO

    def move_towards_pacman_smart(self, pacman, game_maze):
        """
            Uses A* search to get best move towards pacman
        """
        pass  # TODO

    def move_towards_pacman_random(self):
        """
            Randombly moves anywhere.
        """
        random_number = randint(0, 4)  # 1/5 to maintain too
        if random_number == 0:
            self.move_up()
        elif random_number == 1:
            self.move_down()
        elif random_number == 2:
            self.move_left()
        elif random_number == 3:
            self.move_right()

    def think_next(self, game_maze, pacman):
        """
            Switches between various methods of finding next moves.
            Based on intelligence
        """
        if self.intelligence == 0:
            self.move_towards_pacman_random()
        else:
            pass  # TODO
