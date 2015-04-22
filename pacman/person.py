"""
    A generic class for Persons
"""


class Person(object):
    """
        Generic object
    """

    def __init__(self, position):
        object.__init__(self)
        self.position = list(position)
        self.direction_vector = (0, 0)

    def move_up(self):
        """
            Moves move_up
        """

        self.direction_vector = (0, -1)

    def move_down(self):
        """
            Moves move_down
        """

        self.direction_vector = (0, 1)

    def move_left(self):
        """
            Moves left
        """

        self.direction_vector = (-1, 0)

    def move_right(self):
        """
            Moves move_right
        """

        self.direction_vector = (1, 0)

    def get_current(self):
        """
            Gets Current position
        """

        return self.position[::]

    def move_next(self):
        """
            Moves Next position
        """

        self.position[0] += self.direction_vector[0]
        self.position[1] += self.direction_vector[1]

    def get_next(self):
        """
            Gets tentative next position
        """

        return (self.position[0] + self.direction_vector[0], self.position[1] + self.direction_vector[1])
