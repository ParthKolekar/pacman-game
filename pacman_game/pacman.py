"""
    A pacman object instance
"""

from .person import Person


class Pacman(Person):
    """
        Generic Pacman Object
    """

    def __init__(self, position, score):
        Person.__init__(self, position)
        self.score = score

    def change_score(self, number):
        """
            changes score
        """

        self.score += number

    def collect_coin(self, score):
        """
            Duplicate of change_score
        """
        self.change_score(score)
