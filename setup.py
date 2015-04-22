"""

"""

from setuptools import setup

setup(
    name='Pacman',
    version='1.0',
    description='A simple Pacman Game',
    long_description=__doc__,
    license='LGPLv3',
    author = 'Parth Laxmikant Kolekar',
    author_email = 'parth.kolekar@students.iiit.ac.in',
    packages=['pacman'],
    url = 'https://github.com/ParthKolekar/pacman',
    entry_points={
        'console_scripts': [
            'pacman = pacman.main:main',
        ]
    },
)
