'''
This module creates the Player class.
'''

import random

class Player(object):

    # I originally created this with a name parameter to play one at a time, but set it to default value.
    def __init__(self,name='Mike'):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, iname):
        self._name = iname

    # This is the initial door choice of the player.
    def choosedoor(self):
        return random.choice([1,2,3])

    # This determines whether the user will switch or not.
    def switch(self, choice='Y'):
        return choice
