"""
    A simple python based game

    Contains some basic AI and Randomly generated Maps
    ANSI Colors are added for pretty looks
"""

from setuptools import setup

setup(
    name='pacman-game',
    version='1.0.0.dev1',
    description='A simple Pacman Game',
    long_description=__doc__,
    license='LGPLv3',
    author='Parth Laxmikant Kolekar',
    author_email='parth.kolekar@students.iiit.ac.in',
    packages=['pacman_game'],
    url='https://github.com/ParthKolekar/pacman-game',
    entry_points={
        'console_scripts': [
            'pacman-game = pacman_game.main:main',
        ]
    },
    keywords='pacman console ai simple basic',
)
