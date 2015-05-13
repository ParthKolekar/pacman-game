"""
    A set of custom exceptions defined for pacman game
"""


class KillGhostException(Exception):
    """
        A exception when player attempts to kill a ghost
    """
    def __init__(self):
        Exception.__init__(self)


class KillPlayerException(Exception):
    """
        An exception raised when ghost sucessfully kills a player
    """
    def __init__(self):
        Exception.__init__(self)
